def bubble_sort(numbers):
    length_numbers = len(numbers)
    for j in range(length_numbers - 1):
        for i in range(length_numbers - j - 1):
            if numbers[i] > numbers[i + 1]:
                numbers[i + 1], numbers[i] = numbers[i], numbers[i + 1]
    return numbers


def selection_sort(numbers):
    length_numbers = len(numbers)
    if length_numbers <= 1:
        return numbers

    for i in range(length_numbers):
        minimum = numbers[i]
        index = i
        for j in range(i, length_numbers):
            if numbers[j] < minimum:
                minimum = numbers[j]
                index = j

        numbers[i], numbers[index] = numbers[index], numbers[i]
    return numbers


def insertion_sort(numbers):
    if len(numbers) <= 1:
        return numbers

    sorted_numbers = numbers[:1]
    unsorted_numbers = numbers[1:]

    while unsorted_numbers:
        num = unsorted_numbers.pop(0)
        for index, el in enumerate(sorted_numbers):
            if num < el:
                sorted_numbers.insert(index, num)
                break
        else:
            sorted_numbers.append(num)

    return sorted_numbers
