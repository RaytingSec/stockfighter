""" Test out Stockfighter API using as per official documentation
Note that stockfighter refers to stock exchanges venues, so exchanges will be refered to as such to comply with convention.
"""

import requests as req
import sfutils

api_key = sfutils.getApiKey()
api_base = "https://api.stockfighter.io/ob/api"


def api_heartbeat():
    """ Basic check of API status
    """
    r = req.get(api_base + "heartbeat")
    result = str(r.status_code) + "\n" + r.text
    if not r.ok:
        result = "Error!\n" + result
    return result


def venue_heartbeat(venue="TESTEX"):
    """ Heartbeat check for a specific venue
    """
    r = req.get("{}/venues/{}/heartbeat".format(api_base, venue))
    result = str(r.status_code) + "\n" + r.text
    if not r.ok:
        result = "Error!\n" + result
    return result


def venue_stocks(venue="TESTEX"):
    """ Retrieve listing of stocks on specific venue.
    """
    r = req.get("{}/venues/{}/stocks".format(api_base, venue))
    result = str(r.status_code) + "\n" + r.text
    if not r.ok:
        result = "Error!\n" + result
    return result


def stock_orderbook(venue="TESTEX", stock="FOOBAR"):
    """ Return orderbook on specific venue and stock
    """
    r = req.get("{}/venues/{}/stocks/{}".format(api_base, venue, stock))
    result = str(r.status_code) + "\n" + r.text
    if not r.ok:
        result = "Error!\n" + result
    return result


def stock_order(stock, direction, qty, orderType, price=0, account="EXB123456", venue="TESTEX"):
    """ Make a stock order
    """
    # Error handling
    validOrders = ("limit", "market", "fill-or-kill", "immediate-or-cancel")
    validDirections = ("buy", "sell")
    if orderType not in validOrders:
        print("Invalid order type")
        return
    elif direction not in validDirections:
        print("Invalid direction")
        return
    # Make the order
    order = {
        "stock": stock,
        "direction": direction,
        "qty": qty,
        "orderType": orderType,
        "price": price,
        "account": account,
        "venue": venue,
    }
    print(order)
    headers = sfutils.headers
    r = req.post(
        "{}/venues/{}/stocks/{}/orders".format(api_base, venue, stock),
        headers=headers,
        json=order
    )
    if not r.ok:
        return "Error!\n" + str(r.status_code) + r.text
    return r.text


def stock_quote(venue="TESTEX", stock="FOOBAR"):
    """ Get data on a stock
    """
    r = req.get("{}/venues/{}/stocks/{}/quote".format(api_base, venue, stock))
    result = str(r.status_code) + "\n" + r.text
    if not r.ok:
        result = "Error!\n" + result
    if not r.ok:
        return "Error!\n" + str(r.status_code) + r.text
    return r.text


def order_status(order_id, venue="TESTEX", stock="FOOBAR"):
    """ Status of an existing order
    """
    headers = sfutils.headers
    r = req.get(
        "{}/venues/{}/stocks/{}/orders/{}".format(api_base, venue, stock, order_id),
        headers=headers
    )
    if not r.ok:
        return "Error!\n" + str(r.status_code) + r.text
    return r.text


# result = stock_order("FOOBAR", "buy", 100, "market")
# print(result)
# result = stock_quote()
# print(result)
print(order_status(1142))
