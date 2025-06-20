#%%
user_id = '32415' 
user_id = str(user_id)
user_name = ' mike_reed '
user_name = user_name.strip().replace(' ', '')
user_name = user_name.strip().replace('_', ' ')
user_age = 32.0
user_age = int(user_age)

print(user_id)
print(user_name)
print(user_age)

fav_categories = ['ELECTRONICS', 'SPORT', 'BOOKS']
fav_categories_low = []


for category in fav_categories:
   lower_category = category.lower()
   fav_categories_low.append(lower_category)


print(fav_categories_low)

#%%
user_name = ' mike_reed '
user_name = user_name.strip().replace(' ', '')
user_name = user_name.strip().replace('_', ' ')

print(user_name)

#%%
user_name = 'mike reed'
name_split = "mike reed"
name_split = user_name.split(' ')

print(name_split)

#%%
user_age = 32.0
user_age = int(user_age)

print(user_age)

#%%
user_age = 'treinta y dos' 

try:
  user_age_int = int(user_age)
except ValueError:
  print("Please provide your age as a numerical value.")

#%%
fav_categories = ['ELECTRONICS', 'SPORT', 'BOOKS']
fav_categories_low = []


for category in fav_categories:
   lower_category = category.lower()
   fav_categories_low.append(lower_category)


print(fav_categories_low)

#%%
fav_categories_low = ['electronics', 'sport', 'books']
spendings_per_category = [894, 213, 173]

total_amount = sum(spendings_per_category)
max_amount = max(spendings_per_category)
min_amount = min(spendings_per_category)


print(total_amount)
print(max_amount)
print(min_amount)

#%%
from random import randint

total_amount_spent = 1280
target_amount = 1500

while total_amount_spent <= target_amount:
	new_purchase = randint(30, 80) # generamos un número aleatorio de 30 a 80
	total_amount_spent += new_purchase

print(total_amount_spent)

#%%
user_id = '32415'
user_name = ['mike', 'reed']
user_age = 32

user_info = f"El usuario {user_id} es {user_name[0]}, quien tiene {user_age} años"

print(user_info)

#%%
users = [
	  # este es el inicio de la primera sublista
    ['32415', ['mike', 'reed'], 32, ['electronics', 'sport', 'books'],
        [894, 213, 173]
    ], # este es el final de la primera sublista

    # este es el inicio de la segunda sublista
    ['31980', ['kate', 'morgan'], 24, ['clothes', 'shoes'],
        [439, 390]
    ] # este es el final de la segunda sublista
]

revenue = 0

for user in users:
	spendings_list = user[4][-0:4]
	total_spendings = sum(spendings_list)
	revenue += total_spendings
print(revenue)

#%%
users = [
    ['32415', ['mike', 'reed'], 32, ['electronics', 'sport', 'books'],
     [894, 213, 173]],
    ['31980', ['kate', 'morgan'], 24, ['clothes', 'books'], [439,
     390]],
    ['32156', ['john', 'doe'], 37, ['electronics', 'home', 'food'],
     [459, 120, 99]],
    ['32761', ['samantha', 'smith'], 29, ['clothes', 'electronics',
     'beauty'], [299, 679, 85]],
    ['32984', ['david', 'white'], 41, ['books', 'home', 'sport'], [234,
     329, 243]],
    ['33001', ['emily', 'brown'], 26, ['beauty', 'home', 'food'], [213,
     659, 79]],
    ['33767', ['maria', 'garcia'], 33, ['clothes', 'food', 'beauty'],
     [499, 189, 63]],
    ['33912', ['jose', 'martinez'], 22, ['sport', 'electronics', 'home'
     ], [259, 549, 109]],
    ['34009', ['lisa', 'wilson'], 35, ['home', 'books', 'clothes'],
     [329, 189, 329]],
    ['34278', ['james', 'lee'], 28, ['beauty', 'clothes', 'electronics'
     ], [189, 299, 579]],
    ]

age_client = []
for user in users:
    if user[2] <= 30:
        age_client.append([user[1][0], user[2]])  

for age in age_client:
    print(age)

#%%
users = [
    ['32415', ['mike', 'reed'], 32, ['electronics', 'sport', 'books'],
     [894, 213, 173]],
    ['31980', ['kate', 'morgan'], 24, ['clothes', 'books'], [439,
     390]],
    ['32156', ['john', 'doe'], 37, ['electronics', 'home', 'food'],
     [459, 120, 99]],
    ['32761', ['samantha', 'smith'], 29, ['clothes', 'electronics',
     'beauty'], [299, 679, 85]],
    ['32984', ['david', 'white'], 41, ['books', 'home', 'sport'], [234,
     329, 243]],
    ['33001', ['emily', 'brown'], 26, ['beauty', 'home', 'food'], [213,
     659, 79]],
    ['33767', ['maria', 'garcia'], 33, ['clothes', 'food', 'beauty'],
     [499, 189, 63]],
    ['33912', ['jose', 'martinez'], 22, ['sport', 'electronics', 'home'
     ], [259, 549, 109]],
    ['34009', ['lisa', 'wilson'], 35, ['home', 'books', 'clothes'],
     [329, 189, 329]],
    ['34278', ['james', 'lee'], 28, ['beauty', 'clothes', 'electronics'
     ], [189, 299, 579]],
    ]

list_user = []
for user in users:
    spending_list = user[4]
    total_spendings = sum(spending_list)

    if user[2] < 30 and total_spendings > 1000:
        list_user.append(user[1][0])  # Solo el nombre

for name in list_user:
    print(name)

#%%
users = [
    ['32415', ['mike', 'reed'], 32, ['electronics', 'sport', 'books'],
     [894, 213, 173]],
    ['31980', ['kate', 'morgan'], 24, ['clothes', 'books'], [439,
     390]],
    ['32156', ['john', 'doe'], 37, ['electronics', 'home', 'food'],
     [459, 120, 99]],
    ['32761', ['samantha', 'smith'], 29, ['clothes', 'electronics',
     'beauty'], [299, 679, 85]],
    ['32984', ['david', 'white'], 41, ['books', 'home', 'sport'], [234,
     329, 243]],
    ['33001', ['emily', 'brown'], 26, ['beauty', 'home', 'food'], [213,
     659, 79]],
    ['33767', ['maria', 'garcia'], 33, ['clothes', 'food', 'beauty'],
     [499, 189, 63]],
    ['33912', ['jose', 'martinez'], 22, ['sport', 'electronics', 'home'
     ], [259, 549, 109]],
    ['34009', ['lisa', 'wilson'], 35, ['home', 'books', 'clothes'],
     [329, 189, 329]],
    ['34278', ['james', 'lee'], 28, ['beauty', 'clothes', 'electronics'
     ], [189, 299, 579]],
    ]

user_cloth = []

for user in users:
    if 'clothes' in user[3]:
        user_cloth.append(user)
        print (user[1], user[2])