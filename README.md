


<!DOCTYPE html>
<html lang="en" class="">
  <head prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb# object: http://ogp.me/ns/object# article: http://ogp.me/ns/article# profile: http://ogp.me/ns/profile#">
    <meta charset='utf-8'>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta http-equiv="Content-Language" content="en">
    
    
    <title>rbenv/README.md at master · sstephenson/rbenv · GitHub</title>
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub">
    <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub">
    <link rel="apple-touch-icon" sizes="57x57" href="/apple-touch-icon-114.png">
    <link rel="apple-touch-icon" sizes="114x114" href="/apple-touch-icon-114.png">
    <link rel="apple-touch-icon" sizes="72x72" href="/apple-touch-icon-144.png">
    <link rel="apple-touch-icon" sizes="144x144" href="/apple-touch-icon-144.png">
    <meta property="fb:app_id" content="1401488693436528">

      <meta content="@github" name="twitter:site" /><meta content="summary" name="twitter:card" /><meta content="sstephenson/rbenv" name="twitter:title" /><meta content="rbenv - Groom your app’s Ruby environment" name="twitter:description" /><meta content="https://avatars2.githubusercontent.com/u/2603?v=3&amp;s=400" name="twitter:image:src" />
      <meta content="GitHub" property="og:site_name" /><meta content="object" property="og:type" /><meta content="https://avatars2.githubusercontent.com/u/2603?v=3&amp;s=400" property="og:image" /><meta content="sstephenson/rbenv" property="og:title" /><meta content="https://github.com/sstephenson/rbenv" property="og:url" /><meta content="rbenv - Groom your app’s Ruby environment" property="og:description" />
      <meta name="browser-stats-url" content="https://api.github.com/_private/browser/stats">
    <meta name="browser-errors-url" content="https://api.github.com/_private/browser/errors">
    <link rel="assets" href="https://assets-cdn.github.com/">
    
    <meta name="pjax-timeout" content="1000">
    

    <meta name="msapplication-TileImage" content="/windows-tile.png">
    <meta name="msapplication-TileColor" content="#ffffff">
    <meta name="selected-link" value="repo_source" data-pjax-transient>
      <meta name="google-analytics" content="UA-3769691-2">

    <meta content="collector.githubapp.com" name="octolytics-host" /><meta content="collector-cdn.github.com" name="octolytics-script-host" /><meta content="github" name="octolytics-app-id" /><meta content="025245CD:02C6:5A63ABE:554EAFAD" name="octolytics-dimension-request_id" />
    
    <meta content="Rails, view, blob#show" name="analytics-event" />
    <meta class="js-ga-set" name="dimension1" content="Logged Out">
    <meta class="js-ga-set" name="dimension2" content="Header v3">
    <meta name="is-dotcom" content="true">
    <meta name="hostname" content="github.com">
    <meta name="user-login" content="">

    
    <link rel="icon" type="image/x-icon" href="https://assets-cdn.github.com/favicon.ico">


    <meta content="authenticity_token" name="csrf-param" />
<meta content="15Pl+3hEMROTUrFN6ml78rquYZcaC8v12oRx2qeB1Gjt/pZFZ4fxk404481dD3M3Y4wviuGyOg3ilCQxVmAMXg==" name="csrf-token" />

    <link href="https://assets-cdn.github.com/assets/github-c486157afcc5f58155a921bc675afb08733fbaa8dcf39ac2104d381dd9c82ac2.css" media="all" rel="stylesheet" />
    <link href="https://assets-cdn.github.com/assets/github2-da2e842cc3f0aaf33b727d0ef034243c12ab008fd09b24868b97719683b40ee7.css" media="all" rel="stylesheet" />
    
    


    <meta http-equiv="x-pjax-version" content="4426702614c8182f33d1780ad1169662">

      
  <meta name="description" content="rbenv - Groom your app’s Ruby environment">
  <meta name="go-import" content="github.com/sstephenson/rbenv git https://github.com/sstephenson/rbenv.git">

  <meta content="2603" name="octolytics-dimension-user_id" /><meta content="sstephenson" name="octolytics-dimension-user_login" /><meta content="2139017" name="octolytics-dimension-repository_id" /><meta content="sstephenson/rbenv" name="octolytics-dimension-repository_nwo" /><meta content="true" name="octolytics-dimension-repository_public" /><meta content="false" name="octolytics-dimension-repository_is_fork" /><meta content="2139017" name="octolytics-dimension-repository_network_root_id" /><meta content="sstephenson/rbenv" name="octolytics-dimension-repository_network_root_nwo" />
  <link href="https://github.com/sstephenson/rbenv/commits/master.atom" rel="alternate" title="Recent Commits to rbenv:master" type="application/atom+xml">

  </head>


  <body class="logged_out  env-production  vis-public page-blob">
    <a href="#start-of-content" tabindex="1" class="accessibility-aid js-skip-to-content">Skip to content</a>
    <div class="wrapper">
      
      
      


        
        <div class="header header-logged-out" role="banner">
  <div class="container clearfix">

    <a class="header-logo-wordmark" href="https://github.com/" data-ga-click="(Logged out) Header, go to homepage, icon:logo-wordmark">
      <span class="mega-octicon octicon-logo-github"></span>
    </a>

    <div class="header-actions" role="navigation">
        <a class="btn btn-primary" href="/join" data-ga-click="(Logged out) Header, clicked Sign up, text:sign-up">Sign up</a>
      <a class="btn" href="/login?return_to=%2Fsstephenson%2Frbenv%2Fblob%2Fmaster%2FREADME.md" data-ga-click="(Logged out) Header, clicked Sign in, text:sign-in">Sign in</a>
    </div>

    <div class="site-search repo-scope js-site-search" role="search">
      <form accept-charset="UTF-8" action="/sstephenson/rbenv/search" class="js-site-search-form" data-global-search-url="/search" data-repo-search-url="/sstephenson/rbenv/search" method="get"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /></div>
  <input type="text"
    class="js-site-search-field is-clearable"
    data-hotkey="s"
    name="q"
    placeholder="Search"
    data-global-scope-placeholder="Search GitHub"
    data-repo-scope-placeholder="Search"
    tabindex="1"
    autocapitalize="off">
  <div class="scope-badge">This repository</div>
</form>
    </div>

      <ul class="header-nav left" role="navigation">
          <li class="header-nav-item">
            <a class="header-nav-link" href="/explore" data-ga-click="(Logged out) Header, go to explore, text:explore">Explore</a>
          </li>
          <li class="header-nav-item">
            <a class="header-nav-link" href="/features" data-ga-click="(Logged out) Header, go to features, text:features">Features</a>
          </li>
          <li class="header-nav-item">
            <a class="header-nav-link" href="https://enterprise.github.com/" data-ga-click="(Logged out) Header, go to enterprise, text:enterprise">Enterprise</a>
          </li>
          <li class="header-nav-item">
            <a class="header-nav-link" href="/blog" data-ga-click="(Logged out) Header, go to blog, text:blog">Blog</a>
          </li>
      </ul>

  </div>
</div>



      <div id="start-of-content" class="accessibility-aid"></div>
          <div class="site" itemscope itemtype="http://schema.org/WebPage">
    <div id="js-flash-container">
      
    </div>
    <div class="pagehead repohead instapaper_ignore readability-menu">
      <div class="container">
        
<ul class="pagehead-actions">

  <li>
      <a href="/login?return_to=%2Fsstephenson%2Frbenv"
    class="btn btn-sm btn-with-count tooltipped tooltipped-n"
    aria-label="You must be signed in to watch a repository" rel="nofollow">
    <span class="octicon octicon-eye"></span>
    Watch
  </a>
  <a class="social-count" href="/sstephenson/rbenv/watchers">
    264
  </a>

  </li>

  <li>
      <a href="/login?return_to=%2Fsstephenson%2Frbenv"
    class="btn btn-sm btn-with-count tooltipped tooltipped-n"
    aria-label="You must be signed in to star a repository" rel="nofollow">
    <span class="octicon octicon-star"></span>
    Star
  </a>

    <a class="social-count js-social-count" href="/sstephenson/rbenv/stargazers">
      6,531
    </a>

  </li>

    <li>
      <a href="/login?return_to=%2Fsstephenson%2Frbenv"
        class="btn btn-sm btn-with-count tooltipped tooltipped-n"
        aria-label="You must be signed in to fork a repository" rel="nofollow">
        <span class="octicon octicon-repo-forked"></span>
        Fork
      </a>
      <a href="/sstephenson/rbenv/network" class="social-count">
        625
      </a>
    </li>
