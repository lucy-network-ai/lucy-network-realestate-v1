# ========================================
# Lucy Network Real Estate V1 - API Bruno
# ========================================

from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

# --- 1️⃣ Endpoint de verificación básica ---
@app.route('/')
def index():
    return '✅ Lucy Network Real Estate V1 está corriendo correctamente en Cloud Run.'

@app.route('/status', methods=['GET'])
def status():
    return jsonify({
        "status": "online",
        "timestamp": datetime.datetime.now().isoformat(),
        "agent": "Bruno (Real Estate AI)",
        "message": "Servicio operativo y en espera de datos"
    })

# --- 2️⃣ Endpoint de carga de propiedades (mock) ---
@app.route('/upload-property', methods=['POST'])
def upload_property():
    data = request.get_json()

    if not data or 'address' not in data or 'price' not in data:
        return jsonify({
            "success": False,
            "error": "Faltan campos obligatorios: address o price"
        }), 400

    # Simula análisis básico de Bruno
    response = {
        "success": True,
        "analysis": {
            "address": data['address'],
            "price": data['price'],
            "timestamp": datetime.datetime.now().isoformat(),
            "estimated_value": float(data['price']) * 1.08,
            "comment": "✅ Datos recibidos correctamente por Bruno AI (modo demo)"
        }
    }

    return jsonify(response), 200


# --- 3️⃣ Lanzador principal ---
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
