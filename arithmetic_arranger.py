def arithmetic_arranger(problems, show_answer=False):
  if len(problems) > 5:
    return "Error: Too many problems."

  # problems_split = []
  spacing = get_spacing(problems)
  top     = ""
  mid     = ""
  line    = ""
  res     = ""

  for elem in problems:
    test = elem.split(" ")
    if not test[0].isnumeric():
      return "Error: Numbers must only contain digits."
    if not test[2].isnumeric():
      return "Error: Numbers must only contain digits."
    if test[1] != "+" and test[1] != "-":
      return "Error: Operator must be '+' or '-'."
    if len(test[0]) > 4 or len(test[2]) > 4:
      return "Error: Numbers cannot be more than four digits."

    arry = split_elements(elem,show_answer)

    length = 0
    if len(arry[0]) >= len(arry[2]):
      length = len(arry[0]) + 2
    else:
      length = len(arry[2]) + 2
    # problems_split.append(arry)

    for i in range(length-len(arry[0])):
      top += " "
    top += arry[0]
    top += spacing

    mid += arry[1] + " "
    for i in range(length-2-len(arry[2])):
      mid += " "
    mid += arry[2]
    mid += spacing

    for i in range(length):
      line += "-"
    line += spacing

    if show_answer:
      for i in range(length-len(arry[3])):
        res += " "
      res += arry[3]
      res += spacing

  if show_answer:
      return top.rstrip() + "\n" + mid.rstrip() + "\n" + line.rstrip() + "\n" + res.rstrip()
  else:
      return top.rstrip() + "\n" + mid.rstrip() + "\n" + line.rstrip()

def split_elements(element, show_answer=False, PrintArr=False):
  arry = element.split(" ")
  if show_answer:
    arry.append(" " + str(get_result(arry)))
  if PrintArr:
      print(arry)
  return arry

def get_result(array):
  a = int(array[0]) 
  b = int(array[2])
  op = array[1]
  if op == "+":
    return a+b
  elif op == "-":
    return a-b

def get_spacing(problems):
  if len(problems) != 1:
    return "    "
  else:
    return ""
