#!/bin/env python

from sklearn import metrics
import json
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import SVC
import pickle


y = np.loadtxt('yt.txt')
yp = np.loadtxt('ypred.txt')
f = open('classes.txt','r')
cls = f.read().split(',')

print "accuracy"
print metrics.accuracy_score(y, yp)

p, r, f, s = metrics.precision_recall_fscore_support(y, yp)
print "precision, recall, fscore, support"
for i in range(len(cls)):
    print "%s\t%.2f\t%.2f\t%.2f\t%.2f" % (cls[i].strip(), p[i], r[i], f[i], s[i])


X_N = 18000
model = open('./model.txt', 'r')

with open('./data3-x.json') as f:
    content = f.readlines()

with open('./data3-y.json') as f:
    y_content = f.readlines()


train_x = content[0:X_N]
train_y_str = y_content[0:X_N]
train_y = [i.strip().split(",") for i in train_y_str]


vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.5, stop_words='english')
mlb = MultiLabelBinarizer()

X_train = vectorizer.fit_transform(train_x)
y_train = mlb.fit_transform(train_y)

clf = pickle.load(model)
pred = clf.predict(X_train)

p, r, f, s = metrics.precision_recall_fscore_support(y_train, pred)
print "precision, recall, fscore, support"
for i in range(len(cls)):
    print "%s\t%.2f\t%.2f\t%.2f\t%.2f" % (cls[i].strip(), p[i], r[i], f[i], s[i])


