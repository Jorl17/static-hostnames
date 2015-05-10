# static-hostnames
 static-hostnames is a python 3 script that helps you manage /etc/hosts without explicitly editing it. It allows for static "host => ip" mappings to be made, as they would be made by manually editing /etc/hosts.  It extends this by adding the notion of presets, which are sets of mappings

## Why use this if I can just edit /etc/hosts myself?
Editing /etc/hosts can be tedious, so this tool makes it easier. If you want to add a mapping, just do

``static-hostnames -a <ip> <host>``

However, the great advantage of using static-hostnames is that it allows the use of presets, so you have different mappings in different presets. Additionally, static-hostnames does not touch any other lines in /etc/hosts, it only adds an additional layer. So if you want to remove all your static host rules, you just do

``static-hostnames -D``

and your /etc/hosts is just as it was before you started using static-hostnames.

## How does it really work?
static-hostnames presets are files identical to /etc/hosts, with the difference that they're stored somewhere else. The names of active presets are stored in the /etc/static-hostnames/presets/active_presets.txt. Whenever you do something in static-hostnames, the active presets are copied one by one to the end of your /etc/hosts file. They are placed between comments for later easy identification. This means that whatever lines you have in your /etc/hosts are left unchanged. It's really that simple.


## What Operating Systems does it work on?
Any UNIX-like operating system. That includes OS X.

## How do I install/uninstall it?
 Just clone the repository and run ``install.sh``, or ``uninstall.sh`` to remove it. It will install to /usr/bin, but you can change this by passing your desired prefix to install.sh, as an argument.

###Examples:
#### Install
    git clone https://github.com/Jorl17/static-hostnames.git
    cd static-hostnames
    chmod +x install.sh uninstall.sh
    sudo ./install.sh
#### Install to /usr/local prefix
    git clone https://github.com/Jorl17/static-hostnames.git
    cd static-hostnames
    chmod +x install.sh uninstall.sh
    sudo ./install.sh /usr/local
#### Uninstall 
    ./uninstall.sh
#### Uninstall from /usr/local prefix
    ./uninstall.sh /usr/local

## The help command shows a bunch of commands! Why so many?
If you look carefully, there aren't that many commands. It's just that there are multiple syntactic ways to do the same thing. In addition, you will often just want to edit the default preset, so we don't force you to have to say which preset you want to edit -- this adds more commands (aliases). All of this make it easier on different sysadmins, coming from different backgrounds and familiarity with other tools. Take the *delete* command, for example, the short-hand version is just

``static-hostnames -D``

which deletes all presets and static host rules. You may also write ``static-hostnames del``, ``static-hostnames -D all`` or ``static-hostnames del all``. If you want to delete a specific preset, you can do

``static-hostnames -D <preset>``

or, as before, by its alias ``static-hostnames del <preset>``. You can also pass an ip instead of a preset, and static-hostnames will detect that and delete the ip from the default preset, as so:

``static-hostnames -D <ip>``

but you can delete from other presets by doing

``static-hostnames del <ip> from <preset>``

or

``static-hostnames -D <ip> from <preset>``

The point is that you have flexibility and don't have to memorize the kind of commands you hate. Some people like short command line flags, and others like to almost write full sentences. static-hostnames lets you choose what you like the most

## I can't delete the default preset!
That's intended. You can delete its content, but static-hostnames ensures there's always a 'default' preset, even if it's empty. Don't worry, though, it won't pollute /etc/hosts at all if there are no mappings.

Also note that if you don't have any presets (for instance after running ``static-hostnames -D``) the default preset will also be marked as active by default. Really, don't disable it, there's no reason.

## Do I need to be root or does static-hostnames do it for me?
You have to be root (we check). ``sudo`` that thing.

## Where does static-hostnames store its data? Is it by-user or for all users?
static-hostnames' rules are global. /etc/hosts itself is global, so doing it the other way around would probably be very difficult. You can find all static-hostnames data under the */etc/static-hostnames* directory. It is created whenever you run the application, if it doesn't exist

## Can I map the same host to different ips?
/etc/hosts allows for this, so why should static-hostnames prevent you from doing it? What we don't allow for is to map the same ip to different hosts -- that is, on concurrently active presets.

## Is there a port for Python 2?
There are currently no plans, but it shouldn't be too hard. After all, this is really easy stuff.

##Example usage
Here are some examples of how to use static-hostnames. We show many different ways of doing it, but not all of them! Check the help of the tool!
###Add a mapping (to the default preset)
    static-hostnames -a 8.8.8.8 google-dns
    static-hostnames add 8.8.8.8 google-dns
    static-hostnames map 8.8.8.8 google-dns
    static-hostnames add default 8.8.8.8 google-dns
    static-hostnames add 8.8.8.8 google-dns to default
    static-hostnames map 8.8.8.8 google-dns on default
###Add a mapping (to another preset)
    _Note that you don't need to create presets. They're created for you when you add something to them_
    static-hostnames -a 8.8.8.8 google-dns on alternative-dns
    static-hostnames add 8.8.8.8 google-dns on alternative-dns
###Delete a mapping (from the default preset)
    static-hostnames -D 8.8.8.8
    static-hostnames del 8.8.8.8
    static-hostnames del 8.8.8.8 from default
###Delete a preset (and all its mappings)
    static-hostnames -D mypreset
    static-hostnames del mypreset
###List/Show all presets
    static-hostnames -l presets
    static-hostnames show presets
###List/Show all active presets
    static-hostnames -l active presets
    static-hostnames show acive presets
    static-hostnames list acive presets
###List/Show all static host mappings
    static-hostnames -l maps
    static-hostnames show maps
###List/Show all active static host mappings
    static-hostnames -l active maps
    static-hostnames show active maps
    static-hostnames list active maps
###Enable a preset
    static-hostnames -e preset
    static-hostnames enable preset
    static-hostnames activate preset
###Disable a preset
    static-hostnames -d preset
    static-hostnames disable preset
    static-hostnames deactivate preset
