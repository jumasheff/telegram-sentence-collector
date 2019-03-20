from telegrambot.handlers import command

from handlers.views import StartView


urlpatterns = [
    command('start', StartView.as_command_view()),
]
