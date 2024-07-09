def exponentiate(num1, num2): 
    return num1**num2
    """Returns num1 to the power of num2"""

   
def raise_to_fourth_power(num1):
    return exponentiate(num1,4)
    """Returns num1 to the power of num2"""

square = lambda x: exponentiate(x,2)
"""Returns square"""

cube = lambda x: exponentiate(x,3)
"""Returns cube"""

print(square(2))
print(cube(2))
print(raise_to_fourth_power(2))

