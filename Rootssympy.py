#Root Finding using Python "Sympy" - Algebraic Method for Exact solutions

#Single Non Linear Equation

#No need to take manual Derivative

#Cubic Function: f(x) = 5x3 - 7x2 + 4x + 15

#All roots will be found
#All imaginary roots if they are mathematically zero will not be shown in the answer

from sympy import symbols, Eq, solve, N

#Defing the variable and equation
x = symbols('x')
equation = 5*x**3 - 7*x**2 + 4*x + 15

#Solve the equation symbolically
roots = solve(Eq(equation,0),x)

#Display the roots numerically without imaginary components if they are miniscule

print("The roots of the equation are:")
for root in roots:
    numeric_root = N(root)
    
    real_part,imaginary_part=numeric_root.as_real_imag()	##This will split real and imaginary parts of the roots
    
    if abs(imaginary_part)< 1e-12:  ##Check if the imaginary part is essentially zero
        print(real_part)   ##Print only the real part
        
    else:
       print(f"{real_part} + {imaginary_part}i") ##This will print both real and imaginary roots if imaginary roots are present
       
       ############################
       