</ul>

        <h1 itemscope itemtype="http://data-vocabulary.org/Breadcrumb" class="entry-title public">
          <span class="mega-octicon octicon-repo"></span>
          <span class="author"><a href="/sstephenson" class="url fn" itemprop="url" rel="author"><span itemprop="title">sstephenson</span></a></span><!--
       --><span class="path-divider">/</span><!--
       --><strong><a href="/sstephenson/rbenv" class="js-current-repository" data-pjax="#js-repo-pjax-container">rbenv</a></strong>

          <span class="page-context-loader">
            <img alt="" height="16" src="https://assets-cdn.github.com/assets/spinners/octocat-spinner-32-e513294efa576953719e4e2de888dd9cf929b7d62ed8d05f25e731d02452ab6c.gif" width="16" />
          </span>

        </h1>
      </div><!-- /.container -->
    </div><!-- /.repohead -->

    <div class="container">
      <div class="repository-with-sidebar repo-container new-discussion-timeline  ">
        <div class="repository-sidebar clearfix">
            
<nav class="sunken-menu repo-nav js-repo-nav js-sidenav-container-pjax js-octicon-loaders"
     role="navigation"
     data-pjax="#js-repo-pjax-container"
     data-issue-count-url="/sstephenson/rbenv/issues/counts">
  <ul class="sunken-menu-group">
    <li class="tooltipped tooltipped-w" aria-label="Code">
      <a href="/sstephenson/rbenv" aria-label="Code" class="selected js-selected-navigation-item sunken-menu-item" data-hotkey="g c" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches /sstephenson/rbenv">
        <span class="octicon octicon-code"></span> <span class="full-word">Code</span>
        <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/assets/spinners/octocat-spinner-32-e513294efa576953719e4e2de888dd9cf929b7d62ed8d05f25e731d02452ab6c.gif" width="16" />
</a>    </li>

      <li class="tooltipped tooltipped-w" aria-label="Issues">
        <a href="/sstephenson/rbenv/issues" aria-label="Issues" class="js-selected-navigation-item sunken-menu-item" data-hotkey="g i" data-selected-links="repo_issues repo_labels repo_milestones /sstephenson/rbenv/issues">
          <span class="octicon octicon-issue-opened"></span> <span class="full-word">Issues</span>
          <span class="js-issue-replace-counter"></span>
          <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/assets/spinners/octocat-spinner-32-e513294efa576953719e4e2de888dd9cf929b7d62ed8d05f25e731d02452ab6c.gif" width="16" />
</a>      </li>

    <li class="tooltipped tooltipped-w" aria-label="Pull requests">
      <a href="/sstephenson/rbenv/pulls" aria-label="Pull requests" class="js-selected-navigation-item sunken-menu-item" data-hotkey="g p" data-selected-links="repo_pulls /sstephenson/rbenv/pulls">
          <span class="octicon octicon-git-pull-request"></span> <span class="full-word">Pull requests</span>
          <span class="js-pull-replace-counter"></span>
          <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/assets/spinners/octocat-spinner-32-e513294efa576953719e4e2de888dd9cf929b7d62ed8d05f25e731d02452ab6c.gif" width="16" />
</a>    </li>

      <li class="tooltipped tooltipped-w" aria-label="Wiki">
        <a href="/sstephenson/rbenv/wiki" aria-label="Wiki" class="js-selected-navigation-item sunken-menu-item" data-hotkey="g w" data-selected-links="repo_wiki /sstephenson/rbenv/wiki">
          <span class="octicon octicon-book"></span> <span class="full-word">Wiki</span>
          <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/assets/spinners/octocat-spinner-32-e513294efa576953719e4e2de888dd9cf929b7d62ed8d05f25e731d02452ab6c.gif" width="16" />
</a>      </li>
  </ul>
  <div class="sunken-menu-separator"></div>
  <ul class="sunken-menu-group">

    <li class="tooltipped tooltipped-w" aria-label="Pulse">
      <a href="/sstephenson/rbenv/pulse" aria-label="Pulse" class="js-selected-navigation-item sunken-menu-item" data-selected-links="pulse /sstephenson/rbenv/pulse">
        <span class="octicon octicon-pulse"></span> <span class="full-word">Pulse</span>
        <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/assets/spinners/octocat-spinner-32-e513294efa576953719e4e2de888dd9cf929b7d62ed8d05f25e731d02452ab6c.gif" width="16" />
</a>    </li>

    <li class="tooltipped tooltipped-w" aria-label="Graphs">
      <a href="/sstephenson/rbenv/graphs" aria-label="Graphs" class="js-selected-navigation-item sunken-menu-item" data-selected-links="repo_graphs repo_contributors /sstephenson/rbenv/graphs">
        <span class="octicon octicon-graph"></span> <span class="full-word">Graphs</span>
        <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/assets/spinners/octocat-spinner-32-e513294efa576953719e4e2de888dd9cf929b7d62ed8d05f25e731d02452ab6c.gif" width="16" />
</a>    </li>
  </ul>


</nav>

              <div class="only-with-full-nav">
                  
<div class="clone-url open"
  data-protocol-type="http"
  data-url="/users/set_protocol?protocol_selector=http&amp;protocol_type=clone">
  <h3><span class="text-emphasized">HTTPS</span> clone URL</h3>
  <div class="input-group js-zeroclipboard-container">
    <input type="text" class="input-mini input-monospace js-url-field js-zeroclipboard-target"
           value="https://github.com/sstephenson/rbenv.git" readonly="readonly">
    <span class="input-group-button">
      <button aria-label="Copy to clipboard" class="js-zeroclipboard btn btn-sm zeroclipboard-button tooltipped tooltipped-s" data-copied-hint="Copied!" type="button"><span class="octicon octicon-clippy"></span></button>
    </span>
  </div>
</div>

  
<div class="clone-url "
  data-protocol-type="subversion"
  data-url="/users/set_protocol?protocol_selector=subversion&amp;protocol_type=clone">
  <h3><span class="text-emphasized">Subversion</span> checkout URL</h3>
  <div class="input-group js-zeroclipboard-container">
    <input type="text" class="input-mini input-monospace js-url-field js-zeroclipboard-target"
           value="https://github.com/sstephenson/rbenv" readonly="readonly">
    <span class="input-group-button">
      <button aria-label="Copy to clipboard" class="js-zeroclipboard btn btn-sm zeroclipboard-button tooltipped tooltipped-s" data-copied-hint="Copied!" type="button"><span class="octicon octicon-clippy"></span></button>
    </span>
  </div>
</div>



<p class="clone-options">You can clone with
  <a href="#" class="js-clone-selector" data-protocol="http">HTTPS</a> or <a href="#" class="js-clone-selector" data-protocol="subversion">Subversion</a>.
  <a href="https://help.github.com/articles/which-remote-url-should-i-use" class="help tooltipped tooltipped-n" aria-label="Get help on which URL is right for you.">
    <span class="octicon octicon-question"></span>
  </a>
</p>




                <a href="/sstephenson/rbenv/archive/master.zip"
                   class="btn btn-sm sidebar-button"
                   aria-label="Download the contents of sstephenson/rbenv as a zip file"
                   title="Download the contents of sstephenson/rbenv as a zip file"
                   rel="nofollow">
                  <span class="octicon octicon-cloud-download"></span>
                  Download ZIP
                </a>
              </div>
        </div><!-- /.repository-sidebar -->

        <div id="js-repo-pjax-container" class="repository-content context-loader-container" data-pjax-container>

          

