Sweet_number = int(input("Enter the total number of sweets you have:  "))
Pupils = int(input("Enter total number of pupils in the class: "))

Sweets_per_pupil = Sweet_number // Pupils
print(f"You should give each child {Sweets_per_pupil} sweet(s) with {Sweet_number % Pupils} left over.")