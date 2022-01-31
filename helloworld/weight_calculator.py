weight = input("weight: ")
specify_unit = str.lower(input("(L)bs or (K)g: "))

if specify_unit == "l":
    w_pounds = float(weight) * 0.45
    print(f'You are a {float(w_pounds)}: Kilos')

elif specify_unit == 'k':
    w_kilo = float(weight) * 2.20462
    print(f'You are a {float(w_kilo)}: Pounds')

else:
    print("you entered wrong Unit")