<a href="/sstephenson/rbenv/blob/5b9e4f05846f6bd03b09b8572142f53fd7a46e62/README.md" class="hidden js-permalink-shortcut" data-hotkey="y">Permalink</a>

<!-- blob contrib key: blob_contributors:v21:69ea6473aae3a9c57afbadd715a7a30a -->

<div class="file-navigation js-zeroclipboard-container">
  
<div class="select-menu js-menu-container js-select-menu left">
  <span class="btn btn-sm select-menu-button js-menu-target css-truncate" data-hotkey="w"
    data-master-branch="master"
    data-ref="master"
    title="master"
    role="button" aria-label="Switch branches or tags" tabindex="0" aria-haspopup="true">
    <span class="octicon octicon-git-branch"></span>
    <i>branch:</i>
    <span class="js-select-button css-truncate-target">master</span>
  </span>

  <div class="select-menu-modal-holder js-menu-content js-navigation-container" data-pjax aria-hidden="true">

    <div class="select-menu-modal">
      <div class="select-menu-header">
        <span class="select-menu-title">Switch branches/tags</span>
        <span class="octicon octicon-x js-menu-close" role="button" aria-label="Close"></span>
      </div>

      <div class="select-menu-filters">
        <div class="select-menu-text-filter">
          <input type="text" aria-label="Filter branches/tags" id="context-commitish-filter-field" class="js-filterable-field js-navigation-enable" placeholder="Filter branches/tags">
        </div>
        <div class="select-menu-tabs">
          <ul>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="branches" data-filter-placeholder="Filter branches/tags" class="js-select-menu-tab">Branches</a>
            </li>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="tags" data-filter-placeholder="Find a tag…" class="js-select-menu-tab">Tags</a>
            </li>
          </ul>
        </div>
      </div>

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="branches">

        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/sstephenson/rbenv/blob/bundle-rehash/README.md"
               data-name="bundle-rehash"
               data-skip-pjax="true"
               rel="nofollow">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <span class="select-menu-item-text css-truncate-target" title="bundle-rehash">
                bundle-rehash
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/sstephenson/rbenv/blob/gh-pages/README.md"
               data-name="gh-pages"
               data-skip-pjax="true"
               rel="nofollow">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <span class="select-menu-item-text css-truncate-target" title="gh-pages">
                gh-pages
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open selected"
               href="/sstephenson/rbenv/blob/master/README.md"
               data-name="master"
               data-skip-pjax="true"
               rel="nofollow">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <span class="select-menu-item-text css-truncate-target" title="master">
                master
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/sstephenson/rbenv/blob/user-gems/README.md"
               data-name="user-gems"
               data-skip-pjax="true"
               rel="nofollow">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <span class="select-menu-item-text css-truncate-target" title="user-gems">
                user-gems
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/sstephenson/rbenv/blob/version-aliases/README.md"
               data-name="version-aliases"
               data-skip-pjax="true"
               rel="nofollow">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <span class="select-menu-item-text css-truncate-target" title="version-aliases">
                version-aliases
              </span>
            </a>
        </div>

          <div class="select-menu-no-results">Nothing to show</div>
      </div>

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="tags">
        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/sstephenson/rbenv/tree/v0.4.0/README.md"
                 data-name="v0.4.0"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="v0.4.0">v0.4.0</a>
            </div>
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/sstephenson/rbenv/tree/v0.3.0/README.md"
                 data-name="v0.3.0"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="v0.3.0">v0.3.0</a>
            </div>
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/sstephenson/rbenv/tree/v0.2.1/README.md"
                 data-name="v0.2.1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="v0.2.1">v0.2.1</a>
            </div>
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/sstephenson/rbenv/tree/v0.2.0/README.md"
                 data-name="v0.2.0"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="v0.2.0">v0.2.0</a>
            </div>
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/sstephenson/rbenv/tree/v0.1.2/README.md"
                 data-name="v0.1.2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="v0.1.2">v0.1.2</a>
            </div>
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/sstephenson/rbenv/tree/v0.1.1/README.md"
                 data-name="v0.1.1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="v0.1.1">v0.1.1</a>
            </div>
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/sstephenson/rbenv/tree/v0.1.0/README.md"
                 data-name="v0.1.0"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="v0.1.0">v0.1.0</a>
            </div>
        </div>

        <div class="select-menu-no-results">Nothing to show</div>
      </div>

    </div>
  </div>
</div>

  <div class="btn-group right">
    <a href="/sstephenson/rbenv/find/master"
          class="js-show-file-finder btn btn-sm empty-icon tooltipped tooltipped-s"
          data-pjax
          data-hotkey="t"
          aria-label="Quickly jump between files">
      <span class="octicon octicon-list-unordered"></span>
    </a>
    <button aria-label="Copy file path to clipboard" class="js-zeroclipboard btn btn-sm zeroclipboard-button tooltipped tooltipped-s" data-copied-hint="Copied!" type="button"><span class="octicon octicon-clippy"></span></button>
  </div>

  <div class="breadcrumb js-zeroclipboard-target">
    <span class='repo-root js-repo-root'><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/sstephenson/rbenv" class="" data-branch="master" data-direction="back" data-pjax="true" itemscope="url"><span itemprop="title">rbenv</span></a></span></span><span class="separator">/</span><strong class="final-path">README.md</strong>
  </div>
</div>


  <div class="commit file-history-tease">
    <div class="file-history-tease-header">
        <img alt="Mislav Marohnić" class="avatar" data-user="887" height="24" src="https://avatars3.githubusercontent.com/u/887?v=3&amp;s=48" width="24" />
        <span class="author"><a href="/mislav" rel="contributor">mislav</a></span>
        <time datetime="2015-03-13T08:14:24Z" is="relative-time">Mar 13, 2015</time>
        <div class="commit-title">
            <a href="/sstephenson/rbenv/commit/7ad01b2b485fb635d7a96daef33f6a733e5b1c80" class="message" data-pjax="true" title="Document rbenv environment variables

