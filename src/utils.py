# src/utils.py

from sklearn.metrics import classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

def print_classification_report(y_true, y_pred):
    """
    Menampilkan classification report.
    """
    print("=== Classification Report ===")
    print(classification_report(y_true, y_pred))

def plot_confusion_matrix(y_true, y_pred):
    """
    Menampilkan confusion matrix.
    """
    cm = confusion_matrix(y_true, y_pred)
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=[0, 1], yticklabels=[0, 1])
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.title("Confusion Matrix")
    plt.tight_layout()
    plt.show()
