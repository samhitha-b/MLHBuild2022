# to reverse a string :weary:
yourString = input("Enter a string to be reversed: ")
output = ""

# i'll pretend like the reverse fuction doesnt exist :pensive:
for i in range(len(yourString), 0, -1):
    output = output + yourString[i-1]

print(output)
