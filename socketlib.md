socket
- INET (IPv4)
smtplib : 메일 보낼 때 

selet : 하나의 프로세스로 여러 클라이언트와 통신하는 방법

1. 스트림(TCP)
- 양방향으로 바이트 스트림을 전송, 연결지향성
- 오류수정, 정송처리, 흐름제어 보장
- 송신된 순서에 따라 중복되지 않게 데이터를 수신 -> 오버헤드 발생
- 소량의 데이터 보단 대량 데이터 전송 적합

2. 데이터그램(UDP)
- 비연결형 소켓
- 데이터 크기제한
- 확실하게 전달이 보장되지 않음, 손실되어도 오류 발생되지 않음
- 실시간 멀티미디어 정보 처리를 위해 주로 사용 ex) 전화

#### HTTP통신과 SOCKET
- HTTP : 클라이언트 요청에만 응답 받음 서버가
- socket : 실시간 양방향성


물건 계산 프로그램?

[byte](https://dojang.io/mod/page/view.php?id=2462)

[python socket data recv](https://medium.com/@devfallingstar/python-python%EC%97%90%EC%84%9C-socket%EC%9C%BC%EB%A1%9C-%EB%8D%B0%EC%9D%B4%ED%84%B0%EB%A5%BC-%EC%A3%BC%EA%B3%A0-%EB%B0%9B%EC%9D%84-%EB%95%8C-%EA%B0%92%EC%9D%84-%EB%81%9D%EA%B9%8C%EC%A7%80-recv%ED%95%98%EC%A7%80-%EB%AA%BB%ED%95%98%EB%8A%94-%EB%AC%B8%EC%A0%9C-ed1830a0a4a6)

```python
def _get_bytes_stream(sock, length):
    buf = b''
    try:
        step = length
        while True:
            data = sock.recv(step)
            buf += data
            if len(buf) == length:
                break
            elif len(buf) < length:
                step = length - len(buf)
    except Exception as e:
        print(e)
    return buf[:length]
```