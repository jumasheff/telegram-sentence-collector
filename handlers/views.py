import logging
from telegrambot.bot_views.generic import TemplateCommandView

logger = logging.getLogger(__name__)


class StartView(TemplateCommandView):
    template_text = 'bot/messages/command_start_text.txt'
    logger.debug('me here')

    def handle(self, bot, update, **kwargs):
        super().handle(bot, update, **kwargs)
        chat_id = update.message.chat_id
        log_msg = 'THIS IS IN StartView: {}'.format(chat_id)
        logger.debug(log_msg)
