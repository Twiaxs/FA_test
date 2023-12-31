# FastAPI Калькулятор страхования

Это FastAPI-приложение, которое предоставляет эндпоинты для расчета стоимости страхования на основе загруженных тарифов из файла.

### Установка / Installation

    docker-compose up --build
  
### Запуск / Run

    docker-compose up

## Методы

### `POST /load_rates`

Загрузка тарифов из файла.

#### Запрос

- Эндпоинт: `/load_rates`
- Метод: `POST`
- Параметры:
  - `file` (UploadFile): Файл с тарифами для загрузки.

#### Ответ

- Код состояния `200 OK`: Тарифы успешно загружены.

---

### `GET /calculate_insurance_cost`

Расчет стоимости страхования.

#### Запрос

- Эндпоинт: `/calculate_insurance_cost`
- Метод: `GET`
- Параметры:
  - `cargo_type` (строка): Тип груза.
  - `declared_value` (число): Заявленная стоимость груза.
  - `calculation_date` (дата): Дата расчета стоимости.

#### Ответ

- Код состояния `200 OK`: Успешный запрос. В ответе содержится стоимость страхования.

- Код состояния `404 Not Found`: Тариф для указанного типа груза и даты не найден.


