import numpy as np
import math
epsilon=1.449e-4
#print("epsilon is: ",epsilon)
iteration11=1
iteration21=1
iteration31=1
iteration12=1
iteration22=1
iteration32=1
k=1
e1=0.5/(k**0.5)
e2=0.5/k
e3=0.5/(k**2)
#while e1> epsilon:
#    e1=0.5/(iteration11**0.5)
#    iteration11+=1
#print("no of iterations required for below epsilon for e1: ",iteration11)  

#while e2> epsilon:
#    e2=0.5/iteration21
#    iteration21+=1
#print("No of iterations required for below epsilon for e2: ",iteration21)

#while e3> epsilon:
#    e3=0.5/(iteration31**2)
#    iteration31+=1
#print("No of iterations required for below epsilon for e3: ",iteration31)  
  
#print("0.1*epsilon is: ",0.1*epsilon)  
 
#while e1> (0.1* epsilon):
#    e1=0.5/(iteration12**0.5)
#    iteration12+=10
#print("no.of iteration required for below 0.1*epsilon for e1: ",iteration12) 

#while e2>(0.1*epsilon):
#    e2=0.5/iteration22
#    iteration22+=1
#print("No. of iteration required for below 0.1*epsilon for e2: ",iteration22)

#while e3>(0.1*epsilon):
#   e3=0.5/(iteration32**2)
#   iteration32+=1
#print("No. of iteration required for below 0.1*epsilon for e3: ",iteration32)

#print("0.01*epsilon is: ",0.01*epsilon)

#iteration13=1
#while e1> (0.01*epsilon):
#    e1=0.5/(iteration13**0.5)
#    iteration13+=100
#print("No. of iteration required for below 0.01*epsilon for e1: ",iteration13)    

#iteration23=1
#while e2>(0.01*epsilon):
#    e2=0.5/iteration23
#    iteration23+=1
#print("No. of iteration required for below 0.01*epsilon for e2: ",iteration23) 
   
#iteration33=1
#while e3>(0.01*epsilon):
#    e3=0.5/(iteration33**2)
#    iteration33+=1
#print("No. of iteration required for below 0.01*epsilon for e3: ",iteration33)    

#print("0.0001*epsilon is: ",0.0001*epsilon)

#iteration14=1
#while e1>(0.0001*epsilon):
#    e1=0.5/(iteration14**0.5)
#    iteration14+=10**6              # it does not give result,taking too long
#print("No.of iterations required for below 0.0001*epsilon for e1: ",iteration14)    

#iteration24=1
#while e2>(0.0001*epsilon):
#    e2=0.5/iteration24
#    iteration24+=1
#print("No. of iteration required for below 0.0001*epsilon for e2: ",iteration24)

#iteration34=1
#while e3>(0.0001*epsilon):
#    e3=0.5/(iteration34**2)
#    iteration34+=1
#print("No. of iteration required for below 0.0001*epsilon for e3: ",iteration34)

e4=[]
e4.append(0.5) 
#iteration41=0  
#while e4[iteration41] > epsilon:
#    e4.append(.975*e4[iteration41])
#    iteration41+=1
#print("No of iterations required for below epsilon for e4: ",iteration41) 

#iteration42=0
#while e4[iteration42]>(0.1*epsilon):
#    e4.append(0.975*e4[iteration42])
#    iteration42+=1
#print("No. of iterations required for below 0.1*epsilon for e4: ",iteration42)    

#iteration43=0
#while e4[iteration43]>(0.01*epsilon):
#    e4.append(0.975*e4[iteration43])
#    iteration43+=1
#print("No. of iterations required for below 0.01*epsilon for e4: ",iteration43)

#iteration44=0
#while e4[iteration44]>(0.0001*epsilon):
#    e4.append(0.975*e4[iteration44])
#    iteration44+=1
#print("No. of iterations required for below 0.0001*epsilon for e4: ",iteration44)

e5=[]
e5.append(0.5)
#iteration51=0
#while e5[iteration51] > epsilon:
#    e5.append(1.9*(e5[iteration51]**2))
#    iteration51+=1
#print("No. of iterations required for below epsilon for e5: ",iteration51)

#iteration52=0
#while e5[iteration52] >(0.1*epsilon):
#    e5.append(1.9*(e5[iteration52]**2))
#    iteration52+=1
#print("No. of iterations required for below 0.1*epsilon for e5: ",iteration52)

#iteration53=0
#while e5[iteration53] > (0.01*epsilon):
#    e5.append(1.9*(e5[iteration53]**2))
#    iteration53+=1
#print("No. of iterations required for below 0.01*epsilon for e5: ",iteration53)

iteration54=0
while e5[iteration54] > (.0001*epsilon):
    e5.append(1.9*(e5[iteration54]**2))
    iteration54+=1
print("No. of iterations required for below 0.0001* epsilon for e5: ",iteration54)    
    
    




   
    
    
     


   
    
    
    
    
    
    
