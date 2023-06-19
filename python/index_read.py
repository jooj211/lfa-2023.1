from AFD import AFD
import time

afd = AFD()

means = []

for i in range(15):
    print("Iteracao: {}".format(i + 1))
    start = time.time()

    for i in range(100000):
        afd.from_xml("hello.xml")

    end = time.time()
    timer = end - start
    means.append(timer)


print("Tempos decorrido: {}".format(means))