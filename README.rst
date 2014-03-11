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

Pure cpython
+++++++++++

Embeded cpython
++++++++++++++

Method 2 
----------
blocking, ipython, tty independent

Pure cpython
+++++++++++

Embeded cpython
++++++++++++++

Method 3
----------
non-blocking, greenlets, tty independent

Pure cpython
+++++++++++

Embeded cpython
++++++++++++++
