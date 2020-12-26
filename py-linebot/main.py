from flask import Flask, request, abort
import os,json,shutil,urllib,random
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

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

# これから追加する.pyファイルのimportはここにしてほしい（コピペしにくい）
from omikuji import omikuji
from yaminabe import yaminabe
from massage import res
from help import help

app = Flask(__name__)

#環境変数取得
YOUR_CHANNEL_ACCESS_TOKEN = os.environ["YOUR_CHANNEL_ACCESS_TOKEN"]
YOUR_CHANNEL_SECRET = os.environ["YOUR_CHANNEL_SECRET"]

line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(YOUR_CHANNEL_SECRET)

@app.route("/")
def hello_world():
    return "Hello world!"

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if (event.message.text == "おみくじ" or event.message.text == "おみくじをひく"):
        omikuji(event, line_bot_api)
    elif (event.message.text =='闇鍋ガチャ' or event.message.text == '闇鍋'):
        yaminabe(event, line_bot_api)
    elif (event.message.text =='参拝' or event.message.text =='デバック神社'):
        debugjinja(event, line_bot_api)
    elif (event.message.text =='ヘルプ' or event.message.text == 'help'):
        help(event, line_bot_api)

    else:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=event.message.text)
        )

if (__name__ == "__main__"):

    port = int(os.getenv("PORT"))
    app.run(host="0.0.0.0", port = port)

