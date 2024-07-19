def recursive_prime(i: int, n: int, primes: list[int], marked: list[int]) -> list[int]:
    if i not in marked:
        primes.append(i)
        marked.append(i)

        for j in range(i, n+1, i):
            if j not in marked:
                marked.append(j)

    if i == n:
        return primes

    return recursive_prime(i+1, n, primes, marked)


def linear_prime(n: int) -> list[int]:
    primes = list()
    marked = list()

    for i in range(2, n+1):
        if i not in marked:
            primes.append(i)
            marked.append(i)

            for j in range(i, n+1, i):
                if j not in marked:
                    marked.append(j)

    return primes


def main() -> None:
    choice = int(input('Enter 1 for recursive.\nEnter 2 for linear.\n'))
    value = int(input('Enter N.\n'))

    if value < 1:
        print('Invalid value for N. N must be higher than 1.\n')

    if choice == 1:
        print(recursive_prime(2, value, [], []))
    elif choice == 2:
        print(linear_prime(value))



if __name__ == '__main__':
    main()