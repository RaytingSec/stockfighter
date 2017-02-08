import urllib.request
import urllib.parse
import json

# Static
key = "d80d3fa3997766b285d110375b3bc4cce095e31c"
url_base = "https://api.stockfighter.io/ob/api"
headers = {"X-Starfighter-Authorization": key}

# Variable
account = "EXB123456"
venue = "TESTEX"
stock = "FOOBAR"
price = 0
qty = 100
direction = "buy"  # buy, sell
orderType = "market"  # market, limit, fok, ioc.
values = {
    "account": account,
    "venue": venue,
    "stock": stock,
    "qty": qty,
    "direction": direction,
    "orderType": orderType
}

# Test by accessing API
response = urllib.request.urlopen(url_base + "/heartbeat")
if response.getcode() != 200:
    print("Something went horribly wrong!")


for x in range(0, qty/100):
    # make trade of 1000 qty

    # Stock order
    url = url_base + "/venues/" + venue + "/stocks/" + stock + "/orders"
    print(url)

    data = json.dumps(values).encode('utf-8')
    req = urllib.request.Request(url, data, headers)
    print(req)
    # Stock order
url = url_base + "/venues/" + venue + "/stocks/" + stock + "/orders"
print(url)

data = json.dumps(values).encode('utf-8')
req = urllib.request.Request(url, data, headers)
print(req)

response = urllib.request.urlopen(req)
print(response.getcode())
print(response.read())
if response.getcode() != 200:
    print("Something went horribly wrong!")


    response = urllib.request.urlopen(req)
    print(response.getcode())
    print(response.read())
    if response.getcode() != 200:
        print("Something went horribly wrong!")
