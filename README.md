# Job Backend API

API REST construida con FastAPI para gestionar ofertas de trabajo y perfiles de usuarios.

## 🚀 Características

- Autenticación JWT
- Gestión de usuarios
- Base de datos SQLite
- Documentación automática con Swagger
- Dockerizado para fácil despliegue

## 📋 Prerrequisitos

- Python 3.11+
- Docker y Docker Compose (opcional)

## 🔧 Instalación

### Instalación Local

1. Clonar el repositorio:

```bash
git clone <url-del-repositorio>
cd job-backend
```

2. Crear y activar entorno virtual:

```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. Instalar dependencias:

```bash
pip install -r requirements.txt
```

4. Ejecutar la aplicación:

```bash
uvicorn app.main:app --reload
```

### Instalación con Docker

1. Construir y levantar los contenedores:

```bash
docker-compose up --build
```

2. Para ejecutar en segundo plano:

```bash
docker-compose up -d
```

3. Para detener los contenedores:

```bash
docker-compose down
```

## 📚 Documentación de la API

Una vez que la aplicación esté corriendo, puedes acceder a la documentación interactiva:

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## 🔐 Endpoints Principales

### Autenticación

- `POST /users/login` - Iniciar sesión
- `POST /users/register` - Registrar nuevo usuario
- `GET /users/me` - Obtener información del usuario actual

### Usuarios

- `GET /users` - Listar todos los usuarios
- `GET /users/{id}` - Obtener usuario por ID
- `PUT /users/{id}` - Actualizar usuario
- `DELETE /users/{id}` - Eliminar usuario

## 🛠️ Estructura del Proyecto

```
job-backend/
├── app/
│   ├── core/           # Configuraciones centrales
│   ├── db/            # Configuración de base de datos
│   ├── models/        # Modelos SQLAlchemy
│   ├── routes/        # Rutas de la API
│   ├── schemas/       # Esquemas Pydantic
│   ├── services/      # Lógica de negocio
│   └── utils/         # Utilidades
├── tests/             # Tests unitarios
├── Dockerfile         # Configuración de Docker
├── docker-compose.yml # Configuración de Docker Compose
├── requirements.txt   # Dependencias del proyecto
└── README.md         # Este archivo
```

## 🧪 Ejecutar Tests

```bash
pytest
```

## 🔄 Variables de Entorno

El proyecto utiliza las siguientes variables de entorno (configuradas en `app/core/config.py`):

- `SECRET_KEY`: Clave secreta para JWT
- `ALGORITHM`: Algoritmo para JWT (por defecto: "HS256")
- `ACCESS_TOKEN_EXPIRE_MINUTES`: Tiempo de expiración del token (por defecto: 60)

## 📦 Docker

El proyecto está dockerizado para facilitar su despliegue. Los archivos principales son:

- `Dockerfile`: Define la imagen de la aplicación
- `docker-compose.yml`: Configura los servicios
- `.dockerignore`: Excluye archivos innecesarios del build

### Puertos

- `8000`: API FastAPI

## 🤝 Contribuir

1. Fork el proyecto
2. Crea tu rama de características (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📝 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.