Closes #699, fixes #666 [ci skip]">Document rbenv environment variables</a>
        </div>
    </div>

    <div class="participation">
      <p class="quickstat">
        <a href="#blob_contributors_box" rel="facebox">
          <strong>26</strong>
           contributors
        </a>
      </p>
          <a class="avatar-link tooltipped tooltipped-s" aria-label="sstephenson" href="/sstephenson/rbenv/commits/master/README.md?author=sstephenson"><img alt="Sam Stephenson" class="avatar" data-user="2603" height="20" src="https://avatars3.githubusercontent.com/u/2603?v=3&amp;s=40" width="20" /></a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="mislav" href="/sstephenson/rbenv/commits/master/README.md?author=mislav"><img alt="Mislav Marohnić" class="avatar" data-user="887" height="20" src="https://avatars1.githubusercontent.com/u/887?v=3&amp;s=40" width="20" /></a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="tundramonkey" href="/sstephenson/rbenv/commits/master/README.md?author=tundramonkey"><img alt="Daryl Manning" class="avatar" data-user="2866" height="20" src="https://avatars2.githubusercontent.com/u/2866?v=3&amp;s=40" width="20" /></a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="guilleiguaran" href="/sstephenson/rbenv/commits/master/README.md?author=guilleiguaran"><img alt="Guillermo Iguaran" class="avatar" data-user="160941" height="20" src="https://avatars3.githubusercontent.com/u/160941?v=3&amp;s=40" width="20" /></a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="josh" href="/sstephenson/rbenv/commits/master/README.md?author=josh"><img alt="Joshua Peek" class="avatar" data-user="137" height="20" src="https://avatars0.githubusercontent.com/u/137?v=3&amp;s=40" width="20" /></a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="jeremy" href="/sstephenson/rbenv/commits/master/README.md?author=jeremy"><img alt="Jeremy Kemper" class="avatar" data-user="199" height="20" src="https://avatars3.githubusercontent.com/u/199?v=3&amp;s=40" width="20" /></a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="radar" href="/sstephenson/rbenv/commits/master/README.md?author=radar"><img alt="Ryan Bigg" class="avatar" data-user="2687" height="20" src="https://avatars0.githubusercontent.com/u/2687?v=3&amp;s=40" width="20" /></a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="gma" href="/sstephenson/rbenv/commits/master/README.md?author=gma"><img alt="Graham Ashton" class="avatar" data-user="2122" height="20" src="https://avatars3.githubusercontent.com/u/2122?v=3&amp;s=40" width="20" /></a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="javierjulio" href="/sstephenson/rbenv/commits/master/README.md?author=javierjulio"><img alt="Javier Julio" class="avatar" data-user="198547" height="20" src="https://avatars2.githubusercontent.com/u/198547?v=3&amp;s=40" width="20" /></a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="jonathandean" href="/sstephenson/rbenv/commits/master/README.md?author=jonathandean"><img alt="Jonathan Dean" class="avatar" data-user="307888" height="20" src="https://avatars2.githubusercontent.com/u/307888?v=3&amp;s=40" width="20" /></a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="oscardelben" href="/sstephenson/rbenv/commits/master/README.md?author=oscardelben"><img alt="Oscar Del Ben" class="avatar" data-user="3892" height="20" src="https://avatars3.githubusercontent.com/u/3892?v=3&amp;s=40" width="20" /></a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="jvirtanen" href="/sstephenson/rbenv/commits/master/README.md?author=jvirtanen"><img alt="Jussi Virtanen" class="avatar" data-user="183430" height="20" src="https://avatars2.githubusercontent.com/u/183430?v=3&amp;s=40" width="20" /></a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="atz" href="/sstephenson/rbenv/commits/master/README.md?author=atz"><img alt="Joe Atzberger" class="avatar" data-user="109954" height="20" src="https://avatars1.githubusercontent.com/u/109954?v=3&amp;s=40" width="20" /></a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="lyrixx" href="/sstephenson/rbenv/commits/master/README.md?author=lyrixx"><img alt="Grégoire Pineau" class="avatar" data-user="408368" height="20" src="https://avatars1.githubusercontent.com/u/408368?v=3&amp;s=40" width="20" /></a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="yjpa7145" href="/sstephenson/rbenv/commits/master/README.md?author=yjpa7145"><img alt="yjpa7145" class="avatar" data-user="6790070" height="20" src="https://avatars2.githubusercontent.com/u/6790070?v=3&amp;s=40" width="20" /></a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="asymmetric" href="/sstephenson/rbenv/commits/master/README.md?author=asymmetric"><img alt="Lorenzo Manacorda" class="avatar" data-user="101816" height="20" src="https://avatars0.githubusercontent.com/u/101816?v=3&amp;s=40" width="20" /></a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="candeira" href="/sstephenson/rbenv/commits/master/README.md?author=candeira"><img alt="Javier Candeira" class="avatar" data-user="91694" height="20" src="https://avatars0.githubusercontent.com/u/91694?v=3&amp;s=40" width="20" /></a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="Hijadelsol" href="/sstephenson/rbenv/commits/master/README.md?author=Hijadelsol"><img alt="Gunes" class="avatar" data-user="5443027" height="20" src="https://avatars3.githubusercontent.com/u/5443027?v=3&amp;s=40" width="20" /></a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="dentarg" href="/sstephenson/rbenv/commits/master/README.md?author=dentarg"><img alt="Patrik Ragnarsson" class="avatar" data-user="42626" height="20" src="https://avatars0.githubusercontent.com/u/42626?v=3&amp;s=40" width="20" /></a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="mattdbridges" href="/sstephenson/rbenv/commits/master/README.md?author=mattdbridges"><img alt="Matt Bridges" class="avatar" data-user="442443" height="20" src="https://avatars1.githubusercontent.com/u/442443?v=3&amp;s=40" width="20" /></a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="audionerd" href="/sstephenson/rbenv/commits/master/README.md?author=audionerd"><img alt="Eric Skogen" class="avatar" data-user="23459" height="20" src="https://avatars2.githubusercontent.com/u/23459?v=3&amp;s=40" width="20" /></a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="baer" href="/sstephenson/rbenv/commits/master/README.md?author=baer"><img alt="Eric Baer" class="avatar" data-user="940667" height="20" src="https://avatars2.githubusercontent.com/u/940667?v=3&amp;s=40" width="20" /></a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="eddorre" href="/sstephenson/rbenv/commits/master/README.md?author=eddorre"><img alt="Carlos Rodriguez" class="avatar" data-user="32438" height="20" src="https://avatars0.githubusercontent.com/u/32438?v=3&amp;s=40" width="20" /></a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="almog" href="/sstephenson/rbenv/commits/master/README.md?author=almog"><img alt="Almog Kurtser" class="avatar" data-user="83724" height="20" src="https://avatars2.githubusercontent.com/u/83724?v=3&amp;s=40" width="20" /></a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="aprescott" href="/sstephenson/rbenv/commits/master/README.md?author=aprescott"><img alt="Adam Prescott" class="avatar" data-user="342081" height="20" src="https://avatars2.githubusercontent.com/u/342081?v=3&amp;s=40" width="20" /></a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="sodabrew" href="/sstephenson/rbenv/commits/master/README.md?author=sodabrew"><img alt="Aaron Stone" class="avatar" data-user="39406" height="20" src="https://avatars1.githubusercontent.com/u/39406?v=3&amp;s=40" width="20" /></a>


    </div>
    <div id="blob_contributors_box" style="display:none">
      <h2 class="facebox-header">Users who have contributed to this file</h2>
      <ul class="facebox-user-list">
          <li class="facebox-user-list-item">
            <img alt="Sam Stephenson" data-user="2603" height="24" src="https://avatars1.githubusercontent.com/u/2603?v=3&amp;s=48" width="24" />
            <a href="/sstephenson">sstephenson</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="Mislav Marohnić" data-user="887" height="24" src="https://avatars3.githubusercontent.com/u/887?v=3&amp;s=48" width="24" />
            <a href="/mislav">mislav</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="Daryl Manning" data-user="2866" height="24" src="https://avatars0.githubusercontent.com/u/2866?v=3&amp;s=48" width="24" />
            <a href="/tundramonkey">tundramonkey</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="Guillermo Iguaran" data-user="160941" height="24" src="https://avatars1.githubusercontent.com/u/160941?v=3&amp;s=48" width="24" />
            <a href="/guilleiguaran">guilleiguaran</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="Joshua Peek" data-user="137" height="24" src="https://avatars2.githubusercontent.com/u/137?v=3&amp;s=48" width="24" />
            <a href="/josh">josh</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="Jeremy Kemper" data-user="199" height="24" src="https://avatars1.githubusercontent.com/u/199?v=3&amp;s=48" width="24" />
            <a href="/jeremy">jeremy</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="Ryan Bigg" data-user="2687" height="24" src="https://avatars2.githubusercontent.com/u/2687?v=3&amp;s=48" width="24" />
            <a href="/radar">radar</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="Graham Ashton" data-user="2122" height="24" src="https://avatars1.githubusercontent.com/u/2122?v=3&amp;s=48" width="24" />
            <a href="/gma">gma</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="Javier Julio" data-user="198547" height="24" src="https://avatars0.githubusercontent.com/u/198547?v=3&amp;s=48" width="24" />
            <a href="/javierjulio">javierjulio</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="Jonathan Dean" data-user="307888" height="24" src="https://avatars0.githubusercontent.com/u/307888?v=3&amp;s=48" width="24" />
            <a href="/jonathandean">jonathandean</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="Oscar Del Ben" data-user="3892" height="24" src="https://avatars1.githubusercontent.com/u/3892?v=3&amp;s=48" width="24" />
            <a href="/oscardelben">oscardelben</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="Jussi Virtanen" data-user="183430" height="24" src="https://avatars0.githubusercontent.com/u/183430?v=3&amp;s=48" width="24" />
            <a href="/jvirtanen">jvirtanen</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="Joe Atzberger" data-user="109954" height="24" src="https://avatars3.githubusercontent.com/u/109954?v=3&amp;s=48" width="24" />
            <a href="/atz">atz</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="Grégoire Pineau" data-user="408368" height="24" src="https://avatars3.githubusercontent.com/u/408368?v=3&amp;s=48" width="24" />
            <a href="/lyrixx">lyrixx</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="yjpa7145" data-user="6790070" height="24" src="https://avatars0.githubusercontent.com/u/6790070?v=3&amp;s=48" width="24" />
            <a href="/yjpa7145">yjpa7145</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="Lorenzo Manacorda" data-user="101816" height="24" src="https://avatars2.githubusercontent.com/u/101816?v=3&amp;s=48" width="24" />
            <a href="/asymmetric">asymmetric</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="Javier Candeira" data-user="91694" height="24" src="https://avatars2.githubusercontent.com/u/91694?v=3&amp;s=48" width="24" />
            <a href="/candeira">candeira</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="Gunes" data-user="5443027" height="24" src="https://avatars1.githubusercontent.com/u/5443027?v=3&amp;s=48" width="24" />
            <a href="/Hijadelsol">Hijadelsol</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="Patrik Ragnarsson" data-user="42626" height="24" src="https://avatars2.githubusercontent.com/u/42626?v=3&amp;s=48" width="24" />
            <a href="/dentarg">dentarg</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="Matt Bridges" data-user="442443" height="24" src="https://avatars3.githubusercontent.com/u/442443?v=3&amp;s=48" width="24" />
            <a href="/mattdbridges">mattdbridges</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="Eric Skogen" data-user="23459" height="24" src="https://avatars0.githubusercontent.com/u/23459?v=3&amp;s=48" width="24" />
            <a href="/audionerd">audionerd</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="Eric Baer" data-user="940667" height="24" src="https://avatars0.githubusercontent.com/u/940667?v=3&amp;s=48" width="24" />
            <a href="/baer">baer</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="Carlos Rodriguez" data-user="32438" height="24" src="https://avatars2.githubusercontent.com/u/32438?v=3&amp;s=48" width="24" />
            <a href="/eddorre">eddorre</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="Almog Kurtser" data-user="83724" height="24" src="https://avatars0.githubusercontent.com/u/83724?v=3&amp;s=48" width="24" />
            <a href="/almog">almog</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="Adam Prescott" data-user="342081" height="24" src="https://avatars0.githubusercontent.com/u/342081?v=3&amp;s=48" width="24" />
            <a href="/aprescott">aprescott</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="Aaron Stone" data-user="39406" height="24" src="https://avatars3.githubusercontent.com/u/39406?v=3&amp;s=48" width="24" />
            <a href="/sodabrew">sodabrew</a>
          </li>
      </ul>
    </div>
  </div>

