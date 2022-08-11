from metaflow import Flow


if __name__ == "__main__":
    run = Flow('ClassifierTrainFlow').latest_run
    print(f"{run['start'].task.data.train_data=}")
    print(f"{run['start'].task.created_at}")
    print(f"{help(run)}")
