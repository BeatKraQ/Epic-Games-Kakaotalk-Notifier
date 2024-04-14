import requests
import json
from template import template

def send():
    # 'access_token.json' 파일에서 액세스 토큰을 로드합니다.
    with open("access_token.json", "r") as kakao:
        tokens = json.load(kakao)
    ACCESS_TOKEN = tokens['access_token']
    
    # 요청 헤더를 설정합니다.
    headers = {
        'Authorization': f'Bearer {ACCESS_TOKEN}',  # Bearer 토큰으로 인증
        'Content-Type': 'application/x-www-form-urlencoded'  # 컨텐츠 유형 설정
    }

    # 데이터에 템플릿 객체를 포함시킵니다.
    data = {
        'template_object': template()  # template 함수에서 반환된 템플릿 사용
    }

    # 카카오 API에 POST 요청을 보냅니다.
    response = requests.post("https://kapi.kakao.com/v2/api/talk/memo/default/send", headers=headers, data=data)

    # 응답 상태 코드에 따라 결과를 출력합니다.
    if response.status_code == 200:
        print("메시지가 성공적으로 발송되었습니다!")
    else:
        print("메시지 발송에 실패했습니다.")
        print("상태 코드:", response.status_code)
        print("응답:", response.text)