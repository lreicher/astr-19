# Lucas Reicher Prompt #3 - Coding Journal #1

def main():
    # Uses formatted strings to output the required info (result & type)

    # Adds floats
    x = 1.342 # float
    y = 3.433 # float
    z = x + y # float
    float_sum_string = "Addition: {0} + {1} = {2} with type = {3}".format(str(x),str(y),str(z),str(type(z)))
    print(float_sum_string)

    # Subtracts integers
    x = 5 # int
    y = 2 # int
    z = x - y # int
    float_difference_string = "Subtraction: {0} - {1} = {2} with type = {3}".format(str(x),str(y),str(z),str(type(z)))
    print(float_difference_string)

    # Multiplies float and int
    x = 1.342 # float
    y = 3 # int
    z = x * y # float
    float_product_string = "Multiplication: {0} * {1} = {2} with type = {3}".format(str(x),str(y),str(z),str(type(z)))
    print(float_product_string)


if __name__ == "__main__":
    main()
