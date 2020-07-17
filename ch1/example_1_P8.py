def binary_search(list, item):
  low = 0
  high = len(list) - 1
  print('List Length: {}'.format(len(list)))
  while low <= high:
    # It is an assignment and function hence mid and guess have to be inside loop
    # as something is being calcuated
    mid = round((low + high) / 2)
    guess = list[mid]
    if guess == item:
      print('Jenga -- Low: {}, Mid: {}, High: {}'.format(low, mid, high))
      return True
    elif guess < item:
      low = mid + 1
      print('Too Low -- Low: {}, Mid: {}, High: {}'.format(low, mid, high))
      print('Low value changed to: ', low)
    elif guess > item:
      high = mid - 1
      print('Too High --Low: {}, Mid: {}, High: {}'.format(low, mid, high))
    else:
      low = mid + 1
  return None

my_list=[1,3,5,7,9]
   
binary_search(my_list, -1)