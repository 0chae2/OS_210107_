import urllib.request

def request(url):
    """지정한 url의 웹 문서를 요청하여, 본문을 반환한다."""
    response = urllib.request.urlopen(url)
    byte_data = response.read()
    text_data = byte_data.decode('utf-8')
    text_data_json = urllib.request.urlopen(url).read().decode('utf-8')
    return print(text_data, text_data_json)

request('https://python.bakyeono.net')