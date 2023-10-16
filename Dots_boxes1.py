Your_name = input("What is your name: ")
max_possible_boxes = 49
print()

#Game 1
Opponent_name1 = input("What is your first opponent's name: ")
Your_boxes1 = int(input("How many boxes did you have for your first game: "))
Opponent_boxes1 = int(input("How many boxes did you opponent get for the first game: "))
Adding_Boxes1 = Your_boxes1 + Opponent_boxes1
percentage_created1 = (Adding_Boxes1 // max_possible_boxes) * 100
print()

#Game 2
Opponent_name2 = input("What is your second opponent's name: ")
Your_boxes2 = int(input("How many boxes did you have for your second game: "))
Opponent_boxes2 = int(input("How many boxes did you opponent get for the second game: "))
Adding_Boxes2 = Your_boxes2 + Opponent_boxes2
percentage_created2 = (Adding_Boxes2 // max_possible_boxes) * 100
print()

#Game 3
Opponent_name3 = input("What is your third opponent's name: ")
Your_boxes3 = int(input("How many boxes did you have for your third game: "))
Opponent_boxes3 = int(input("How many boxes did you opponent get for the third game: "))
Adding_boxes3 = Your_boxes3 + Opponent_boxes3
percentage_created3 = (Adding_boxes3 // max_possible_boxes) * 100
print()

#Game 4
Opponent_name4 = input("What is your fourth opponent's name: ")
Your_boxes4 = int(input("How many boxes did you have for your fourth game: "))
Opponent_boxes4 = int(input("How many boxes did you opponent get for the fourth game: "))
percentage_created4 = (Your_boxes4 + Opponent_boxes4 // max_possible_boxes) * 100
Adding_boxes4 = Your_boxes4 + Opponent_boxes4
percentage_created4 = (Adding_boxes4 // max_possible_boxes) * 100
print()

#Game 5
Opponent_name5 = input("What is your fifth opponent's name: ")
Your_boxes5 = int(input("How many boxes did you have for your fifth game: "))
Opponent_boxes5 = int(input("How many boxes did you opponent get for the fifth game: "))
percentage_created5 = (Your_boxes5 + Opponent_boxes5//max_possible_boxes) * 100
Adding5 = Your_boxes5 + Opponent_boxes5
percentage_created5 = (Adding5 // max_possible_boxes) * 100
print()


#Variables
Opponent_name = "Opponent's name"
Total_opponents_points = Opponent_boxes1 + Opponent_boxes2 + Opponent_boxes3 + Opponent_boxes4 + Opponent_boxes5
Your_points = "Your points"
Opponent_points = "Opponent's points"
your_max_points2 =  Your_boxes1 + Your_boxes2+ Your_boxes3 + Your_boxes4 + Your_boxes5
your_max_points3 = int(your_max_points2)
your_max_points1 = "Your max points"
percentage_print = "Box%"
Total_percentage = ((percentage_created1 + percentage_created2 + percentage_created3 + percentage_created4 + percentage_created5)//5)


#Other variables


#Printing
print(f"Players name: {Your_name}")
print(f"{Opponent_name:>20} {Your_points:>20}  {Opponent_points:>20}  {percentage_print:>20}")
print(f"=========================================================================================================")
print(f"{Opponent_name1:<20} {Your_boxes1:>20} {Opponent_boxes1:>20}  {percentage_created1:>20}")
print(f"{Opponent_name2:<20} {Your_boxes2:>20} {Opponent_boxes2:>20}  {percentage_created2:>20}")
print(f"{Opponent_name3:<20} {Your_boxes3:>20} {Opponent_boxes3:>20}  {percentage_created3:>20}")
print(f"{Opponent_name4:<20} {Your_boxes4:>20} {Opponent_boxes4:>20}  {percentage_created4:>20}")
print(f"{Opponent_name5:<20} {Your_boxes5:>20} {Opponent_boxes5:>20}  {percentage_created5:>20}")
print()

print(f"Summary:")
print(f"Your total points: {your_max_points3}")
print (f"Total opponent points: {Total_opponents_points}")
print(f"Percentage points received: {Total_percentage}")


