num1 = float(input("PRIMEIRO NUMERO: "))
oper = input("QUAL OPERAÇÃO?")
num2 = float(input("SEGUNDO NÚMERO: "))

calc = lambda firstN, operator, secondN: (
    num1 + num2 if oper == "+" else
    num1 - num2 if oper == "-" else
    num1 / num2 if oper == "/" else
    num1 * num2 if oper == "*" else 
    "Your result is: "
)
print(calc(num1,oper,num1))