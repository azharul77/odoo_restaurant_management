
def limit(str, size):
    if len(str) <= size:
        return str
    return str[0:str]