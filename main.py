#Variables
age = 12
name = "Bob"
#Or
age, name = 12, 'Bob'

#List
names = ["Liz", "Lee", "Vee", "Dee"]
ages = [12, 43, 56, 76]

# for index, n in enumerate(names):
#     print(f'Name: {n} Age: {ages[index]}')

# dictionary

people = {
    "Lee": 43,

    "Liz": [12,34,45],

    "Vee": {
        "place": "Rongai",
        "School": "Dogomothi preparatory rehab center",
        "phone": 7123456789
        },

    "Dee": [
            {"SocialMedia": 'ig', "Personality": "extrovat"}, 
            {"Bio":
                 {"Dob": '12/53/5', "id": 452324}
                 }
                ]
}

print(people["Dee"][1]['Bio']["Dob"])



PEOPLE = {
    "Lee": 43,

    "Liz": [12,34,45],

    "Vee": {
        "place": "Rongai",
        "School": "Dogomothi preparatory rehab center",
        "phone": 7123456789
        },

    "Dee": [
            {"SocialMedia": 'ig', "Personality": "extrovat"}, 
            {"Bio":
                 {"Dob": '12/53/5', "id": 452324}
                 }
                ]
}

print(people["Dee"][1]['Bio']["Dob"])