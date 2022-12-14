from metaflow import FlowSpec, Parameter, step

class ParameterFlow(FlowSpec):
    animal = Parameter(
        "creature",
        help="Specify a creature",
        required=True
    )

    count = Parameter(
        "count",
        help="Number of creatures",
        default=1
    )

    ratio = Parameter(
        "ratio",
        help="Ratio between 0.0 and 1.0",
        type=float
    )

    @step
    def start(self):
        print(self.animal, self.count, self.ratio)
        self.next(self.end)

    @step
    def end(self):
        print(self.animal, self.count, self.ratio)


if __name__ == "__main__":
    ParameterFlow()

