import threading, requests, time
"""
Thread 클래스에서 daemon 속성은 Sub thread가 daemon thread인지 아닌지를 지정.
daemon thread는 백그라운드에서 실행되는 thread로 Main thread가 종료되면 즉시 종료.
반면 deamon thread가 아닌 thread는 Main thread가 종료되더라도 자신의 작업이 끝날 때까지 계속 실행됨
"""
def getHtml(url):
    resp = requests.get(url)
    time.sleep(1)
    print(url, len(resp.text), ' chars')
t = threading.Thread(target=getHtml, args=('http://google.com',))
t.daemon = True
t.start()

print('### End ###')