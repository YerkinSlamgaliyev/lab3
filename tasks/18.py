def histogram(numbers):
    for num in numbers:
        print('*' * num)

user_input = input("Enter a list: ")
numbers = [int(num) for num in user_input.split()]

histogram(numbers)
