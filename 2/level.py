""" Stockfighter lvl 02
"""

import sfapi
import json

account = "YAS950545"
venue = "RPGTEX"
stock = "BWM"
target_price = 2188

qty = 100000
block = 500
bought = 1500

while bought < qty:
    result = sfapi.stock_quote(venue=venue, stock=stock)
    # print(result.text)
    if result.ok:
        last = json.loads(result.text)["last"]
        if (last - target_price) < 0:
            result = sfapi.stock_order(stock, "buy", block, "limit", price=last, venue=venue, account=account)
            print(result)
            bought += block
            print("Bought @ {}, {}/{}".format(last, bought, qty))
        else:
            print("Last @ {} waiting for {}".format(last, target_price))

# print("Initial price: " + str(target_price))
# while bought < qty:
#     result = sfapi.stock_order(stock, "buy", block, "limit", price=target_price, venue=venue, account=account)
#     print(result)
#     order_id = json.loads(result.text)["id"]
#     price = json.loads(result.text)["price"]
#     unfilled = True
#     while unfilled:
#         status = sfapi.order_status(order_id)
#         print(status)
#         json.loads(status)["open"]
#     bought += block
#     print("Bought @ {}, {}/{}".format(price, bought, qty))

