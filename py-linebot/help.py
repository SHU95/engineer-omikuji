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
    TemplateSendMessage,ButtonsTemplate,URIAction,MessageAction
)

#TODO ヘルプコメントとコマンド誰か書いて
help_comment = " コロナ禍でもエンジニアが年末年始を楽しむために作ったLINEBotです。"

def help(event, line_bot_api):
    line_bot_api.reply_message(
        event.reply_token,
        TemplateSendMessage(
            alt_text="ヘルプ",
            template=ButtonsTemplate(
                text=help_comment,
                title="ヘルプ",
                actions=[
                    MessageAction(
                        text="おみくじ",
                        label="おみくじ"
                    ),
                    MessageAction(
                        text="闇鍋",
                        label="闇鍋ガチャ"
                    ),
                    MessageAction(
                        text="参拝",
                        label="デバッグ神社"
                    ),
                    MessageAction(
                        text="help",
                        label="help"
                    )
                ]
            )
        )
    )