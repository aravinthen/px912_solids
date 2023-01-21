import sympy as sym
import numpy as np
import math
from sympy.matrices import Matrix, eye, zeros, ones, diag, MatMul

class Workshop3:
    def __init__(self, ):
        print("Grader Library Loaded!")
        self.q1a = False
        self.q1c = False

        self.q2a = False
        self.q2b = False
        self.q2c = False
        self.q2d = False
        
    def hint1a(self,):
        print("The shape functions are quadratics, and they are constrained by the fact that they must be")
        print("equal to one at one node and equal to zero at the others. Just take y = A*x*x + B*x + C and")
        print("apply these constraints to get the values of A, B, and C.")
        
    def check1a(self, y1, y2,y3):
        x = sym.symbols('x')        
        name = ["y1", "y2", "y3"]
        answer = [y1,y2,y3]
        solution = [0.5*x**2 - 0.5*x, 
                   1.0 - x**2, 
                   0.5*x**2 + 0.5*x]
        
        incorrect = []
        for i in range(3):
            if answer[i] != solution[i]:
                incorrect.append(name[i])
                
        if len(incorrect) == 0:
            print("\033[1;32m Correct!")
            self.q1a = True
        else:
            incorrect_str = ", ".join(incorrect)
            print(f"\033[0;31m Incorrect. Check your answers for: {incorrect_str}.")
            self.q1a = False

            
    def hint1b(self,):
        print("Plot sympy functions usng: plot1 = sym.plotting.plot(y_i, (x,min,max)") 
    
    def hint1c(self,):
        print("You need to integrate for this question. You can do that with sym.integrate(integrand, (x, 0, L)).")
    def check1c(self, k):
        A, E, L = sym.symbols('A E L')
        solution = Matrix([[0.333333333333333*A*E*L**3 - 0.5*A*E*L**2 + 0.25*A*E*L,
                            -0.666666666666667*A*E*L**3 + 0.5*A*E*L**2,
                            0.333333333333333*A*E*L**3 - 0.25*A*E*L],
                           [-0.666666666666667*A*E*L**3 + 0.5*A*E*L**2,
                            4*A*E*L**3/3,
                            -0.666666666666667*A*E*L**3 - 0.5*A*E*L**2],
                            [0.333333333333333*A*E*L**3 - 0.25*A*E*L,
                             -0.666666666666667*A*E*L**3 - 0.5*A*E*L**2,
                             0.333333333333333*A*E*L**3 + 0.5*A*E*L**2 + 0.25*A*E*L]])
        
        for a in sym.preorder_traversal(k):
            if isinstance(a, sym.Float):
                k = k.subs(a, round(a, 1))
        for a in sym.preorder_traversal(solution):
            if isinstance(a, sym.Float):
                solution = solution.subs(a, round(a, 1))
                
        if k == solution:
            print("\033[1;32m Correct!")
            self.q1c = True
        else:
            print(f"\033[0;31m Incorrect.")
            self.q1c = False


    
    # -----------------------------------------------------------------------
    # Problem 2
    def hint2a(self,):
        print("For the assembly function, consider using np.ix_(global_indices[i], global_indices[i])].")
        print("This function constructs a index mesh based sequences. It'll stop you from fiddling with indices!")
        
    def check2a(self, K_global):
        answer = [[ 200000.,       0., -200000.],
                  [      0.,   50000.,  -50000.], 
                  [-200000.,  -50000.,  250000.]]
        if np.array_equal(K_global, answer):
            print("\033[1;32m Correct!")
            self.q2a = True
        else:
            print(f"\033[0;31m Incorrect.")
            self.q2a = False


    def hint2b(self,):
        print("What portion of the matrix do you need? That is, what index of K_global corresponds to node where a force is acting?")
    def check2b(self, d_3):
        if d_3 == 4e-05:
            print("\033[1;32m Correct!")
            self.q2b = True
        else:
            print(f"\033[0;31m Incorrect.")
            self.q2b = False           
 

    def hint2c(self,):
        print("For this we have to multiply the portion of the global stiffness matrix that we need and the displacement vector that we have already found.") 
    def check2c(self, R_F):
        solution = [-8., -2.]
        if np.array_equal(solution, R_F):
            print("\033[1;32m Correct!")
            self.q2c = True
        else:
            print(f"\033[0;31m Incorrect.")
            self.q2c = False           

    def hint2d(self,):
        print("For this, you need to find the derivatives of the shape functions. You can use those to find the elemental strains. These, in turn, can be used to find the elemental stresses.") 
    def check2d(self, eps_1, eps_2, eps_3, sigma_1, sigma_2, sigma_3):
        name = ["eps_1",
                "eps_2",
                "eps_3",
                "sigma_1",
                "sigma_2",
                "sigma_3"]
        
        answer = [eps_1, eps_2, eps_3, sigma_1, sigma_2, sigma_3]
        solution = [0.0004, 0.0004, -0.0008, 4000000.0, 4000000.0, -4000000.0]
        incorrect = []
        
        for i in range(6):
            if answer[i] != solution[i]:
                incorrect.append(name[i])
                
        if len(incorrect) == 0:
            print("\033[1;32m Correct!")
            self.q2d = True
        else:
            incorrect_str = ", ".join(incorrect)
            print(f"\033[0;31m Incorrect. Check your answers for: {incorrect_str}.")
            self.q2d = False
            
            
    def results(self):
        performance = [self.q1a,
                       self.q1c,
                       self.q2a, 
                       self.q2b,
                       self.q2c,
                       self.q2d]
        
        names = ["Question 1a",
                 "Question 1c",
                 "Question 2a",
                 "Question 2b",
                 "Question 2c",
                 "Question 2d"]

        coupled = [(performance[i], names[i]) for i in range(6)]
        
        total_score = sum(performance)
        
        print(f"Your score for this assignment: {total_score}/6")
        if total_score == 6:
            print("Excellent work!")
        else:
            print("The following questions have yet to be answered correctly:")
            for i in coupled:
                if i[0] == False:
                    print(i[1])
            print("Please feel free to reach out if you need any help.")
