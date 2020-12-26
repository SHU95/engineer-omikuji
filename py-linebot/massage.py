
from linebot import LineBotApi
from linebot.models import CarouselContainer
from linebot.models import TextSendMessage,  FlexSendMessage

#line_bot_api = LineBotApi('発行されたCHANNEL_ACCESS_TOKEN')


def res():
    payload={
    "type": "bubble",
    "body": { 
        "type": "box", 
        "layout": "horizontal", 
        "contents": [ 
        {
            "type": "text", 
            "text": "Hello,"
        },
        {
            "type": "text", 
            "text": "World!"
        }
        ]
    }
    }

    #container_obj = CarouselContainer.new_from_json_dict(payload)
    container_obj = FlexSendMessage.new_from_json_dict(payload)
    return container_obj
    #line_bot_api.push_message(, messages=container_obj)