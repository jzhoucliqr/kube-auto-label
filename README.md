Quick and dirty tryout with multiple classifiers for kubernetes PR auto labeling.

Results eg:
```
================================================================================
Ridge Classifier
________________________________________________________________________________
Training:
RidgeClassifier(alpha=1.0, class_weight=None, copy_X=True, fit_intercept=True,
        max_iter=None, normalize=False, random_state=None, solver='sag',
        tol=0.001)
train time: 13.693s
test time:  0.041s
accuracy:   0.548
classification report:
    precision    recall  f1-score   support

    area/HA       0.69      0.55      0.61        20
    area/admin       0.10      0.28      0.15        25
    area/admission-control       0.80      0.24      0.37       164
    area/api       0.11      0.28      0.15        18
    area/apiserver       0.67      0.75      0.71        16
    area/app-lifecycle       0.41      0.62      0.49        37
    area/batch       0.33      0.25      0.29         4
    area/build-release       0.40      0.17      0.24        12
    area/cadvisor       0.00      0.00      0.00         1
    area/client-libraries       0.00      0.00      0.00         1
    area/cloudprovider       0.50      0.05      0.09        40
    area/configmap-api       0.80      0.31      0.44        13
    area/controller-manager       0.36      0.25      0.30        16
    area/dns       0.17      1.00      0.29         1
    area/docker       0.65      0.68      0.67        25
    area/downward-api       0.45      1.00      0.62         5
    area/ecosystem       0.00      0.00      0.00         1
    area/etcd       0.00      0.00      0.00         1
    area/example       0.00      0.00      0.00         0
    area/example/cassandra       0.00      0.00      0.00         2
    area/extensibility       0.62      0.44      0.51        48
    area/images-registry       0.85      0.85      0.85       119
    area/ingress       0.60      0.66      0.63       384
    area/introspection       0.60      0.41      0.49       207
    area/isolation       0.00      0.00      0.00        19
    area/kube-proxy       0.48      0.59      0.53        17
    area/kubeadm       0.20      0.50      0.29         2
    area/kubectl       0.49      0.47      0.48        90
    area/kubelet       0.00      0.00      0.00         1
    area/kubelet-api       0.56      0.11      0.19        45
    area/logging       0.00      0.00      0.00         0
    area/monitoring       0.26      0.13      0.17        39
    area/node-e2e       0.00      0.00      0.00         2
    area/node-lifecycle       0.22      0.60      0.32        25
    area/nodecontroller       0.00      0.00      0.00         2
    area/os/coreos       0.00      0.00      0.00         2
    area/os/fedora       0.18      0.20      0.19        10
    area/os/gci       0.00      0.00      0.00         2
    area/os/ubuntu       0.00      0.00      0.00         0
    area/platform/aws       0.00      0.00      0.00         0
    area/platform/azure       0.00      0.00      0.00         7
    area/platform/gce       0.00      0.00      0.00         0
    area/platform/gke       0.00      0.00      0.00         3
    area/platform/mesos       0.14      0.29      0.19         7
    area/platform/vagrant       0.72      0.54      0.62        39
    area/platform/vsphere       0.00      0.00      0.00         0
    area/release-infra       0.24      0.46      0.32       104
    area/reliability       0.77      0.93      0.84       374
    area/rkt       0.00      0.00      0.00         1
    area/secret-api       0.00      0.00      0.00         1
    area/security       0.33      0.08      0.13        12
    area/stateful-apps       0.00      0.00      0.00         3
    area/swagger       0.00      0.00      0.00         1
    area/system-requirement       0.33      0.04      0.07        24
    area/teardown       0.00      0.00      0.00         7

    avg / total       0.59      0.55      0.54      1999

    ================================================================================
    Perceptron
    ________________________________________________________________________________
    Training:
Perceptron(alpha=0.0001, class_weight=None, eta0=1.0, fit_intercept=True,
        max_iter=1000, n_iter=None, n_jobs=1, penalty=None, random_state=0,
        shuffle=True, tol=None, verbose=0, warm_start=False)
    train time: 115.440s
    test time:  0.034s
    accuracy:   0.460
    classification report:
    /usr/local/lib/python3.6/site-packages/sklearn/metrics/classification.py:1428: UserWarning: labels size, 64, does not match size of target_names, 66
.format(len(labels), len(target_names))
    /usr/local/lib/python3.6/site-packages/sklearn/metrics/classification.py:1135: UndefinedMetricWarning: Precision and F-score are ill-defined and being set to 0.0 in labels with no predicted samples.
    'precision', 'predicted', average, warn_for)
    /usr/local/lib/python3.6/site-packages/sklearn/metrics/classification.py:1137: UndefinedMetricWarning: Recall and F-score are ill-defined and being set to 0.0 in labels with no true samples.
    'recall', 'true', average, warn_for)
    precision    recall  f1-score   support

    area/HA       0.29      0.10      0.15        20
    area/admin       0.00      0.00      0.00         0
    area/admission-control       0.11      0.20      0.14        25
    area/api       0.64      0.18      0.28       164
    area/apiserver       0.17      0.22      0.20        18
    area/app-lifecycle       0.57      0.50      0.53        16
    area/batch       0.43      0.51      0.47        37
    area/build-release       0.20      0.25      0.22         4
    area/cadvisor       0.33      0.33      0.33        12
    area/client-libraries       0.00      0.00      0.00         1
    area/cloudprovider       0.00      0.00      0.00         1
    area/configmap-api       0.09      0.03      0.04        40
    area/controller-manager       0.38      0.23      0.29        13
    area/dns       0.16      0.19      0.17        16
    area/docker       0.09      1.00      0.17         1
    area/downward-api       0.00      0.00      0.00         0
    area/ecosystem       0.56      0.40      0.47        25
    area/etcd       0.33      0.60      0.43         5
    area/example       0.00      0.00      0.00         1
    area/example/cassandra       0.00      0.00      0.00         1
    area/extensibility       0.00      0.00      0.00         0
    area/images-registry       0.00      0.00      0.00         0
    area/ingress       0.00      0.00      0.00         2
    area/introspection       0.50      0.44      0.47        48
    area/isolation       0.81      0.81      0.81       119
    area/kube-proxy       0.62      0.46      0.53       384
    area/kubeadm       0.48      0.29      0.37       207
    area/kubectl       0.20      0.05      0.08        19
    area/kubelet       0.30      0.35      0.32        17
    area/kubelet-api       0.00      0.00      0.00         2
    area/logging       0.74      0.39      0.51        90
    area/monitoring       0.10      1.00      0.18         1
    area/node-e2e       0.44      0.09      0.15        45
    area/node-lifecycle       0.00      0.00      0.00         0
    area/nodecontroller       0.00      0.00      0.00         0
    area/os/coreos       0.45      0.38      0.42        39
    area/os/fedora       0.09      0.50      0.15         2
    area/os/gci       0.22      0.44      0.29        25
    area/os/ubuntu       0.00      0.00      0.00         2
    area/platform/aws       0.00      0.00      0.00         2
    area/platform/azure       0.00      0.00      0.00        10
    area/platform/gce       0.00      0.00      0.00         2
    area/platform/gke       0.00      0.00      0.00         0
    area/platform/mesos       0.00      0.00      0.00         0
    area/platform/vagrant       0.00      0.00      0.00         7
    area/platform/vsphere       0.00      0.00      0.00         0
    area/release-infra       0.00      0.00      0.00         0
    area/reliability       0.02      0.33      0.03         3
    area/rkt       0.14      0.29      0.19         7
    area/secret-api       0.85      0.56      0.68        39
    area/security       0.00      0.00      0.00         0
    area/stateful-apps       0.00      0.00      0.00         0
    area/swagger       0.00      0.00      0.00         0
    area/system-requirement       0.24      0.30      0.27       104
    area/teardown       0.85      0.88      0.87       374
    area/test       0.00      0.00      0.00         1
    area/test-infra       0.00      0.00      0.00         1
    area/third-party-resource       0.25      0.08      0.12        12
    area/ui       0.00      0.00      0.00         0
    area/upgrade       0.40      0.67      0.50         3
    area/usability       0.00      0.00      0.00         1
    area/workload-api/cronjob       0.21      0.29      0.25        24
    area/workload-api/daemonset       0.00      0.00      0.00         0
    area/workload-api/deployment       0.67      0.29      0.40         7

    avg / total       0.57      0.46      0.49      1999

    ================================================================================

```
