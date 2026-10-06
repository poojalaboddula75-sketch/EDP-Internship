import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

# Load dataset
df = pd.read_csv("spam_messages.csv")

print("DATASET")
print(df)

# Convert labels into numbers
df["Label"] = df["Label"].map({"ham": 0, "spam": 1})

# Features and target
X = df["Message"]
y = df["Label"]

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)

# Convert text into numerical features using TF-IDF
vectorizer = TfidfVectorizer()
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

# Train Naive Bayes classifier
model = MultinomialNB()
model.fit(X_train_tfidf, y_train)

# Make predictions
y_pred = model.predict(X_test_tfidf)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)

print("\nACCURACY")
print(accuracy)

print("\nCLASSIFICATION REPORT")
print(classification_report(
    y_test,
    y_pred,
    target_names=["ham", "spam"],
    zero_division=0
))

# Test new messages
new_messages = [
    "Congratulations! You won a free prize!",
    "Can you send me the project notes?"
]

new_messages_tfidf = vectorizer.transform(new_messages)
predictions = model.predict(new_messages_tfidf)

print("\nNEW MESSAGE PREDICTIONS")

for message, prediction in zip(new_messages, predictions):
    label = "spam" if prediction == 1 else "ham"
    print(message, "->", label)