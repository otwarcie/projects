# name = "Julie"
# age = "42"
# sentence = "Hi my name is {} and I am {} years old".format(name, age)
# print(sentence)

# year = 1004

# if 1000 < year < 2000:
# 	print('you are in 1000 to 2000 a.d.')
# else:
# 	print('you are not')

# year = 3004

# if 1000 < year < 2000:
# 	print('you are in 1000 to 2000 a.d.')
# else:
# 	print('you are not')

# def tripleprint(one_string):
# 	print(one_string*3)

# tripleprint('ahoj')

shoes = ['Spizikes', 'Air Force 1', 'Curry 2', 'Melo 5']
print(shoes)

for shoe in shoes:
	print(shoe)

for x in range(1, 10):
	print(x)
print()

numbers = [76, 83, 16, 69, 52, 78, 10, 77, 45, 52, 32, 17, 58, 54, 79, 72, 55, 50, 81, 74, 45, 33, 38, 10, 40, 44, 70, 81, 79, 28, 83, 41, 14, 16, 27, 38, 20, 84, 24, 50, 59, 71, 1, 13, 56, 91, 29, 54, 65, 23, 60, 57, 13, 39, 58, 94, 94, 42, 46, 58, 59, 29, 69, 60, 83, 9, 83, 5, 64, 70, 55, 89, 67, 89, 70, 8, 90, 17, 48, 17, 94, 18, 98, 72, 96, 26, 13, 7, 58, 67, 38, 48, 43, 98, 65, 8, 74, 44, 92]

for number in numbers:
	if number > 90:
		print(number)

print()

[print(x) for x in numbers if x > 90]

words = ["PoGo","Spange","Lie-Fi"]
definitions = ["Slang for Pokemon Go","To collect spare change, either from couches, passerbys on the street or any numerous other ways and means","When your phone or tablet indicates that you are connected to a wireless network, however you are still unable to load webpages or use any internet services with your device"]
cooldictionary = {}
for i, x in enumerate(words):
	cooldictionary[x] = definitions[i]
print(cooldictionary)


class Car:
    def __init__(self,year, make, model):
        self.year = year
        self.make = make
        self.model = mode

    def age(self):
    	return 2020 - self.year

