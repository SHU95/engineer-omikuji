from flask import Flask, request, abort
import os,json,shutil,random
import urllib
from PIL import Image, ImageDraw, ImageFont
from massage import res
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


def omikuji(event, line_bot_api):

    text=dic()
    #path="https://hackathon-engineer-omikuji.herokuapp.com/static/mikuji/base.jpg"
    #image = Image.open('py-linebot/static/mikuji/base.jpg')

    image_path,comment=make_mikuji(text)
    import os
    path = os.getcwd()
    files = os.listdir(path)
    print(type(files))  # <class 'list'>
    print(files) 


    url = f"https://hackathon-engineer-omikuji.herokuapp.com/static/mikuji/{image_path}"

    #image_path = "base.jpg"
    #comment='test'
    
    main.line_bot_api.reply_message(
        event.reply_token,
        TemplateSendMessage(
            alt_text="占い結果",
            template=ButtonsTemplate(
                text=comment + "だよ～",
                title="占い結果",
                image_size="contain",
                thumbnail_image_url=url,
                actions=[
                    URIAction(
                        uri="https://twitter.com/intent/tweet?" + 
                            urllib.parse.urlencode(
                            {
                                "url": url,
                                "hashtags": "えんじにあうらない",
                                "text": comment + "だよ～"
                            }
                        ),
                        label="Twitterで共有"
                    )
                ]
            )
        )
    )

def dic():
    mikuji = [['大吉','中吉','吉','小吉','末吉','凶'],
    ['python','C','C++','C+','C#','HTML','CSS','R','Go','PHP','java','Ruby','Swift','JS','Kotlin'],
    ['広い視野をもて','すぐに解決する','一度時間を置け','とにかく調べよ','誤字に気をつけよ','ひとまず落ち着け'],
    ['椅子を買うべし','キーボードを買うべし','モニターを買うべし','macを買うべし','そのままで良い'],
    ['積ん読を消費すべし','気になったものを買うべし','迷ったら買うべし'],
    ['Atcoderを続けるべし','英語の音読を続けるべし','タイピング練習を続けるべし','必ずコードを読むべし','githubを触るべし']]

    ans=[]
    for i in mikuji:
        ans.append(random.choice(i))

    return ans


def make_mikuji(text):
    base_text=['エンジニアおみくじ','縁起の良い言語','デバッグ運','開発環境','技術書','行うべき習慣']
    
    #元画像を読み込んでくる場合

    #path='./static/mikuji/base.jpg'
    image = Image.open('py-linebot/static/mikuji/base.jpg')
    # image = Image.open("https://cdn.shibe.online/shibes/907fed97467e36f3075211872d98f407398126c4.jpg")

    #文字を書きこむ為のオブジェクトが用意されているので取得する
    draw = ImageDraw.Draw(image)

    #フォントを決める
    font = ImageFont.truetype("py-linebot/static/mikuji/AoyagiKouzanTOTF.otf", size=95)
    font2 = ImageFont.truetype("py-linebot/static/mikuji/AoyagiKouzanTOTF.otf", size=70)
    font3 = ImageFont.truetype("py-linebot/static/mikuji/AoyagiKouzanTOTF.otf", size=190)

    #描きたい文字のサイズを取得する
    draw_text_width, draw_text_height = draw.textsize(base_text[0], font=font3)
    #描きたい文字のサイズと元画像のサイズを元に、描画開始ポイントの座標を決める
    start_X_point = image.size[0] / 2 - draw_text_width / 2
    start_Y_point = image.size[1] / 7.5 - draw_text_height / 2
    #draw.text((start_X_point, start_Y_point), base_text[0], fill=(0, 0, 0), font=font3)

    #描きたい文字のサイズを取得する
    draw_text_width, draw_text_height = draw.textsize(text[0], font=font3)
    #描きたい文字のサイズと元画像のサイズを元に、描画開始ポイントの座標を決める
    start_X_point = image.size[0] / 2 - draw_text_width / 2
    start_Y_point = start_Y_point+draw_text_height
    draw.text((start_X_point, start_Y_point), text[0], fill=(200, 50, 50), font=font3)



    start_Y_point=start_Y_point+15
    for i in range (len(text)-1):
        draw_text_width, draw_text_height = draw.textsize(base_text[i+1], font=font)
        start_X_point = image.size[0] / 2 - draw_text_width / 2
        start_Y_point = start_Y_point+draw_text_height+90
        draw.text((start_X_point, start_Y_point), base_text[i+1], fill=(0, 0, 0), font=font)

        draw_text_width, draw_text_height = draw.textsize(text[i+1], font=font2)
        start_X_point = image.size[0] / 2 - draw_text_width / 2
        start_Y_point = start_Y_point+draw_text_height+40
        draw.text((start_X_point, start_Y_point), text[i+1], fill=(0, 0, 0), font=font2)

    no=random.randint(0,300)

    #出来上がった画像を保存する
    image.save(f"py-linebot/static/mikuji/result{no}.png")

    return f"result{no}.png",text[0]



#text=dic()
#make_mikuji(text)
