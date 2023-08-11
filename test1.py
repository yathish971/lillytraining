ip_address="192.168.{}.{}"

for i in range(2):
    for j in range(11):
        print(ip_address.format(i,j))