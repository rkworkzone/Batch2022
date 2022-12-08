import multiprocessing
import time

result = []

def cal_squire(numbers):
    global result
    for n in numbers:
        time.sleep(5)
        print('squire ' + str(n * n ))
        result.append(n)

def cal_cube(numbers):
    global result
    for n in numbers:
        time.sleep(5)
        print('squire ' + str(n * n * n ))
        result.append(n)

if __name__ == "__main__":
    start = time.time()
    arr = [3, 4, 5,6 ,7,8 ,9, 20, 45, 23, 34,5 , 6,7 ,80]
    t1 = multiprocessing.Process(target=cal_squire, args=(arr,))
    t2 = multiprocessing.Process(target=cal_cube, args=(arr,))

    t1.start()
    t2.start()
    t1.join()
    t2.join()

    end = time.time()
    print(end- start)
    print(result)

# ps -aux | grep python