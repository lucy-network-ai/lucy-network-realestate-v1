from flask import Flask, request, jsonify
from google.cloud import firestore
import os

# Inicialización de la app Flask
app = Flask(__name__)

# Inicialización de Firestore
db = firestore.Client()

# 🔹 Ruta principal (GET) → Verifica conexión
@app.route("/", methods=["GET"])
def index():
    return "<h3>✅ Lucy Network Real Estate V1 – Conectado a Firestore</h3>", 200

# 🔹 Ruta principal (POST) → Recibe y guarda datos
@app.route("/", methods=["POST"])
def receive_data():
    try:
        data = request.get_json(force=True)
        address = data.get("address", "Sin dirección")
        price = float(data.get("price", 0))
        estimated_value = data.get("estimated_value", round(price * 1.1, 2))

        # Guardar en Firestore
        doc_ref = db.collection("properties").add({
            "address": address,
            "price": price,
            "estimated_value": estimated_value
        })

        return jsonify({
            "status": "✅ Datos recibidos correctamente",
            "address": address,
            "price": price,
            "estimated_value": estimated_value,
            "firestore_id": doc_ref[1].id
        }), 200

    except Exception as e:
        return jsonify({
            "status": "❌ Error al procesar los datos",
            "detalle": str(e)
        }), 500


# 🔹 Ejecución local (solo si se ejecuta en la iMac, no en Cloud Run)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port, debug=True)
