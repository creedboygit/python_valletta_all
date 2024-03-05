# signal 적용
# CMD에서 실행 확인
# Ctrl + C를 입력할 경우, 키보드 인터럽트(SIGINT) 신호를 감지하고 handler 함수 실행

import signal
import time


def handler(signum, frame):  # signum : 발생한 신호의 숫자, frame : 프로그램 실행 스택 프레임
    print("Ctrl + C 신호를 수신했습니다.")


# 처리할 신호 유형, 실행할 함수
signal.signal(signal.SIGINT, handler)

while True:
    print("대기 중...")
    time.sleep(3)
