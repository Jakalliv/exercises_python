def square_root_bisection(number_to_square, tolerance=0.01, iterations=100):
    if number_to_square < 0:
        raise ValueError("Square root of negative number is not defined in real numbers")
    elif number_to_square == 0:
        print(f"The square root of {number_to_square} is {number_to_square}")
        return 0    
    elif number_to_square == 1:
        print(f"The square root of {number_to_square} is {number_to_square}")
        return 1
    else:
        if number_to_square > 1:
            start = 1
            end = number_to_square/2
        else:
            start = number_to_square/2
            end = 1
        counter = 0
        mid = 0
        while counter < iterations:
            mid = (start + end) /2
            if abs(start - end) < tolerance:
                print(f"The square root of {number_to_square} is approximately {mid}")
                return mid
            elif mid * mid < number_to_square:
                start = mid  
            else:
                end = mid    
            counter += 1
            print("..................\n", start, mid, end, counter,"Parametri:", number_to_square, tolerance, iterations )
        if abs(start - end) > tolerance:
            print(f"Failed to converge within {iterations} iterations")
            return None