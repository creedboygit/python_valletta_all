import socket
import select
import random

HOST = 'localhost'  # 접속 서버 주소
PORT = 50007  # 클라이언트 접속을 대기하는 포트 번호

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:  # 소켓 생성

    # 포트 사용 중이라 연결할 수 없다는 WinError 10048 에러 해결을 위해 필요
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    s.bind((HOST, PORT))  # 소켓과 포트 연결
    s.listen()  # 소켓 listening 시작
    print('서버가 시작되었습니다.')

    readsocks = [s]  # select 함수에서 관찰될 소켓 리스트 생성
    answers = {}  # 정답 딕셔너리 생성 (플레이어 별 정답 저장)
    num_clients = 0  # 현재 접속자 수

    while True:
        # select 함수로 소켓들의 상태를 확인
        readables, writeables, exceptions = select.select(readsocks, [], [])

        for sock in readables:
            if sock == s:  # 신규 클라이언트 접속
                newsock, addr = s.accept()
                num_clients += 1  # 접속자 수 증가

                print(f'클라이언트가 접속했습니다:{addr}, 정답은 {num_clients}입니다.')

                readsocks.append(newsock)

                answers[newsock] = num_clients  # 신규 클라이언트 정답 생성
                for key in answers.keys():  # 기존 클라이언트 정답 업데이트
                    answers[key] = num_clients

            else:  # 이미 접속한 클라이언트의 요청 (게임 진행을 위한 요청)
                conn = sock
                data = conn.recv(1024).decode('utf-8')
                print(f'데이터:{data}')

                try:  # 숫자를 입력하지 않았을 경우 응답 메시지
                    n = int(data)
                except ValueError:
                    conn.sendall(f'입력값이 올바르지 않습니다:{data}'.encode('utf-8'))
                    continue

                # 정답 가져오기
                answer = answers.get(conn)

                if n == 0:  # 클라이언트가 종료 0을 입력할 경우
                    conn.sendall(f"종료".encode('utf-8'))
                    conn.close()
                    num_clients -= 1  # 접속자 수 감소
                    print(f'클라이언트가 게임을 종료했습니다:{addr}, 정답은 {num_clients} 입니다.')

                    for key in answers.keys():  # 기존 클라이언트 정답 업데이트
                        answers[key] = num_clients
                    readsocks.remove(conn)  # 클라이언트 접속 해제 시 readsocks에서 제거

                # 클라이언트의 입력값 채점
                elif n > answer:
                    conn.sendall("너무 높아요.".encode('utf-8'))
                elif n < answer:
                    conn.sendall("너무 낮아요.".encode('utf-8'))
                else:
                    conn.sendall("정답입니다!".encode('utf-8'))
