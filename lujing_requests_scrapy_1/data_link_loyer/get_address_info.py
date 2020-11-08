import psutil

#AddressFamily.AF_LINK标识MAC地址信息
#AddressFamily.AF_INET标识IPV4地址信息
#AddressFamily.AF_INET_6标识IPV6地址信息
info = psutil.net_if_addrs()
print(info["WLAN"][0].address)