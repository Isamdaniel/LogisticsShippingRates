#Pido cosas primero
weight=float(input("Enter the package weight in kilograms: "))
rate=float(input("Enter the shipping rate per kilogram: "))
#Calculo cosas
shipping_cost=weight*rate
#Mostramos el resultado
print('The shipping_cost is:', shipping_cost)
