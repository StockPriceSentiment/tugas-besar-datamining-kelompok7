# src/model.py

from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB

def train_model(X, y):
    """
    Melatih dua model klasifikasi: SVM dan Naive Bayes.

    Returns:
        dict: Berisi hasil prediksi dan objek model untuk SVM & Naive Bayes
    """
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    results = {}

    # Naive Bayes
    nb_model = GaussianNB()
    nb_model.fit(X_train, y_train)
    nb_pred = nb_model.predict(X_test)
    results['Naive Bayes'] = {
        'model': nb_model,
        'y_test': y_test,
        'y_pred': nb_pred
    }

    # SVM
    svm_model = SVC(kernel='linear', random_state=42)
    svm_model.fit(X_train, y_train)
    svm_pred = svm_model.predict(X_test)
    results['SVM'] = {
        'model': svm_model,
        'y_test': y_test,
        'y_pred': svm_pred
    }

    return results
