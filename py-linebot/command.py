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
    TemplateSendMessage,ButtonsTemplate,URIAction,VideoSendMessage
)

helpMsg ="""
ls   \n
sl   蒸気機関車が走ります。\n
"""

def command(event, line_bot_api):
    if event.message.text=='ls':
        text='docker  static  command.py  debugjinja.py docker-compose.yml  Dockerfile  help.py  main.py omikuji.py requirements.txt  runtime.txt  yaminabe.py'
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
            TextSendMessage(text='/app/py-linebot')
        )
    elif event.message.text=='help':
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=helpMsg)
        )
    elif event.message.text.startswith('echo '):
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=str.lstrip(event.message.text[5:]))
        )
    elif event.message.text=='date':
        tdatetime =  datetime.datetime.now()
        tstr = tdatetime.strftime('%Y/%m/%d')
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=tstr)
        )
    else:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text='command not found')
        )
        

        







        







        







        

























