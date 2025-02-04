[![Black Formatting](https://github.com/MonkeyQY/insurance_calculation/actions/workflows/black.yml/badge.svg)](https://github.com/MonkeyQY/insurance_calculation/actions/workflows/black.yml)
[![Flake8 Linting](https://github.com/MonkeyQY/insurance_calculation/actions/workflows/flake8.yml/badge.svg)](https://github.com/MonkeyQY/insurance_calculation/actions/workflows/flake8.yml)
[![Run pytest](https://github.com/MonkeyQY/insurance_calculation/actions/workflows/pytest.yml/badge.svg)](https://github.com/MonkeyQY/insurance_calculation/actions/workflows/pytest.yml)
## Предустановка

Для успешного запуска приложения необходимо убедиться, что на вашей машине установлены следующие утилиты:

- `docker compose plugin` и `docker`

## Запуск

Подключиться к бд и создать базу данных

### Prod

Для того, чтобы запустить приложение в Production режиме, вам необходимо создать `.env` файл в корне репозитория. Можете посмотреть содержимое [`example_env`](example_env) для ознакомления. Полный список возможных переменных окружения в `.env` файле приведен в [`ENVIRONMENTS.md`](ENVIRONMENTS.md) файле.

После создания `.env` файла, можно выполнить следующую команду:

```
$ docker compose -f docker-compose.prod.yml up --build
```

## Документация

**URLS**:

- Локально - http://localhost:8000/docs/