import random
file_name = "verbes.carte"
deck = []
deck_range = []
counter = 0

def str_sum(array):
    result = ""
    for element in array:
        if result == "":  
            result += element
        else:
            result += " "
            result += element
    return result

with open(file_name, "r") as card: #To change
    content = card.readline()
    while content != "":
        deck.append({})
        deck[counter]["heads"] = content.split(":")[0]
        deck[counter]["tails"] = str_sum(content.split(":")[1].split())
        deck[counter]["success"] = True
        counter += 1
        content = card.readline()

content_number = int(input(f"Number of thing to see (0 for all, to {len(deck)}): "))

random.shuffle(deck) #important!

if content_number == 0:
    for element in deck:
        deck_range.append(element)
elif content_number < len(deck):
    for i in range(content_number):
        deck_range.append(deck[i])
else:
    print("Error")
    quit()

# print(deck_range)

if content_number == 0:
    content_number = len(deck_range)

for i in range(len(deck_range)): #A changer en fonction de i
    heads_or_tails = random.randint(1,2)
    if heads_or_tails == 1:
        entry = input(f"[{i + 1}/{content_number}] {deck_range[i]['heads']} : ")
        if entry != deck_range[i]["tails"]:
            deck_range[i]["success"] = False
    elif heads_or_tails == 2:
        entry = input(f"[{i + 1}/{content_number}] {deck_range[i]['tails']} : ")
        if entry != deck_range[i]["heads"]:
            deck_range[i]["success"] = False

print("\nTo review :")
for element in deck_range:
    if element["success"] == False:
        print(f"\033[31m{element['heads']} : {element['tails']}\033[0m")
