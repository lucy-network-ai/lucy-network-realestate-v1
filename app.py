from flask import Flask, request, jsonify, render_template_string
from google.cloud import firestore
from datetime import datetime
import os

app = Flask(__name__)

# Inicializar Firestore
db = firestore.Client()

# Página principal (verificación)
@app.route('/')
def home():
    return "<h3>✅ Lucy Network Real Estate V1 – Conectado a Firestore</h3>"

# Endpoint de estado
@app.route('/status')
def status():
    return jsonify({
        "agent": "Bruno (Real Estate AI)",
        "message": "Servicio operativo y vinculado con Firestore",
        "status": "online",
        "timestamp": datetime.utcnow().isoformat()
    })

# Formulario web
@app.route('/form')
def form():
    html_form = """
    <h2>Lucy Network – Cargar propiedad</h2>
    <form action="/upload-property" method="post">
        Dirección:<br><input type="text" name="address" required><br><br>
        Precio (USD):<br><input type="number" name="price" required><br><br>
        <button type="submit">Enviar a Bruno</button>
    </form>
    """
    return render_template_string(html_form)

# Endpoint de carga (POST)
@app.route('/upload-property', methods=['POST'])
def upload_property():
    address = request.form.get('address')
    price = float(request.form.get('price'))
    estimated_value = round(price * 1.08, 2)  # simulación simple

    data = {
        "address": address,
        "price": price,
        "estimated_value": estimated_value,
        "timestamp": datetime.utcnow().isoformat()
    }

    # Guardar en Firestore
    db.collection('properties').add(data)

    return render_template_string(f"""
        <h3>✅ Datos enviados correctamente</h3>
        <p><b>Dirección:</b> {address}</p>
        <p><b>Precio informado:</b> {price}</p>
        <p><b>Valor estimado:</b> {estimated_value}</p>
        <p><i>Registro guardado en Firestore</i></p>
    """)

# Run local (solo si se ejecuta manualmente)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
