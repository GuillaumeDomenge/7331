import pandas as pd
import numpy as np
import scipy.stats as ss
import matplotlib.pyplot as plt
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report


df_train = pd.read_csv("/home/guillaume/Documents/7331/Kaggle/Titanic/train.csv")
df_test = pd.read_csv("/home/guillaume/Documents/7331/Kaggle/Titanic/test.csv")
df_train["Cabin_clean"] = df_train["Cabin"].fillna('').astype(str)
df_train["Deck"] = df_train["Cabin_clean"].str[0].replace('',np.nan)
df_train["Cabin_num"] = pd.to_numeric(df_train['Cabin_clean'].str[1:], errors='coerce')
cols = ["Pclass","Sex",]
ohe = OneHotEncoder(handle_unknown='ignore', sparse_output=False)
le = LabelEncoder()
ohe.fit(df_train[["Embarked"]])
# le.fit(df_train[["Sex"]])
a = ohe.transform(df_train[["Embarked"]])
# df_train["Embarked_encoded"] = ohe.transform(df_train[["Embarked"]])
print(a.shape)

