from flask import Flask, request, abort
import os
from dic import dic
from make_mikuji import make_mikuji
from PIL import Image, ImageDraw, ImageFont
from PIL import Image
from massage import res

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, ImageSendMessage,FlexSendMessage
)


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

        omikuji(event)
        
        """
        image_link, lucky_text = make_mikuji.get_mikuji()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=lucky_text)
        )

        image_message = ImageSendMessage(
            content_url = image_link,
        )
        line_bot_api.reply_message(event.reply_token,image_message)
        """
    else:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=event.message.text)
        )

def omikuji(event):
   
    container_obj=res()
    #line_bot_api.push_message(messages=container_obj)
    line_bot_api.reply_message(
            event.reply_token,
            FlexSendMessage(messages=container_obj)
        )
    

    '''
    text=dic()
    #path="https://hackathon-engineer-omikuji.herokuapp.com/static/mikuji/base.jpg"
    #image = Image.open(path)

    #image_path,comment=make_mikuji(text,image)

    image_path = "base.jpg"
    comment='test'

    
    line_bot_api.reply_message(
        event.reply_token,
        [
            TextSendMessage(
                text = "おみくじの結果は？？？？\n" + comment
            ),
            ImageSendMessage(
                original_content_url= f"https://hackathon-engineer-omikuji.herokuapp.com/static/mikuji/{image_path}",
                preview_image_url=f"https://hackathon-engineer-omikuji.herokuapp.com//static/mikuji/{image_path}",
                #original_content_url='https://cdn.shibe.online/shibes/907fed97467e36f3075211872d98f407398126c4.jpg' ,
                #preview_image_url='https://cdn.shibe.online/shibes/907fed97467e36f3075211872d98f407398126c4.jpg',
            )
        ]
    )
    '''

    



if (__name__ == "__main__"):

    port = int(os.getenv("PORT"))
    app.run(host="0.0.0.0", port = port)

