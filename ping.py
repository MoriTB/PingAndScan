import os

import ping3


def pingDefault(file, specific, model):
    # change the ip list according to the question.
    ips = []
    if model == "1":
        for i in range(0, 7):
            for j in range(0, 256):
                ips.append('89.43.{}.{}'.format(i, j))
    elif model == "2":
        ips.append(specific)
    # ips1 = ['192.168.1.1', 'bing.com', 'google.com'] test box.
    defaultSent = 3
    timeout = 0.0001  # default timeout suggested.
    size = 56  # default use for ICMP suggested.

    for i in ips:

        rtt = []  # we use it for each packet to be added. ( round trip time )
        txt = ""
        result = []
        for j in range(0, defaultSent):
            try:
                result0 = ping3.ping(i, timeout=timeout, size=size)
                result.append(result0)
                real_size = size + 8
                if result[j] is not None:  # possibility to fail and give none.
                    print("================================")
                    print("pinging ", i, " ...")
                    result[j] = int(result[j] * 1000)  # to show the time in ms
                    str = f"{real_size} bytes from {i}: time={result[j]}ms"
                    txt = txt + str
                    # print(str)
                    rtt.append(result)  # later will be used for the packet that actually went through.
            except ping3.errors.Timeout as timeoutError:
                print("error", timeoutError)
        for chk in result:  # only for the same ping with packets we measure the details
            if chk is not None:
                total = defaultSent
                wentThrough = len(rtt)
                loss = total - wentThrough
                PackLoss = round((total - wentThrough) / total * 100, 2)
                txt = txt + "  "
                tmp = f"packets:> sent:{total}   received:{wentThrough}  lost:{loss}   {PackLoss}% packet loss  "
                #avg = (min(rtt)+ max(rtt)) // 2
                #tmp_2 = f"{min(rtt)}, {max(rtt)}, {avg}"
                #print("this",tmp_2)
                txt = txt + tmp
                file.write("\n================================================")
                file.write("\n")
                file.writelines(txt)
                print(txt)
                break


if __name__ == '__main__':
    specific_add = ""
    file0 = open("result_[ping].txt", "w")  # over write module.
    print("------------------------------")
    print(
        "default model checks between the range 89.43.00 till ...\n and specific model check the ip that has been given too.")
    print("------------------------------")
    check = input("what model you want to use? default = 1 , specific = 2\n")
    if check == "2":
        specific_add = input("enter the address :) \n")
    file0.write("result of pinging \n")
    pingDefault(file0, specific_add, check)
    file0.close()
