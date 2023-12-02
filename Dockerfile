# Сначала мы тянем питоно-образ
FROM python:3.11-bullseye

# копируем и устанаваливаем
COPY ./requirements.txt /app/requirements.txt

# переключимся на наш /app
WORKDIR /app

# Теперь можем установить наше окружение
RUN pip install -r requirements.txt

# Теперь перетащим всё остальное
COPY . /app

# Настроим, что будет делать контейнер при запуске

# настраиваем с помощью какого менеджера запускается код
ENTRYPOINT [ "python3" ]

# что делаем с энтрипоинтом
CMD [ "app.py" ]
