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
        text='docker  static  command.py  debugjinja.py  docker-compose.yml  Dockerfile  help.py  main.py  omikuji.py requirements.txt  runtime.txt  yaminabe.py'
        line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text=text)
            )
    elif event.message.text=='sl':
        line_bot_api.reply_message(
            event.reply_token,
            VideoSendMessage(
                original_content_url= f"https://hackathon-engineer-omikuji.herokuapp.com/static/mikuji/sl.mp4",
                preview_image_url=f"https://hackathon-engineer-omikuji.herokuapp.com/static/mikuji/sl.jpg",
            )
            )
    elif event.message.text=='pwd':
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text='/app/py-lnebot')
        )

    
    else:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text='command not found')
        



