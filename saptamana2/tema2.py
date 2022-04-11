def param_sum(*args):
    sum = 0

    for i in args:
        if type(i) is int:
            sum += i

    return sum


print(param_sum(2, 4, 'abc'))


def sum_to_n(n: int):
    sum = 0
    odd_numbers_sum = 0
    even_numebrs_sum = 0

    for i in range(n):
        if (i + 1) % 2 == 0:
            even_numebrs_sum += i + 1
        else:
            odd_numbers_sum += i + 1

        sum += i + 1

    return sum, even_numebrs_sum, odd_numbers_sum


print(sum_to_n(4))


def e_intreg(nr):
    try:
        val = int(nr)
        return True
    except ValueError:
        return False


def intreg():
    nr = input()

    if e_intreg(nr) is True:
        print(nr)
    else:
        return 0


if intreg() == 0:
    print("nu a fost introdus un numar")
