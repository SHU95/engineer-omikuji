
from linebot import LineBotApi
from linebot.models import TextSendMessage,  FlexSendMessage

#line_bot_api = LineBotApi('発行されたCHANNEL_ACCESS_TOKEN')


def res():
    payload={
    "type": "bubble", // ①
    "body": { // ②
        "type": "box", // ③
        "layout": "horizontal", // ④
        "contents": [ // ⑤
        {
            "type": "text", // ⑥
            "text": "Hello,"
        },
        {
            "type": "text", // ⑥
            "text": "World!"
        }
        ]
    }
    }

    container_obj = FlexSendMessage.new_from_json_dict(payload)
    return container_obj
    #line_bot_api.push_message(, messages=container_obj)