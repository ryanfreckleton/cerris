#############################
Notes on Upgrading to Mint 18
#############################
:date: 2016-08-12

I've upgraded my laptop to Linux Mint 18, using XFCE, of course.
This time I'm attempting to keep it in better sync with my dekstop through the use of vcsh and myrepos.

The changes I had ot make were the standard modifications to the panel and using the Mist-X look and feel.

There's a misconfiguration with the XFCE shortcuts that prevents me from making my own.
The solution, as described in the following `here`__, `here`__ and `here`__ is to delete the

::

    /usr/share/mint-configuration-xfce/xfce4/xfconf/xfce-perchannel-xml/xfce4-keyboard-shortcuts.xml

file.


They did fix the key-up triggering the whisker menu instead of keydown, however it still didn't work with my preferred hotkeys for switching virtual desktops.

__ http://unix.stackexchange.com/questions/44643/xfce-4-change-global-keyboard-shortcuts
__ http://unix.stackexchange.com/questions/152897/cannot-change-global-keyboard-shortcuts-in-linux-mint-xfce
__ httpe://forums.linuxmint.com/viewtopic.php?t=172333
