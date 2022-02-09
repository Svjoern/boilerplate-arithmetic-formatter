def arithmetic_arranger(problems, show_answer=False):
  # problems_split = []
  spacing = get_spacing(problems)
  top     = ""
  mid     = ""
  line    = ""
  res     = ""

  for elem in problems:
    arry = split_elements(elem,show_answer,True)

    if len(arry[0]) >= len(arry[2]):
      length = len(arry[0]) + 2
    else:
      length = len(arry[2]) + 2
    # problems_split.append(arry)

  for i in range(length-arry[0]):
    pass

  if show_answer:
    return top + mid + line + res
  else:
    return top + mid + line

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
  if op == "-":
    return a-b

def get_spacing(problems):
  if len(problems) != 1:
    return "   "
  else:
    return ""
