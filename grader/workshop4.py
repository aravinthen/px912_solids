import sympy as sym
import numpy as np
import math
from sympy.matrices import Matrix, eye, zeros, ones, diag, MatMul

class Workshop4:
    def __init__(self, ):
        print("Grader Library Loaded!")
        self.q1a = False
        self.q1b = False

        self.q2ai  = False
        self.q2aii = False
        self.q2aiii = False
        self.q2aiv = False
        
        self.q2biii = False
        self.q2biv = False
        
        self.q2ci = False
        self.q2cii = False
        self.q2ciii = False

    # Problem 2 ----------------------------------------------------------------------------------
    def hint1a(self,):
        print("How many Gauss points do you need in this case?")
        print("Weights are by far the most annoying thing about the Galerkin method.")
        print("Normally, these are coded within FEA software. For now, use the weight values")
        print("that you can find in the lecture notes.")
        
    def check1a(self, numerical, exact):
        if np.round(numerical, 5) == 1.73333:
            if str(exact) == "26/15":
                print("\033[1;32m Correct!")
                self.q1a = True
            else:
                print(f"\033[0;31m Incorrect. Check your exact calculation.")
                self.q1a = False
        else:
            print(f"\033[0;31m Incorrect. Check your numerical calculation.")
            self.q1a = False

    def hint1a(self,):
        print("The Jacobian is the tricky part about this question. Consider the range of the system.")           
    def check1b(self, numerical, exact):
        if np.round(numerical, 5) == 25.33333:
            if str(exact) == "76/3":
                print("\033[1;32m Correct!")
                self.q1b = True
            else:
                print(f"\033[0;31m Incorrect. Check your exact calculation.")
                self.q1b = False
        else:
            print(f"\033[0;31m Incorrect. Check your numerical calculation.")
            self.q1b = False
    
    # Problem 2 ----------------------------------------------------------------------------------
    def hint2ai(self,):
        print("Check the previous workshops! You've probably coded this already.")        

    def hint2aii(self,):
        print("If a displacement is fixed, it cannot move.")

    def hint2aiii(self,):
        print("You need to map the coordinates (-1,-1), (1,-1), (-1,1) and (1,1) to the coordinates of the shape on the diagram.")
            
    def hint2aiv(self,):        
        print("The expression for these are in the lecture notes.")

    def hint2bi(self,):
        print("1. Specifiy the quadrilateral in natural coordinates.")
        print("2. Write the derivatives of the shape functions in terms of eta and xi.")
        print("   This is expression 2.50 in the notes.")
        print("3. Calculate the element Jacobian matrix. You'll need np.dot() and np.linalg.det.")
        print("4. The final matrix should have dimensions (3x8). Check against the notes!")
        
    def hint2bii(self,):
        print("This relies very heavily on the answer you got for functions xf() and yf().")
        
    def hint2biii(self,):
        print("Steps:")
        print("1. Build a boundary conditions vector, BC. You only need this to modify the")
        print("   elemental stiffness matrix.")
        print("2. Be sure to set the fixed nodes to zero.")
        print("3. Obtain the indices of the non-zero nodes.")
        print("4. Build the elemental stiffness matrix: easy because there's only one.")
        print("   Remember, you only need the component of ke that isn't fixed.")
        print("   Keep in mind that this is an integration. You will have to implement")
        print("   Gauss quadrature in order to carry this out.")        

    def hint2biv(self, ):
        print("Which nodes actually have a force acting on them? Your answer should be multiplicable with the expression for the elemental stiffness matrix.")        
    
    def hint2ci(self,):
        print("Use np.linalg.solve to solve a linear system.")
        print("Your solution should be a vector of 4 values. Remember to add the displacements")
        print("for nodes that were fixed! (basically, add a bunch of zeros).")            

    def hint2cii(self,):
        print("All required components are present. Use a for-loop to calculate each strain.")
    
    def hint2ciii(self,):
        print("Remember to use the Jacobian when summing the stresses!")

            
    def results(self):
        performance = [self.q1a,
                       self.q1b,
                       self.q2ai,
                       self.q2aii,
                       self.q2aiii,
                       self.q2aiv,
                       self.q2biii,
                       self.q2biv,
                       self.q2ci,
                       self.q2cii,
                       self.q2ciii]
        
        names = ["Question 1a",
                 "Question 1b"]

        coupled = [(performance[i], names[i]) for i in range(len(performance))]
        
        total_score = sum(performance)
        
        print(f"Your score for this assignment: {total_score}/{len(performance)}")
        if total_score == len(performance):
            print("Excellent work!")
        else:
            print("The following questions have yet to be answered correctly:")
            for i in coupled:
                if i[0] == False:
                    print(i[1])
            print("Please feel free to reach out if you need any help.")
