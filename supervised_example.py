import random
from pandas import read_csv
from sklearn import tree
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split

# Main Function

# Sets random seed to increase repeatability
random.seed(42)

if __name__ == "__main__":
    
    # 0) Load Dataset (Library: PANDAS / NUMPY)

    my_dataset = read_csv("labelled_dataset.csv")
    label_obj = my_dataset["label"]
    data_obj = my_dataset.drop(columns=["time", "datetime", "label"])

    # 1) Split Dataset

    train_data, test_data, train_label, test_label = train_test_split(data_obj, label_obj, test_size = 0.5)

    # 2) Choose Classifier (Library: SCIKIT LEARN)

    # Algorithm: Decision Tree in general
    # Model: Decision Tree trained on the train data set (= Result of training the algorithm)

    clf = tree.DecisionTreeClassifier()

    # 3) Train Classifier

    clf = clf.fit(train_data, train_label)

    # 4) Test Classifier

    predicted_labels = clf.predict(test_data)
    acc_score = accuracy_score(test_label, predicted_labels)
    print("Accuracy: " + str(acc_score))

    tn, fp, fn, tp = confusion_matrix(test_label, predicted_labels).ravel()
    print("TP: "+str(tp)+" TN: "+str(tn)+" FP: "+str(fp)+" FN: "+str(fn))