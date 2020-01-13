# Brandon Morris    Lab 1B     1/6/2020

#Variable dictionary
#Variable dictionary
#capacity = max cap
#attending = people attending
#total_seats_avail = seats left
#total_seats_avail_diff = seats not available

answer = "y"

while answer == "Y" or answer == "y":
    capacity = int(input("What is the max capacity of the room? :")) #Room capacity
    attending = int(input("How many people want to attend the meeting? :")) #attending the meeting
    total_seats_avail = capacity - attending
    total_seats_avail_diff = total_seats_avail - capacity
    if attending <= capacity:
        print("The conference can be held.",total_seats_avail, "total seats available") #total seats available for a meeting that can take place.
        answer = input("Would you like to enter another room? (y/n) :")
    else:
        print("The conference can't be held.",total_seats_avail_diff, "total people cant attend")#total seats not available for a meeting that can't take place.
        answer = input("Would you like to enter another room? (y/n) :")
    while answer != "Y" and  answer != "y" and  answer != "N" and answer != "n":
        answer = input("Would you like to enter another room? (y/n) :")
print("End of Program.")
