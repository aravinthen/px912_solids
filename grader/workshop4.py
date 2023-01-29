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
    def check2ai(self, ps):
        answer = np.array([[32967032.96703297,  9890109.89010989,        0.        ],
                           [ 9890109.89010989, 32967032.96703297,        0.        ],
                           [       0.        ,        0.        , 11538461.53846154]])

        if np.allclose(np.round(ps,5), np.round(answer, 5)):
            print("\033[1;32m Correct!")
            self.q2ai = True
        else:
            print(f"\033[0;31m Incorrect.")
            self.q2ai = False           

    def hint2aii(self,):
        print("If a displacement is fixed, it cannot move.")
    def check2aii(self, fixed_disp):
        if set(fixed_disp) == set([0,1,2,3]):
            print("\033[1;32m Correct!")
            self.q2aii = True
        else:
            print(f"\033[0;31m Incorrect.")
            self.q2aii = False                       

    def hint2aiii(self,):
        print("You need to map the coordinates (-1,-1), (1,-1), (-1,1) and (1,1) to the coordinates of the shape on the diagram.")
    def check2aiii(self, funx, funy):
        points = [(1,-1), (-1,1),(-1,-1), (1,1)]
        solution = np.array([[2.0, 0.5], [0.0, 1.0], [0.0, 0.0], [2.0, 1.0]])
        answer = np.array([[funx(i[0], i[1]), funy(i[0], i[1])] for i in points])
        
        if np.array_equal(np.round(solution,5), np.round(answer, 5)):
            print("\033[1;32m Correct!")
            self.q2aiii = True
        else:
            print(f"\033[0;31m Incorrect.")
            self.q2aiii = False
            
    def hint2aiv(self,):        
        print("The expression for these are in the lecture notes.")
    def check2aiv(self, N):
        points = [(-1,1), (-1,-1), (1,-1), (1,1)]
        solution = np.array([[0., 0., 0., 1.],
                             [1., 0., 0., 0.],
                             [0., 1., 0., 0.],
                             [0., 0., 1., 0.]])

        answer = np.array([N(i[0], i[1]) for i in points])
        
        if np.allclose(np.round(solution,5), np.round(answer, 5)):
            print("\033[1;32m Correct!")
            self.q2aiv = True
        else:
            print(f"\033[0;31m Incorrect.")
            self.q2aiv = False

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
    def check2biii(self, ke):
        answer = np.array([[ 18058716.4314975,    1584953.50803043, -15205800.11704272, 5071851.22569738],
                             [  1584953.50803043,  44321396.05956174,   4120879.12087912, -43322875.34950256],
                             [-15205800.11704272,   4120879.12087912,  24715521.1652253,  -10777683.85460693],
                             [  5071851.22569738, -43322875.34950256, -10777683.85460693,   46651277.71636646]])
        
        if np.allclose(np.round(ke,5), np.round(answer, 5)):
            print("\033[1;32m Correct!")
            self.q2biii = True
        else:
            print(f"\033[0;31m Incorrect.")
            self.q2biii = False           

    def hint2biv(self, ):
        print("Which nodes actually have a force acting on them? Your answer should be multiplicable with the expression for the elemental stiffness matrix.")
        
    def check2biv(self, f_e):
        answer = np.array([0, 0, 0, -20])
        if np.array_equal(np.round(f_e,5), np.round(answer, 5)):
            print("\033[1;32m Correct!")
            self.q2biv = True
        else:
            print(f"\033[0;31m Incorrect.")
            self.q2biv = False           
    
    def hint2ci(self,):
        print("Use np.linalg.solve to solve a linear system.")
        print("Your solution should be a vector of 4 values. Remember to add the displacements")
        print("for nodes that were fixed! (basically, add a bunch of zeros).")
    def check2ci(self, d_e):
        answer = [ 0.00000000e+00,
                   0.00000000e+00,
                   0.00000000e+00,
                   0.00000000e+00,                   
                   3.22667984e-06,
                   -1.11131358e-05,
                   -1.11446419e-06,
                   -1.13572362e-05]

        if np.allclose(np.round(d_e,15), np.round(answer, 15)):
            print("\033[1;32m Correct!")
            self.q2ci = True
        else:
            print(f"\033[0;31m Incorrect.")
            self.q2ci = False
            

    def hint2cii(self,):
        print("All required components are present. Use a for-loop to calculate each strain.")
    def check2cii(self,strains):
        answer = np.array([[-3.00787629e-07,  5.76789847e-08, -4.63842049e-06],
                          [ 1.10045099e-06,  5.76789847e-08, -4.55962954e-06],
                          [8.55994221e-07, 3.17860083e-07, 5.37521788e-08],
                          [-1.21311271e-06,  3.17860083e-07, -6.25926864e-08]])
        
        if np.allclose(np.round(strains,5), np.round(answer, 5)):
            print("\033[1;32m Correct!")
            self.q2cii = True
        else:
            print(f"\033[0;31m Incorrect.")
            self.q2cii = False        
    
    def hint2ciii(self,):
        print("Remember to use the Jacobian when summing the stresses!")
    def check2ciii(self, sum_stress):
        answer = [5.68434189e-14,
                  8.44962902e+00,
                  -4.00000000e+01]
        
        if np.allclose(np.round(answer,15), np.round(sum_stress, 15)):
            print("\033[1;32m Correct!")
            self.q2ciii = True
        else:
            print(f"\033[0;31m Incorrect.")
            self.q2ciii = False        

            
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
                 "Question 1b",
                 "Question 2a,i",
                 "Question 2a,ii",
                 "Question 2a,iii",
                 "Question 2a,iv",
                 "Question 2b,iii",
                 "Question 2b,iv",
                 "Question 2c,i",
                 "Question 2c,ii",
                 "Question 2c,iii"]

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

