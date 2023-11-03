#   Service App
Небольшое django-приложение, для отработки celery, redis, docker.

## Установка 

#### Запустим контейнеры:
docker compose -f docker-compose.yml up -d

#### Зайдем в контейнер приложения и произведем необходимые команды
docker exec -it service_app-web-app-1 /bin/sh \
python manage.py migrate \
python manage.py createsuperuser \
exit 
