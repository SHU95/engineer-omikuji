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
help コマンドのマニュアルを表示します。
ls   ファイルやディレクトリの情報を表示します。
sl   蒸気機関車が走ります。
pwd  カレントディレクトリを表示します。
echo メッセージや環境変数を表示します。
date 現在日時を表示します。
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
        from pytz import timezone
        tdatetime =  datetime.datetime.now(timezone('Asia/Tokyo'))
        tstr=str(tdatetime)
        #tstr = tdatetime.strftime.today()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=tstr)
        )
    elif event.message.text=='echo':
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text='echo')
        )
    elif event.message.text=='contributors':
        text="""
        contributors:

        Moriten 
        https://twitter.com/ImR0305

        Arai 
        https://twitter.com/ElectroARAIsan

        SHU 
        https://twitter.com/shark95shu

        Kalancs
        https://twitter.com/kalancs17

        Special thanks:
        Nao Tagai
        """

        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=text)
        )
    elif event.message.text=='ぬるぽ':
        text='ｶﾞｯ'
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=text)
        )

    else:
        line_bot_api.reply_message(
            event.reply_token,
            #TextSendMessage(text='command not found')
            TextSendMessage(text="command '"+event.message.text+"' not found")
        )






        






















































