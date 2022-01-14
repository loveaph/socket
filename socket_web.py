import socket

page = """HTTP/1.1 200 OK\r
Content-Type: text/html;charset=utf-8\r\r
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Title</title>
    <style>
        .parent {
            display: grid;
            grid-template-columns: repeat(12, 1fr);
            grid-template-rows: repeat(7, 1fr);
            grid-column-gap: 0px;
            grid-row-gap: 0px;
        }

        .div1 {
            grid-area: 3 / 3 / 4 / 4;
        }

        .div2 {
            grid-area: 4 / 2 / 5 / 3;
        }

        .div3 {
            grid-area: 4 / 4 / 5 / 5;
        }

        .div4 {
            grid-area: 5 / 3 / 6 / 4;
        }

        .div5 {
            grid-area: 2 / 10 / 5 / 12;
        }

        .div6 {
            grid-area: 5 / 10 / 5 / 12;
        }

        button:first-child {
            width: 80px;
            height: 80px;
        }
    </style>
</head>
<div class="parent">
    <div class="div1"><button onclick="fetch('a')">a</button></div>
    <div class="div2"><button onclick="fetch('b')">b</button></div>
    <div class="div3"><button onclick="fetch('c')">c</button></div>
    <div class="div4"><button onclick="fetch('d')">d</button></div>
    <div class="div5"><button onclick="fetch('e')">e</button></div>
    <div class="div6"><button onclick="fetch('f')">f</button></div>
</div>
</html>
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

