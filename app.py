from flask import Flask, request, jsonify, render_template_string
import datetime

app = Flask(__name__)

# ---------- HOME ----------
@app.route('/')
def index():
    return '✅ Lucy Network Real Estate V1 está corriendo correctamente en Cloud Run.'

# ---------- STATUS ----------
@app.route('/status', methods=['GET'])
def status():
    return jsonify({
        "status": "online",
        "timestamp": datetime.datetime.now().isoformat(),
        "agent": "Bruno (Real Estate AI)",
        "message": "Servicio operativo y en espera de datos"
    })

# ---------- FORMULARIO HTML ----------
@app.route('/form', methods=['GET', 'POST'])
def form():
    html = """
    <html>
      <body style="font-family: sans-serif; max-width: 500px; margin: 30px auto;">
        <h2>Lucy Network – Cargar propiedad</h2>
        <form method="post">
          <label>Dirección:</label><br>
          <input name="address" style="width:100%; padding:6px;" required><br><br>
          <label>Precio (USD):</label><br>
          <input name="price" type="number" style="width:100%; padding:6px;" required><br><br>
          <button type="submit" style="padding:8px 16px;">Enviar a Bruno</button>
        </form>
        {{result_block}}
      </body>
    </html>
    """
    if request.method == 'POST':
        address = request.form.get('address')
        price = request.form.get('price')
        # Simulación de análisis por Bruno
        analysis = {
            "address": address,
            "price": float(price),
            "estimated_value": round(float(price) * 1.08, 2),
            "comment": "✅ Datos recibidos correctamente por Bruno AI (form web)"
        }
        result_html = f"""
        <div style="margin-top:20px; padding:10px; background:#e8ffe8;">
          <strong>Resultado:</strong><br>
          Dirección: {analysis['address']}<br>
          Precio informado: {analysis['price']}<br>
          Valor estimado: {analysis['estimated_value']}<br>
          Nota: {analysis['comment']}
        </div>
        """
        return render_template_string(html, result_block=result_html)

    return render_template_string(html, result_block="")

# ---------- ENDPOINT JSON ----------
@app.route('/upload-property', methods=['POST'])
def upload_property():
    data = request.get_json()
    if not data or 'address' not in data or 'price' not in data:
        return jsonify({
            "success": False,
            "error": "Faltan campos obligatorios: address o price"
        }), 400

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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
