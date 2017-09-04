#!/bin/env python
#from __future__ import print_function

import json
import numpy as np
from time import time
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.multiclass import OneVsRestClassifier
from sklearn.linear_model import RidgeClassifier
from sklearn.svm import LinearSVC
from sklearn.linear_model import SGDClassifier
from sklearn.linear_model import Perceptron
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.naive_bayes import BernoulliNB, MultinomialNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neighbors import NearestCentroid
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn import metrics
from sklearn import preprocessing
import pickle


# X_N = 2
# X_N = 18000
#Train_S = 0
#Train_E = 18000
#Test_S = 18001
#Test_E = 21027

#sig
#Train_S = 0
#Train_E = 8500
#Test_S = 8501
#Test_E = 10308

#area
Train_S = 0
Train_E = 9000
Test_S = 9001
Test_E = 11000

#with open('./data3-x.json') as f:
#with open('./kind_x.txt') as f:
#with open('./sig_x.txt') as f:
with open('./area_x.txt') as f:
    content = f.readlines()

#with open('./data3-y.json') as f:
#with open('./kind_y.txt') as f:
#with open('./sig_y.txt') as f:
with open('./area_y.txt') as f:
    y_content = f.readlines()

train_x = content[Train_S:Train_E]
train_y_str = y_content[Train_S:Train_E]
train_y = [i.strip().split(",")[0] for i in train_y_str]

test_x = content[Test_S:Test_E]
test_y_str = y_content[Test_S:Test_E]
test_y = [i.strip().split(",")[0] for i in test_y_str]


alldata_file= open('./alldata.txt', 'w')
vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.5, stop_words='english')
#mlb = MultiLabelBinarizer()
mlb = preprocessing.LabelEncoder()

X_train = vectorizer.fit_transform(train_x)
y_train = mlb.fit_transform(train_y)

X_test = vectorizer.transform(test_x)
y_test = mlb.transform(test_y)

feature_names = vectorizer.get_feature_names()
feature_names = np.asarray(feature_names)

classes = open('./classes.txt', 'w')

#print>>classes, ",".join(mlb.classes_)

comp= open('./comp.txt', 'w')
ypred = open('./ypred.txt', 'w')
yt = open('./yt.txt', 'w')
model = open('./model.txt', 'w')

#np.savetxt(yt, y_test, fmt="%d")
cls = mlb.classes_

#print cls

fp_report = open('./report.txt', 'w')
#for vector_df in [0.8]:
#   for kernel_c in [0.01]:
#for vector_df in np.arange(0.5,0.8,0.1):
#    for kernel_c in np.arange(1.0,2.0,0.25):
#        clf = OneVsRestClassifier(SVC(kernel='linear', C=kernel_c))
#        #clf = OneVsRestClassifier(RidgeClassifier(tol=1e-2, solver='sag'))
#        clf.fit(X_train, y_train)
#        #pickle.dump(clf, model)
#        pred = clf.predict(X_test)
#
#        p, r, f, s = metrics.precision_recall_fscore_support(y_test, pred)
#        alldata=np.asarray([p,r,f,s])
#        print "df: %.2f c: %.2f" % (vector_df, kernel_c)
#        print np.true_divide(alldata.sum(1),(alldata!=0).sum(1))
#        print>>alldata_file, "df: %.2f c: %.2f" % (vector_df, kernel_c)
#        print>>alldata_file, alldata.sum(1),(alldata!=0).sum(1)
#        print>>alldata_file, np.true_divide(alldata.sum(1),(alldata!=0).sum(1))
#
#        result_file = "./%.2f_%.2f.txt" % (vector_df, kernel_c)
#        fp = open(result_file, 'w')
#        for i in range(len(cls)):
#            print>>fp, "%s\t%.2f\t%.2f\t%.2f\t%.2f" % (cls[i].strip(), p[i], r[i], f[i], s[i])
#
#        print>>fp_report, metrics.classification_report(y_test, pred, target_names=cls)

#exit(0)

def benchmark(clf_org):
    print('_' * 80)
    print("Training: ")
    print(clf_org)
    #clf = OneVsRestClassifier(clf_org)
    clf = clf_org
    t0 = time()
    clf.fit(X_train, y_train)
    train_time = time() - t0
    print("train time: %0.3fs" % train_time)

    t0 = time()
    pred = clf.predict(X_test)
    test_time = time() - t0
    print("test time:  %0.3fs" % test_time)

    score = metrics.accuracy_score(y_test, pred)
    print("accuracy:   %0.3f" % score)

    print("classification report:")
    print(metrics.classification_report(y_test, pred, target_names=cls))

    clf_descr = str(clf_org).split('(')[0]
    return clf_descr, score, train_time, test_time


results = []
for clf, name in (
        (RidgeClassifier(tol=1e-3, solver="sag"), "Ridge Classifier"),
        (Perceptron(n_iter=1000), "Perceptron"),
        (PassiveAggressiveClassifier(n_iter=1000), "Passive-Aggressive"),
        (KNeighborsClassifier(n_neighbors=20), "kNN"),
        (RandomForestClassifier(n_estimators=50), "Random forest")):
    print('=' * 80)
    print(name)
    results.append(benchmark(clf))

for penalty in ["l2", "l1"]:
    print('=' * 80)
    print("%s penalty" % penalty.upper())
    # Train Liblinear model
    results.append(benchmark(LinearSVC(loss='squared_hinge', penalty=penalty,
                                            dual=False, tol=1e-3)))

    # Train SGD model
    results.append(benchmark(SGDClassifier(alpha=.0001, n_iter=1000,
                                           penalty=penalty)))

# Train SGD with Elastic Net penalty
print('=' * 80)
print("Elastic-Net penalty")
results.append(benchmark(SGDClassifier(alpha=.0001, n_iter=1000,
                                       penalty="elasticnet")))

# Train NearestCentroid without threshold
print('=' * 80)
print("NearestCentroid (aka Rocchio classifier)")
results.append(benchmark(NearestCentroid()))

# Train sparse Naive Bayes classifiers
print('=' * 80)
print("Naive Bayes")
results.append(benchmark(MultinomialNB(alpha=.01)))
results.append(benchmark(BernoulliNB(alpha=.01)))

print('=' * 80)
print("LinearSVC with L1-based feature selection")
# The smaller C, the stronger the regularization.
# The more regularization, the more sparsity.
results.append(benchmark(Pipeline([
  ('feature_selection', LinearSVC(penalty="l1", dual=False, tol=1e-3)),
  ('classification', LinearSVC())
])))

print(results, alldata_file)

#pred = clf.predict(X_train)
#p, r, f, s = metrics.precision_recall_fscore_support(y_train, pred)
#print "precision, recall, fscore, support"
#for i in range(len(cls)):
#    print "%s\t%.2f\t%.2f\t%.2f\t%.2f" % (cls[i].strip(), p[i], r[i], f[i], s[i])
#

#np.savetxt(ypred, pred, fmt="%d")
#
#for i in range(len(pred)):
#    print>>comp, i
#    print>>comp, test_y_str[i]
#    for j in range(len(pred[i])):
#        if pred[i][j] == 1:
#            print>>comp, mlb.classes_[j]
#


