import socket

page = """HTTP/1.1 200 OK\r
Content-Type: text/html;charset=utf-8\r
\r
<button onclick="fetch('a')">a</button>
<button onclick="fetch('b')">b</button>
<button onclick="fetch('c')">c</button>
<button onclick="fetch('d')">d</button>
"""

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('0.0.0.0', 8002))
    s.listen(1)
    while True:
        conn, addr = s.accept()
        with conn:
            data = conn.recv(1024).decode("ascii")
            cmd = data[5:data.find("HTTP")-1]
            if cmd:
                print("%s is onclick."%cmd)
                # TODO
            conn.sendall(page.encode("utf8"))
            conn.close()

