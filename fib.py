def recursive_fib(n: int) -> int:
    if n == 1 or n==2:
        return 1
    if n == 0:
        return 0
    return recursive_fib(n-1) + recursive_fib(n-2)


def linear_fib(n: int) -> int:
    if n == 0:
        return 0
    
    fn = 1
    f1 = 1
    f2 = 1
    for i in range(2, n):
        fn = f1 + f2
        f2 = f1
        f1 = fn

    return fn


def main() -> None:
    choice = int(input('Enter 1 for recursive.\nEnter 2 for linear.\n'))
    value = int(input('Enter N.\n'))

    if value < 0:
        print('Invalid value for N. N must be equal ou higher than 0.\n')

    if choice == 1:
        print(recursive_fib(value))
    elif choice == 2:
        print(linear_fib(value))



if __name__ == '__main__':
    main()