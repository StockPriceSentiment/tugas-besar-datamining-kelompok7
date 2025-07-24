# src/sentiment_ihsg_loader.py

"""
sentiment_ihsg_loader.py

Module ini digunakan untuk memuat dataset final hasil preprocessing 
terkait sentimen saham dan data historis IHSG dari folder data/processed/.
"""

import pandas as pd
import os

# Folder path relatif dari root repository
PROCESSED_DATA_PATH = "data/processed/"

def load_final_csv(filename):
    """
    Memuat file CSV dari folder data/processed/.

    Parameters:
        filename (str): Nama file (contoh: 'final_data_sentiment.csv')

    Returns:
        pd.DataFrame: Dataframe dari file yang dimuat.
    """
    file_path = os.path.join(PROCESSED_DATA_PATH, filename)

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File tidak ditemukan di folder processed: {file_path}")

    # Khusus untuk data IHSG, pastikan kolom 'Date' dibaca sebagai index
    if 'IHSG' in filename:
        return pd.read_csv(file_path, index_col='Date', parse_dates=True, encoding='latin1')
    
    return pd.read_csv(file_path, encoding='latin1') # Tambahkan encoding di sini

def preview_data(df, rows=5):
    """
    Menampilkan preview awal dari dataframe.

    Parameters:
        df (pd.DataFrame): Dataframe yang akan dipreview.
        rows (int): Jumlah baris untuk ditampilkan.
    """
    print(df.head(rows))

# Contoh pemanggilan untuk memuat data final
if __name__ == "__main__":
    try:
        print("Memuat data sentimen final...")
        df_sentiment = load_final_csv("IDSMSA_final.csv")
        preview_data(df_sentiment)

        print("\n" + "="*50 + "\n")

        print("Memuat data IHSG final...")
        df_ihsg = load_final_csv("IHSG_final.csv")
        preview_data(df_ihsg)

    except Exception as e:
        print(e)