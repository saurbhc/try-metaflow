from metaflow import Flow


if __name__ == "__main__":
    for step in Flow('ClassifierTrainFlow').latest_run:
        for task in step:
            if not task.successful:
                print(f"Task {task.pathspec} failed")
                print("-- Stdout --")
                print(task.stdout)
                print("-- Stderr --")
                print(task.stderr)

