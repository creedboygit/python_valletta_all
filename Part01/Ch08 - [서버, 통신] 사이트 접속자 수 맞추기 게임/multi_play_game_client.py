import socket

HOST = 'localhost'  # 접속 서버 주소
PORT = 50007  # 클라이언트 접속을 대기하는 포트 번호

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:  # 소켓 생성
    s.connect((HOST, PORT))  # 서버 연결

    while True:
        # 정답 입력
        n = input("예상 플레이어 숫자를 입력하세요(0은 게임 포기): ")

        # 입력값이 없을 경우
        if not n.strip():
            print('입력값이 잘못되었습니다.')
            continue

        # 서버 송신 (인코딩)
        s.sendall(n.encode('utf-8'))

        # 서버 응답 수신 (디코딩)
        data = s.recv(1024).decode('utf-8')

        # 서버 응답이 '정답'이거나 '종료'이면 게임 종료
        print(f'서버 응답:{data}')
        if data == "정답" or data == "종료":
            break
