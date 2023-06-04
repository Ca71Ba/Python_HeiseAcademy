foods = []
foods.append("Steak")
foods.append("Nudeln")
foods.append("Gemüse")

foods.pop()

foods.insert(1, "Reis")

last = len(foods)
lastfood = foods[last-1]

print(foods)

print(f"Letztes Gericht: {last}")
#print(f"Letztes Gericht: {lastfood}")
#print(f"Letztes Gericht: {foods[len(foods)-1]}")
print(f"Letztes Gericht: {foods[-1]}")
