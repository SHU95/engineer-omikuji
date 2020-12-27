from flask import Flask, request, abort
import os,json,shutil,urllib,random
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import requests

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)

from linebot.models import (
    MessageEvent, TextMessage, PostbackTemplateAction, PostbackEvent, PostbackAction, QuickReplyButton, QuickReply,
    FlexSendMessage, BubbleContainer, CarouselContainer, TextSendMessage,ImageSendMessage,
    TemplateSendMessage,ButtonsTemplate,URIAction,MessageAction
)

def make_random_day():
    rand_year = random.randint(2018,2020)
    rand_month = 0
    if rand_year == 2018:
        rand_month = random.randint(9,12)
    else:
        rand_month = random.randint(1,12)

    rand_day = 0
    if rand_month in {1,3,5,7,8,10,11}:
        rand_day = random.randint(1,31)
    elif rand_month in {2}:
        rand_day = random.randint(1,28)
    elif rand_month in {12}:
        rand_day = random.randint(1,21)
    else:
        rand_day = random.randint(1,30)

    day = str(rand_year)+'-'+str(rand_month).zfill(2)+'-'+str(rand_day).zfill(2)

    return day

def qiita(event, line_bot_api):
    day = make_random_day()
    ranking_api = 'https://us-central1-qiita-trend-web-scraping.cloudfunctions.net/qiitaScraiping/daily/' + day
    resp = requests.get(ranking_api)
    json_load = resp.json()

    urls = []
    for item in json_load['data']:
        #urls.append(item['url'])
        urls.append(item)

    url_count = len(urls)
    ret_id = random.randint(0,url_count-1)

    line_bot_api.reply_message(
        event.reply_token,
        TemplateSendMessage(
            alt_text="qiita",
            template=ButtonsTemplate(
                text=urls[ret_id]['title'],
                title="おすすめの記事！",
                actions=[
                    URIAction(
                        uri=urls[ret_id]['url'],
                        label=urls[ret_id]['url']
                    ),
                    MessageAction(
                        text="qiita",
                        label="qiita"
                    )
                ]
            )
        )
    )
