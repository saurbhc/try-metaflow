from metaflow import FlowSpec, step


class ForEachFlow(FlowSpec):

    @step
    def start(self):
        self.creatures = ['bird', 'mouse', 'dog'] * 100
        self.next(self.analyze_creature, foreach='creatures')

    @step
    def analyze_creature(self):
        print('Analyzing creatures', self.input)
        self.creature = self.input
        self.score = len(self.creature)
        self.next(self.join)

    @step
    def join(self, inputs):
        self.best = max(inputs, key=lambda x: x.score).creature
        self.next(self.end)

    @step
    def end(self):
        print(self.best, 'won!')


if __name__ == "__main__":
    """
        python foreachflow-bignumbers.py run --max-num-splits 300 --max-workers 3
    """
    ForEachFlow()

