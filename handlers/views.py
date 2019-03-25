import logging
from telegram import ParseMode
from telegram import InlineKeyboardMarkup
from telegrambot.bot_views.generic import TemplateCommandView
from telegrambot.bot_views.generic.responses import TextResponse

from django.template.loader import get_template


logger = logging.getLogger(__name__)


class StartView(TemplateCommandView):
    template_text = 'handlers/messages/command_start_text.txt'
    template_keyboard = 'handlers/messages/command_languages_list_keyboard.txt'


def start(bot, update, **kwargs):
    template_text = 'handlers/messages/command_start_text.txt'
    template_keyboard = 'handlers/messages/command_languages_list_keyboard.txt'
    template_kbrd = get_template(template_keyboard)
    text = TextResponse(template_text, {}).render()
    keyboard = template_kbrd.render()
    keyboard = InlineKeyboardMarkup(keyboard, resize_keyboard=True)
    bot.send_message(chat_id=update.message.chat_id, text=text, reply_markup=keyboard, parse_mode=ParseMode.MARKDOWN)
