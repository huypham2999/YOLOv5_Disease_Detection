from sklearn.metrics import roc_curve, auc
import numpy as np
import matplotlib.pyplot as plt
from itertools import cycle

# scores = [0.88,0.87,0.74,0.74,0.84,0.85,0.88,0.88,0.79,0.87,0.86,0.85,0.88,0.87,0.88,0.82,0.88,0.88,0.81,0.8,0.81,0.76,0.78,0.21,0.87]
# y_true = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
thres = [1,0.95,0.9,0.85,0.8,0.75,0.7,0.65,0.6,0.55,0.5,0.45,0.4,0.35,0.3,0.25,0.2,0.15,0.1,0.05,0]
'''Healthy
scores = [0.88,0.92,0.74,0.92,0.91,0.88,0.76,0.76,0.76,0.67,0.69,0.94,0.9,0.94,0.86,0.91,0.93,0.94,0.79,0.92,0.85,0.91,0.7,0.92,0.78,0.93,0.91,0.86,0.91,0.92,0.9,0.65,0.93,0.69,0.92,0.88,0.84,0.78,0.88,0.86]
y_true =[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]'''
'''Bacterial
scores = [0.91,0.76,0.9,0.91,0.94,0.53,0.7,0.91,0.77,0.92,0.76,0.83,0.94,0.74,0.95,0.69,0.94,0.9,0.83,0.93,0.92,0.91,0.76,0.9,0.94,0.9,0.53,0.88,0.93,0.94,0.93,0.62,0.92,0.88,0.73,0.96,0.89,0.9,0.89,0.67]
y_true =[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]'''
'''Yellow
scores = [0.72,0.76,0.73,0.93,0.82,0.72,0.91,0.7,0.76,0.89,0.87,0.9,0.67,0.74,0.9,0.66,0.85,0.92,0.93,0.8,0.63,0.83,0.77,0.85,0.66,0.94,0.81,0.76,0.84,0.56,0.81,0.81,0.95,0.87,0.88,0.66,0.9,0.92,0.85,0.64]
y_true =[3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3]'''
'''Late
scores = [0.94,0.74,0.83,0.88,0.69,0.87,0.91,0.87,0.72,0.93,0.72,0.87,0.9,0.82,0.85,0.9,0.92,0.92,0.33,0.94,0.84,0.84,0.82,0.86,0.82,0.9,0.93,0.87,0.87,0.75,0.9,0.92,0.91,0.79,0.9,0.86,0.3,0.92,0.93,0.81]
y_true =[4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4]'''
#data01
# scores =[0.9,0.92,0.92,0.91,0.92,0.9,0.68,0.83,0.93,0.91,0.92,0.84,0.73,0.85,0.69,0.74,0.79,0.84,0.92,0.87,0.92,0.93,0.85,0.91,0.91,0.91,0.91,0.92,0.91,0.85,0.88,0.71,0.7,0.87,0.86,0.87,0.86,0.81,0.85,0.84,0.88,0.87,0.74,0.74,0.84,0.85,0.88,0.88,0.79,0.87,0.86,0.85,0.88,0.87,0.88,0.82,0.88,0.88,0.81,0.8,0.81,0.76,0.78,0.21,0.86,0.88,0.87,0.87,0.85,0.85,0.15,1,0.89,0.89,0.85,0.78,0.85,0.88,0.83,0.8,0.7,0.86,0.79,0.84,0.76,0.85,0.82,0.83,0.85,0.88,0.48,0.89,0.38,0.86,0.76,0.72,0.72,0.82,0.82,0.84,0.86,0.86,0.85,0.56,0.8,0.9,0.81,0.89,0.81,0.78,0.84,0.8,0.83,0.86,0.82,0.85,0.74,0.73,0.52,0.52,0.81,0.81,0.89,0.89,0.88,0.87,0.87,0.86,0.81,0.81,0.87,0.87,0.84,0.86,0.86,0.5,0.88,0.86,0.86,0.8,0.8,0.87,0.7,0.87,0.87,0.82,0.82,0.88,0.87,0.7,0.7,0.92,0.84,0.87,0.86,0.87,0.87,0.86,0.86,0.84,0.9,0.83,0.87,0.86,0.82,0.87,0.77,0.86,0.89,0.84,0.82,0.87,0.88,0.86,0.85,0.84,0.86,0.83,0.82,0.77,0.74,0.86,0.77,0.86,0.89,0.89,0.89,0.89,0.87,0.88,0.77,0.81,0.73,0.74,0.76,0.78,0.74,0.78,0.81,0.76]
# y_true = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,22,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,33,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,44,4,4,4,4,4,4,4,4,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]

