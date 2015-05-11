#
# This is really lacking documentation. That's a FIXME :)
#
from copy import deepcopy
from genericpath import isfile
from os import listdir
import os
from os.path import join
import sys
import socket

__author__ = 'jorl17'
PRESET_STRING = "### static-hostnames preset {:s} "
PRESET_STRING_END = "### END static-hostnames preset {:s} "

ACTIVE_PRESETS_FILE="/etc/static-hostnames/presets/active-presets.txt"
STATIC_HOSTNAMES_FOLDER='/etc/static-hostnames'
PRESETS_FOLDER="/etc/static-hostnames/presets/"
DEFAULT_PRESET='default'
HOSTS_FILE="/etc/hosts"

VERSION='0.1'

def ensure_crucial_files_exist():
    try:
        os.mkdir(STATIC_HOSTNAMES_FOLDER)
    except:
        pass
    try:
        os.mkdir(PRESETS_FOLDER)
    except:
        pass
    try:
        open(ACTIVE_PRESETS_FILE, 'a+').close()
    except:
        pass
    if not preset_exists(DEFAULT_PRESET):
        ensure_preset_file_exists(DEFAULT_PRESET)
        activate_preset(DEFAULT_PRESET)


def is_ip(s):
    try:
        socket.inet_aton(s)
    except socket.error:
        try:
            socket.inet_pton(socket.AF_INET6, s)
        except socket.error:
            return False
        return True
    return True


def is_application_line(line):
    line = line.strip()
    return line.startswith('#') and ("static-hostnames" in line)

def read_static_hostnames(path=HOSTS_FILE):
    with open(path) as f:
        static_hostnames = [i.replace("\n","").strip().split() for i in f.readlines() if not i.replace("\n","").strip().startswith('#')]
    return static_hostnames

def read_preset(preset_name):
    return read_static_hostnames(PRESETS_FOLDER + '/' + preset_name + '.preset')

def check_static_ip(static_hostnames, ip):
    for static_ip,static_host in static_hostnames:
        if static_ip == ip:
            return static_host

    return ""

#A Mariana é Linda!

def add_static_ip(static_hostnames, ip, host):
    static_hostnames.append ( [ip, host] )

def preset_exists(preset_name):
    return os.path.isfile(PRESETS_FOLDER + '/' + preset_name + '.preset')

def ensure_preset_file_exists(preset_name):
    path = PRESETS_FOLDER + '/' + preset_name + '.preset'
    if not preset_exists(preset_name):
        open(path, 'w').close()


def add_static_ip_to_preset(preset_name, ip, host):
    ensure_preset_file_exists(preset_name)
    preset = read_preset(preset_name)
    curr_host = check_static_ip(preset, ip)
    if curr_host != "":
        return "IP '" + ip + "' already assigned to '" + curr_host + "'"
    add_static_ip(preset, ip, host)
    save_preset(preset_name, preset)
    return ""

def del_static_ip_from_preset(preset_name, ip):
    if not preset_exists(preset_name):
        return "No such preset"
    else:
        static_hostnames = read_preset(preset_name)
        if del_static_ip(static_hostnames, ip):
            save_preset(preset_name, static_hostnames)
            return ""
        else:
            return "No such ip in preset"


def del_static_ip(static_hostnames, ip):
    for index, [static_ip,static_host] in  enumerate(static_hostnames):
        if ip == static_ip:
            static_hostnames.pop(index)
            return True
    return False

def write_static_hostnames(path, static_hostnames):
    with open(path, 'w+') as f:
        for ip,host in static_hostnames:
            f.write(ip + " " + host + "\n")


def save_preset(preset_name, preset):
    write_static_hostnames(PRESETS_FOLDER + '/' + preset_name + '.preset', preset)

def get_presets(basepath):
    return [f[:-7] for f in listdir(basepath) if isfile(join(basepath, f)) and f.endswith(".preset")]

def get_all_ips_for_host(static_hostnames, host):
    ips = []
    for static_ip, static_host in static_hostnames:
        if static_host == host:
            ips.append(static_ip)

    return ips


def remove_from_active_presets(presetname):
    with open(ACTIVE_PRESETS_FILE) as f:
        lines = [i.replace("\n", "") for i in f.readlines()]

    final_lines = []
    for index, line in enumerate(lines):
        if line.strip() != presetname:
            final_lines.append(line)

    with open(ACTIVE_PRESETS_FILE, 'w') as f:
        for line in final_lines:
            f.write(line + "\n")


def delete_preset(presetname):
    if not preset_exists(presetname):
        return "Preset " + presetname + " does not exist"
    active_presets = get_active_presets()
    remove_from_active_presets(presetname)
    os.remove(PRESETS_FOLDER + '/' + presetname + '.preset')
    if presetname in active_presets:
        rebuild_hosts_file(HOSTS_FILE)

    return ""


