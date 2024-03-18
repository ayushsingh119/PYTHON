# slicing: crate a substring by extracting elements from another string
# indexing[] or slice()
# [start:stop:step]

name = "supernova"
first_name = name[0:5]  # here in slicing the first index is inclusive and second index is exclusive.
print(first_name)

first_name = name[:5]  # if we not give the initial index in slicing then it will automatically take index from 0.
print(first_name)

second_name = name[5:]  # if we not give the ending index in slicing then it will automatically take index to the last.
print(second_name)

last_name = name[0:9:1]
print(last_name)

last_name = name[0:9:2]
print(last_name)

reversed_name = name[::-1]  # it will reverse the string
print(reversed_name)

#============================= SLINCE () ===================================#

website1 = "http://google.com"
website2 = "http://wikipedia.com"
slice = slice(7,-4)
print(website1[slice])
print(website2[slice])