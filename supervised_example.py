from pandas import read_csv
from sklearn.model_selection import train_test_split

# Main Function
first_time = True
if __name__ == "__main__":
    
    # 0) Load Dataset (Library: PANDAS / NUMPY)

    my_dataset = read_csv("./labelled_dataset.csv")
    label_obj = my_dataset["label"]
    data_obj = my_dataset.drop(columns="label")

    # 1) Split Dataset

    train_data, train_label, test_data, test_label = train_test_split(data_obj, label_obj, test_size = 0.5)

    # 2) Choose Classifier (Library: SCIKIT LEARN)

    # 3) Train Classifier

    # 4) Test Classifier

    a = 1

    pass