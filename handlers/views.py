import logging
from telegram import ParseMode
from telegram import InlineKeyboardButton
from telegram import InlineKeyboardMarkup
from telegrambot.bot_views.generic import TemplateCommandView
from telegrambot.bot_views.generic.responses import TextResponse

from django.template.loader import get_template


logger = logging.getLogger(__name__)


class StartView(TemplateCommandView):
    template_text = 'handlers/messages/command_start_text.txt'


class AcceptView(TemplateCommandView):
    template_text = 'handlers/messages/command_accept_text.txt'
