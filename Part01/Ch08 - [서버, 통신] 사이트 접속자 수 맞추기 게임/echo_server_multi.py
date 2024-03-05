# echo_server_multi.py
import socket

import select

# 접속할 서버 주소. 여기에서는 localhost를 사용
HOST = '127.0.0.1'

# 클라이언트 접속을 대기하는 포트 번호
PORT = 9999

# 소켓 객체를 생성
# 주소 체계(address family)로 IPv4, 소켓 타입으로 TCP를 사용
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 포트 사용 중이라 연결할 수 없다는 WinError 10048 에러 해결을 위해 필요
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# bind 함수는 소켓을 특정 네트워크 인터페이스와 포트번호에 연결하는데 사용
# HOST는 hostname, ip address, 빈 문자열 ""이 될 수 있음
# 빈 문자열이면 모든 네트워크 인터페이스로부터의 접속을 허용
# PORT는 1-65535 사이의 숫자를 사용할 수 있음
server_socket.bind((HOST, PORT))

# 서버가 클라이언트의 접속을 허용하도록 합니다.
server_socket.listen()
print('서버가 실행되었습니다.')

# select 함수에서 관찰될 소켓 리스트 생성
readsocks = [server_socket]

while True:
    # select 함수로 소켓들의 상태를 확인
    readables, writeables, exceptions = select.select(readsocks, [], [])

    for sock in readables:

        # 신규 클라이언트 접속
        if sock == server_socket:
            # accept 함수에서 대기하다가 클라이언트가 접속하면 새로운 소켓을 리턴
            client_socket, addr = server_socket.accept()

            # 접속한 클라이언트의 주소
            print('접속한 클라이언트의 주소입니다')
            print('Connected by', addr)

            # 소켓 리스트에 추가
            readsocks.append(client_socket)

        # 기존 클라이언트 응답
        else:
            # 무한루프를 돌면서
            while True:
                # 클라이언트가 보낸 메시지를 수신하기 위해 대기
                data = sock.recv(1024)

                # 빈 문자열을 수신하면 루프를 중지
                if not data:
                    print(sock.getpeername(), '접속 종료')

                    # 소켓을 닫음
                    sock.close()
                    readsocks.remove(sock)
                    break

                # 수신받은 문자열을 출력
                print('Received from', sock.getpeername(), data.decode())

                # 받은 문자열을 다시 클라이언트로 전송(에코)
                sock.sendall(data)

# 서버 종료
server_socket.close()
