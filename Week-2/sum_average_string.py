def sum_and_average_of_digits(s1):
    total_sum = 0
    count = 0

    for char in s1:
        if char.isdigit():
            total_sum += int(char)
            count += 1

    if count > 0:
        average = total_sum / count 
    else:
        average = 0

    return total_sum, average

if __name__ == "__main__":
    s1 = input("Enter a string: ")
    total_sum, average = sum_and_average_of_digits(s1)
    print(f"Sum of digits: {total_sum}")
    print(f"Average of digits: {average}")

