class MyDict(dict):
    def get(self, key, default=0):
        return super().get(key, default)


a = MyDict()
a[1] = 2
a[3] = 4
print(type(a))
print(a)
print(a.get(1))
print(a.get(4))
