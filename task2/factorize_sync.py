from datetime import datetime

def factorize(*numbers):
    
    def get_factors(n):
        factors = []
        for i in range(1, n + 1):
            if n % i == 0:
                factors.append(i)
        return factors

    results = []
    for number in numbers:
        results.append(get_factors(number))
    
    return results

start_time = datetime.now()
print(factorize(128, 255, 99999, 10651060))
print(f'Runtime of the program: {datetime.now()-start_time}')
