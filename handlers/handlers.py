from telegrambot.handlers import command

from handlers.views import StartView
from handlers.views import AcceptView


urlpatterns = [
    command('start', StartView.as_command_view()),
    command('accept', AcceptView.as_command_view()),
]
