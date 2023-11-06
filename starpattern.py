def display_triangle_pattern(rows):
    for i in range(1, rows + 1):
        print(i,end=" ")
        for j in range(1, i + 1):
            print("*",end=" ")
        print()

# Example usage: Display a triangle pattern with 5 rows
display_triangle_pattern(5)

