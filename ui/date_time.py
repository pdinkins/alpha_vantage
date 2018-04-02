class DateTime:

    def dt(self):
        import datetime
        print(datetime.datetime.now().timestamp())

dt1 = DateTime()

t = []
t1 = []
a = []
b = []

def main():

    for i in range(0, 1):
        for i in range(0, 50):
            a = dt1.dt()
            t.append(a)
            b = dt1.dt()
            t1.append(b)
            t[i]
            t1[i]

main()
