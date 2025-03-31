# Single Non Linear Equation - Cubic
# Newton Raphson Method to find Roots
# Only One root will be found
# f(x) = -x3 + 3x2 + 4x -10


## Define the function and its derivative
def f(x):
    return -x**3 + 3*x**2 + 4*x - 10

def f_derivative(x):
    return -3*x**2 + 6*x + 4

## Define Newton Raphson Formula
def newton_raphson(x0, tolerance=1e-4, max_iterations=50):
    x_n = x0		##x_n is a variable and represents the current approximation for the root
    
    for i in range(max_iterations):
        f_xn= f(x_n)		##f(x_n) is a variable
        f_prime_xn = f_derivative(x_n)		##f_prime_xn is a variable
        
        
        #Avoid division by zero if derivative is zero
        #The loop should stop if the derivative is zero and code should terminate without crashing. Initial guess will need to be revised to get the roots
        
        if f_prime_xn ==0:
            print("Derivative is Zero. Iteration failed. Revise initial guess")
            return None
        
        #Compute next approximation
        x_next = x_n - f_xn/f_prime_xn
        
        #Check for convergence
        if abs(x_next - x_n) < tolerance:
            print(f"Converged to a root at x = {x_next}, after {i+1} iterations")
            return x_next
        
        x_n= x_next
        
    print("Newton Raphson Method did not converge within the maximum number of iterations. Revise the no. of maximum iterations or revise initial guess")
    return None

#Initial Guess
initial_guess = 3.5

#Call Newton Raphson function to solve the equation (find its roots)
root = newton_raphson(initial_guess)		##x0 will become initial_guess which is 1.5
if root is not None:
    print(f"Root found: {root}")
    
    

