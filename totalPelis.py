#encoding: UTF-8
# Armando Tapia Campos A01169413
# calcular el total con funciones

# calcula el total a pagar por las peliculas
def calcularTotal (numeroEstrenos, numeroNormal):
    total = (numeroEstrenos*45) + (numeroNormal*27)    
    print("total a pagar $ %.2f" %(total))
    
# pide cuantas peliculas de cada cosa se rentaron e imprime los resultados
def main():
    a = int(input("cuantos estrenos compraste"))
    b = int(input("cuantas peliculas normales compraste"))
    calcularTotal(a,b)
    print("peliculas de estreno compradas:", a)
    print("peliculas normales compradas:", b)
    
    
main()        