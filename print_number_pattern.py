def print_without_new_line(string):
  print(string, end="")

def padding_length(row_number):
  return (row_number - 1)

def print_row_without_padding(max_number, row_number):
  start_number = row_number
  end_number = max_number

  for i in range(start_number, end_number):
    print_without_new_line(i)
    print_without_new_line(" ")

  print_without_new_line(end_number)

def print_row(max_number, row_number):
  padding = " " * padding_length(row_number)
  print_without_new_line(padding)
  print_row_without_padding(max_number, row_number)
  print_without_new_line(padding)

def print_number_pattern(max_number):
  for i in range(1, (max_number + 1)):
    print_row(max_number, i)
    print("")
  for i in range((max_number - 1), 0, -1):
    print_row(max_number, i)
    print("")

max_number = 4
print_number_pattern(max_number)