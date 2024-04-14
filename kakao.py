import requests
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from urllib.parse import urlparse, parse_qs
from selenium.webdriver.common.keys import Keys
import time
import keyring

url = "https://kauth.kakao.com/oauth/token"
REST_API_KEY = keyring.get_password('KAKAOAPI', 'REDIRECT')
REDIRECT_URI = 'https://example.com/oauth'
authorization_url = f"https://kauth.kakao.com/oauth/authorize?response_type=code&client_id={REST_API_KEY}&redirect_uri={REDIRECT_URI}"

def token():
    driver = webdriver.Chrome()

    # 권한 부여 URL로 이동
    driver.get(authorization_url)
    time.sleep(5)  

    # 사용자 ID와 비밀번호 입력 필드 찾기
    username = driver.find_element(By.ID, 'loginId--1')  
    password = driver.find_element(By.ID, 'password--2')  

    # 보안 저장된 사용자 ID와 비밀번호 입력
    username.send_keys(keyring.get_password('KAKAO_ID', 'stanfm')) 
    password.send_keys(keyring.get_password('KAKAO_PW', 'stanfm')) 

    # 로그인 폼 제출
    password.send_keys(Keys.RETURN)  
    time.sleep(10)

    # 리디렉션 후 URL에서 코드 추출
    redirected_url = driver.current_url
    parsed_url = urlparse(redirected_url)
    CODE = parse_qs(parsed_url.query).get('code', [None])[0]

    # 토큰 요청 데이터 준비
    data = {
        'grant_type': 'authorization_code',
        'client_id': REST_API_KEY,
        'redirect_uri': REDIRECT_URI,
        'code': CODE
    }

    # 토큰 요청 및 응답 저장
    response = requests.post(url, data=data)
    tokens = response.json()

    # 토큰 파일 저장
    with open("token.json", "w") as kakao:
        json.dump(tokens, kakao)

def refresh():
    # 저장된 토큰 로드
    with open('token.json', 'r') as kakao:
        token = json.load(kakao)
    refresh_token = token['refresh_token']
    
    # 토큰 갱신 데이터 준비
    data={
        'grant_type': 'refresh_token',
        'client_id': REST_API_KEY,
        'refresh_token': refresh_token
    }
    response = requests.post(url, data=data)
    tokens = response.json()

    # 새 접근 토큰 저장
    with open("access_token.json", "w") as kakao:
        json.dump(tokens, kakao)

    # 리프레시 토큰 기한 마감이 한달 이내라면 파일 갱신
    if 'refresh_token' in tokens:
        with open("token.json", "w") as kakao:
            json.dump(tokens, kakao)