#data02
#scores = [0.88,0.92,0.74,0.92,0.91,0.88,0.76,0.76,0.76,0.67,0.69,0.94,0.9,0.94,0.86,0.91,0.93,0.94,0.79,0.92,0.85,0.91,0.7,0.92,0.78,0.93,0.91,0.86,0.91,0.92,0.9,0.65,0.93,0.69,0.92,0.88,0.84,0.78,0.88,0.86,0.91,0.76,0.9,0.91,0.94,0.53,0.7,0.91,0.77,0.92,0.76,0.83,0.94,0.74,0.95,0.69,0.94,0.9,0.83,0.93,0.92,0.91,0.76,0.9,0.94,0.9,0.53,0.88,0.93,0.94,0.93,0.62,0.92,0.88,0.73,0.96,0.89,0.9,0.89,0.67,0.72,0.76,0.73,0.93,0.82,0.72,0.91,0.7,0.76,0.89,0.87,0.9,0.67,0.74,0.9,0.66,0.85,0.92,0.93,0.8,0.63,0.83,0.77,0.85,0.66,0.94,0.81,0.76,0.84,0.56,0.81,0.81,0.95,0.87,0.88,0.66,0.9,0.92,0.85,0.64,0.94,0.74,0.83,0.88,0.69,0.87,0.91,0.87,0.72,0.93,0.72,0.87,0.9,0.82,0.85,0.9,0.92,0.92,0.33,0.94,0.84,0.84,0.82,0.86,0.82,0.9,0.93,0.87,0.87,0.75,0.9,0.92,0.91,0.79,0.9,0.86,0.3,0.92,0.93,0.81]
#y_true = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4]
#y_pred = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,2,2]
'''
#Healthy vs all
scores_healthy = [0.88,0.92,0.74,0.92,0.91,0.88,0.76,0.76,0.76,0.67,0.69,0.94,0.9,0.94,0.86,0.91,0.93,0.94,0.79,0.92,0.85,0.91,0.7,0.92,0.78,0.93,0.91,0.86,0.91,0.92,0.9,0.65,0.93,0.69,0.92,0.88,0.84,0.78,0.88,0.86]
scores_all = [0.91,0.76,0.9,0.91,0.94,0.53,0.7,0.91,0.77,0.92,0.76,0.83,0.94,0.74,0.95,0.69,0.94,0.9,0.83,0.93,0.92,0.91,0.76,0.9,0.94,0.9,0.53,0.88,0.93,0.94,0.93,0.62,0.92,0.88,0.73,0.96,0.89,0.9,0.89,0.67,0.72,0.76,0.73,0.93,0.82,0.72,0.91,0.7,0.76,0.89,0.87,0.9,0.67,0.74,0.9,0.66,0.85,0.92,0.93,0.8,0.63,0.83,0.77,0.85,0.66,0.94,0.81,0.76,0.84,0.56,0.81,0.81,0.95,0.87,0.88,0.66,0.9,0.92,0.85,0.64,0.94,0.74,0.83,0.88,0.69,0.87,0.91,0.87,0.72,0.93,0.72,0.87,0.9,0.82,0.85,0.9,0.92,0.92,0.33,0.94,0.84,0.84,0.82,0.86,0.82,0.9,0.93,0.87,0.87,0.75,0.9,0.92,0.91,0.79,0.9,0.86,0.3,0.92,0.93,0.81]
y_true_healthy = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
y_true_all = [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4]
#y_pred = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]
'''
'''
#Bacterial vs all
scores_bacterial = [0.91,0.76,0.9,0.91,0.94,0.53,0.7,0.91,0.77,0.92,0.76,0.83,0.94,0.74,0.95,0.69,0.94,0.9,0.83,0.93,0.92,0.91,0.76,0.9,0.94,0.9,0.53,0.88,0.93,0.94,0.93,0.62,0.92,0.88,0.73,0.96,0.89,0.9,0.89,0.67]
scores_all = [0.88,0.92,0.74,0.92,0.91,0.88,0.76,0.76,0.76,0.67,0.69,0.94,0.9,0.94,0.86,0.91,0.93,0.94,0.79,0.92,0.85,0.91,0.7,0.92,0.78,0.93,0.91,0.86,0.91,0.92,0.9,0.65,0.93,0.69,0.92,0.88,0.84,0.78,0.88,0.86,0.72,0.76,0.73,0.93,0.82,0.72,0.91,0.7,0.76,0.89,0.87,0.9,0.67,0.74,0.9,0.66,0.85,0.92,0.93,0.8,0.63,0.83,0.77,0.85,0.66,0.94,0.81,0.76,0.84,0.56,0.81,0.81,0.95,0.87,0.88,0.66,0.9,0.92,0.85,0.64,0.94,0.74,0.83,0.88,0.69,0.87,0.91,0.87,0.72,0.93,0.72,0.87,0.9,0.82,0.85,0.9,0.92,0.92,0.33,0.94,0.84,0.84,0.82,0.86,0.82,0.9,0.93,0.87,0.87,0.75,0.9,0.92,0.91,0.79,0.9,0.86,0.3,0.92,0.93,0.81]
'''
'''
#Yellow vs all
scores_yellow = [0.72,0.76,0.73,0.93,0.82,0.72,0.91,0.7,0.76,0.89,0.87,0.9,0.67,0.74,0.9,0.66,0.85,0.92,0.93,0.8,0.63,0.83,0.77,0.85,0.66,0.94,0.81,0.76,0.84,0.56,0.81,0.81,0.95,0.87,0.88,0.66,0.9,0.92,0.85,0.64]
scores_all = [0.88,0.92,0.74,0.92,0.91,0.88,0.76,0.76,0.76,0.67,0.69,0.94,0.9,0.94,0.86,0.91,0.93,0.94,0.79,0.92,0.85,0.91,0.7,0.92,0.78,0.93,0.91,0.86,0.91,0.92,0.9,0.65,0.93,0.69,0.92,0.88,0.84,0.78,0.88,0.86,0.91,0.76,0.9,0.91,0.94,0.53,0.7,0.91,0.77,0.92,0.76,0.83,0.94,0.74,0.95,0.69,0.94,0.9,0.83,0.93,0.92,0.91,0.76,0.9,0.94,0.9,0.53,0.88,0.93,0.94,0.93,0.62,0.92,0.88,0.73,0.96,0.89,0.9,0.89,0.67,0.94,0.74,0.83,0.88,0.69,0.87,0.91,0.87,0.72,0.93,0.72,0.87,0.9,0.82,0.85,0.9,0.92,0.92,0.33,0.94,0.84,0.84,0.82,0.86,0.82,0.9,0.93,0.87,0.87,0.75,0.9,0.92,0.91,0.79,0.9,0.86,0.3,0.92,0.93,0.81]
'''
'''
#Late vs all
scores_late = [0.94,0.74,0.83,0.88,0.69,0.87,0.91,0.87,0.72,0.93,0.72,0.87,0.9,0.82,0.85,0.9,0.92,0.92,0.33,0.94,0.84,0.84,0.82,0.86,0.82,0.9,0.93,0.87,0.87,0.75,0.9,0.92,0.91,0.79,0.9,0.86,0.3,0.92,0.93,0.81]
scores_all = [0.88,0.92,0.74,0.92,0.91,0.88,0.76,0.76,0.76,0.67,0.69,0.94,0.9,0.94,0.86,0.91,0.93,0.94,0.79,0.92,0.85,0.91,0.7,0.92,0.78,0.93,0.91,0.86,0.91,0.92,0.9,0.65,0.93,0.69,0.92,0.88,0.84,0.78,0.88,0.86,0.91,0.76,0.9,0.91,0.94,0.53,0.7,0.91,0.77,0.92,0.76,0.83,0.94,0.74,0.95,0.69,0.94,0.9,0.83,0.93,0.92,0.91,0.76,0.9,0.94,0.9,0.53,0.88,0.93,0.94,0.93,0.62,0.92,0.88,0.73,0.96,0.89,0.9,0.89,0.67,0.72,0.76,0.73,0.93,0.82,0.72,0.91,0.7,0.76,0.89,0.87,0.9,0.67,0.74,0.9,0.66,0.85,0.92,0.93,0.8,0.63,0.83,0.77,0.85,0.66,0.94,0.81,0.76,0.84,0.56,0.81,0.81,0.95,0.87,0.88,0.66,0.9,0.92,0.85,0.64]
'''

