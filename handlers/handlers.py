from telegrambot.handlers import command

from handlers.views import start


urlpatterns = [
    command('start', start),
]