def clear_hosts_file(path):
    with open(path) as f:
        lines= [i.replace("\n","") for i in f.readlines()]

    final_lines = []
    in_application_code = False
    for index,line in enumerate(lines):
        if not is_application_line(line) and not in_application_code:
            final_lines.append(line)
        elif is_application_line(line) and in_application_code:
            in_application_code = False
        else:
            in_application_code = True

    with open(path, 'w') as f:
        for line in final_lines:
            f.write(line + "\n")

def add_preset_to_file(file_handle, static_hostnames, preset_name):
    file_handle.write(PRESET_STRING.format(preset_name) + '\n')
    for ip, host in static_hostnames:
        file_handle.write(ip + " " + host + "\n")
    file_handle.write(PRESET_STRING_END.format(preset_name) + '\n'
    )

def get_active_presets():
    with open(ACTIVE_PRESETS_FILE) as f:
        return [line.replace('\n','').strip() for line in f.readlines() if '#' not in line]


def activate_preset(preset_name):
    active_presets = get_active_presets()
    if preset_name in active_presets:
        return "Preset '" + preset_name + "' already active"
    else:
        with open(ACTIVE_PRESETS_FILE, 'a') as f:
            f.write(preset_name + "\n")

def disable_preset(preset_name):
    active_presets = get_active_presets()
    if not preset_name in active_presets:
        return "Preset '" + preset_name + "' not active"
    active_presets.remove(preset_name)
    with open(ACTIVE_PRESETS_FILE, 'a') as f:
        f.write(preset_name + "\n")


def load_presets(preset_names):
    preset_data = []
    for preset in preset_names:
        preset_data.append(read_preset(preset))
    return preset_names, preset_data

def load_active_presets():
    return load_presets(get_active_presets())

def load_all_presets():
    return load_presets(get_presets(PRESETS_FOLDER))

def build_ips_hosts_origin_lists_from_preset_data(preset_names, preset_data):
    ips = []
    hosts = []
    origin = []
    for index, preset in enumerate(preset_data):
        for mapping in preset:
            ips.append(mapping[0])
            hosts.append(mapping[1])
            origin.append(preset_names[index])
    return ips, hosts, origin

def get_active_mappings():
    preset_names,preset_data=load_active_presets()
    return build_ips_hosts_origin_lists_from_preset_data(preset_names, preset_data)

def get_all_mappings():
    preset_names, preset_data = load_all_presets()
    return build_ips_hosts_origin_lists_from_preset_data(preset_names, preset_data)

def rebuild_hosts_file(path=HOSTS_FILE):
    clear_hosts_file(path)
    presets_names, presets = load_active_presets()

    with open(path, 'a') as f:
        for i in range(len(presets_names)):
            add_preset_to_file(f, presets[i], presets_names[i])

def del_static_ip_from_all_presets(ip):
    presets = get_presets(PRESETS_FOLDER)
    for preset in presets:
        del_static_ip_from_preset(preset, ip)


def delete_all_presets():
    presets = get_presets(PRESETS_FOLDER)
    for preset in presets:
        delete_preset(preset)

def print_presets(presets, verbosity=False):
    for i,preset in enumerate(presets):
        print("\t{:d}. {:s}".format(i+1,preset))


def print_presets_with_active_info(presets, active_presets, verbosity):
    for i, preset in enumerate(presets):
        if preset in active_presets:
            print("\t{:d}.\t{:s}\t[Active]".format(i + 1, preset))
        else:
            print("\t{:d}.\t{:s}".format(i + 1, preset))


def print_mappings(ips, hosts, origin, verbosity=False):
    for i in range(len(ips)):
        print("\t{:d}.\t{:s} => {:s}\t[{:s}]".format(i + 1, hosts[i], ips[i], origin[i]))

def print_mappings_with_active_info(ips, hosts, origin, active_origin, verbosity=False):
    for i in range(len(ips)):
        if origin[i] in active_origin:
            print("\t{:d}.\t{:s} => {:s}\t[{:s}]\t[Active]".format(i + 1, hosts[i], ips[i], origin[i]))
        else:
            print("\t{:d}.\t{:s} => {:s}\t[{:s}]".format(i + 1, hosts[i], ips[i], origin[i]))