<div class="file">
  <div class="file-header">
    <div class="file-actions">

      <div class="btn-group">
        <a href="/sstephenson/rbenv/raw/master/README.md" class="btn btn-sm " id="raw-url">Raw</a>
          <a href="/sstephenson/rbenv/blame/master/README.md" class="btn btn-sm js-update-url-with-hash">Blame</a>
        <a href="/sstephenson/rbenv/commits/master/README.md" class="btn btn-sm " rel="nofollow">History</a>
      </div>


          <button type="button" class="octicon-btn disabled tooltipped tooltipped-n" aria-label="You must be signed in to make or propose changes">
            <span class="octicon octicon-pencil"></span>
          </button>

        <button type="button" class="octicon-btn octicon-btn-danger disabled tooltipped tooltipped-n" aria-label="You must be signed in to make or propose changes">
          <span class="octicon octicon-trashcan"></span>
        </button>
    </div>

    <div class="file-info">
        436 lines (315 sloc)
        <span class="file-info-divider"></span>
      15.082 kb
    </div>
  </div>
    <div id="readme" class="blob instapaper_body">
    <article class="markdown-body entry-content" itemprop="mainContentOfPage"><h1>
<a id="user-content-groom-your-apps-ruby-environment-with-rbenv" class="anchor" href="#groom-your-apps-ruby-environment-with-rbenv" aria-hidden="true"><span class="octicon octicon-link"></span></a>Groom your app’s Ruby environment with rbenv.</h1>

<p>Use rbenv to pick a Ruby version for your application and guarantee
that your development environment matches production. Put rbenv to work
with <a href="http://bundler.io/">Bundler</a> for painless Ruby upgrades and
bulletproof deployments.</p>

<p><strong>Powerful in development.</strong> Specify your app's Ruby version once,
  in a single file. Keep all your teammates on the same page. No
  headaches running apps on different versions of Ruby. Just Works™
  from the command line and with app servers like <a href="http://pow.cx">Pow</a>.
  Override the Ruby version anytime: just set an environment variable.</p>

<p><strong>Rock-solid in production.</strong> Your application's executables are its
  interface with ops. With rbenv and <a href="https://github.com/sstephenson/rbenv/wiki/Understanding-binstubs">Bundler
  binstubs</a>
  you'll never again need to <code>cd</code> in a cron job or Chef recipe to
  ensure you've selected the right runtime. The Ruby version
  dependency lives in one place—your app—so upgrades and rollbacks are
  atomic, even when you switch versions.</p>

<p><strong>One thing well.</strong> rbenv is concerned solely with switching Ruby
  versions. It's simple and predictable. A rich plugin ecosystem lets
  you tailor it to suit your needs. Compile your own Ruby versions, or
  use the <a href="https://github.com/sstephenson/ruby-build#readme">ruby-build</a>
  plugin to automate the process. Specify per-application environment
  variables with <a href="https://github.com/sstephenson/rbenv-vars">rbenv-vars</a>.
  See more <a href="https://github.com/sstephenson/rbenv/wiki/Plugins">plugins on the
  wiki</a>.</p>

<p><a href="https://github.com/sstephenson/rbenv/wiki/Why-rbenv%3F"><strong>Why choose rbenv over
RVM?</strong></a></p>

<h2>
<a id="user-content-table-of-contents" class="anchor" href="#table-of-contents" aria-hidden="true"><span class="octicon octicon-link"></span></a>Table of Contents</h2>

<ul>
<li>
<a href="#how-it-works">How It Works</a>

<ul>
<li><a href="#understanding-path">Understanding PATH</a></li>
<li><a href="#understanding-shims">Understanding Shims</a></li>
<li><a href="#choosing-the-ruby-version">Choosing the Ruby Version</a></li>
<li><a href="#locating-the-ruby-installation">Locating the Ruby Installation</a></li>
</ul>
</li>
<li>
<a href="#installation">Installation</a>

<ul>
<li>
<a href="#basic-github-checkout">Basic GitHub Checkout</a>

<ul>
<li><a href="#upgrading">Upgrading</a></li>
</ul>
</li>
<li><a href="#homebrew-on-mac-os-x">Homebrew on Mac OS X</a></li>
<li><a href="#how-rbenv-hooks-into-your-shell">How rbenv hooks into your shell</a></li>
<li><a href="#installing-ruby-versions">Installing Ruby Versions</a></li>
<li><a href="#uninstalling-ruby-versions">Uninstalling Ruby Versions</a></li>
</ul>
</li>
<li>
<a href="#command-reference">Command Reference</a>

<ul>
<li><a href="#rbenv-local">rbenv local</a></li>
<li><a href="#rbenv-global">rbenv global</a></li>
<li><a href="#rbenv-shell">rbenv shell</a></li>
<li><a href="#rbenv-versions">rbenv versions</a></li>
<li><a href="#rbenv-version">rbenv version</a></li>
<li><a href="#rbenv-rehash">rbenv rehash</a></li>
<li><a href="#rbenv-which">rbenv which</a></li>
<li><a href="#rbenv-whence">rbenv whence</a></li>
</ul>
</li>
<li><a href="#environment-variables">Environment variables</a></li>
<li><a href="#development">Development</a></li>
</ul>

<h2>
<a id="user-content-how-it-works" class="anchor" href="#how-it-works" aria-hidden="true"><span class="octicon octicon-link"></span></a>How It Works</h2>

