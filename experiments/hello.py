from artiq.experiment import *

class Hello(EnvExperiment):
    def build(self):
        self.setattr_argument("count", NumberValue(default=10, precision=0, step=1))

    def run(self):
        for i in range(int(self.count)):
            print("Hello ARTIQ", i)
