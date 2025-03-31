# By Kratos, Mar2025
# Single Non Linear Equation - Cubic
# Newton Raphson Method to find Roots
# All Three roots will be found
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
        f_xn= f(x_n)		##f_xn is a variable. f(x_n) represents the value of the function f(x) at the point ( x_n ), where ( x_n ) is the current approximation of the root

        f_prime_xn = f_derivative(x_n)		##f_prime_xn is a variable
        
        
        #Avoid division by zero if derivative is zero
        #The loop should stop if the derivative is zero and code should terminate without crashing...
        #...Initial guess will need to be revised to get the roots
        
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


# Find all roots using multiple guesses
# Define Roots function for all the roots

def all_roots(guesses, tolerance=1e-4):
    roots = []  ##Empty list of roots []. When roots will be found, they will be stored here and displayed as the answer
    for guess in guesses:
        root = newton_raphson(guess) ##Calling Newton Raphson function
        if root is not None:
            #Round the root to avoid duplicates due to floating-point errors
            root = round(root,6)   ##This part of the code is working to ensure that the list  contains unique roots without duplicates,...
#... even when small floating-point precision errors might create near-identical values
            if root not in roots:	#Avoid duplicates
                roots.append(root)
    return roots
       
        
#Initial Guesses for all the Roots
initial_guesses = [-1, 1.5, 3, 3.5]  ##4 initial guesses have been listed which is one more than the maximum number of expected roots. This ensures that no root is accidentally missed because of the limitations of the initial guesses failing to converge

#Call all_roots function to find and print all roots
find_roots = all_roots(initial_guesses)
print("The roots of the equation are : ", find_roots)



