# Create your models here.

from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

'''
Строки, начинающиеся с from или import, открывают доступ к коду из других файлов. Так что вместо того,
чтобы копировать и вставлять один и тот же код во все файлы, ты можешь сослаться на него при помощи 
from ... import ....

class Post(models.Model): — эта строка определяет нашу модель (объект).
•	class — это специальное ключевое слово для определения объектов.
•	Post — это имя нашей модели, мы можем поменять его при желании (специальные знаки и пробелы использовать нельзя). 
Всегда начинай имена классов с прописной буквы.
•	models.Model означает, что объект Post является моделью Django, так Django поймет,
что он должен сохранить его в базу данных.
Дальше мы задаем свойства, о которых уже говорили: title, text, created_date, published_date и author. 
Чтобы это сделать, нам нужно определиться с типом полей (это текст? число? дата? ссылка на другой объект? например, 
на пользователя?).
•	models.CharField — так мы определяем текстовое поле с ограничением на количество символов.
•	models.TextField — так определяется поле для неограниченно длинного текста. 
•	models.DateTimeField — дата и время.
•	models.ForeignKey — ссылка на другую модель.

def publish(self)
Это как раз метод публикации для записи. def  означает, что создаётся функция/метод, 
а publish — это название этого метода. 
Существует правило для имён функций: нужно использовать строчные буквы, а пробелы заменять на подчёркивания. 
Например, метод, вычисляющий среднюю цену, может называться calculate_average_price.

Методы часто возвращают что-то. Например, метод __str__. В нашем случае после вызова метода __str__() 
мы получим текст (строку) с заголовком записи.

оба метода def publish(self): и def __str__(self): внутри класса имеют дополнительный отступ. 
Поскольку в Python важны отступы, нам необходимо использовать их для методов внутри класса — 
иначе методы не будут принадлежать к классу, и при запуске программы может получиться что-то неожиданное.

'''