<p>At a high level, rbenv intercepts Ruby commands using shim
executables injected into your <code>PATH</code>, determines which Ruby version
has been specified by your application, and passes your commands along
to the correct Ruby installation.</p>

<h3>
<a id="user-content-understanding-path" class="anchor" href="#understanding-path" aria-hidden="true"><span class="octicon octicon-link"></span></a>Understanding PATH</h3>

<p>When you run a command like <code>ruby</code> or <code>rake</code>, your operating system
searches through a list of directories to find an executable file with
that name. This list of directories lives in an environment variable
called <code>PATH</code>, with each directory in the list separated by a colon:</p>

<pre><code>/usr/local/bin:/usr/bin:/bin
</code></pre>

<p>Directories in <code>PATH</code> are searched from left to right, so a matching
executable in a directory at the beginning of the list takes
precedence over another one at the end. In this example, the
<code>/usr/local/bin</code> directory will be searched first, then <code>/usr/bin</code>,
then <code>/bin</code>.</p>

<h3>
<a id="user-content-understanding-shims" class="anchor" href="#understanding-shims" aria-hidden="true"><span class="octicon octicon-link"></span></a>Understanding Shims</h3>

<p>rbenv works by inserting a directory of <em>shims</em> at the front of your
<code>PATH</code>:</p>

<pre><code>~/.rbenv/shims:/usr/local/bin:/usr/bin:/bin
</code></pre>

<p>Through a process called <em>rehashing</em>, rbenv maintains shims in that
directory to match every Ruby command across every installed version
of Ruby—<code>irb</code>, <code>gem</code>, <code>rake</code>, <code>rails</code>, <code>ruby</code>, and so on.</p>

<p>Shims are lightweight executables that simply pass your command along
to rbenv. So with rbenv installed, when you run, say, <code>rake</code>, your
operating system will do the following:</p>

<ul>
<li>Search your <code>PATH</code> for an executable file named <code>rake</code>
</li>
<li>Find the rbenv shim named <code>rake</code> at the beginning of your <code>PATH</code>
</li>
<li>Run the shim named <code>rake</code>, which in turn passes the command along to
rbenv</li>
</ul>

<h3>
<a id="user-content-choosing-the-ruby-version" class="anchor" href="#choosing-the-ruby-version" aria-hidden="true"><span class="octicon octicon-link"></span></a>Choosing the Ruby Version</h3>

<p>When you execute a shim, rbenv determines which Ruby version to use by
reading it from the following sources, in this order:</p>

<ol>
<li><p>The <code>RBENV_VERSION</code> environment variable, if specified. You can use
the <a href="#rbenv-shell"><code>rbenv shell</code></a> command to set this environment
variable in your current shell session.</p></li>
<li><p>The first <code>.ruby-version</code> file found by searching the directory of the
script you are executing and each of its parent directories until reaching
the root of your filesystem.</p></li>
<li><p>The first <code>.ruby-version</code> file found by searching the current working
directory and each of its parent directories until reaching the root of your
filesystem. You can modify the <code>.ruby-version</code> file in the current working
directory with the <a href="#rbenv-local"><code>rbenv local</code></a> command.</p></li>
<li><p>The global <code>~/.rbenv/version</code> file. You can modify this file using
the <a href="#rbenv-global"><code>rbenv global</code></a> command. If the global version
file is not present, rbenv assumes you want to use the "system"
Ruby—i.e. whatever version would be run if rbenv weren't in your
path.</p></li>
</ol>

<h3>
<a id="user-content-locating-the-ruby-installation" class="anchor" href="#locating-the-ruby-installation" aria-hidden="true"><span class="octicon octicon-link"></span></a>Locating the Ruby Installation</h3>

<p>Once rbenv has determined which version of Ruby your application has
specified, it passes the command along to the corresponding Ruby
installation.</p>

<p>Each Ruby version is installed into its own directory under
<code>~/.rbenv/versions</code>. For example, you might have these versions
installed:</p>

<ul>
<li><code>~/.rbenv/versions/1.8.7-p371/</code></li>
<li><code>~/.rbenv/versions/1.9.3-p327/</code></li>
<li><code>~/.rbenv/versions/jruby-1.7.1/</code></li>
</ul>

<p>Version names to rbenv are simply the names of the directories in
<code>~/.rbenv/versions</code>.</p>

<h2>
<a id="user-content-installation" class="anchor" href="#installation" aria-hidden="true"><span class="octicon octicon-link"></span></a>Installation</h2>

<p><strong>Compatibility note</strong>: rbenv is <em>incompatible</em> with RVM. Please make
  sure to fully uninstall RVM and remove any references to it from
  your shell initialization files before installing rbenv.</p>

<p>If you're on Mac OS X, consider
<a href="#homebrew-on-mac-os-x">installing with Homebrew</a>.</p>

<h3>
<a id="user-content-basic-github-checkout" class="anchor" href="#basic-github-checkout" aria-hidden="true"><span class="octicon octicon-link"></span></a>Basic GitHub Checkout</h3>

<p>This will get you going with the latest version of rbenv and make it
easy to fork and contribute any changes back upstream.</p>

<ol>
<li>
<p>Check out rbenv into <code>~/.rbenv</code>.</p>

<div class="highlight highlight-sh"><pre>$ git clone https://github.com/sstephenson/rbenv.git <span class="pl-k">~</span>/.rbenv</pre></div>
</li>
<li>
<p>Add <code>~/.rbenv/bin</code> to your <code>$PATH</code> for access to the <code>rbenv</code>
command-line utility.</p>

<div class="highlight highlight-sh"><pre>$ <span class="pl-c1">echo</span> <span class="pl-s"><span class="pl-pds">'</span>export PATH="$HOME/.rbenv/bin:$PATH"<span class="pl-pds">'</span></span> <span class="pl-k">&gt;&gt;</span> <span class="pl-k">~</span>/.bash_profile</pre></div>

<p><strong>Ubuntu Desktop note</strong>: Modify your <code>~/.bashrc</code> instead of <code>~/.bash_profile</code>.</p>

<p><strong>Zsh note</strong>: Modify your <code>~/.zshrc</code> file instead of <code>~/.bash_profile</code>.</p>
</li>
<li>
<p>Add <code>rbenv init</code> to your shell to enable shims and autocompletion.</p>

<div class="highlight highlight-sh"><pre>$ <span class="pl-c1">echo</span> <span class="pl-s"><span class="pl-pds">'</span>eval "$(rbenv init -)"<span class="pl-pds">'</span></span> <span class="pl-k">&gt;&gt;</span> <span class="pl-k">~</span>/.bash_profile</pre></div>

<p><em>Same as in previous step, use <code>~/.bashrc</code> on Ubuntu, or <code>~/.zshrc</code> for Zsh.</em></p>
</li>
<li>
<p>Restart your shell so that PATH changes take effect. (Opening a new
terminal tab will usually do it.) Now check if rbenv was set up:</p>

<div class="highlight highlight-sh"><pre>$ <span class="pl-c1">type</span> rbenv
<span class="pl-c">#=&gt; "rbenv is a function"</span></pre></div>
</li>
<li><p><em>(Optional)</em> Install <a href="https://github.com/sstephenson/ruby-build#readme">ruby-build</a>, which provides the
<code>rbenv install</code> command that simplifies the process of
<a href="#installing-ruby-versions">installing new Ruby versions</a>.</p></li>
</ol>

<h4>
<a id="user-content-upgrading" class="anchor" href="#upgrading" aria-hidden="true"><span class="octicon octicon-link"></span></a>Upgrading</h4>

<p>If you've installed rbenv manually using git, you can upgrade your
installation to the cutting-edge version at any time.</p>

<div class="highlight highlight-sh"><pre>$ <span class="pl-c1">cd</span> <span class="pl-k">~</span>/.rbenv
$ git pull</pre></div>

<p>To use a specific release of rbenv, check out the corresponding tag:</p>

