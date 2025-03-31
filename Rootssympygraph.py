#Graph of function along with Real Roots Only

#Root Finding using Python "Sympy" - Algebraic Method for Exact solutions

#Single Non Linear Equation

#No need to take manual Derivative

#Cubic Function: f(x) = -x3 + 3x2 + 4x - 10
#Cubic Function: f(x) = 5x3 - 7x2 + 4x + 15

#All roots will be found
#All imaginary roots if they are mathematically zero will not be shown in the answer

from sympy import symbols, Eq, solve, N, lambdify
import numpy as np
import matplotlib.pyplot as plt

#Defing the variable and equation
x = symbols('x')
equation = -x**3 + 3*x**2 + 4*x - 10	##This is a Symbolic Equation....
###... It cannot be used for numerical evaluation purposes. To evaluate it numerically for various inputs of x to plot the graph in Python,...
###... this needs to beconverted to a Python Function

#Write a Variable to hold string representation of the symbolic equation so that it can be displayed in the graph
disp="-x^3 + 3*x^2 + 4*x - 10"  

#Solve the equation symbolically
roots = solve(Eq(equation,0),x)

#Display the roots numerically without imaginary components if they are miniscule

print("The roots of the equation are:")
real_roots = [] ##To store real roots only. Imaginary roots cannot be plotted on the graph so we need real roots. 
for root in roots:
    numeric_root = N(root)
    
    real_part,imaginary_part=numeric_root.as_real_imag()	##This will split real and imaginary parts of the roots
    
    if abs(imaginary_part)< 1e-12:  ##Check if the imaginary part is essentially zero
        real_roots.append(float(real_part)) ##This will add real roots to the list above
        print(real_part)   ##Print only the real part
        
    else:
       print(f"{real_part} + {imaginary_part}i") ##This will print both real and imaginary roots if imaginary roots are present
    
######Plot the function usig matplotlib
    
f=lambdify(x,equation, 'numpy')  ##lambdify will convert the Symbolic Equation into Python function so that it can be evaluated...
##... for numerical inputs for values of x in Python, so that the curve of the function can be drawn in graph

#Generate x values for plotting
x_values = np.linspace(-5,5,500)  #Adjust the range as needed. '-5' &'5' are the lower and upper bound limits of the graph for x-axis ...
##...and '500' is the no. of points (values of x) at which the function (or y value) will be calculated to draw a smooth curve

y_values = f(x_values) ##y axis lower and upper bound values will be whatever they are at x values, so no need to define the y-axis limits

#Create x values for plotting
plt.figure(figsize=(8,6))
plt.plot(x_values, y_values, label=f'f(x) = {disp}',color='blue')
plt.axhline(0, color='black', linestyle='--', linewidth=0.8) # x-axis
plt.axvline(0, color='black', linestyle='--', linewidth=0.8) # y-axis

#Highlight the roots on the graph
for real_root in real_roots: ##This will only show real roots
    plt.scatter(real_root,0,color='red', zorder=5, label=f'Root:{real_root:.3f}')
    
#Add labels and legend
plt.title(f"Graph of f(x) = {disp}")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(color='grey', linestyle='--', linewidth=0.5)
plt.show()


