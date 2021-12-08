def checkPrime(n):
    ans = []
    [ans.append(i) for i in range(1, n+1) if n % i == 0]
    if len(ans) < 2 or len(ans) > 2:
        return False
    else:
        return True


num = int(input("Enter a number: "))
print(checkPrime(num))
