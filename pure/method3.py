import sys
from datetime import datetime

import eventlet
import eventlet.greenthread
from eventlet import backdoor


def _loop():
    while True:
        print "{0} Looping forever ...".format(datetime.utcnow())
        eventlet.greenthread.sleep(1)


def _find_objects(klass):
    import gc
    return filter(lambda obj: isinstance(obj, klass), gc.get_objects())


def main():
    backdoor_thr = eventlet.spawn(
        backdoor.backdoor_server, eventlet.listen(("localhost", 3000)),
        locals={'sys': sys,
                'fo': '_find_objects'})
    main_thr = eventlet.spawn(_loop)
    backdoor_thr.wait()
    main_thr.wait()


# Dummy objects defined to try the namespace of the debuger
class Foo(object):
    def __init__(self, val):
        self.val = val


global_foo = Foo("global")


if __name__ == "__main__":
    main()
