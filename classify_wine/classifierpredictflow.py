from metaflow import FlowSpec, step, Parameter, JSONType, Flow


class ClassifierPredictFlow(FlowSpec):

    vector = Parameter(
        'vector',
        type=JSONType,
        required=True
    )

    @step
    def start(self):
        run = Flow('ClassifierTrainFlow').latest_run
        self.train_run_id = run.pathspec
        self.model = run['end'].task.data.model
        print("Input Vector: ", self.vector)
        self.next(self.end)

    @step
    def end(self):
        print('Model: ', self.model)


if __name__ == "__main__":
    ClassifierPredictFlow()

