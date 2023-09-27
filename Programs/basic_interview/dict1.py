
# <<<<<<<<<<<< assigning value to the dictionary
wdict = {}
wdict[0] = "make"
wdict[1] = "it"
wdict[2] = "easy"
print("assigning values to empty dict: ", wdict)

wdict[0] = "do"
print("updating a dictionary: ", wdict)

# <<<<<<<<<<<< merging to dictionaries
vdict = {0: 'benz', 1: 'BMW',2: 'maseratti', 3: 'ferrari'}
vdict.update({4:'RR',5:'Range Rover'})
print("merging two dicts: ", vdict)


# <<<<<<<<<<<< converting two list to dict using zip
roll_no = [10, 20, 30, 40, 50]
names = ['Ramesh', 'Mahesh', 'Kamlesh','Suresh', 'Dinesh']

cdict = dict(zip(roll_no, names))
print("zipping two list: ", cdict)

# <<<<<<<<<<<< converting list to dict
cars = ['romeo','ghost','compass','jeep']
print("list to dict using enumerate: ", dict(enumerate(cars)))


employee_names = ['Ramesh', 'Mahesh', 'Kamlesh', 'Suresh']
new_dict = {}
for i, name in enumerate(employee_names):
    new_dict[i] = name
print("list to dict using for loop: ",new_dict)

ndict = dict([(i,x) for i,x in enumerate(employee_names)])
print("list to dict using list comp and enumerate: ",ndict)

# <<<<<<<<<<<< converting list of tuples to dict
a = [(1, 2, 3, 4, 5, 6), (1, 4), (3, 5, 3, 4, 5, 6), (5, 7),(5, 6), (4, 4)]
b = dict(enumerate([list(i) for i in a]))
print("converting list of tuples to dict:", b)