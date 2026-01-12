def number_pattern(n):
    if isinstance(n, int) == False:
        return  "Argument must be an integer value."
    if n<1:
        return "Argument must be an integer greater than 0."
    temp_string=" "
    for i in range (1,n+1):
        temp_string+=(str(i)+" ")
        
    return (temp_string.rstrip()).lstrip()