#Healthy vs all test2
scores_healthy = [0.88,0.92,0.74,0.92,0.91,0.88,0.76,0.76,0.76,0.67,0.69,0.94,0.9,0.94,0.86,0.91,0.93,0.94,0.79,0.92,0.85,0.91,0.7,0.92,0.78,0.93,0.91,0.86,0.91,0.92,0.9,0.65,0.93,0.69,0.92,0.88,0.84,0.78,0.88,0.86]
scores_all = [0.88,0.93,0.94,0.93,0.62,0.92,0.88,0.73,0.96,0.89,0.9,0.89,0.67,0.76,0.84,0.56,0.81,0.81,0.95,0.87,0.88,0.66,0.9,0.92,0.85,0.64,0.86,0.82,0.9,0.93,0.87,0.87,0.75,0.9,0.92,0.91,0.79,0.9,0.86,0.3]



TP = np.zeros(len(thres), dtype = int)
FN = np.zeros(len(thres), dtype = int)
TN = np.zeros(len(thres), dtype = int)
FP = np.zeros(len(thres), dtype = int)
a = 0
b = 0

n1 = 1
n2 = 2
n3 = 3
n4 = 4

for x in thres:
    for i in scores_healthy:
        if (i >= x):
            TP[a] += 1
        else:
            FN[a] += 1
    for i in scores_all:
        if (1-i >= x):
            FP[a] += 1
        else:
            TN[a] += 1
    a += 1

print('TP =',TP)
print('FP =',FP)
print('FN =',FN)
print('TN =',TN)



# print('True labels:')
# print(y_true)
# print('\nScores:')
# print(scores)

# fpr, tpr, thresholds = roc_curve(y_true, scores, pos_label = 1)
# print('\nThreshold:')
# print(thresholds)
# print('True Positive Rate:')
# print(tpr)
# print('False Positive Rate:')
# print(fpr)

# plt.figure()
# lw = 2
# plt.plot(fpr, tpr, color='darkorange',
#          lw=lw, label='ROC curve (area = %0.2f)' % auc(fpr, tpr))
# plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
# plt.xlim([0.0, 1.0])
# plt.ylim([0.0, 1.05])
# plt.xlabel('False Positive Rate')
# plt.ylabel('True Positive Rate')
# plt.title('Receiver operating characteristic example')
# plt.legend(loc="lower right")
# plt.show()






