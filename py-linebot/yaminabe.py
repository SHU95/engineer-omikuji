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
  gatixya=[['HTML','CSS','JS'],['python','Go','R','Ruby']]
