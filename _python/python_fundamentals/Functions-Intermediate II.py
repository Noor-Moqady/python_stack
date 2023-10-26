x = [ [5,2,3], [10,8,9] ] 
x[1][0] = 15 #Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] 
print (x)
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
students[0]['last_name'] = 'Bryant' #Change the last_name of the first student from 'Jordan' to 'Bryant'
print (students)
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
sports_directory ['soccer'][0] = 'Andres' #In the sports_directory, change 'Messi' to 'Andres'
print (sports_directory)
z = [ {'x': 10, 'y': 20} ]
z [0]['y'] = 30  #Change the value 20 in z to 30
print (z)

#################################################################################################### cant do the bouns!!!
def iterateDictionary(any_list):
    for i in range(len(any_list)):
        any_list [i]["first_name"]
        print("first_name- "+ any_list [i]["first_name"] +", "+ "last_name- "+any_list [i]["last_name"])
        #for key, val in any_list[i].items():
            #print(key, '-', val)
            #print("- ".join([key, val])) #.join function just for list
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
iterateDictionary(students) 
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

##################################################################################################################

def iterateDictionary2(any_list):
    for i in range(len(any_list)):
        for k in any_list[i]:
            print((any_list[i])[k])
            print(k)
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
iterateDictionary2(students)

#####################################################################################################
def printInfo(dojo_dictionary):
    for k in dojo_dictionary:
        print(len(dojo_dictionary[k]), k.upper())
        for val in dojo_dictionary[k]:
                print (val)
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)
# output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
    
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon
















