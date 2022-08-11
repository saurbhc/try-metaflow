from metaflow import Flow
from sklearn import metrics
import matplotlib.pyplot as plt


if __name__ == "__main__":
 
    run = Flow('ClassifierTrainFlow').latest_run
    model, score = run.data.results[0]
    test_data = run['start'].task.data.test_data
    test_labels = run['start'].task.data.test_labels
    metrics.plot_confusion_matrix(model, test_data, test_labels)
    plt.show()
    
