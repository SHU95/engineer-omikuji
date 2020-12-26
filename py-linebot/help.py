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
help_comment = ""
msgActions = [
    MessageAction(
        label="おみくじ",
        text="おみくじ"
    ),
    MessageAction(
        label="闇鍋ガチャ",
        text="闇鍋"
    )
]

def help(event, line_bot_api):
    line_bot_api.reply_message(
        event.reply_token,
        TemplateSendMessage(
            alt_text="ヘルプ",
            template=TemplateSendMessage(
                title="ヘルプ",
                text=help_comment,
                actions=msgActions
            )
        )
    )