def print_help_show():
    print('\tstatic-hostnames [show|list|-s|-l] active presets               Show all active presets')
    print('\tstatic-hostnames [show|list|-s|-l] active maps                  Show all active host => ip maps')
    print('\tstatic-hostnames [show|list|-s|-l] all presets                  Show all presets')
    print('\tstatic-hostnames [show|list|-s|-l] presets                      Show all presets')
    print('\tstatic-hostnames [show|list|-s|-l] all maps                     Show all host => ip maps')
    print('\tstatic-hostnames [show|list|-s|-l] maps                         Show all host => ip maps')
    print('\tstatic-hostnames [show|list|-s|-l] all                          Show all presets and maps')
    print('\tstatic-hostnames [show|list|-s|-l]                              Show all presets and maps')

def print_help_add():
    print('\tstatic-hostnames [add|map|-a|-m|-A] preset_name ip host         Map host => ip in preset preset_name')
    print('\tstatic-hostnames [add|map|-a|-m|-A] ip host [to|on] preset_name Map host => ip in preset preset_name')
    print('\tstatic-hostnames [add|map|-a|-m|-A] ip host                     Map host => ip in default preset')

def print_help_del():
    print('\tstatic-hostnames [del|-D] ip from preset_name                   Delete ip mappings from preset preset_name')
    print('\tstatic-hostnames [del|-D] ip from all                           Delete ip mappings from all presets')
    print('\tstatic-hostnames [del|-D] ip                                    Delete ip mappings from default preset')
    print('\tstatic-hostnames [del|-D] preset_name                           Delete preset preset_name (and its mappings)')
    print('\tstatic-hostnames [del|-D] all                                   Delete all presets and mappings')
    print('\tstatic-hostnames [del|-D]                                       Delete all presets and mappings')

def print_help_enable():
    print('\tstatic-hostnames [enable|activate|-e] preset_name               Enable preset preset_name')
    print('\tstatic-hostnames [enable|activate|-e] all                       Enable all presets')

def print_help_disable():
    print('\tstatic-hostnames [disable|deactivate|-d] preset_name            Disable preset preset_name')
    print('\tstatic-hostnames [disable|deactivate|-d] all                    Disable all presets')

def print_help_create():
    print('\tstatic-hostnames [create|-c] preset_name                        Create preset preset_name (starts empty)')
    print('\tstatic-hostnames [create|-c] preset preset_name                 Create preset preset_name (starts empty)')

def print_help_help():
    print('\tstatic-hostnames [help|--help|-h]                               Display this message')

def print_help():
    print('static-hostnames ' + VERSION + ' by João Ricardo Lourenço')
    print('static-hostnames helps you manage static "host => ip" rules by modifying /etc/hosts dynamically.')
    print('Commands:')
    print_help_add()
    print('')
    print_help_del()
    print('')
    print_help_create()
    print('')
    print_help_enable()
    print('')
    print_help_disable()
    print('')
    print_help_show()
    print('')
    print_help_help()
def cmd_show(args, verbosity=False):
    if len(args) == 1 and (args[0] == 'presets' or args[0] == 'maps'):
        args = deepcopy(args)
        args.append(args[0])
        args[0] = 'all'
    elif len(args)==0 or (len(args) == 1 and args[0] == 'all'):
        # Use a trick and recurse
        cmd_show(['presets'])
        cmd_show(['maps'])
        return
    elif len(args) != 2 or (args[1] != 'presets' and args[1] != 'maps') or (args[0] != 'active' and args[0] != 'all'):
        print('Invalid usage. Usage:')
        print_help_show()
        return

    if args[1] == 'presets':
        active_presets = get_active_presets()

        if verbosity:
            print('List of {:s} presets (at {:s}):'.format(args[0],PRESETS_FOLDER))
        else:
            print('List of {:s} presets:'.format(args[0]))

        if args[0] == 'active':
            print_presets(active_presets, verbosity)
        else:
            presets = get_presets(PRESETS_FOLDER)
            print_presets_with_active_info(presets, active_presets, verbosity)
    else:
        print('List of {:s} mappings:'.format(args[0]))
        active_ips, active_hosts, active_origin = get_active_mappings()
        if args[0] == 'active':
            print_mappings(active_ips, active_hosts, active_origin, verbosity)
        else:
            ips, hosts, origin = get_all_mappings()
            print_mappings_with_active_info(ips, hosts, origin, active_origin, verbosity)


def cmd_add(args, verbosity=False):
    if len(args) == 2:
        preset = DEFAULT_PRESET
        ip = args[0]
        host = args[1]
    elif len(args) == 3:
        preset = args[0]
        ip = args[1]
        host = args[2]
    elif len(args) == 4 and args[2] in ['to','on']:
        preset = args[3]
        ip = args[0]
        host = args[1]
    else:
        print('Invalid usage. Usage:')
        print_help_add()
        return

    retstring = add_static_ip_to_preset(preset, ip, host)
    if retstring == "":
        print('Mapped {:s} to {:s} on preset {:s}'.format(host, ip, preset))
    else:
        print('Error mapping {:s} to {:s} on preset {:s}: {:s}'.format(host, ip, preset, retstring))

