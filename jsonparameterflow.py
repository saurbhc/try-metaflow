from metaflow import FlowSpec, Parameter, step, JSONType


class JSONParameterFlow(FlowSpec):

    mapping = Parameter(
        "mapping",
        help="Specify a mapping",
        default='{"some": "default"}',
        type=JSONType
    )

    @step
    def start(self):
        print('start...')
        for key, value, in self.mapping.items():
            print(key, value)
        self.next(self.end)

    @step
    def end(self):
        print('end...')



if __name__ == "__main__":
    JSONParameterFlow()

