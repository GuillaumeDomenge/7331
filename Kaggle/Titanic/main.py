import pandas as pd
import numpy as np
import scipy.stats as ss
import matplotlib.pyplot as plt
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

df = pd.read_csv("/home/guillaume/Documents/7331/Kaggle/Titanic/train.csv")
df_test = pd.read_csv("/home/guillaume/Documents/7331/Kaggle/Titanic/test.csv")

le = LabelEncoder()
oe1 = OneHotEncoder()
oe2 = OneHotEncoder()
le.fit(df[["Sex"]])
oe2.fit(df[["Embarked"]])

df["Sex_encoded"] = le.transform(df[["Sex"]])
df["Cabin_clean"] = df["Cabin"].fillna('').astype(str)
df["Deck"] = df["Cabin_clean"].str[0].replace('',np.nan)
df["Cabin_num"] = pd.to_numeric(df["Cabin_clean"].str[1:], errors="coerce")

oe1.fit(df[["Deck"]])
df["Deck_encoded"] = oe1.transform(df[["Deck"]])
df["Embarked_encoded"] = oe2.transform(df[["Embarked"]])

df_test["Sex_encoded"] = le.transform(df_test[["Sex"]])
df_test["Cabin_clean"] = df_test["Cabin"].fillna('').astype(str)
df_test["Deck"] = df_test["Cabin_clean"].str[0].replace('',np.nan)
df_test["Cabin_num"] = pd.to_numeric(df_test["Cabin_clean"].str[1:], errors="coerce")

df_test["Sex_encoded"] = le.transform(df_test[["Sex"]])
df_test["Deck_encoded"] = oe1.transform(df_test[["Deck"]])
df_test["Embarked_encoded"] = oe2.transform(df_test[["Embarked"]])

model = LogisticRegression(max_iter=1000)

xs = ["Sex_encoded","Deck_encoded","Embarked_encoded","Pclass","Age","SibSp","Parch","Fare","Cabin_num"]
y = ["Survived"]
X_train = df[xs]
y_train = df[y]

X_test = df_test[xs]
y_test = df_test[y]
model.fit(X_train, y_train.values.ravel())


y_pred = model.predict(X_test)

# Evaluate model
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

