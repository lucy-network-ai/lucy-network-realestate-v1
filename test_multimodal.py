import requests
import json

# URL exacta del servicio activo
URL = "https://multimodal-fusion-v1-804643441779.southamerica-east1.run.app/"

# Datos de prueba
data = {
    "address": "Av. Santa María 1500, Nordelta",
    "price": 250000
}

print("Enviando datos al servidor...")

try:
    response = requests.post(URL, json=data)

    if response.status_code == 200:
        print("✅ Respuesta del servidor:")
        print(json.dumps(response.json(), indent=4, ensure_ascii=False))
    else:
        print("❌ Error:")
        print(f"Código: {response.status_code}")
        print(response.text)

except Exception as e:
    print("⚠️ Error de conexión:", e)
