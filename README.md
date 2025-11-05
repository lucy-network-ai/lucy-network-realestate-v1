# 🧠 Lucy Network Real Estate V1

**Proyecto:** Lucy Network – Real Estate Intelligence  
**Versión:** V1 (Deploy automático con Cloud Build + Cloud Run)  
**Región:** southamerica-east1  
**Repositorio:** [lucy-network-ai/lucy-network-realestate-v1](https://github.com/lucy-network-ai/lucy-network-realestate-v1)

---

## ⚙️ Descripción

Este servicio procesa análisis multimodales y conexión con Firestore para el sistema **Lucy Network – Real Estate**, dentro del ecosistema Lucy AI.

Está diseñado para ejecutarse de forma **automática** mediante Cloud Build y desplegarse en Cloud Run en cada actualización de la rama `main`.

---

## 🔗 Endpoints principales

| Endpoint | Descripción | Estado |
|-----------|--------------|--------|
| `/` | Página de verificación de conexión | ✅ Conectado a Firestore |
| `/ingest` | Endpoint de prueba para recibir datos | ⚙️ En desarrollo |

---

## 🚀 Despliegue automático

Cada vez que se realiza un **commit en la rama `main`**, este repositorio dispara el activador  
`deploy-lucy-network-realestate-v1` configurado en Google Cloud Build.

Ese activador compila el código fuente y actualiza automáticamente el servicio  
`multimodal-fusion-v1` en **Google Cloud Run**.

---

## 🧩 Estado actual

- ✅ Repositorio conectado con Cloud Build  
- ✅ Activador configurado  
- ✅ Despliegue automático activo  
- 🔄 Test de commit en curso  

---

## 🧪 Test de Build Automático

> Último commit de prueba:  
> ✅ **Cloud Build Test – 2025-11-05 10:07 (ARG)**

*(Este bloque confirma que el sistema de despliegue automático está funcionando correctamente.)*

---

**Autor:** Lucy Network AI  
**Infraestructura:** Google Cloud Platform  
**Contacto:** support@lucy-network.ai
