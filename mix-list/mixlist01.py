#!/usr/bin/env python3
import random

my_list =["192.168.0.5", 5060, "UP"]


#prints the first IP 
print("The first item in the list (IP): " + my_list[0] )

#prints the port
print("The second item in the list(port): " + str(my_list[1]))

#prints the state
print("The last item in the list (state): " + my_list[2] )



iplist = [5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh"]

print("The ip addresses are " + iplist[3] +" "+ iplist[4])


wordbank = ["indentation", "spaces"]
tlgstudents= ['Albert', 'Anthony', 'Brenden', 'Craig', 'Deja', 'Elihu', 'Eric', 'Giovanni', 'James', 'Joshua', 'Maria', 'Mohamed', 'PJ', 'Philip', 'Sagan', 'Suchit', 'Meka', 'Trey', 'Winton', 'Xiuxiang', 'Yaping']

wordbank.append(4)

num = int(input("Please enter a number between 0 and 20"))

student_name =   random.choice(tlgstudents)


print(student_name + " always uses " + str(wordbank[2]) + " spaces to indent ") 










