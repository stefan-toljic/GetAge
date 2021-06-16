"""
3. Get age

Dictionary contains name, age and gender (m/f) of team members (Andrea(40/f), Loren (26/f), Paul(32/m), Mike(45/m), Simon (25/m), Frank (30/m)). 

Ask user to enter team member name. If the member is male write his age to console and if the value is greater than 30 the message ‘you are getting older’. If the team member is female write ‘you are still young’ disregarding the age.
"""

team_members = [
    { "name": "Andrea", "age": 40, "gender": 'f' },
    { "name": "Loren", "age": 26, "gender": 'f' },
    { "name": "Paul", "age": 32, "gender": 'm' },
    { "name": "Mike", "age": 45, "gender": 'm' },
    { "name": "Simon", "age": 25, "gender": 'm' },
    { "name": "Frank", "age": 30, "gender": 'm' }
]

def check_gender(member):
    if member["gender"] == 'm':
        print("\n- {} is {} years old.".format(member["name"], member["age"]))
        if member["age"] > 30:
            print("- You are getting older.")
    else:
        print("\n- You are still too young.")

user_input = input("Please enter a team member's name:\n\t")

for member in team_members:
    if user_input == member["name"]:
        check_gender(member)
        break

#-----------------------------------