import pandas as pd
import graphviz

import sklearn

import numpy as np
from matplotlib import pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree

model_rules = tree.DecisionTreeClassifier()
model_rules.fit()

>>> dot_data = tree.export_graphviz(clf, out_file=None,
     ...: ...                      feature_names=iris.feature_names,
     ...: ...                      class_names=iris.target_names,
     ...: ...                      filled=True, rounded=True,
     ...: ...                      special_characters=True)


