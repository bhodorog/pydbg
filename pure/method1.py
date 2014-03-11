import code
import signal
import sys
import time
from datetime import datetime


def _loop():
    while True:
        print "{0} Looping forever ...".format(datetime.utcnow())
        time.sleep(1)


def _block_on_repl(sig, frame):
    local = globals()
    local.update({'sys': sys})
    code.interact("Blocked on std cpython REPL. Ctrl-D to resume...",
                  local=local)


def _init_debug():
    signal.signal(signal.SIGUSR2, _block_on_repl)


def main():
    foo = Foo("local to main")
    _init_debug()
    _loop()


class Foo(object):
    def __init__(self, val):
        self.val = val


global_foo = Foo("global")


if __name__ == "__main__":
    main()
