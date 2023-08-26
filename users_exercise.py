users = {
  "Jonathan": {
    "twitter": "jonnyt",
    "lottery_numbers": [6, 12, 49, 33, 45, 20],
    "home_town": "Stirling",
    "pets": [
    {
      "name": "fluffy",
      "species": "cat"
    },
    {
      "name": "fido",
      "species": "dog"
    },
    {
      "name": "spike",
      "species": "dog"
    }
  ]
  },
  "Erik": {
    "twitter": "eriksf",
    "lottery_numbers": [18, 34, 8, 11, 24],
    "home_town": "Linlithgow",
    "pets": [
    {
      "name": "nemo",
      "species": "fish"
    },
    {
      "name": "kevin",
      "species": "fish"
    },
    {
      "name": "spike",
      "species": "dog"
    },
    {
      "name": "rupert",
      "species": "parrot"
    }
  ]
  },
  "Avril": {
    "twitter": "bridgpally",
    "lottery_numbers": [12, 14, 33, 38, 9, 25],
    "home_town": "Dunbar",
    "pets": [
      {
        "name": "monty",
        "species": "snake"
      }
    ]
  }
}

# 1. Get Jonathan's Twitter handle (i.e. the string `"jonnyt"`)
Jonathan_twitter = users["Jonathan"]["twitter"]
print(Jonathan_twitter)
# 2. Get Erik's hometown
def get_hometown(name):
  return users[name]["home_town"]
print(get_hometown("Erik"))
# 3. Get the list of Erik's lottery numbers
def get_lottery_numbers(name):
   return users[name]["lottery_numbers"]
print(get_lottery_numbers("Erik"))
# 4. Get the species of Avril's pet Monty
Monty_species = users["Avril"]["pets"][0]["species"]
print(Monty_species)
# 5. Get the smallest of Erik's lottery numbers
Erik_lottery_sorted = sorted(get_lottery_numbers("Erik"))
print(Erik_lottery_sorted[0])
# 6. Return an list of Avril's lottery numbers that are even
Avril_lottery = get_lottery_numbers("Avril")
Avril_even_numbers = []
for number in Avril_lottery:
    if number % 2 == 0:
      Avril_even_numbers.append(number)
print(Avril_even_numbers)
# 7. Erik is one lottery number short! Add the number `7` to be included in his lottery numbers
users["Erik"]["lottery_numbers"].append(7)
print
# 8. Change Erik's hometown to Edinburgh
users["Erik"]["home_town"] = "Edinburgh"
print(get_hometown("Erik"))
# 9. Add a pet dog to Erik called "fluffy"
users["Erik"]["pets"].append({
   "name" : "fluffy",
   "species" : "cat"
})
print(users["Erik"]["pets"])
# 10. Add another person to the users dictionary
users["Molly"] = {
    "twitter" : "greyedout",
    "lottery_numbers" : [],
    "home_town" : "Balerno",
    "pets" :[
       {"name" : "Dumbledore",
        "species" : "cat"
        }
    ]
}
print(users)