<div class="highlight highlight-sh"><pre>$ <span class="pl-c1">cd</span> <span class="pl-k">~</span>/.rbenv
$ git fetch
$ git checkout v0.3.0</pre></div>

<p>If you've <a href="#homebrew-on-mac-os-x">installed via Homebrew</a>, then upgrade
via its <code>brew</code> command:</p>

<div class="highlight highlight-sh"><pre>$ brew update
$ brew upgrade rbenv ruby-build</pre></div>

<h3>
<a id="user-content-homebrew-on-mac-os-x" class="anchor" href="#homebrew-on-mac-os-x" aria-hidden="true"><span class="octicon octicon-link"></span></a>Homebrew on Mac OS X</h3>

<p>As an alternative to installation via GitHub checkout, you can install
rbenv and <a href="https://github.com/sstephenson/ruby-build#readme">ruby-build</a> using the <a href="http://brew.sh">Homebrew</a> package
manager on Mac OS X:</p>

<pre><code>$ brew update
$ brew install rbenv ruby-build
</code></pre>

<p>Afterwards you'll still need to add <code>eval "$(rbenv init -)"</code> to your
profile as stated in the caveats. You'll only ever have to do this
once.</p>

<h3>
<a id="user-content-how-rbenv-hooks-into-your-shell" class="anchor" href="#how-rbenv-hooks-into-your-shell" aria-hidden="true"><span class="octicon octicon-link"></span></a>How rbenv hooks into your shell</h3>

<p>Skip this section unless you must know what every line in your shell
profile is doing.</p>

<p><code>rbenv init</code> is the only command that crosses the line of loading
extra commands into your shell. Coming from RVM, some of you might be
opposed to this idea. Here's what <code>rbenv init</code> actually does:</p>

<ol>
<li><p>Sets up your shims path. This is the only requirement for rbenv to
function properly. You can do this by hand by prepending
<code>~/.rbenv/shims</code> to your <code>$PATH</code>.</p></li>
<li><p>Installs autocompletion. This is entirely optional but pretty
useful. Sourcing <code>~/.rbenv/completions/rbenv.bash</code> will set that
up. There is also a <code>~/.rbenv/completions/rbenv.zsh</code> for Zsh
users.</p></li>
<li><p>Rehashes shims. From time to time you'll need to rebuild your
shim files. Doing this automatically makes sure everything is up to
date. You can always run <code>rbenv rehash</code> manually.</p></li>
<li><p>Installs the sh dispatcher. This bit is also optional, but allows
rbenv and plugins to change variables in your current shell, making
commands like <code>rbenv shell</code> possible. The sh dispatcher doesn't do
anything crazy like override <code>cd</code> or hack your shell prompt, but if
for some reason you need <code>rbenv</code> to be a real script rather than a
shell function, you can safely skip it.</p></li>
</ol>

<p>Run <code>rbenv init -</code> for yourself to see exactly what happens under the
hood.</p>

<h3>
<a id="user-content-installing-ruby-versions" class="anchor" href="#installing-ruby-versions" aria-hidden="true"><span class="octicon octicon-link"></span></a>Installing Ruby Versions</h3>

<p>The <code>rbenv install</code> command doesn't ship with rbenv out of the box, but
is provided by the <a href="https://github.com/sstephenson/ruby-build#readme">ruby-build</a> project. If you installed it either
as part of GitHub checkout process outlined above or via Homebrew, you
should be able to:</p>

<div class="highlight highlight-sh"><pre><span class="pl-c"># list all available versions:</span>
$ rbenv install -l

<span class="pl-c"># install a Ruby version:</span>
$ rbenv install 2.0.0-p247</pre></div>

<p>Alternatively to the <code>install</code> command, you can download and compile
Ruby manually as a subdirectory of <code>~/.rbenv/versions/</code>. An entry in
that directory can also be a symlink to a Ruby version installed
elsewhere on the filesystem. rbenv doesn't care; it will simply treat
any entry in the <code>versions/</code> directory as a separate Ruby version.</p>

<h3>
<a id="user-content-uninstalling-ruby-versions" class="anchor" href="#uninstalling-ruby-versions" aria-hidden="true"><span class="octicon octicon-link"></span></a>Uninstalling Ruby Versions</h3>

<p>As time goes on, Ruby versions you install will accumulate in your
<code>~/.rbenv/versions</code> directory.</p>

<p>To remove old Ruby versions, simply <code>rm -rf</code> the directory of the
version you want to remove. You can find the directory of a particular
Ruby version with the <code>rbenv prefix</code> command, e.g. <code>rbenv prefix
1.8.7-p357</code>.</p>

<p>The <a href="https://github.com/sstephenson/ruby-build#readme">ruby-build</a> plugin provides an <code>rbenv uninstall</code> command to
automate the removal process.</p>

<h2>
<a id="user-content-command-reference" class="anchor" href="#command-reference" aria-hidden="true"><span class="octicon octicon-link"></span></a>Command Reference</h2>

<p>Like <code>git</code>, the <code>rbenv</code> command delegates to subcommands based on its
first argument. The most common subcommands are:</p>

<h3>
<a id="user-content-rbenv-local" class="anchor" href="#rbenv-local" aria-hidden="true"><span class="octicon octicon-link"></span></a>rbenv local</h3>

<p>Sets a local application-specific Ruby version by writing the version
name to a <code>.ruby-version</code> file in the current directory. This version
overrides the global version, and can be overridden itself by setting
the <code>RBENV_VERSION</code> environment variable or with the <code>rbenv shell</code>
command.</p>

<pre><code>$ rbenv local 1.9.3-p327
</code></pre>

<p>When run without a version number, <code>rbenv local</code> reports the currently
configured local version. You can also unset the local version:</p>

<pre><code>$ rbenv local --unset
</code></pre>

<p>Previous versions of rbenv stored local version specifications in a
file named <code>.rbenv-version</code>. For backwards compatibility, rbenv will
read a local version specified in an <code>.rbenv-version</code> file, but a
<code>.ruby-version</code> file in the same directory will take precedence.</p>

<h3>
<a id="user-content-rbenv-global" class="anchor" href="#rbenv-global" aria-hidden="true"><span class="octicon octicon-link"></span></a>rbenv global</h3>

<p>Sets the global version of Ruby to be used in all shells by writing
the version name to the <code>~/.rbenv/version</code> file. This version can be
overridden by an application-specific <code>.ruby-version</code> file, or by
setting the <code>RBENV_VERSION</code> environment variable.</p>

<pre><code>$ rbenv global 1.8.7-p352
</code></pre>

<p>The special version name <code>system</code> tells rbenv to use the system Ruby
(detected by searching your <code>$PATH</code>).</p>

<p>When run without a version number, <code>rbenv global</code> reports the
currently configured global version.</p>

<h3>
<a id="user-content-rbenv-shell" class="anchor" href="#rbenv-shell" aria-hidden="true"><span class="octicon octicon-link"></span></a>rbenv shell</h3>

<p>Sets a shell-specific Ruby version by setting the <code>RBENV_VERSION</code>
environment variable in your shell. This version overrides
application-specific versions and the global version.</p>

<pre><code>$ rbenv shell jruby-1.7.1
</code></pre>

<p>When run without a version number, <code>rbenv shell</code> reports the current
value of <code>RBENV_VERSION</code>. You can also unset the shell version:</p>

<pre><code>$ rbenv shell --unset
</code></pre>

<p>Note that you'll need rbenv's shell integration enabled (step 3 of
the installation instructions) in order to use this command. If you
prefer not to use shell integration, you may simply set the
<code>RBENV_VERSION</code> variable yourself:</p>

<pre><code>$ export RBENV_VERSION=jruby-1.7.1
</code></pre>

<h3>
<a id="user-content-rbenv-versions" class="anchor" href="#rbenv-versions" aria-hidden="true"><span class="octicon octicon-link"></span></a>rbenv versions</h3>

<p>Lists all Ruby versions known to rbenv, and shows an asterisk next to
the currently active version.</p>

<pre><code>$ rbenv versions
  1.8.7-p352
  1.9.2-p290
