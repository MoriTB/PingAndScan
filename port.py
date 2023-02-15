import socket


def checkPort(host, port):
    s = socket.socket()
    s.settimeout(1)  # the default timeout setter.
    try:
        s.connect((host, port))
        return True
    except:
        return False


def checkPorts(ip, start, end, file):
    open_ports = []
    for p in range(start, end + 1):
        if checkPort(ip, p):  # we use the previous function
            tmp = f"ip:{ip},port:{p} is open."
            open_ports.append((ip, p))
            print(tmp)
            file.write(tmp)
            file.write("\n")


if __name__ == '__main__':
    file0 = open("result_[port].txt", "w")
    host = input(str("host address : "))
    host = socket.gethostbyname(host)
    start = input(str("Start of range: "))
    if start is '':
        start = 0
    end = input(str("End of range: "))
    print(checkPorts(host, int(start), int(end), file=file0))
    file0.close()
