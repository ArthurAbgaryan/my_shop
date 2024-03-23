import os
# from celery import Celery

#задаем перем. окружения , содерж. название файла настроек нашего проекта, для консольных команд Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE','my_shop.settings')

app = Celery('my_shop') #Создаем экземпляр приложения

app.config_from_object('django.conf:settings', namespace = 'CELERY')
app.autodiscover_tasks() #поиск и запуск ассинхронных приложений и задач

__all__ = ('my_shop',)