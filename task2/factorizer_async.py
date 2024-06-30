from datetime import datetime
from multiprocessing import cpu_count, Pool

numbers = [128, 255, 99999, 10651060]

def factorize(n):
        factors = []
        for i in range(1, n + 1):
            if n % i == 0:
                factors.append(i)
        return factors

def callback(result):
    print(f'Result list: {result}')   

if __name__ == '__main__':
    start_time = datetime.now()
    with Pool(cpu_count()) as p:
        p.map_async(
        factorize,
        numbers,
        callback=callback,  
        )

        p.close()
        p.join()
    
    print(f'Runtime of the program: {datetime.now()-start_time}')