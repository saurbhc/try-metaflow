from metaflow import FlowSpec, step


class HelloWorldFlow(FlowSpec):

    @step
    def start(self):
        print('this is start step')
        self.next(self.hello)

    @step
    def hello(self):
        print('this is hello')
        self.next(self.end)

    @step
    def end(self):
        print('this is end')


if __name__ == '__main__':
    HelloWorldFlow()

