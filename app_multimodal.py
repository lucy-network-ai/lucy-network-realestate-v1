from flask import Flask, request, jsonify
from google.cloud import firestore
from datetime import datetime
import cv2
import numpy as np
import tempfile
import os
import librosa

app = Flask(__name__)
db = firestore.Client()

# --- Análisis de video ---
def analyze_video(video_path):
    cap = cv2.VideoCapture(video_path)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    brightness_values, texture_values = [], []

    for _ in range(min(frame_count, 30)):  # primeros 30 fotogramas
        ret, frame = cap.read()
        if not ret:
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        brightness_values.append(np.mean(gray))
        texture_values.append(np.std(gray))

    cap.release()
    return (
        float(np.mean(brightness_values)) if brightness_values else 0.0,
        float(np.mean(texture_values)) if texture_values else 0.0
    )

# --- Análisis de audio ---
def analyze_audio(audio_path):
    y, sr = librosa.load(audio_path, sr=None)
    rms = float(np.mean(librosa.feature.rms(y=y)))
    centroid = float(np.mean(librosa.feature.spectral_centroid(y=y, sr=sr)))
    return rms, centroid

@app.route('/')
def home():
    return "<h2>Lucy Network – Multimodal + GPS V1.1 🧠</h2><p>Servicio activo y listo para analizar.</p>"

@app.route('/upload', methods=['POST'])
def upload_media():
    try:
        address = request.form.get('address', 'unknown')
        latitude = request.form.get('latitude')
        longitude = request.form.get('longitude')
        gps_data = None
        if latitude and longitude:
            gps_data = {'lat': float(latitude), 'lng': float(longitude)}

        media = request.files['file']
        _, temp_path = tempfile.mkstemp()
        media.save(temp_path)

        result = {}
        filename = media.filename.lower()

        if filename.endswith(('.mp4', '.mov', '.avi')):
            brightness, texture = analyze_video(temp_path)
            result = {
                'media_type': 'video',
                'brightness': round(brightness, 2),
                'texture': round(texture, 2)
            }
        elif filename.endswith(('.mp3', '.wav', '.m4a')):
            rms, centroid = analyze_audio(temp_path)
            result = {
                'media_type': 'audio',
                'rms_level': round(rms, 4),
                'spectral_centroid': round(centroid, 2)
            }
        else:
            return jsonify({'error': 'Formato no soportado'}), 400

        os.remove(temp_path)

        record = {
            'address': address,
            'gps': gps_data,
            'timestamp': datetime.utcnow().isoformat(),
            'result': result
        }
        db.collection('multimodal_results').add(record)

        return f"""
        <h3>✅ Análisis completado y guardado</h3>
        <b>Dirección:</b> {address}<br>
        <b>GPS:</b> {gps_data}<br>
        <b>Tipo:</b> {result['media_type']}<br>
        <b>Datos:</b> {result}<br>
        <p>Registro almacenado en Firestore (multimodal_results)</p>
        """
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
