import logging
from telegrambot.bot_views.generic import TemplateCommandView

logger = logging.getLogger(__name__)


class StartView(TemplateCommandView):
    template_text = 'handlers/messages/command_start_text.txt'
