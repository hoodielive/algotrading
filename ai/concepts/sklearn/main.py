import sklearn
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

# load dataset

data = load_breast_cancer()

# Organize Data

label_names = data['target_names']
labels = data['target']
feature_names = data['feature_names']
features = data['data']

# Take a look at the data

print(label_names)
print(labels[0])
print(feature_names[0])
print(features[0])


# Train data
train, test, train_labels, test_labels = train_test_split(features, labels, test_size=0.33, random_state=42)

# Build and evaluating the model

# Initialize the classifier

gnb = GaussianNB()

# Train our classifier

model = gnb.fit(train, train_labels)

# Make predictions

preds = gnb.predict(test)
print(preds)

# Evaluate Accuracy

print(accuracy_score(test_labels, preds))
