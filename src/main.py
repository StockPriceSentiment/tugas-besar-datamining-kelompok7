"""
Main pipeline for Data Mining project: Analisis Sentimen terhadap IHSG.
Langkah-langkah:
1. Load data sentimen & IHSG
2. Preprocessing & Feature Engineering
3. Train model
4. Evaluasi model
"""

import pandas as pd
from data_loader import load_final_csv
from model import train_model
from utils import print_classification_report, plot_confusion_matrix

def main():
    # 1. Load data
    try:
        df_sentiment = load_final_csv("IDSMSA_Final.csv")
        df_ihsg = load_final_csv("IHSG_final.csv")
    except FileNotFoundError as e:
        print(f"File tidak ditemukan: {e}")
        return

    # 2. Preprocessing & Feature Engineering
    df_sentiment['Tweet Date'] = pd.to_datetime(df_sentiment['Tweet Date'])
    df_sentiment.set_index('Tweet Date', inplace=True)

    # Agregasi sentimen harian
    daily_sentiment = (
        df_sentiment['Sentiment']
        .groupby(df_sentiment.index.date)
        .value_counts()
        .unstack(fill_value=0)
    )
    daily_sentiment.index = pd.to_datetime(daily_sentiment.index)

    # Pastikan index IHSG adalah datetime
    df_ihsg.index = pd.to_datetime(df_ihsg.index)

    # Gabungkan
    df_merged = df_ihsg.join(daily_sentiment, how='inner')

    # Pastikan kolom sentimen lengkap
    for col in ['Positive', 'Negative', 'Neutral']:
        if col not in df_merged.columns:
            print(f"Kolom {col} tidak ditemukan dalam data gabungan.")
            return

    # Feature dan Target
    X = df_merged[['Positive', 'Negative', 'Neutral']]
    df_merged['Target'] = (df_merged['Close'].shift(-1) > df_merged['Close']).astype(int)
    df_merged = df_merged.dropna(subset=['Target'])
    y = df_merged['Target']
    X = X.loc[y.index]

    print("Tahap pelatihan model...")
    results = train_model(X, y)

    print("Tahap evaluasi model...")
    for model_name, res in results.items():
        print(f"\n=== Evaluasi Model: {model_name} ===")
        print_classification_report(res['y_test'], res['y_pred'])
        plot_confusion_matrix(res['y_test'], res['y_pred'])


    print("Pipeline selesai.")

if __name__ == "__main__":
    main()
