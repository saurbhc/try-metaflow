from metaflow import FlowSpec, step


class CounterFlow(FlowSpec):

    @step
    def start(self):
        self.count = 0
        self.count += 1
        print('this is start step', self.count)
        self.next(self.hello)

    @step
    def hello(self):
        self.count += 1
        print('this is hello', self.count)
        self.next(self.end_maybe)

    @step
    def end_maybe(self):
        self.count += 1
        print('this is end', self.count)
        self.next(self.decide_for_me())

    def decide_for_me(self):
        print('deciding...', self.count)
        if self.count == 10:
            return self.end
        else:
            return self.hello

    @step
    def end(self):
        print('end finally.')


if __name__ == '__main__':
    CounterFlow()
