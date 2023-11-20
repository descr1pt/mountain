# Проект виртуальной стажировки онлайн-школы Skillfactory
## Описание проекта
### Мобильное приложение для оправки информации туристами о посещённых ими горных перевалов.

Мобильное приложение для Android и IOS, пользователями которого будут туристы. В горах они будут вносить данные о перевале в приложение и отправлять их в ФСТР ( Федерация спортивного туризма России ), как только появится доступ в Интернет, для того чтобы поделиться информацией с другими людьми, увлеющимися туризмом и преодолением горных перевалов.
## Работа проекта
### Внесение личной информации.

Для отправки информации туристу необходимо будет заполнить данные о себе (регистрация не требуется):
1. Фамилия
2. Имя
3. Отчество
4. Электронная почта
5. Номер телефона

### Внесение информации о горном перевале.

Для отправки информации о горном перевале, туристу необходимо будет также заполнить несколько полей:
1. Название горного перевала
2. Альтернативное название горного перевала
3. Произвольный текст ввиде комментария
4. Координаты горного перевала
5. Сложность восхождения (в зависимости от времени года)
6. Несколько фотографий

### Обработка информации.

Модератор из федерации будет верифицировать и вносить в базу данных информацию, полученную от пользователей, а те в свою очередь смогут увидеть в мобильном приложении статус модерации и просматривать базу с объектами, внесёнными другими.

## Содержание проекта

### Основные пункты.

* Проект выполнен на языке программирования Python
* С использованием фреймворка Django
* В проекте используется СУБД PostgreSQL

### Модели проекта.

Модель пользователя `MyUser` содержит 5 полей для заполнения данных о пользователе:
* 4 поля `CharField` для заполения данных
* 1 поле `EmailField` для указания электронной почты

Модель `Coord` служит для указания координат горного перевала и имеет 3 поля:
* 2 поля `FloatField` для указания широты и долготы
* 1 поле `IntegerField` для указания высоты

Модель `Level` служит для указания уровня сложности восхождения на тот или иногй горный перевал:
* Имеет 4 поля `CharField` в каждом из которых необходимо выбрать уровень сложности восхождения от 1А до 5Б

Основной моделью проекта является модель `Pereval` включающая в себя 9 полей:
* 4 поля `CharField` включающие в себя общее название, название и альтернативное название горного перевала, а таже поле `status` с выбором статуса модерации.
* 1 поле `DateTimeField` для даты и времени добавления горного перевала
* 1 поле `TextField` для добавления произвольного комментария от пользователя
* Поля `level_id` и `user_id` имеющие отношения один ко многим с соответствующими моделями
* Поле `coord_id` имеющее отношение один к одному с соответствующей моделью

Модель `Images` служит для добавления фото горного перевала, имеет 3 поля:
* Поле `pereval_id` имеющее имеющие отношения один ко многим с соответствующей моделью
* Поле `data` имеющее тип `URLField` для добавления ссылки на изображение
* А также поле `title` для обозначения названия изображения

### Сериализаторы проекта.

Каждая модель проекта имеет соответствующий сериализатор.
Основным сериализатором проекта служит `PerevalSerializer` содержащий в себе сериализаторы остальных моделей.

```
class PerevalSerializer(WritableNestedModelSerializer):
    user_id = MyUserSerializer()
    coord_id = CoordSerializer()
    level_id = LevelSerializer(allow_null=True)
    images = ImagesSerializer(many=True)
```

### Представления и маршрутизация проекта.

В качестве представлений в проекте используется наследование класса `ModelViewSet`.
```
class PerevalViewSet(viewsets.ModelViewSet):
    queryset = Pereval.objects.all()
    serializer_class = PerevalSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ["user_id__email"]
```
В проекте используются единственный url, предоставляющий список всех добавленных перевалов от пользователей
`path('submitData/', include(router.urls))`
Можно просмотреть информацию об отдельном перевале по id.
При этом есть возможность использовать CRUD методы, а также фильтровать добавленную информацию по электронной почте пользователя.

### Ограничения в проекте.

В проекте существует условие при котором пользователь может изменить отправленные данные:
1. Данные не должны относиться к данным о самом пользователе (фамилия, имя, телефон и т.д.)
2. Статус модерации данной информации должен быть статусом 'NEW', при остальных статусах модерации, изменение данных невозможно 

### Данный проект есть на хостинге pythonanywhere
ссылка

### Пример JSON файла с данными.

{
        "beauty_title": "Арарат",
        "title": "Вершина в Турции",
        "other_titles": "Гора",
        "connect": "комментарий",
        "level_id": {
            "winter": "2a",
            "summer": "2b",
            "autumn": "1a",
            "spring": "2a"
        },
        "user_id": {
            "email": "example3@gmail.com",
            "phone": "+7774444",
            "fam": "Петров",
            "name": "Иван",
            "otc": "Иванович"
        },
        "coord_id": {
            "latitude": 12.234333,
            "longitude": 123.3333,
            "height": 10005
        },
        "images": [
            {
                "data": "https://images.app.goo.gl/jN6hc6jrN8Pw54q69",
                "title": "Elbrus.jpg"
            }
        ]
    }

### Документация проекта с помощью Swagger.

http://127.0.0.1:8000/redoc/

http://127.0.0.1:8000/swagger/