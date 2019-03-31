from telegrambot.handlers import command

from handlers.views import StartView
from handlers.views import AcceptView
from handlers.views import ListLangsView


urlpatterns = [
    command('start', StartView.as_command_view()),
    command('accept', AcceptView.as_command_view()),
    command('list', ListLangsView.as_command_view()),
]
