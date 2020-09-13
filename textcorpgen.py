def generate_corpus(object):
  """
    params:
      package: package_name for the query to get document from
      query: the user query attached to help with the function / class / attribute

    return:
      dictionary: a dictionary object to return a pair of key and values containing information about the package
  """

  keys = []
  values = []

  import numpy as np

  # each = str(object).__doc__
  each = eval("np.mean.__doc__")
  each = "\n\n".join([each.strip() for each in each.split("\n\n") if each])
  each = "\n".join([each.strip() for each in each.split("\n") if each])

  indexed_list = []
  for char in range(len(each)):
    updated_index = 0
    if (each[char] == "\n"):
      if (char + 1) == len(each):
        break
      if each[char + 1] == "-" or each[char + 1] == "=":
        if each[char + 2] == each[char + 1]:
          for index in range(char-1, 0, -1):
            if each[index] == "\n":
              updated_index = index+1
              indexed_list.append([char, updated_index])
              break
          # print(each[updated_index:char])
          keys.append(each[updated_index:char])
    if len(indexed_list) > 1:
      for i in range(len(indexed_list)):
        # print(each[indexed_list[i][0]:indexed_list[i+1][1]])
        values.append(each[indexed_list[i][0]:indexed_list[i+1][1]])
        if i != len(indexed_list)-1:
          indexed_list.remove([indexed_list[i][0], indexed_list[i][1]])
        break
  values.append(each[indexed_list[0][0]:])

  dictionary = {}
  for each in range(len(keys)):
    dictionary[keys[each]] = values[each]

  return dictionary

print(generate_corpus("numpy.mean"))

def wrapper_helper():
  """
    params: 
      package: a package name
  """
  import pydoc
  import inspect

  if inspect.isroutine(object):
    dictionary = generate_corpus(object)
  else:
    dictionary = pydoc.doc(object)
  if dictionary:
    for key, value in dictionary.items():
      print("{}: {}".format(key, value))

wrapper_helper()