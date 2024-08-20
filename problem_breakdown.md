# Problem Solving

 - What makes a prime number? --> Only being divisible by 1 and itself (2 factors)

 - How can I check if a number is a factor of another number? --> Using `%` (modulo)
```py
  4 % 2 == 0
  4 % 3 == 1
```

 - How can I use the above to check if a number is prime? --> Looping through lower numbers and checking if they are factors, up to half the original number
```py
num = 4
is_prime = True
for i in range(2, round((num + 1)/2)): # To go from 2 up to over half the passed number
    if num % i == 0:
        is_prime = False
```
This looks too complex, can we use a simpler loop? --> Yes!
```py
num = 7
is_prime = True
i = 2
while i <= num/2:
    if num % i == 0:
        is_prime = False
        break
    i += 1
```

 - How can I then apply this to find a list of all primes? --> introduce a second loop
```py
num = 10
primes = []
for i in range(1, num + 1): # to include 1 and num
    is_prime = True
    for j in range(2, num):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(i)    
```

 - Make it a function:
```py
def find_primes(num):
    primes = []
    for i in range(2, num + 1): # to start at 2 and include num
        is_prime = True
        for j in range(2, num):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)  
    return primes  
```