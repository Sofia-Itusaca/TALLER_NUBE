# TALLER_NUBE

Proyecto base para taller de despliegue en la nube.

## Arquitectura

- Frontend: Svelte + Vite
- Estilos: Tailwind CSS
- Servidor web: Nginx
- Contenedores: Docker
- Orquestación local: Docker Compose
- Cloud: Microsoft Azure
- Control de versiones: Git + GitHub

## Ramas

- `main`: versión principal y desplegada.
- `feature/2-apis-clima`: futura modificación para integrar dos APIs de clima con mecanismo de respaldo.

## Estructura

```text
TALLER_NUBE/
├── deploy/
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   └── pages/
│   ├── tests/
│   ├── Dockerfile
│   ├── nginx.conf
│   ├── package.json
│   ├── svelte.config.js
│   ├── tailwind.config.js
│   └── vite.config.js
├── specs/
├── .env.example
├── .gitignore
├── docker-compose.yml
└── README.md
```
