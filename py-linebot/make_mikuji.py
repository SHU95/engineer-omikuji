from PIL import Image, ImageDraw, ImageFont
import random
from dic import dic

def make_mikuji(text):
    base_text=['エンジニアおみくじ','縁起の良い言語','デバッグ運','開発環境','技術書','行うべき習慣']
    
    #元画像を読み込んでくる場合
    #image = Image.open("https://hackathon-engineer-omikuji.herokuapp.com/static/mikuji/lena.jpg")
    image = Image.open("https://cdn.shibe.online/shibes/907fed97467e36f3075211872d98f407398126c4.jpg")

    #文字を書きこむ為のオブジェクトが用意されているので取得する
    draw = ImageDraw.Draw(image)

    #フォントを決める
    font = ImageFont.truetype("static/mikuji/AoyagiKouzanTOTF.otf", size=95)
    font2 = ImageFont.truetype("static/mikuji/AoyagiKouzanTOTF.otf", size=70)
    font3 = ImageFont.truetype("static/mikuji/AoyagiKouzanTOTF.otf", size=190)

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
    image.save(f"./static/mikuji/result{no}.jpg")

    return f"result{no}.jpg",text[0]



#text=dic()
#make_mikuji(text)
