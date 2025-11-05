import requests
import json

# URL del servicio activo en Cloud Run
URL = "https://multimodal-fusion-v1-804643441779.southamerica-east1.run.app/"

# Datos simulados para la prueba
payload = {
    "address": "Av. del Golf 320, Nordelta",
    "price": 285000,
    "estimated_value": 305000,
    "latitude": -34.3935,
    "longitude": -58.6468,
    "property_type": "Casa",
    "ambient_noise": 42.5,  # nivel simulado en decibelios
    "video_reference": "sample_video_001.mp4"
}

# Envío del POST request al endpoint
print("Enviando datos al servidor...")
response = requests.post(URL, json=payload)

# Mostrar resultado
if response.status_code == 200:
    print("✅ Respuesta del servidor:")
    print(response.text)
else:
    print("❌ Error:")
    print(f"Código: {response.status_code}")
    print(response.text)
