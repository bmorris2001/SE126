# Brandon Morris    Lab 1C     1/6/2020

#Variable dictionary------------------------------------------------------------
#Variable dictionary
#capacity = max cap
#attending = people attending
#total_seats_avail = seats left
#total_seats_avail_diff = seats not available

#FUNCTIONS------------------------------------------------------------------------


def capacity(): #Asking the user for the max capacity
    room_max = int(input("What is the max capacity of the room? :"))
    return room_max

def attendees(): #asking the user how many people can attend the meeting
    attend_meet = int(input("How many people want to attend the meeting? :"))
    return attend_meet

def register(x,y): # Finding how many seats are avaiable or not
    diff_seats = x - y  
    return diff_seats


def another_room(): #Loop to only allow for y,Y,n,N
    answer = input("Would you like to enter another room? (y/n) :")
    while answer != "Y" and  answer != "y" and  answer != "N" and answer != "n":
        answer = input("Would you like to enter another room? (y/n) :")
    return answer
#START OF CODE-----------------------------------------------------------------------
answer = "y"
while answer == "y" or answer == "Y":
    room_cap= capacity()
    attending = attendees()
    seats_avail = room_cap - attending
    total_diff = register(room_cap , attending)
    if attending <= room_cap:
        print("The conference can be held.",seats_avail , "total seats available")
    else:
        print("The conference can't be held.",total_diff * -1, "total people cant attend")
    answer = another_room()
print("End of Program.")

