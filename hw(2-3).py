class Class:
    def __init__(self, text):
        self.data = text
        self.list = str(self).split()

        for i in range(len(self.list)):
            try:
                self.list[i] = float(self.list[i])
                if self.list[i] - int(self.list[i]) == 0:
                    self.list[i] = int(self.list[i])
            except:
                pass

    def __str__(self):
        return str(self.data)

    def __len__(self):
        return len(self.list)

    def __add__(self, x):
        return self.data + " " + str(x)

    def __radd__(self, x):
        return str(x) + " " + self.data

    def __iadd__(self, x):
        self.data += " " + x
        self.list += str(x).split()


obj = Class("some words here 102 1.231 0 -56 073abs")
print(obj)
print(obj.list)
print(len(obj))
print(obj+"string")