* 1.9.3-p327 (set by /Users/sam/.rbenv/version)
  jruby-1.7.1
  rbx-1.2.4
  ree-1.8.7-2011.03
</code></pre>

<h3>
<a id="user-content-rbenv-version" class="anchor" href="#rbenv-version" aria-hidden="true"><span class="octicon octicon-link"></span></a>rbenv version</h3>

<p>Displays the currently active Ruby version, along with information on
how it was set.</p>

<pre><code>$ rbenv version
1.9.3-p327 (set by /Users/sam/.rbenv/version)
</code></pre>

<h3>
<a id="user-content-rbenv-rehash" class="anchor" href="#rbenv-rehash" aria-hidden="true"><span class="octicon octicon-link"></span></a>rbenv rehash</h3>

<p>Installs shims for all Ruby executables known to rbenv (i.e.,
<code>~/.rbenv/versions/*/bin/*</code>). Run this command after you install a new
version of Ruby, or install a gem that provides commands.</p>

<pre><code>$ rbenv rehash
</code></pre>

<h3>
<a id="user-content-rbenv-which" class="anchor" href="#rbenv-which" aria-hidden="true"><span class="octicon octicon-link"></span></a>rbenv which</h3>

<p>Displays the full path to the executable that rbenv will invoke when
you run the given command.</p>

<pre><code>$ rbenv which irb
/Users/sam/.rbenv/versions/1.9.3-p327/bin/irb
</code></pre>

<h3>
<a id="user-content-rbenv-whence" class="anchor" href="#rbenv-whence" aria-hidden="true"><span class="octicon octicon-link"></span></a>rbenv whence</h3>

<p>Lists all Ruby versions with the given command installed.</p>

<pre><code>$ rbenv whence rackup
1.9.3-p327
jruby-1.7.1
ree-1.8.7-2011.03
</code></pre>

<h2>
<a id="user-content-environment-variables" class="anchor" href="#environment-variables" aria-hidden="true"><span class="octicon octicon-link"></span></a>Environment variables</h2>

<p>You can affect how rbenv operates with the following settings:</p>

<table>
<thead>
<tr>
<th>name</th>
<th>default</th>
<th>description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>RBENV_VERSION</code></td>
<td></td>
<td>Specifies the Ruby version to be used.<br>Also see <a href="#rbenv-shell"><code>rbenv shell</code></a>
</td>
</tr>
<tr>
<td><code>RBENV_ROOT</code></td>
<td><code>~/.rbenv</code></td>
<td>Defines the directory under which Ruby versions and shims reside.<br>Also see <code>rbenv root</code>
</td>
</tr>
<tr>
<td><code>RBENV_DEBUG</code></td>
<td></td>
<td>Outputs debug information.<br>Also as: <code>rbenv --debug &lt;subcommand&gt;</code>
</td>
</tr>
<tr>
<td><code>RBENV_HOOK_PATH</code></td>
<td><a href="https://github.com/sstephenson/rbenv/wiki/Authoring-plugins#rbenv-hooks"><em>see wiki</em></a></td>
<td>Colon-separated list of paths searched for rbenv hooks.</td>
</tr>
<tr>
<td><code>RBENV_DIR</code></td>
<td><code>$PWD</code></td>
<td>Directory to start searching for <code>.ruby-version</code> files.</td>
</tr>
</tbody>
</table>

<h2>
<a id="user-content-development" class="anchor" href="#development" aria-hidden="true"><span class="octicon octicon-link"></span></a>Development</h2>

<p>The rbenv source code is <a href="https://github.com/sstephenson/rbenv">hosted on
GitHub</a>. It's clean, modular,
and easy to understand, even if you're not a shell hacker.</p>

<p>Tests are executed using <a href="https://github.com/sstephenson/bats">Bats</a>:</p>

<pre><code>$ bats test
$ bats test/&lt;file&gt;.bats
</code></pre>

<p>Please feel free to submit pull requests and file bugs on the <a href="https://github.com/sstephenson/rbenv/issues">issue
tracker</a>.</p>
</article>
  </div>

</div>

<a href="#jump-to-line" rel="facebox[.linejump]" data-hotkey="l" style="display:none">Jump to Line</a>
<div id="jump-to-line" style="display:none">
  <form accept-charset="UTF-8" action="" class="js-jump-to-line-form" method="get"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /></div>
    <input class="linejump-input js-jump-to-line-field" type="text" placeholder="Jump to line&hellip;" autofocus>
    <button type="submit" class="btn">Go</button>
</form></div>

        </div>

      </div><!-- /.repo-container -->
      <div class="modal-backdrop"></div>
    </div><!-- /.container -->
  </div><!-- /.site -->


    </div><!-- /.wrapper -->

      <div class="container">
  <div class="site-footer" role="contentinfo">
    <ul class="site-footer-links right">
        <li><a href="https://status.github.com/" data-ga-click="Footer, go to status, text:status">Status</a></li>
      <li><a href="https://developer.github.com" data-ga-click="Footer, go to api, text:api">API</a></li>
      <li><a href="https://training.github.com" data-ga-click="Footer, go to training, text:training">Training</a></li>
      <li><a href="https://shop.github.com" data-ga-click="Footer, go to shop, text:shop">Shop</a></li>
        <li><a href="https://github.com/blog" data-ga-click="Footer, go to blog, text:blog">Blog</a></li>
        <li><a href="https://github.com/about" data-ga-click="Footer, go to about, text:about">About</a></li>

    </ul>

    <a href="https://github.com" aria-label="Homepage">
      <span class="mega-octicon octicon-mark-github" title="GitHub"></span>
</a>
    <ul class="site-footer-links">
      <li>&copy; 2015 <span title="0.03484s from github-fe119-cp1-prd.iad.github.net">GitHub</span>, Inc.</li>
        <li><a href="https://github.com/site/terms" data-ga-click="Footer, go to terms, text:terms">Terms</a></li>
        <li><a href="https://github.com/site/privacy" data-ga-click="Footer, go to privacy, text:privacy">Privacy</a></li>
        <li><a href="https://github.com/security" data-ga-click="Footer, go to security, text:security">Security</a></li>
        <li><a href="https://github.com/contact" data-ga-click="Footer, go to contact, text:contact">Contact</a></li>
    </ul>
  </div>
</div>


    <div class="fullscreen-overlay js-fullscreen-overlay" id="fullscreen_overlay">
  <div class="fullscreen-container js-suggester-container">
    <div class="textarea-wrap">
      <textarea name="fullscreen-contents" id="fullscreen-contents" class="fullscreen-contents js-fullscreen-contents" placeholder=""></textarea>
      <div class="suggester-container">
        <div class="suggester fullscreen-suggester js-suggester js-navigation-container"></div>
      </div>
    </div>
  </div>
  <div class="fullscreen-sidebar">
    <a href="#" class="exit-fullscreen js-exit-fullscreen tooltipped tooltipped-w" aria-label="Exit Zen Mode">
      <span class="mega-octicon octicon-screen-normal"></span>
    </a>
    <a href="#" class="theme-switcher js-theme-switcher tooltipped tooltipped-w"
      aria-label="Switch themes">
      <span class="octicon octicon-color-mode"></span>
    </a>
  </div>
</div>



    
    

    <div id="ajax-error-message" class="flash flash-error">
      <span class="octicon octicon-alert"></span>
      <a href="#" class="octicon octicon-x flash-close js-ajax-error-dismiss" aria-label="Dismiss error"></a>
      Something went wrong with that request. Please try again.
    </div>


      <script crossorigin="anonymous" src="https://assets-cdn.github.com/assets/frameworks-06533d99d3f0ca9115a0563dec4017e1bfad7758231e12b95a178cef2cdc3d4c.js"></script>
      <script async="async" crossorigin="anonymous" src="https://assets-cdn.github.com/assets/github-59cbed91abaeebed35de0a12f8c3adfea46b14dd56c5019b18a7dcdaf3c88a92.js"></script>
      
      

  </body>
</html>

