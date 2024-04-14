import json
from info import title, description, release_date, image, price, event_start, event_end

def template():
    # 게임 정보를 이용해 카카오톡 메시지 템플릿을 생성하고 JSON 문자열로 반환합니다.
    template_object = json.dumps({
        "object_type": "feed",
            "content": {
                "title": title(),  # 게임 제목
                "description": description(),  # 게임 설명
                "image_url": image(),  # 이미지 URL
                "image_width": 640,
                "image_height": 640,
                "link": {
                    "web_url": "https://store.epicgames.com/en-US/free-games",  # 웹 링크
                    "mobile_web_url": "https://store.epicgames.com/en-US/free-games",
                    "android_execution_params": "contentId=100",
                    "ios_execution_params": "contentId=100"
                }
            },
            "item_content" : {
                "profile_text" :"THIS WEEK'S FREE EPIC GAME",  # 프로필 텍스트
                "title_image_text" : title(),  # 이미지 타이틀 텍스트
                "title_image_category" : "Base",
                "items" : [
                    {
                        "item" :"PRICE",
                        "item_op" : f'{price()} → FREE!'  # 가격
                    },
                    {
                        "item" :"Sale starts at",
                        "item_op" : event_start()  # 할인 시작 시간
                    },
                    {
                        "item" :"Sale ends at",
                        "item_op" : event_end()  # 할인 종료 시간
                    },
                    {
                        "item" :"Release Date",
                        "item_op" : release_date()  # 출시 날짜
                    }
                ],
            },
            "buttons": [
                {
                    "title": "웹으로 이동",  # 버튼 제목
                    "link": {
                        "web_url": "https://store.epicgames.com/en-US/free-games",  # 링크 URL
                        "mobile_web_url": "https://store.epicgames.com/en-US/free-games"
                    }
                }
            ]
        })
    return template_object
