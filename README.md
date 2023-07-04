# Tech assessment
This tech assessment was built using FastAPI with PostgreSQL DB, and using React. It was containerized for ease of running and developing the application

## Run instructions
1. Be sure to have latest docker installed
2. Create a .env file in the root of the project with the following contents
```Dotenv
BACK_NAME=backend
BACK_HOST=0.0.0.0
BACK_PORT=8000

POSTGRES_HOST=db
POSTGRES_PORT=5432
POSTGRES_USER=admin
POSTGRES_PASSWORD=admin
POSTGRES_DB=backend

PGADMIN_EMAIL=admin@admin.com
PGADMIN_PASSWORD=admin
PGADMIN_PORT=5050

FRONTEND_PORT=8000
FRONTEND_NODE_ENV=development
```
3. (Optional) Go to `docker-compose.yml` and uncomment de pgadmin image if you want to have it to check the DB
4. Build up containers and run it with the following
```bash
$ docker-compose up -d
```
5. Test the app in `localhost:8000` for Frontend and `localhost:8000/api` for the Backend. The docs are located in `localhost:8000/api/docs`

## Decisions
1. Docker setup was done to ease development and further dockerization on deployment.
2. Postgres used for robustness and reliability
3. FastAPI to declare a simple and scalable API, taking appropriate decisions (Backend by layers, repository pattern, etc)
4. Tests are not yet added, but for functionality after version 1 should be the top priority