"""
3. Get age

Dictionary contains name, age and gender (m/f) of team members (Andrea(40/f), Loren (26/f), Paul(32/m), Mike(45/m), Simon (25/m), Frank (30/m)). 

Ask user to enter team member name. If the member is male write his age to console and if the value is greater than 30 the message ‘you are getting older’. If the team member is female write ‘you are still young’ disregarding the age.
"""

class DatabaseError(Exception):
    pass

KEY_1 = "name"
KEY_2 = "age"
KEY_3 = "gender"

# Old requirement
team_members = [
    { KEY_1: "Andrea",  KEY_2: 40,  KEY_3: 'f' },
    { KEY_1: "Loren",   KEY_2: 26,  KEY_3: 'f' },
    { KEY_1: "Paul",    KEY_2: 32,  KEY_3: 'm' },
    { KEY_1: "Mike",    KEY_2: 45,  KEY_3: 'm' },
    { KEY_1: "Simon",   KEY_2: 25,  KEY_3: 'm' },
    { KEY_1: "Frank",   KEY_2: 30,  KEY_3: 'm' }
]

# New requirement
names = [member[KEY_1] for member in team_members]
ages = [member[KEY_2] for member in team_members]
genders = [member[KEY_3] for member in team_members]

team_members = {KEY_1: names, KEY_2: ages, KEY_3: genders}

def check_gender(index):
    name = team_members[KEY_1][index]
    age = team_members[KEY_2][index]
    gender = team_members[KEY_3][index]

    if gender == 'm':
        print("\n- {} is {} years old.".format(name, age))
        if age > 30:
            print("- You are getting older.")
    else:
        print("\n- You are still too young.")

try:
    user_input = input("Please enter a team member's name:\n\t")

    if not user_input in team_members[KEY_1]:
        raise DatabaseError 

    for name in team_members[KEY_1]:
        if user_input == name:
            check_gender(team_members[KEY_1].index(name))
            break
except DatabaseError:
    print("\n- This name is not in our database.")

#-------------------------------------------------