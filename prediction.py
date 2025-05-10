import joblib
import pandas as pd

# Load pipeline: preprocessor, feature selector (RFE), dan model
preprocessor = joblib.load('model/preprocessor.pkl')
rfe_selector = joblib.load('model/rfe_selector.pkl')
model = joblib.load('model/model_logistic_regression.pkl')

# Fungsi prediksi
def predict_attrition(df_raw: pd.DataFrame) -> pd.DataFrame:
    # Transform dengan preprocessor (scaling + encoding)
    X_processed = preprocessor.transform(df_raw)

    # Seleksi fitur (RFE)
    X_selected = rfe_selector.transform(X_processed)

    # Prediksi
    predictions = model.predict(X_selected)

    # Tambahkan kolom prediksi
    df_result = df_raw.copy()
    df_result['Predicted_Attrition'] = predictions

    return df_result

# Contoh penggunaan
if __name__ == "__main__":
    # Load sample data mentah (belum di-encode)
    sample = pd.read_csv('dataset/sample_data.csv')

    # Prediksi
    hasil = predict_attrition(sample)

    # Tampilkan hasil
    print(hasil)

    # Simpan ke file
    hasil.to_csv('dataset/hasil_prediksi.csv', index=False)
    print("Hasil prediksi disimpan'")