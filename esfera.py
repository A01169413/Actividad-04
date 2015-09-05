#encoding: UTF-8
# Armando Tapia Campos A01169413
# Esferas

# calcula el diametro 
def calcularDiametro(radio):
    diametro = radio*2
    print("su diametro es de: %.2f" %diametro)
    
# calcula el volumen
def calcularVolumen(radio):
    volumen = (4/3)*3.1416*(radio**3)
    print("su volumen es de: %.2f" %volumen)

# calcula el area
def calcularArea(radio):
    area = 4*3.1416*(radio**2)
    print("su area es de: %.2f" %area)
    
# pide el radio de la esfera e imprime
def main():
    r = float(input("cual es el radio de la esfera"))
    calcularDiametro(r)
    calcularVolumen(r)
    calcularArea(r)
    print("es una esfera de radio:", r)
    
    
main()