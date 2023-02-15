import nmap


def hostScan(networkAdd, start, end, file):
    scan = nmap.PortScanner()

    for i in range(int(start), int(end) + 1):
        networkAdd = networkAdd.split('.')[0] + '.' + netAddress.split('.')[1] + '.' + netAddress.split('.')[
            2] + '.' + str(i)
        scan.scan(networkAdd, '1', '-v')
        stri = networkAdd + " is " + scan[networkAdd].state()
        print(stri)
        file.write(stri)
        file.write("\n")


if __name__ == '__main__':
    file0 = open("result_[host].txt", "w")  # over write module.
    netAddress = input('Enter network address:   ')
    start = input('Enter the starting number:   ')
    end = input('Enter the last number:   ')
    hostScan(netAddress, start, end,file0)
    file0.close()

