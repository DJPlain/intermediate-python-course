import random

def main():

  # These are the variables for the dice
  
  dice_rolls = int(input("How many dice? "))
  dice_size = int(input("How many sides are on the dice?"))

  # These are the variables for the totals of all the rolls
  
  dice_sum = 0
  critical_fail_count = 0
  critical_roll_count = 0

  for i in range(0,dice_rolls):  
    roll = random.randint(1,dice_size)
    dice_sum += roll
    
    if roll == 1:
      critical_fail_count += 1
      print(f"you rolled a {roll}! Critical Fail!")
    elif roll == dice_size:
      critical_roll_count += 1
      print(f"you got a critical {roll}!")
    else:
      print(f'You rolled a {roll}')

  # Results are displayed here
  
  print (f"\nyou rolled {dice_rolls} dice. Here are your results:")
  print (f"your total roll was {dice_sum}")
  print (f"You got {critical_fail_count} critical fails!")
  print (f"you got {critical_roll_count} critical hits!")

if __name__== "__main__":
  main()
