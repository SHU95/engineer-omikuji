from flask import Flask, request, abort
import os,json,shutil
import urllib
from PIL import Image, ImageDraw, ImageFont
from massage import res
import datetime
import random

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, PostbackTemplateAction, PostbackEvent, PostbackAction, QuickReplyButton, QuickReply,
    FlexSendMessage, BubbleContainer, CarouselContainer, TextSendMessage,ImageSendMessage,
    TemplateSendMessage,ButtonsTemplate,URIAction
)

def command(event, line_bot_api):
    if event.message.text=='ls':
        text='docker, static, command.py, debugjinja.py'
        line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text=text)
            )
    else:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=event.message.text)
        )
