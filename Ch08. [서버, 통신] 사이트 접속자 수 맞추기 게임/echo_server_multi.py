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
