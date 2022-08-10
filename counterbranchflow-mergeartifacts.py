from metaflow import FlowSpec, Parameter, step


class CounterBranchFlow(FlowSpec):

    @step
    def start(self):
        self.creature = "dog"
        self.count = 0
        self.height = 0
        print(f"{self.count=}")
        self.next(
            self.add_one,
            self.add_two
        )

    @step
    def add_one(self):
        self.count += 1
        self.height += 1
        print(f"{self.count=}")
        self.next(self.join)

    @step
    def add_two(self):
        self.count += 2
        self.height += 2
        print(f"{self.count=}")
        self.next(self.join)

    @step
    def join(self, inputs):
        self.count = max(inp.count for inp in inputs)
        print(f"{self.count=} , {inputs.add_one.count=} , {inputs.add_two.count=} , {inputs}")
        #self.creature = inputs[0].creature
        self.merge_artifacts(inputs)
        self.next(self.end)

    @step
    def end(self):
        print(f"{self.count=} {self.creature=} {self.height=}")


if __name__ == "__main__":
    CounterBranchFlow()

