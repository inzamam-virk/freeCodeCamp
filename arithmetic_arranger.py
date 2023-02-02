# def arithmetic_arranger(problems):
def arithmetic_arranger(list , isTrue = False):
  # isTrue = True
  if len(list) > 5:
    return "Error: Too many problems."
  else:
    stringg = ""
    for i in list:
      list1 = i.split()
      operand1 = list1[0]
      operator = list1[1]
      operand2 = list1[2]
      if operand1.isdigit() == False or operand2.isdigit() == False:
        return "Error: Numbers must only contain digits."
      if len(operand1) > 4 or len(operand2) > 4:
        return "Error: Numbers cannot be more than four digits."
      if operator != '+' and operator!='-':
        print(operator)
        return "Error: Operator must be '+' or '-'."
      if (len(operand1) >= len(operand2)):
        stringg = stringg +"  " + operand1
      else:
        lengthh = len(operand2) - len(operand1)
        # print("Length --> " , lengthh)
        stringg = stringg + "   " + operand1.rjust(lengthh, " ")
      if i != list[-1]:
        stringg = stringg + "    "
    stringg = stringg + "\n"

    for i in list:
      list1 = i.split()
      operand1 = list1[0]
      operator = list1[1]
      operand2 = list1[2]
      # print(operand1)
      stringg = stringg + operator
      if (len(operand1) <= len(operand2)):
        stringg = stringg + " " + operand2
      else:
        lengthh = len(operand1) - len(operand2)
        stringg = stringg + "  "+ operand2.rjust(lengthh, " ")
      if i != list[-1]:
        stringg = stringg + "    "
    stringg = stringg + ("\n")

    for i in list:
      list1 = i.split()
      operand1 = list1[0]
      operand2 = list1[2]
      maxLen = max(len(operand1), len(operand2)) + 2
      stringg = stringg + maxLen * "-"
      if i != list[-1]:
        stringg = stringg + "    "

  if isTrue:
    stringg = stringg + "\n"
    for i in list:
      list1 = i.split()
      operand1 = list1[0]
      operator = list1[1]
      operand2 = list1[2]
      # print(operand1)
      if operator == '+':
        result = int(operand1) + int(operand2)
        # print(result)
      elif operator == '-':
        result = int(operand1) - int(operand2)
      maxLen = max(len(operand1) , len(operand2))
      if int(maxLen)-3 == len(str(result)):
        stringg = stringg + "     " + str(result)
      elif int(maxLen)-2 == len(str(result)):
        stringg = stringg + ("    " + str(result))
      elif int(maxLen)-1 == len(str(result)):
        stringg = stringg + ("   " + str(result))
      if maxLen == len(str(result)):
        stringg = stringg + ("  " + str(result))
      elif int(maxLen)+1 == len(str(result)):
        stringg= stringg + (" " + str(result))
      elif int(maxLen)+2 == len(str(result)):
        stringg = stringg + (result)
      if i != list[-1]:
        stringg = stringg + "    "
  return stringg
  
