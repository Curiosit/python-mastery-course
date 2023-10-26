def consumer(func):
    def start(*args,**kwargs):
        cr = func(*args,**kwargs)
        cr.send(None)
        return cr
    return start

@consumer
def match(pattern):
    print('Looking for %s' % pattern)
    while True:
        line = yield
        if pattern in line:
            print(line)

match('a')


g = match('python')
g.send(None)          # Prime it (explained shortly)

g.send('Yeah, but no, but yeah, but no')
g.send('A series of tubes')