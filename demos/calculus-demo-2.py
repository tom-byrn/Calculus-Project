import matplotlib.pyplot as plt
import sympy as sp
import re

hb = 0
lb = 0

equation = 0



def preprocess_input(equation):
    # Replace any occurrences of Nx with N*x
    equation = re.sub(r'(\d+)([a-zA-Z])', r'\1*\2', equation)
    return equation


def define_graph():

    #DEFINE THE SET OF CHARACTERS ALLOWED
    allowed_characters = set("0123456789()*^-+.x ")
    preprocess_input(equation)
    if not set(equation).issubset(allowed_characters):
        return
        
    #TRANSLATE TO BE READABLE
    x = sp.symbols("x")

    equation_expression = sp.sympify(equation)



    #CONVERT TO AN ACTUALLY USABLE FUNCTION
    equation_function = sp.lambdify(x, equation_expression)
    
    #CHECK IF LOWER & HIGHER BOUNDARIES HAVE BEEN DEFINED
    global lb, hb
    if (lb == 0 and hb == 0):
        x_values = range(-10, 11)
    else:
        x_values = range((hb*2), (lb*2))
    
    y_values = [equation_function(x_val) for x_val in x_values]

    plt.plot(x_values, y_values)
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    plt.title(f"f(x) = {equation}")
    plt.grid(True)

    plt.show()
    return


equation = input("Equation: ")
preprocess_input(equation)
define_graph()
