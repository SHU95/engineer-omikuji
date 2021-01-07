from flask import Flask, request, abort
import os,json,shutil
import urllib
from PIL import Image, ImageDraw, ImageFont
from massage import res
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

def yaminabe(event, line_bot_api):
    gatixya=[
        # フロントエンド
        ['HTML','CSS','JS','Node.js','Nuxt.js','Next.js','React.js'],
        # バッグエンド
        ['Java','python','Go','R','Ruby','C#','C++','C','PHP'],
        # 利用サービス
        ['AWS','GCP','Azure','heroku']]

    ans=[]
    for i in gatixya:
        ans.append(random.choice(i))

    text=f'使用技術：{ans[0]} , {ans[1]} , {ans[2]}'

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=text)
    )



