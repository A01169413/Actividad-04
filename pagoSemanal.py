#encoding: UTF-8
# Armando Tapia Campos A01169413
# Pago de un trabajador 

# calcula el pago por las horas normales trabajadas en la semana
def calcularHorasNormales (horasNormales, pagoPorHora) :
    pagoNormal = (horasNormales*pagoPorHora)*7
    return pagoNormal

# calcula el pago por las horas extras trabajadas en la semana
def calcularHorasExtras (horasExtras, pagoPorHoraExtra):
    pagoExtra = (horasExtras*pagoPorHoraExtra)*7
    return pagoExtra
    
# calcula el pago total por las horas extras y normales trabajadas en la semana
def calcularPagoTotal(pagoExtra,pagoNormal):
    pagoTotal = pagoExtra+pagoNormal
    return pagoTotal
    
# pide los valores e imprime lo que se pide
def main():
    hn = float(input("cuanto te pagan por hora"))
    nn = float(input("cuantas horas normales trabajaste"))
    ne = float(input("cuantas horas extras trabajaste"))
    pphe = hn*.5
    
    calcularHorasNormales(hn,nn)
    calcularHorasExtras(ne,pphe)
    calcularPagoTotal(pagoNormal,pagoExtra)
    
    print("horas normales", nn)
    print("horas extra", ne)
    print("pago por hora: %i" %hn)
    print("pago semanal normal: $%i" %pagoNornal)
    print("pago semanal extra: $%i" %pagoExtra)
    print("pago semanal total: $%i" %pagoTotal) 
    
main()
    