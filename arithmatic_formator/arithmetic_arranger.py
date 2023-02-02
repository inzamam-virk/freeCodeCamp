def arithmetic_arranger(list, isTrue):
  if len(list) > 5:
    print("Error: Too many problems.")
    return
  elif isTrue:
    for i in list:
      list1 = i.split()
      operand1 = list1[0]
      operator = list1[1]
      
      operand2 = list1[2]
      if operand1.isdigit() == False:
        print("Error: Numbers must only contain digits.")
        return 
      if len(operand1) > 4 or len(operand2) > 4:
        print("Error: Numbers cannot be more than four digits.")
        return
      if operator != '+' and operator!='-':
        print(operator)
        print("Error: Operator must be '+' or '-'.")
        return
      # print(operand1)
      if (len(operand1) >= len(operand2)):
        print("  " + operand1, end="")
      else:
        lengthh = len(operand2) - len(operand1)
        print("  ", operand1.rjust(lengthh, " "), end="")
        # print("{:>lengthh}".format(operand1))
      print("    ", end="")
    print("")
    for i in list:
      list1 = i.split()
      operand1 = list1[0]
      operator = list1[1]
      operand2 = list1[2]
      # print(operand1)
      print(operator, end="")
      if (len(operand1) <= len(operand2)):
        print(" " + operand2, end="")
      else:
        lengthh = len(operand1) - len(operand2)
        print(" ", operand2.rjust(lengthh, " "), end="")
      print("    ", end="")
    print("")

    for i in list:
      list1 = i.split()
      operand1 = list1[0]
      operator = list1[1]
      operand2 = list1[2]
      maxLen = max(len(operand1), len(operand2)) + 2
      print(maxLen * "-", "   ", end="")
    print("")

    
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
        print("     " + str(result) , end="")
      elif int(maxLen)-2 == len(str(result)):
        print("    " + str(result) , end="")
      elif int(maxLen)-1 == len(str(result)):
        print("   " + str(result) , end="")
      if maxLen == len(str(result)):
        print("  " + str(result) , end="")
      elif int(maxLen)+1 == len(str(result)):
        print(" " + str(result) , end="")
      elif int(maxLen)+2 == len(str(result)):
        print(result , end="")
      print("    " , end="")
    print("")

