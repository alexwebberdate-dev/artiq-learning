from artiq.experiment import *
import numpy as np
import time

class Fake_Measurement(EnvExperiment):
    def build(self):
        self.setattr_argument("npoints", NumberValue(default=50, precision=0, step=1))
        self.setattr_argument("tau", NumberValue(default=10))

    def run(self):
        n = int(self.npoints)
        self.set_dataset("signal", np.full(n, np.nan),
                             broadcast = True)
            
        for i in range(n):
                value = np.exp(-i /self.tau) + np.random.normal(0, 0.02)
                self.mutate_dataset("signal", i, value)
                time.sleep(0.1)