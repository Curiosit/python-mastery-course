class MySpam:
        def __init__(self):
            self._spam = Spam()
        def a(self):
            print('MySpam.a')
            self._spam.a()
        def c(self):
            print('MySpam.c')
        def __getattr__(self, name):
            return getattr(self._spam, name)