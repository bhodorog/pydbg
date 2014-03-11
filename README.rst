=====
Goal
=====

Investigate different options to connect to a running python process and investigate its state. Extra debugging capabilities would be an extra bonus (e.g breakpoints). Consider blocking, non-blocking aspects of the problem

=======
Context
=======

The need for this project appeared when for "mysterious reasons" a python web app started to behave non-deterministic (e.g. reloading the same admin page produced different <option>(s) for the same <select> element). Gorry details of the app:

* apache modwsgi (daemon mode, 1 thread per process)
* django
* mysql, memcache


Investigations lead to the fact that a module wide object (django.contrib.admin.sites.site) was initialized differently for different wsgi daemons. So the logical approach was to find a way to monitor the state of that object.

============
Alternatives
============

Method 1
---------
blocking, cpython std lib, controlling tty

locals needs to be properly initialized for the launched REPL. (e.g. if you pass sys around you'll have access to sys._get_frames(1).func_globals)

Pure cpython
+++++++++++
Target process needs to have a controlling terminal and would be nice to be able to connect to it.
The example implementation is using signals to intrerupt the running process.

Embeded cpython
++++++++++++++

Method 2 
----------
blocking, ipython, tty independent

Pure cpython
+++++++++++
IPython supports a nice way of starting an embeded IPython kernel, to which you can connect using:

```
ipython console --existing

This mechanism is based on zeromq IPC communication. The nice thing is that you don't need to maneuvre around a tty, you just use your current tty.
The trick is that as soon as the ipython kernel is started the process is blocked. The example implementation is using signals to intrerupt the running process.

TODO: how to quit the remote console and resume the target process?

Embeded cpython
++++++++++++++

Method 3
----------
non-blocking, greenlets, tty independent

Pure cpython
+++++++++++
Uses the backdoor offered by greenthreads libraries (eventlet, gevent).
With this approach the process remains non-blocked. On the other hand this means is harder to debug (suspend on breakpoint, sounds like more work). Though may be usefull in environmnents which can't afford having blocked processes.
Lack of readline is quite inconvenient, since you don't have history navigation. Maybe this can be solved. TODO: use readline for backdoor connection.
By default the namespace is not initialized which means is harder to inspect, the main alternatives are:
1. import gc; gc.get_objects
2. pass local argument to backdoor (e.g. use ipython example https://github.com/ipython/ipython/blob/master/IPython/utils/frame.py)

Embeded cpython
++++++++++++++
