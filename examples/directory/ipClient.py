# Fetch your external IP


import quark_twisted_runtime
import ipify


class Consumer(object):
    def __init__(self, runtime):
        self.runtime = runtime

    def consume(self, ip):
        print "IP is", ip
        self.runtime.finish()


def main():
    runtime = quark_twisted_runtime.get_twisted_runtime()
    ipify.MyExternalIP(runtime, Consumer(runtime))
    runtime.launch()


if __name__ == '__main__':
    main()