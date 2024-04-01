# Calculator
from art import logo

def add(n1,n2):
  """Adds two numbers"""
  return n1 + n2

def subtract(n1,n2):
  """Subtracts the second number from the first"""
  return n1 - n2

def multiply(n1,n2):
  """Multiplies two numbers"""
  return n1 * n2

def divide(n1,n2):
  """Divides the first number by the second"""
  return n1 / n2

operations = {
  "+" :add,
  "-" :subtract,
  "*" :multiply,
  "/" :divide,
}
cont = "y"
num = [0]
answer = []
x = 0

def operation_loop():
  print(logo)
  if num[x] == 0:
    num[x] = float(input("What's the first number?: "))
  else:
    num[x] = answer[x-1]
  """Prints operations, accepts next operation and second number, prints formula"""
  for i in operations:
    print(i)
  operation_symbol = input("Pick an operation from the lines above: ")
  num.insert(x+1,float(input("What's the next number?: ")))
  chosen_operation = operations[operation_symbol]
  answer.insert(x,float(chosen_operation(num[x],num[x+1])))
  print(f"{num[x]} {operation_symbol} {num[x+1]} = {answer[x]}")
  

while cont == "y":
  operation_loop()
  cont = input(f"Press 'y' to continue calculating with {answer[x]} or type 'n' to exit. ")
  x +=1  
