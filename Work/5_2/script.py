def parse_line(string):
    val, name = string.split('=')
    if (val and name):
        return {name, val}
    else:
        pass


name, val = parse_line('email=guido@python.org')