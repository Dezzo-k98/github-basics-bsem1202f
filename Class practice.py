# python basics
print ("hello world")
name = ("Amadu" 
        "")
age = 20
if age >= 18:
    print (f"{name} you are old enough")
else:
    print ("you are young")
first_num, second_num, third_num = 1, 2, 3
print (second_num)
Message = "collect my keys from isatu"
print (Message)
message = "Tell collier i will deduct 15%"
print (message)
price_of_product = 34
Student_name = "coiiier"
ce_yams = 23.56
is_married = False

one_line_sentence = ("I love programming"
                     "It pays me a lot"
                     "programming changed my life"
                     "Tho, sometimes it mnakes boring to others")
print (one_line_sentence)
poem = ("""I love programming
           It pays me a lot
           programming changed my life
           Tho, sometimes it makes boring to others.""")

print (poem)
person_age = 17
is_adult_person = person_age >= 18
print (person_age)
try:
    any_number = int ("456")
    print(any_number)

except ValueError: print ("invalid ouput. Try again")
print("programming", "python", "Awesome")
print ("programming" "python" "Awesome" , sep="_")
student = input("please enter your name: ")
print (f" good afternoon, {student}")

try :
    user_age = int(input("please enter your age: "))
    print(f"You are {user_age} years old")
except ValueError:
    print("Invalid input. not a number")

