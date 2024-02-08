import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

def split_data_model(word_list):
    # Read the CSV file
    df = pd.read_csv('Data/TrainModelData/data.csv')

    # Separate input text and labels
    texts = df['Text'].tolist()
    labels = df['Category'].tolist()

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(texts, labels, test_size=0.2, random_state=42)

    # Vectorize the text data
    vectorizer = CountVectorizer()
    X_train_vec = vectorizer.fit_transform(X_train)
    X_test_vec = vectorizer.transform(X_test)

    # Train a simple classifier (Naive Bayes)
    classifier = MultinomialNB()
    classifier.fit(X_train_vec, y_train)

    # Make predictions on the test set
    y_pred = classifier.predict(X_test_vec)

    # Evaluate the accuracy
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Accuracy: {accuracy}")

    # Test with new input data
    # new_inputs = ["Submit", "Username", "User", "Product name", "123456"]
    new_inputs_vec = vectorizer.transform(word_list)
    predictions = classifier.predict(new_inputs_vec)

    prediction_dic = {}

    # Output the predictions
    for input_text, prediction in zip(word_list, predictions):
        prediction_dic[prediction] = input_text

    # print(prediction_dic.keys())
    return prediction_dic
