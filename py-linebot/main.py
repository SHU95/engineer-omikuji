from flask import Flask, request, abort
import os
from dic import dic
import make_mikuji

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, ImageSendMessage,
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
    if (event.message.text != "おみくじ"):
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=event.message.text)
        )

    # 画像送信
    """
    main_image_path = f"lena.jpg"
    image_message = ImageSendMessage(
        original_content_url = f"https://date-the-image.herokuapp.com/{main_image_path}",
    )
    line_bot_api.reply_message(event.reply_token,image_message)
    """

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



def omikuji(event):
    link, identifier = dic()
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(
            text = event.message.text
        )
        [
            TextSendMessage(
                text = "おみくじの結果！" +
                    (identifier == "" if "" else "\n" + identifier)
            ),
            ImageSendMessage(
                original_content_url = link
            )
        ]
    )

if __name__ == "__main__":

    port = int(os.getenv("PORT"))
    app.run(host="0.0.0.0", port = port)

