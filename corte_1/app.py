def calcula ():
   print("Digite x:")
   x=int(input())
   print("Digite  y")
   y=int(input())
   suma(x,y)
   resta(x,y)

def suma(n1,n2):
   resultado = n1+n2
   print("suma", resultado)

def resta(n1,n2):
   resultado = n1-n2
   print("resta", resultado)

calcula ()