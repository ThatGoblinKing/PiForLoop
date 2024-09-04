import math
import threading
from threading import Thread
def addNums(min: int, max: int, numbers: list[int], index) -> None:
    previousTerms = []
    for i in range(min + 1,max + 1):
        previousTerms.append(1/(i**2))
    numbers[index] = sum(previousTerms)
THREAD_COUNT = 10

n = 0
while not n >= 1:
    n = int(input("N: "))
result = [None] * THREAD_COUNT
threads = [None] * THREAD_COUNT 
for i in range(THREAD_COUNT):
    min = int(n * (i/THREAD_COUNT))
    max = int(n * ((i + 1)/THREAD_COUNT))
    threads[i] = Thread(target=addNums, args=(min, max, result, i))
    threads[i].start()

for i in range(len(threads)):
    threads[i].join()

print(math.sqrt(6 * sum(result)))
