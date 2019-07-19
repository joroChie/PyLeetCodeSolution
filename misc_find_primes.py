


def find_count_prime(num):
    primes = [2]

    if num <= 2:
        print("Total Count of Prime is 2")

    it = 3 #iterator

    while it <= num:
        prime_flag = True
        for prime in primes:
            if it % prime == 0:
                prime_flag = False
            
        if prime_flag:
            primes.append(it)
        
        it = it + 2

    print(primes)

    pass


if __name__ == "__main__":
    find_count_prime(100)






