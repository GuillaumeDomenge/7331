import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.impute import SimpleImputer
# Load data
train = pd.read_csv("/home/guillaume/Documents/7331/Kaggle/Titanic/train.csv")
test = pd.read_csv("/home/guillaume/Documents/7331/Kaggle/Titanic/test.csv")
res = pd.read_csv("/home/guillaume/Documents/7331/Kaggle/Titanic/gender_submission.csv")
print(test.info())
y_test = res["Survived"]
# Function to split 'cabin' into 'deck' and 'cabin_num'
def split_cabin(df):
    df = df.copy()
    df['Deck'] = df['Cabin'].str[0]  # Take the first character (deck)
    df['Cabin_num'] = df['Cabin'].str.extract('(\d+)')  # Extract number
    df['Cabin_num'] = pd.to_numeric(df['Cabin_num'], errors='coerce')  # Convert to float
    return df

# Apply to train and test
train = split_cabin(train)
test = split_cabin(test)

# Categorical columns to encode
cat_cols = ['Deck', 'Sex', 'Embarked']
num_cols = ['Pclass', "Age", "SibSp", "Parch", "Fare", "Cabin_num"]



# Impute numeric columns with median
num_imputer = SimpleImputer(strategy='median')
train[num_cols] = num_imputer.fit_transform(train[num_cols])
test[num_cols] = num_imputer.transform(test[num_cols])

# Impute categorical columns with "missing"
cat_imputer = SimpleImputer(strategy='constant', fill_value='missing')
train[cat_cols] = cat_imputer.fit_transform(train[cat_cols])
test[cat_cols] = cat_imputer.transform(test[cat_cols])

# --- Encode categorical columns ---

# Combine for consistent encoding
combined_cats = pd.concat([train[cat_cols], test[cat_cols]], axis=0)
encoder = OneHotEncoder(sparse_output=False, handle_unknown='ignore')
encoded = encoder.fit_transform(combined_cats)
encoded_cols = encoder.get_feature_names_out(cat_cols)

# Split back
encoded_train = pd.DataFrame(encoded[:len(train)], columns=encoded_cols, index=train.index)
encoded_test = pd.DataFrame(encoded[len(train):], columns=encoded_cols, index=test.index)

# --- Final datasets ---
X_train = pd.concat([train[num_cols], encoded_train], axis=1)
X_test = pd.concat([test[num_cols], encoded_test], axis=1)

# Target variable
# print(train.info())
y_train = train['Survived']
model = LogisticRegression(max_iter=1000)


model.fit(X_train, y_train)
# print(test.info())
y_pred = model.predict(X_test)

submission = pd.DataFrame({
    'PassengerId': test['PassengerId'],  # or whatever ID column is present
    'Survived': y_pred
})

# Save to CSV
submission.to_csv('submission.csv', index=False)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

