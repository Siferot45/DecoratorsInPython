

def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        for x in range(2, int(result ** 0.5 )+1):

            if result % x == 0:
                print("Составное")
                break

        else:
            print("Простое")

        return result

    return wrapper


@is_prime
def sum_three(*nums):
    return sum(nums)


result = sum_three(2, 3, 6)
print(result)