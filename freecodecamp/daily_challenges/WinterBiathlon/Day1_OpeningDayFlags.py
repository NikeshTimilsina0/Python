"""Today marks the start of the 2026 Winter Games. The next 17 days will bring you coding challenges inspired by them.

For the first one, you are given a two-letter country code and need to return the flag emoji for that country."""
def get_flag(code):
    result=[]
    for c in code:
        unicod=chr(ord(c.upper()) + 127397)
        result.append(unicod)
    return ''.join(result)
