#importing a 3-class dataset from sklearn's toy dataset
from sklearn.datasets import load_wine

# Test Data
# [[2357, 20, 7], [8, 8, 2], [8, 8, 318]]
#
# Accuracy: 0.981
#
# Micro Precision: 0.981
# Micro Recall: 0.981
# Micro F1-score: 0.981
#
# Weighted Precision: 0.977
# Weighted Recall: 0.981
# Weighted F1-score: 0.978
#
# Classification Report
#
#              precision    recall  f1-score   support
#
#    Positive      0.989     0.993     0.991      2373
#    Possible      0.444     0.222     0.296        36
#    Negative      0.952     0.972     0.962       327
#
# avg / total      0.977     0.981     0.978      2736
def metrics(confusion, print_bool):
    if print_bool:
        print('Confusion Matrix\n')
        print(confusion[0])
        print(confusion[1])
        print(confusion[2])
    y_test = []
    y_pred = []
    #From the confusion matrix, create a y_test and y_pred
    for i in range(0,3):
        num_actual = 0
        for j in range(0,3):
            num_actual += confusion[j][i]
        for _ in range(0, num_actual):
            y_test.append(i)
        for j in range(0,3):
            for _ in range(confusion[j][i]):
                y_pred.append(j)


    #importing accuracy_score, precision_score, recall_score, f1_score
    from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
    if print_bool:
        print('\nAccuracy: {:3.3f}\n'.format(accuracy_score(y_test, y_pred)))

        print('Micro Precision: {:3.3f}'.format(precision_score(y_test, y_pred, average='micro')))
        print('Micro Recall: {:3.3f}'.format(recall_score(y_test, y_pred, average='micro')))
        print('Micro F1-score: {:3.3f}\n'.format(f1_score(y_test, y_pred, average='micro')))

        print('Weighted Precision: {:3.3f}'.format(precision_score(y_test, y_pred, average='weighted')))
        print('Weighted Recall: {:3.3f}'.format(recall_score(y_test, y_pred, average='weighted')))
        print('Weighted F1-score: {:3.3f}'.format(f1_score(y_test, y_pred, average='weighted')))

        from sklearn.metrics import classification_report
        print('\nClassification Report\n')
        print(classification_report(y_test, y_pred, target_names=['Positive', 'Possible', 'Negative'], digits=3))
    return precision_score(y_test, y_pred, average='weighted'), recall_score(y_test, y_pred, average='weighted'), f1_score(y_test, y_pred, average='weighted')
