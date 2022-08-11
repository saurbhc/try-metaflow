from metaflow import FlowSpec, step
import os

global_value = 5

class ProcessDemoFlow(FlowSpec):

    @step
    def start(self):
        global global_value
        global_value = 9

        print(f"process id: {os.getpid()}")
        print(f"global_value is: {global_value}")
        
        self.next(self.end)

    @step
    def end(self):
        print(f"process id: {os.getpid()}")
        print(f"global_value is: {global_value}")


if __name__ == "__main__":
    ProcessDemoFlow()

