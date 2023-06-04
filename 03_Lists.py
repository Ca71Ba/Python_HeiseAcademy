animals = ["Giraffe", "Affe", "Zebra", "Nashorn", "Gans"]
numbers = [1,2,3,4,5]

#print(animals[1])
#print(animals[3])
#print(animals)

#print(numbers[0])
#print(numbers)

#animals.sort()
animals_sorted = sorted(animals)
print(f"sorted: {animals_sorted}")

animals_sorted.sort(reverse=True)
print(f"reverse: {animals_sorted}")

print(f"Lenght of number list: {len(numbers)}")

aninals = []
#print(aninals2)
aninals.append("Affe")
aninals.append("Löwe")
aninals.append("Zebra")
#aninals.insert(2, "Nashorn")
animals.pop()
animals.pop()

print(aninals)

#animals.pop(1)
#animals.pop(2)
print(aninals)
