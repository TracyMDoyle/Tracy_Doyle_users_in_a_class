# creates the user class
class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    # method to print users
    def display_info(self):
        print("*********Customer Details************")
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Rewards Member: {self.is_rewards_member}")
        print(f"Reward Points: {self.gold_card_points}")

    # invokes info display function/method checking to see if working before progressing
    # display_info(user_Dave)   

    # enrolls a new member into the reward member program
    def enroll(self):
        if self.is_rewards_member == False:
                self.is_rewards_self = True
                self.gold_card_points = 200
        else:
            print(f"{self.first_name} is already enrolled")

    # spend points function

    def spend(self, amount):
        if self.gold_card_points > amount:
            self.gold_card_points -= amount
            print(f"{self.first_name} now has {self.gold_card_points} points. ")
            return self.gold_card_points
        else:
            print(f"{self.first_name} does not have enough points.")

# creates users to input into the class
user_Dave = User("Dave", "Smith" , "DSmith@gmail.com" , "32")
user_Pam = User("Pam", "Martin" , "QTPam@gmail.com" , "21")
user_Steve = User("Steve", "Mann" , "damann@gmail.com" , "47")
# enrolls a member and checks that function worked
user_Dave.enroll() 
print("Dave is now a member!")
# print(user_Dave.is_rewards_member)
# print(user_Dave.gold_card_points)

user_Pam.enroll()
print("Pam is now a member!")
# print(user_Pam.is_rewards_member)
# print(user_Pam.gold_card_points)

# call to check to see if user is blocked from enrolling again
user_Dave.enroll()

# calls and tests the spend points function
user_Dave.spend(50)
user_Pam.spend(80)
user_Steve.spend(40)
# print(user_Dave.gold_card_points)

user_Dave.display_info()
user_Pam.display_info()
user_Steve.display_info()

# Steve decided to join, rock on Steve, you now have points
user_Steve.enroll()
print(user_Steve.gold_card_points)




