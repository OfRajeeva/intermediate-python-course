import random
def main():
  dice_rolls=int(input("How many dice would you like to roll?\n"))
  dice_size=int(input("How many sides are in your die?\n")) 
  dice_sum = 0
  for i in range(0,dice_rolls):
    roll = random.randint(1,dice_size)
    if roll==1:
      print('You rolled a', roll, 'Critical Fail!')
    elif roll==dice_size:
      print('You rolled a', roll, 'Critical Success!')
    else:
      print('You rolled a', roll)
    dice_sum+=roll
  print("You have rolled a total of", dice_sum)  
if __name__== "__main__":
    main()

