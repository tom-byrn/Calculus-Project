from flask import Flask, render_template, request, redirect, url_for
import matplotlib.pyplot as plt
import sympy as sp
import numpy as np
import re


app = Flask(__name__)

lb = 0
hb = 0
equation = " "
display_equation = " "
integral_equation = " "
differential_equation = " "
display_integral_equation = " "
display_differential_equation = " "
x_values = 0

#HOMEPAGE
@app.route("/")
def Homepage():
    return render_template("index.html")


#RECIEVE USER INPUT
@app.route("/", methods=["POST"])
def get_equation():
    global equation
    global display_equation
    if request.method == "POST" and request.json:
        plt.cla()
        equation = request.json.get("equation")

        display_equation = equation

        print(f"Equation {equation} obtained from JavaScript")
        print(f"Display Equation: {display_equation}")

        return redirect(url_for("define_graph"), code=307)

def checkInput():

    #DEFINE THE SET OF CHARACTERS ALLOWED
    allowed_characters = set("0123456789()*^-+.x/")
    return set(equation).issubset(allowed_characters)


def equationConversion():

    #equation  (3x+1)(x-2) -> Re equation -> (3*x+1)*(x-2)
    #Use (\d) to represent digits and r to represent raw string, 1 & 2 represent captured item one and captured item two
    global equation
    equation = re.sub(r'(\d)([x(])', r'\1*\2', equation)
    equation = re.sub(r'([x)])(\d)', r'\1*\2', equation)
    equation = re.sub(r'([x)])([(x])', r'\1*\2', equation)
    equation = re.sub(r'\^', r'**', equation)

    print(f"{equation}")
    return equation
        


@app.route("/graph", methods=["POST", "GET"])
def define_graph():

    #ENSURE equation USES VALID CHARACTERS
    if not checkInput():
        print("Invalid Input")
        return math_error

    global equation
    global integral_equation
    global differential_equation
    global x_values
    equationConversion()

        
    #TRANSLATE TO BE READABLE AND CREATE INTEGRAL & DIFFERENTIAL
    x = sp.symbols("x")

    equation_expression = sp.sympify(equation)

    #INTEGRAL
    integral_equation = sp.integrate(equation_expression, x)
    display_integral_equation = str(integral_equation)
    display_integral_equation = re.sub(r'\*\*', r'^', display_integral_equation)
    display_integral_equation = re.sub(r'\*', r'', display_integral_equation)
    
    #DIFFERENTIAL
    differential_equation = sp.diff(equation_expression, x) 
    display_differential_equation = str(differential_equation)
    display_differential_equation = re.sub(r'\*\*', r'^', display_differential_equation)
    display_differential_equation = re.sub(r'\*', r'', display_differential_equation)





    #CONVERT TO AN ACTUALLY USABLE FUNCTION
    equation_function = sp.lambdify(x, equation_expression)
    
    #CHECK IF LOWER & HIGHER BOUNDARIES HAVE BEEN DEFINED
    if request.method == "POST" and request.form:
        plt.cla()
        lb = int(request.form.get("lb"))
        hb = int(request.form.get("hb"))
        if hb == lb or hb < lb:
            return math_error()
        print(f"BOUNDARIES RECEIVED: lb={lb} and hb={hb}")
        print(f"Equation = {equation}")
        print(f"Display Equation = {display_equation}")

        area_under_curve = float(integral_equation.subs(x, hb)) - float(integral_equation.subs(x, lb))
        
        area_string = str(area_under_curve)
        if area_string.endswith(".0"):
            area_under_curve = int(area_under_curve)

        x_values = range(lb-10, hb+10)
        plt.xlim(lb, hb)
        print(f"x_values = {x_values}")

        #CREATE ARRAY OF Y VALUES
        y_values = [equation_function(x_val) for x_val in x_values]

        #PLOT THE GRAPH
        plt.plot(x_values, y_values, color='red')
        plt.title(f"f(x) = {display_equation}")
        plt.grid(True)
        if lb < hb:
            plt.fill_between(x_values, y_values, where=(np.array(x_values) >= lb) & (np.array(x_values) <= hb), color='blue', alpha=0.3)

        plt.savefig("static/image/graph.png")

        return render_template("graph.html", equation=equation, area_under_curve=area_under_curve, display_equation=display_equation, display_integral_equation=display_integral_equation, display_differential_equation=display_differential_equation)

        
    else:
        plt.cla()
        print(f"Boundaries not received, x_values = {x_values}")
        lb = 0
        hb = 0
        x_values = range(-21, 21)
        plt.xlim(-20, 20)

        area_under_curve = "Undefined"

        #CREATE ARRAY OF Y VALUES
        y_values = [equation_function(x_val) for x_val in x_values]

        #PLOT THE GRAPH
        plt.plot(x_values, y_values, color='red')
        plt.title(f"f(x) = {display_equation}")
        plt.grid(True)

        plt.savefig("static/image/graph.png")

        return render_template("graph.html", equation=equation, area_under_curve=area_under_curve, display_equation=display_equation, display_integral_equation=display_integral_equation, display_differential_equation=display_differential_equation)
    




def math_error():
    print("MATH ERROR")
    return redirect(url_for("math_error_page"), code=307) #TODO CHANGE TO MATH ERROR PAGE IF POSSIBLE

@app.route("/error")
def math_error_page():
    return render_template("error.html")


#FIXES RUNTIME ERROR
if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple('localhost', 5000, app)