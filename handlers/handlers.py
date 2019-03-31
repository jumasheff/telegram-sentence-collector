from telegrambot.handlers import command
from telegrambot.handlers import regex

from handlers.views import StartView
from handlers.views import AcceptView
from handlers.views import ListLangsView
from handlers.views import LangView
from handlers.views import NewSentenceView


urlpatterns = [
    command('start', StartView.as_command_view()),
    command('accept', AcceptView.as_command_view()),
    command('list', ListLangsView.as_command_view()),
    regex(r'^[a-z]{2}$', LangView.as_command_view()),
    command('new', NewSentenceView.as_command_view()),
]
