def square_values(start, end):
    square_list = []
    even_square_list = []
    odd_square_list = []
    # Store square values in a list
    for num in range(start, end + 1):
        square_list.append(num ** 2)
    for square in square_list:
        if square % 2 == 0:
            even_square_list.append(square)
        else:
            odd_square_list.append(square)
    print("Square List:", square_list)
    print("Even Square List:", even_square_list)
    print("Odd Square List:", odd_square_list)
square_values(1, 10)