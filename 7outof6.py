import random 
# import this to use the random feature
my_set = [ [] for i in range(7) ] 
# make 7 empty lists
no_of_rolls = 100 
# the larger the better, but no need to get too large (> 500)
list_id = 0
# this is used to identify to a list in my_set
for i in range(no_of_rolls)*7:
  roll_outcome = int(random.random()*6)
  my_set[list_id].append(roll_outcome)
  list_id += 1
  if list_id > 6:
    list_id = 0
winner = [sum(i) for i in my_set ]
print winner
print max(winner), ", random number:", winner.index(max(winner))+1
