
from linebot import LineBotApi
from linebot.models import CarouselContainer
from linebot.models import TextSendMessage,  FlexSendMessage

#line_bot_api = LineBotApi('発行されたCHANNEL_ACCESS_TOKEN')


payload = {
    "type": "flex",
    "altText": "Flex Message",
    "contents": {
        "type": "bubble",
        "hero": {
            "type": "image",
            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_1_cafe.png",
            "size": "full",
            "aspectRatio": "20:13",
            "aspectMode": "cover",
            "action": {
                "type": "uri",
                "label": "Line",
                "uri": "https://linecorp.com/"
            }
        },
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
            {
                "type": "text",
                "text": "Brown Cafe",
                "weight": "bold",
                "size": "xl",
                "align": "center",
                "contents": []
            },
            {
                "type": "box",
                "layout": "vertical",
                "spacing": "sm",
                "margin": "lg",
                "contents": [
                {
                    "type": "box",
                    "layout": "baseline",
                    "spacing": "sm",
                    "contents": [
                    {
                        "type": "text",
                        "text": "Place",
                        "size": "sm",
                        "color": "#AAAAAA",
                        "flex": 1,
                        "contents": []
                    },
                    {
                        "type": "text",
                        "text": "Miraina Tower, 4-1-6 Shinjuku, Tokyo",
                        "size": "sm",
                        "color": "#666666",
                        "flex": 5,
                        "wrap": True,
                        "contents": []
                    }
                    ]
                }
                ]
            }
            ]
        },
        "footer": {
            "type": "box",
            "layout": "vertical",
            "flex": 0,
            "spacing": "sm",
            "contents": [
            {
                "type": "button",
                "action": {
                    "type": "uri",
                    "label": "CALL",
                    "uri": "https://linecorp.com"
                },
                "height": "sm",
                "style": "link"
            },
            {
                "type": "button",
                "action": {
                    "type": "uri",
                    "label": "WEBSITE",
                    "uri": "https://linecorp.com"
                },
                "height": "sm",
                "style": "link"
            },
            {
                "type": "spacer",
                "size": "sm"
            }
            ]
        }
    }
}

def res():
    return FlexSendMessage.new_from_json_dict(payload)
