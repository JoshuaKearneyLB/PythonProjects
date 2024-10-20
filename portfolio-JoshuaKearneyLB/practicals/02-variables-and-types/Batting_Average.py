# batting average = no. of runs / (no. times batted - times not out)

Player_Name = input("Enter the players name: ")

Matches = input(f"Enter the number of matches {Player_Name} played: ")
Times_batted = int(input(f"Enter the number of times {Player_Name} batted: "))
not_out = int(input(f"Enter the number of times {Player_Name} was not out: "))
runs = int(input(f"Enter the total number of runs {Player_Name} completed: "))

Batting_Average = runs / (Times_batted - not_out)
print(f"{Player_Name}'s batting average is: ", round(Batting_Average))