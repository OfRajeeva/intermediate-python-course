import random
def main():
  dice_rolls=2
  dice_sum = 0
  for i in range(0,dice_rolls):
    roll = random.randint(1,6)
    print('You rolled a ', roll)
    dice_sum+=roll
  print("You have rolled a total of", dice_sum)  
if __name__== "__main__":
    main()

