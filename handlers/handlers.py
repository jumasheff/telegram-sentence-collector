from telegrambot.handlers import command
from telegrambot.handlers import regex
from telegrambot.handlers import message

from handlers.views import StartView
from handlers.views import AcceptView
from handlers.views import ListLangsView
from handlers.views import LangView
from handlers.views import AddSentenceView
from handlers.views import ValidateView
from handlers.views import NewSentenceView


urlpatterns = [
    command('start', StartView.as_command_view()),
    command('accept', AcceptView.as_command_view()),
    command('list', ListLangsView.as_command_view()),
    regex(r'^/(?P<lang>[a-z]{2})$', LangView.as_command_view()),
    command('add', AddSentenceView.as_command_view()),
    command('validate', ValidateView.as_command_view()),
    message(NewSentenceView.as_command_view()),
]
