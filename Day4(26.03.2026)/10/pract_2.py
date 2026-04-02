def factorial(n):
    if type(n) != int:
        return(-1)
    if n == 0 or n == 1:
        return(1)
    if n < 0:
        return (-1)
    a = 0
    b = 1
    while (a < n):
        a = a + 1
        b = b * a
    return b