def genRouterDetails():
    loopback_first = 1
    loopback_second = 1
    loopback_third = 1
    loopback_fourth = 1
    counter = 0
    data = {}
    while True:
        if loopback_fourth > 255:
            loopback_fourth = 0
            loopback_third += 1

        if loopback_third > 255:
            loopback_third = 0
            loopback_second += 1

        if loopback_second > 255:
            loopback_second = 0
            loopback_first += 1

        if loopback_first > 255:
            loopback_first = 1

        loopback = str(loopback_first) + '.' + str(loopback_second) + \
            '.' + str(loopback_third) + '.' + str(loopback_fourth)

        data = {
            'sapid': 'sap' + str(counter),
            'hostname': 'hostname' + str(counter),
            'loopback': loopback,
            'mac_addr': 'mac' + str(counter)}
        counter += 1
        loopback_fourth += 1
        yield data

n = int(input("Enter a number: "))
gen = genRouterDetails()

for i in range(n):
    print(next(gen))
