from kakao import token, refresh
from send import send
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.interval import IntervalTrigger

def app():
    try:
        refresh()  # 토큰을 새로고침을 시도합니다.
    except Exception as e:
        # 토큰 새로고침에 실패할 경우, 새로운 토큰을 받아 다시 새로고침을 시도합니다.
        print(f"오류 발생: {e}. 새 토큰을 가져와 다시 시도합니다.")
        token()
        refresh()
    finally:
        # 최종적으로 메시지를 보냅니다.
        send()

if __name__ == "__main__":
    scheduler = BlockingScheduler()

    # 스케줄 시작 날짜 설정 (하루 시간 버퍼)
    start_date = datetime(2024, 4, 13)

    # 매주 한 번씩 실행되는 트리거 설정
    trigger = IntervalTrigger(weeks=1, start_date=start_date)

    # 스케줄러에 작업 추가
    scheduler.add_job(app, trigger)

    # 앱이 언제부터 매 7일마다 실행되는지 출력
    print(f"앱이 {start_date.strftime('%Y-%m-%d')}부터 매 7일마다 실행됩니다.")

    try:
        # 스케줄러 시작
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        # 키보드 인터럽트나 시스템 종료 시 스케줄러를 종료합니다.
        scheduler.shutdown()
