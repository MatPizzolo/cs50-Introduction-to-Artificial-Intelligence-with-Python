import csv
import sys

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

TEST_SIZE = 0.4


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python shopping.py data")

    # Load data from spreadsheet and split into train and test sets
    evidence, labels = load_data(sys.argv[1])
    X_train, X_test, y_train, y_test = train_test_split(
        evidence, labels, test_size=TEST_SIZE
    )

    # Train model and make predictions
    model = train_model(X_train, y_train)
    predictions = model.predict(X_test)
    sensitivity, specificity = evaluate(y_test, predictions)

    # Print results
    print(f"Correct: {(y_test == predictions).sum()}")
    print(f"Incorrect: {(y_test != predictions).sum()}")
    print(f"True Positive Rate: {100 * sensitivity:.2f}%")
    print(f"True Negative Rate: {100 * specificity:.2f}%")


def load_data(filename):
    """
    Load shopping data from a CSV file `filename` and convert into a list of
    evidence lists and a list of labels. Return a tuple (evidence, labels).

    evidence should be a list of lists, where each list contains the
    following values, in order:
        - Administrative, an integer
        - Administrative_Duration, a floating point number
        - Informational, an integer
        - Informational_Duration, a floating point number
        - ProductRelated, an integer
        - ProductRelated_Duration, a floating point number
        - BounceRates, a floating point number
        - ExitRates, a floating point number
        - PageValues, a floating point number
        - SpecialDay, a floating point number
        - Month, an index from 0 (January) to 11 (December)
        - OperatingSystems, an integer
        - Browser, an integer
        - Region, an integer
        - TrafficType, an integer
        - VisitorType, an integer 0 (not returning) or 1 (returning)
        - Weekend, an integer 0 (if false) or 1 (if true)

    labels should be the corresponding list of labels, where each label
    is 1 if Revenue is true, and 0 otherwise.
    """

    evidence = []
    labels = []

    months = ["Jan", "Feb", "Mar", "Apr", "May", "June", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

    with open(filename, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            admin = int(row['Administrative'])
            admin_dur = float(row['Administrative_Duration'])
            infor = int(row['Informational'])
            infor_dur = float(row['Informational_Duration'])
            product = int(row['ProductRelated'])
            product_dur = float(row['ProductRelated_Duration'])
            bounce_rate = float(row['BounceRates'])
            exit_rate = float(row['ExitRates'])
            page_value = float(row['PageValues'])
            special_day = float(row['SpecialDay'])
            month = months.index(row['Month'])
            op_sys = int(row['OperatingSystems'])
            browser = int(row['Browser'])
            region = int(row['Region'])
            traffic_type = int(row['TrafficType'])
            visitor_type = int(0 if row['VisitorType'] == "New_Visitor" else 1)
            weekend = int(0 if row['Weekend'] == "FALSE" else 1)
            row_list = [admin, admin_dur, infor, infor_dur, product, product_dur, bounce_rate, exit_rate, page_value, special_day, month, op_sys, browser, region, traffic_type, visitor_type, weekend]
            evidence.append(row_list)

            rev = int(0 if row['Revenue'] == "FALSE" else 1)
            labels.append(rev)

    return (evidence, labels)


def train_model(evidence, labels):
    """
    Given a list of evidence lists and a list of labels, return a
    fitted k-nearest neighbor model (k=1) trained on the data.
    """
    model = KNeighborsClassifier(n_neighbors=1)
    model.fit(evidence, labels)

    return model


def evaluate(labels, predictions):
    """
    Given a list of actual labels and a list of predicted labels,
    return a tuple (sensitivity, specificity).

    Assume each label is either a 1 (positive) or 0 (negative).

    `sensitivity` should be a floating-point value from 0 to 1
    representing the "true positive rate": the proportion of
    actual positive labels that were accurately identified.

    `specificity` should be a floating-point value from 0 to 1
    representing the "true negative rate": the proportion of
    actual negative labels that were accurately identified.
    """

    total_purchases = labels.count(1)
    total_not_purchases = labels.count(0)

    true_positives = 0
    true_negatives = 0
    for actual, predicted in zip(labels, predictions):
        if actual == 1 and predicted == 1:
            true_positives += 1
        elif actual == 0 and predicted == 0:
            true_negatives += 1

    sensitivity = true_positives / total_purchases
    specificity = true_negatives / total_not_purchases

    return (sensitivity, specificity)


if __name__ == "__main__":
    main()
