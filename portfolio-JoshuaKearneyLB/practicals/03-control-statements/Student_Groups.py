TotalStudents = int(input("How many students? "))
GroupSize = int(input("Required group size? "))

No_Of_Groups = TotalStudents // GroupSize
Students_Left = TotalStudents % GroupSize


if Students_Left == 1:
    print("There will be", No_Of_Groups, "groups with ", Students_Left, "student left over.")
else:
    print("There will be", No_Of_Groups, "groups with ", Students_Left, "students left over.")