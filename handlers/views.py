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


class ListLangsView(TemplateCommandView):
    template_text = 'handlers/messages/command_list_langs_text.txt'


class LangView(TemplateCommandView):
    template_text = 'handlers/messages/command_lang_text.txt'

    def handle(self, bot, update, **kwargs):
        ctx = self.get_context(bot, update, **kwargs)
        text = TextResponse(self.template_text, ctx).render()
        keyboard = [[
            InlineKeyboardButton('New sentence', callback_data='0'),
            InlineKeyboardButton('Validate sentences', callback_data='1')
        ]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        bot.send_message(chat_id=update.message.chat_id, text=text, reply_markup=reply_markup)


class NewSentenceView(TemplateCommandView):
    template_text = 'handlers/messages/command_new_sentence_text.txt'
