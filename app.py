from flask import Flask, request, jsonify, render_template_string
from google.cloud import firestore
from datetime import datetime
import os

app = Flask(__name__)

# Inicializa Firestore
db = firestore.Client()

@app.route('/')
def home():
    return jsonify({
        "agent": "Bruno (Real Estate AI)",
        "status": "online",
        "message": "Servicio operativo y listo para guardar en Firestore"
    })

# Ruta del formulario
@app.route('/form')
def form():
    return render_template_string("""
        <h2>Lucy Network – Cargar propiedad</h2>
        <form action="/upload-property" method="post">
            Dirección:<br><input type="text" name="address"><br>
            Precio (USD):<br><input type="number" name="price"><br><br>
            <input type="submit" value="Enviar a Bruno">
        </form>
    """)

# Endpoint principal
@app.route('/upload-property', methods=['POST'])
def upload_property():
    address = request.form.get('address')
    price = request.form.get('price')

    # Validación básica
    if not address or not price:
        return jsonify({"error": "Faltan datos"}), 400

    # Simulación de análisis de valor
    estimated_value = float(price) * 1.08  # +8% estimado

    # Estructura para guardar en Firestore
    doc = {
        "address": address,
        "price": float(price),
        "estimated_value": round(estimated_value, 2),
        "timestamp": datetime.utcnow().isoformat()
    }

    # Guarda el documento
    db.collection("properties").add(doc)

    return render_template_string(f"""
        <div style='margin-top:20px;padding:10px;background:#e8ffe8;'>
            <strong>Resultado:</strong><br>
            Dirección: {address}<br>
            Precio informado: {price}<br>
            Valor estimado: {estimated_value}<br>
            Nota: ✅ Datos guardados correctamente en Firestore
        </div>
    """)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
