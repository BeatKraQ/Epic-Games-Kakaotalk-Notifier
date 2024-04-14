import requests
from datetime import datetime, timedelta
import keyring

# API 요청 URL 설정
url = "https://free-epic-games.p.rapidapi.com/free"

# API 헤더에 RapidAPI 키와 호스트 정보를 추가
headers = {
	"X-RapidAPI-Key": keyring.get_password('RAPIDAPI', 'KEY'),
	"X-RapidAPI-Host": keyring.get_password('RAPIDAPI', 'HOST')
}

# API 요청을 보내고 응답을 JSON 형태로 받음
response = requests.get(url, headers=headers)
info = response.json()

def to_kr(date):
    # UTC 시간을 한국 시간(KST)으로 변환
    date_format = "%Y-%m-%dT%H:%M:%S.%fZ"
    date_obj = datetime.strptime(date, date_format)
    date_kr = date_obj + timedelta(hours=9)
    date_YMD = date_kr.strftime("%Y-%m-%d")
    return date_YMD

def title():
    # 게임 제목 반환
    title = info['freeGames']['current'][0]['title']
    return title

def description():
    # 게임 설명 반환
    description = info['freeGames']['current'][0]['description']
    return description

def release_date():
    # 게임 출시일 반환
    release_date = info['freeGames']['current'][0]['effectiveDate']
    release_date_YMD = to_kr(release_date)
    return release_date_YMD

def image():
    # 게임 이미지 URL 반환
    image = info['freeGames']['current'][0]['keyImages'][0]['url']
    return image

def price():
    # 게임 원래 가격 반환
    price_original = info['freeGames']['current'][0]['price']['totalPrice']['fmtPrice']['originalPrice']
    return price_original

def event_start():
    # 이벤트 시작 시간 반환
    event_start = info['freeGames']['current'][0]['promotions']['promotionalOffers'][0]['promotionalOffers'][0]['startDate']
    event_start_YMD = to_kr(event_start)
    return event_start_YMD

def event_end():
    # 이벤트 종료 시간 반환
    event_end =  info['freeGames']['current'][0]['promotions']['promotionalOffers'][0]['promotionalOffers'][0]['endDate']
    event_end_YMD = to_kr(event_end)
    return event_end_YMD


