m flask import Flask, request, jsonify
from google.cloud import firestore
import os

app = Flask(__name__)

# Inicializar Firestore
db = firestore.Client()

# Ruta principal
@app.route("/", methods=["GET"])
def home():
    return "✅ Lucy Network Real Estate V1 – Conectado a Firestore"

# Nueva ruta /ingest
@app.route("/ingest", methods=["POST"])
def ingest_data():
    try:
        data = request.get_json()

        if not data:
            return jsonify({"error": "No se recibieron datos"}), 400

        address = data.get("address")
        price = data.get("price")

        if not address or not price:
            return jsonify({"error": "Faltan campos obligatorios: address o price"}), 400

        # Calcular valor estimado
        estimated_value = round(float(price) * 1.12, 2)

        # Guardar en Firestore
        db.collection("properties").add({
            "address": address,
            "price": price,
            "estimated_value": estimated_value
        })

        return jsonify({
            "message": "Datos almacenados correctamente",
            "estimated_value": estimated_value
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


<<<<<<< HEAD
# Ruta POST antigua (mantener compatibilidad)
=======
# Ruta POST base (compatibilidad)
>>>>>>> f1a2a14 (Agregada ruta /ingest al servicio Flask)
@app.route("/", methods=["POST"])
def receive_data():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No se recibieron datos"}), 400

        address = data.get("address")
        price = data.get("price")

        if not address or not price:
            return jsonify({"error": "Faltan campos obligatorios"}), 400

        estimated_value = round(float(price) * 1.1, 2)

        db.collection("properties").add({
            "address": address,
            "price": price,
            "estimated_value": estimated_value
        })

        return jsonify({"message": "Datos recibidos correctamente", "estimated_value": estimated_value}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)


