# Introdução às Generator functions em Python
# generator = (n for n in range(1000000))

def generator(n=0, maximum=10):
    while True:
        yield n # pause | obs: toda função com yield e um genereator
        n += 1

        if n >= maximum:
            return

gen = generator(maximum=1000)
for n in gen:
    print(n)
#print(next(gen))
#print(next(gen))
#print(next(gen))