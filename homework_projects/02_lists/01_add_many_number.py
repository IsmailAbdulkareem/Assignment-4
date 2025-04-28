def add_many_numbers(numbers) -> int:
    total: int = 0
    for number in numbers:
        total += number
    return total

def main():
    numbers: list[int] = [1, 2, 3, 4, 5, 6, 7]
    sum: int = add_many_numbers(numbers)
    print(sum)

if __name__ == '__main__':
    main()