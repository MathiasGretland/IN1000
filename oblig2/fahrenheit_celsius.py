"""
Her er en kalkulator som ber brukeren om å skrive inn en grad i fahrenheit,
så regner den ut hvor mye grader det er i celsius.
"""

#Input som ber brukeren skrive en grad i fahrenheit
inp = input("Hvor mange grader er det ute i fahrenheit? ")
#Lagrer verdien til variabelen, float brukes for å få til desimaltall om det trengs
temperatur_i_fahrenheit = float(inp)

#Printer ut hvor mange grader i fahrenheit
print("Temperaturen i fahrenheit er: ", temperatur_i_fahrenheit)

#Variabelen regner ut hva graden i fahrenheit er i celsius
temperatur_i_celsius = ((temperatur_i_fahrenheit)-32)*5/9

#Printer ut hvor mange grader i celsius
print("Temperaturen i celsius er: ", temperatur_i_celsius)
