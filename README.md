# 🧪 FastAPI User Service

Este proyecto es un microservicio desarrollado con **FastAPI** que permite crear usuarios, autenticarse y obtener la lista de usuarios registrados. Incluye pruebas automáticas con `pytest` y entorno de ejecución en **Docker**.

## 🚀 Características

- Registro de usuarios con `first_name`, `last_name` y `password`.
- Login de usuario con validación de contraseña hasheada.
- Endpoint para listar todos los usuarios (sin mostrar contraseñas).
- Tests automatizados con `pytest` y `httpx`.
- Mock de base de datos MongoDB para pruebas.
- Contenedor Docker listo para ejecutar.

---

## 📦 Instalación y ejecución rápida con Docker

1. Clona el repositorio:

```bash
git clone https://github.com/juancadavid08/XpertGroupPython.git
cd tu_repo
```

2. Construye el contenedor:

```bash
docker build -t fastapi_app .
```

3. Ejecuta el contenedor:

```bash
docker run -d --name fastapi_app -p 8000:8000 fastapi_app
```

4. Abre tu navegador en: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🧪 Ejecutar tests

1. Accede al contenedor:

```bash
docker exec -it fastapi_app bash
```

2. Ejecuta los tests con `pytest`:

```bash
pytest
```

Verás los resultados de los tests directamente en consola.

---

## 📁 Estructura del proyecto

```
.
├── app/
│   ├── main.py              # Punto de entrada de FastAPI
│   ├── api/                 # Rutas
│   ├── models/              # Esquemas Pydantic
│   ├── services/            # Lógica de negocio
│   ├── utils/               # Funciones auxiliares (hashing, seguridad)
│   └── db/                  # Conexión a MongoDB
├── tests/                   # Tests automáticos
│   ├── test_users.py
│   └── conftest.py
├── Dockerfile
├── requirements.txt
└── README.md
```

---

## ✅ Requisitos para desarrollo local

- Python 3.10+
- Docker
- (Opcional) MongoDB si vas a probar fuera de Docker

Instala dependencias:

```bash
pip install -r requirements.txt
```

Ejecuta la API localmente:

```bash
uvicorn app.main:app --reload
```

---

## 🛡️ Seguridad

Las contraseñas son almacenadas de forma segura usando **bcrypt**. Los tests simulan correctamente esta lógica sin conectarse a una base real.

---

## ✍️ Autor

Desarrollado por Juan Cadavid. 
