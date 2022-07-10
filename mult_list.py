def list(lst):
 
  if sum(lst) == 0:
    return 0
  #product starts with first element of list
  prod = lst[0]

  #go through list elements and multiply them together
  if sum(lst) > 1:
    for i in lst[1:]:
      prod = prod * i

  return prod
    
print(list([3,2,4]))
print(list([]))
print(list([7]))