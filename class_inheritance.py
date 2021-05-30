# -*- coding: utf-8 -*-
"""
Created on Sun May 30 13:18:57 2021

@author: Wazir
"""

class X:
    def __init__(self,name):
        self.name = name
        print("The name of the object is : {}".format(self.name))
                
    def execute(self,d):
        print("The arguments passed in this function call is : {}".format(d))
        print("The name of the object is : {}".format(self.name))
                
    def shutdown(self):
        print("The name of the object is : {}".format(self.name))
        

# Defining the subclass A which inherits X
class A(X):
    def __init__(self,name):
        X.__init__(self,name)
        print("This is class {}".format(__class__))
                
    def execute(self,d):
        X.execute(self,d)
        print("This is class {}".format(__class__))
        
    def shutdown(self):
        X.shutdown(self)
        print("This is class {}".format(__class__))

# Defining the subclass B which inherits X      
class B(X):
    def __init__(self,name):
        X.__init__(self,name)
        print("This is class {}".format(__class__))
                
    def execute(self,d):
        X.execute(self,d)
        print("This is class {}".format(__class__))
        
    def shutdown(self):
        X.shutdown(self)
        print("This is class {}".format(__class__))
        
# Defining the subclass C which inherits X
class C(X):
    def __init__(self,name):
        X.__init__(self,name)
        print("This is class {}".format(__class__))
                
    def execute(self,d):
        X.execute(self,d)
        print("This is class {}".format(__class__))
        
    def shutdown(self):
        X.shutdown(self)
        print("This is class {}".format(__class__))
        
# Defining the main function
def main():
    while(True):
        ch = input("Please enter the class of your choice from A,B or C or enter quit if you want to exit : \n")
        name = input("Please enter the name of the object : \n")
        op = input("Please specify whether you want to create or delete an instance of the class by c for create and d for deleting: \n")
        ex_ch = input("Please specify whether you want to run the execute method of the object by pressing 'Y' for yes and 'N' for no: \n")
        count_A = 0
        count_B = 0
        count_C = 0
        countA_ex = 0
        countB_ex = 0
        countC_ex = 0
        
        if ch == "A":
            if op == "c":
                obj_A = A(name)
                d = {"a":1,"b":2,"c":3}
                count_A+=1
                if ex_ch == "Y":
                    obj_A.execute(d)
                    countA_ex += 1
            elif op == "d":
                del obj_A.name
        elif ch == "B":
            if op == "c":
                obj_B = B(name)
                d = {"d":4,"e":5,"f":6}
                count_B+=1
                if ex_ch == "Y":
                    obj_B.execute(d)
                    countB_ex += 1
            elif op == "d":
                del obj_B.name
        elif ch == "C":
            if op == "c":
                obj_B = B(name)
                d = {"d":4,"e":5,"f":6}
                count_B+=1
                if ex_ch == "Y":
                    obj_B.execute(d)
                    countB_ex += 1
            elif op == "d":
                del obj_B.name
        elif ch == "quit":
            break
        else:
            print("Enter a valid choice")
            continue
            
    print("The number of times class A, B and C are invoked are {},{} and {}".format(count_A,count_B,count_C))
    print("The number of times execute method of class A, B and C are invoked are {},{} and {}".format(countA_ex,countB_ex,countC_ex))

main()   