def cmd_del(args, verbosity=False):
    do_delete_preset = False
    delete_from_all_presets = False
    do_delete_all_presets = False
    if len(args) == 0:
        do_delete_preset = True
        do_delete_all_presets = True
    elif len(args) == 1:
        if is_ip(args[0]):
            ip = args[0]
            preset = DEFAULT_PRESET
            #delete_preset = False
        else:
            do_delete_preset = True
            preset = args[0]
            if preset == 'all':
                do_delete_all_presets = True
    elif len(args) == 3 and args[1] == 'from':
        preset = args[2]
        if preset == 'all':
            delete_from_all_presets = True
        ip = args[0]
    else:
        print('Invalid usage. Usage:')
        print_help_del()
        return

    if do_delete_preset:
        if do_delete_all_presets:
            delete_all_presets()
            print('Deleted all known presets')
            return
        retval = delete_preset(preset)
        if retval != "":
            print('Error deleting preset ' + preset + ": " + retval)
        else:
            print('Preset ' + preset + ' deleted.')
        return
    else:
        if delete_from_all_presets:
            del_static_ip_from_all_presets(ip)
            print('Deleted ' + ip + ' from all presets')
        else:
            retstring = del_static_ip_from_preset(preset, ip)

            if retstring == "":
                print('Deleted {:s} from preset {:s}'.format(ip, preset))
            else:
                print('Error deleting {:s} from preset {:s}: {:s}'.format(ip, preset, retstring))
            return

def cmd_enable(args, verbosity=False):
    if len(args) != 1:
        print('Invalid usage. Usage:')
        print_help_enable()
        return
    preset = args[0]
    if preset == 'all':
        presets = get_presets(PRESETS_FOLDER)
        for preset in presets:
            activate_preset(preset)
            print('All presets enabled')
    else:
        if not preset_exists(preset):
            print('Error: preset {:s} does not exist'.format(preset))
            return
        active_presets = get_active_presets()
        if preset in active_presets:
            print('Error: preset {:s} already active'.format(preset))
            return

        activate_preset(preset)
        print('Preset {:s} enabled'.format(preset))

def cmd_create_preset(args, verbosity=False):
    if len(args) == 1:
        preset = args[0]
    elif len(args) == 2 and args[0] == 'preset':
        preset = args[1]
    else:
        print('Invalid usage. Usage:')
        print_help_create()
        return
    if preset_exists(preset):
        print('Preset {:s} already exists'.format(preset))
    else:
        ensure_preset_file_exists(preset)
        print('Preset {:s} created'.format(preset))

def cmd_disable(args, verbosity=False):
    if len(args) != 1:
        print('Invalid usage. Usage:')
        print_help_disable()
        return
    preset = args[0]
    if preset == all:
        presets = get_presets(PRESETS_FOLDER)
        for preset in presets:
            remove_from_active_presets(preset)
    else:
        if not preset_exists(preset):
            print('Error: preset {:s} does not exist'.format(preset))
            return
        active_presets = get_active_presets()
        if preset not in active_presets:
            print('Error: preset {:s} not active'.format(preset))
            return

        remove_from_active_presets(preset)
        print('Preset {:s} disabled'.format(preset))

def parse_cmd(s):
    ensure_crucial_files_exist()
    dict = { 'add': cmd_add,
             'map': cmd_add,
             '-a': cmd_add,
             '-A': cmd_add,
             '-m': cmd_add,

             'show': cmd_show,
             'list': cmd_show,
             '-s': cmd_show,
             '-l': cmd_show,

             'del' : cmd_del,
             '-D': cmd_del,

             'enable': cmd_enable,
             'activate': cmd_enable,
             '-e': cmd_enable,

             'disable': cmd_disable,
             'deactivate': cmd_disable,
             '-d': cmd_enable,

             'create': cmd_create_preset,
             '-c': cmd_create_preset,
            }
    if type(s) == str:
        s = s.split()

    if len(s) == 0:
        print('No arguments given. Use static-hostnames help for help.')
        return

    if s[0] not in dict or s[0] in ['h', '--help', 'help']:
        print('Invalid usage (no such command). Usage: ')
        print_help()
    else:
        dict[s[0]](s[1:])
        ensure_preset_file_exists(DEFAULT_PRESET)
        rebuild_hosts_file()


if __name__ == "__main__":
    if os.geteuid() != 0:
        exit("You need to have root privileges. Please try again, this time using 'sudo'. Exiting.")
    parse_cmd(sys.argv[1:])