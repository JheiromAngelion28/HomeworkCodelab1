### 1. Creating a List
Fruits = ["Mango","Passion Fruit","Orange","Dragon Fruit", "Banana"]
print(Fruits)

### 2. Accessing Elements
colors = ["blue", "Cyan", "Magenta", "Purple", "Orange"]
print(colors [0])
print(colors [2])
print(colors [-1])

### 3. Modifying a List
numbers = ['10','90','30','70', '60']
numbers[2] = 100
print (numbers)

### 4. List Slicing
names = ["josh","mark","elice","annie","joseph","vick"]
print (list[0:3])

### 5. Looping through a List
loopinglist = ["1","2","3","4","5","6","7","8","9","10"]
for x in loopinglist:
  print(x)

### 6. List Methods: Append and Extend

shopping_cart = ["Chicken", "Apple", "cheese"]
shopping_cart.append(["Butter", "Bread", "Eggs"])
sub_cart = ["Beef Whellington" "Salmon"]
shopping_cart.extend(sub_cart)
print(shopping_cart)

### 7. Finding Maximum and Minimum in a List

Minandmaximun = [40, 80, 88, 560, 620, 600]
print(min(Minandmaximun))
print(max(Minandmaximun))


### 8. Counting Occurrences
Alphabets = ["a","a","b","b","e","e","f","j","h","e","k","3","a","H","a"]
count = Alphabets.count("e")
print(count)

### 9. List Comprehension
Even_numbers = ["1","2","3","4","5","6","7","8","9","10"]
Even_numbers = [x**2 for x in range(11) if x % 2 == 0]
print(Even_numbers)

### 10. Removing Duplicates

Nums= [1,2,2,3,3,3,4,4,4,5,5,6,7,8,9,9,9,]
Nums = list(set(Nums))
print(Nums)
