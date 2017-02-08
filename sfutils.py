""" Common tools for stockfighter
"""


def getApiKey():
    """ Reads api key from a file
    """
    f = open("api_key", mode='r')
    contents = f.read().splitlines()
    return contents[0]

api_key = getApiKey()
headers = {"X-Starfighter-Authorization": api_key}
