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

def debugjinja(event, line_bot_api):
  kakugen = ['未来を予測する最善の方法は、それを開発することだ。',
  '完璧を目指すよりも、まずは終わらせろ。',
  'アイデアを思いついたら、まず自分自身でビルドせよ。それが脳を鍛え、イノベーションへとつながる',
  'もしそれがよい考えなら、思い切ってそれをしなさい。許可をもらうよりも、謝るほうが簡単だから。',
  '実のところ、すべてを備えていない言語のほうがプログラミングは簡単である。',
  'シンプルであれ。',
  'たぶん動くと思うからリリースしようぜ',
  '今日なし得ることに全力をつくせ。しからば明日は一段の進歩あらん。',
  '発見のチャンスは、準備のできた者だけに微笑む。',
  ' 変革せよ。変革を迫られる前に。',
  'どんなマーケティングでも、駄作をヒットさせることはできない。',
  'やっつけ仕事は評価が高い',
  '真のプログラマは、楽をするためにはどんな苦労も厭わない。',
  '次の日ぱっと見ると一瞬で原因がわかる。',
  'プログラムは思った通りに動かない。書いた通りに動く。',
  ]

  ans=random.choice(kakugen)
  dt_now = datetime.datetime.now()
  h=dt_now.hour

  if h<=17 or h>8:
    image_path='hiru2.jpg'
  else:
    image_path='yoru2.jpg'



  line_bot_api.reply_message(
        event.reply_token,
        [
            ImageSendMessage(
                original_content_url= f"https://hackathon-engineer-omikuji.herokuapp.com/static/mikuji/{image_path}",
                preview_image_url=f"https://hackathon-engineer-omikuji.herokuapp.com/static/mikuji/{image_path}",
            ),
            TextSendMessage(
                text = ans
            )

        ]
    )



