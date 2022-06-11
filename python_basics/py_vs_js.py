# 1. Code Blocks, comments and template strings

# Example 1
#py:
if number > 0:
    print(f'Number equals {number}') #f-string in py

#js:
if (number > 0) {
    console.log(`Number equals ${number}`); #template string in js
}

# Example 2
#py:
def check(number):
    print(number)

#js:
function check(number){
    console.log(number);
}

# Comments
# js = //, /*multi-line comment*/
# py = #

#################################################    


# 2. Variable Definitions, Naming Conventions, and Constants

#Define the variable
#py:
number = 1

#js:
var number = 1; 
let number = 1;

#Multiple words in variable names
#py:
new_number = 2

#js:
let newNumber = 2;

#Constants
#py:
NEW_CONSTANT_NAME = "Hello,"

#js:
const newConstantName = "Hello,";

#################################################   


# 3. Primitive Data Types and Values

#py None vs js null:
# None - indicates that a variable doesn't have a value (py)
# null - represents the intentional absence of any object value (js)

#js has six primitive data types: 
# Undefined, 
# Boolean: true / false
# String, 
# Number, 
# BigInt, 
# Symbol.


#py has four primitive data types: 
# Integers (int)
# Floats (float)
# Booleans (bool): True / False
# Strings (str)

#################################################   


# 4. Built-in Data Structures

# Tuples (py thing, js does not have tuples):
my_tuple = ("Olgica", 1, True)
print(type(my_tuple)) #<class 'tuple'>
print(my_tuple) # ('Olgica', 1, True)
print(my_tuple[1]) #1
print(my_tuple[-1]) #True
print(len(my_tuple)) #3
# Note: a tuple is an unchangeable collection (we cannot change, add or remove items after the tuple has been created)! 
# Tuple items are ordered (defined order, and that order will not change) and indexed which allows to have duplicate values.

# Lists (py has lists vs js has arrays)
my_list = ["punca", "ima", "rada", "glumiti", "majmuna"]
print(type(my_list)) #<class 'list'>
print(my_list) #['punca', 'ima', 'rada', 'glumiti', 'majmuna']
print(my_list[2]) #rada
print(my_list[-4]) #ima
print(len(my_list))#5
# Note: a list is a changeable collection (we can change, add or remove items at any time)
# List items are ordered (defined order, and that order will not change) and indexed which allows to have duplicate values.

# Dictionary (py thing, js does not have such a type of built-in data structure)
my_dict = {
    "country": "Slovenia",
    "city": "Koper",
    "sea": True,
    "apartment": 1    
}
print(type(my_dict)) #<class 'dict'>
print(my_dict) #{'country': 'Slovenia', 'city': 'Koper', 'sea': True, 'apartment': 1}
print(len(my_dict)) #4
# Note: a dictionary is a collection 

# Sets (one more py thing)
my_set = {"coffee", "milk", "water"}
print(type(my_set)) #<class 'set'>
print(my_set) #{'milk', 'water', 'coffee'}
print(len(my_set)) #3
# Note: A set is a collection which is unordered, unindexed and do not allow duplicate value (duplicate value will be ignored). 
# Values in the dictionary cannot be changed, but they can be added and removed. 

#################################################   


# 5. Operators

# Floor Division 
#py:
print(13 // 6) #2
#js: 
Math.floor(13/6); #2

# Comparing Values and Types
#py:
2 == 2 #True
#js:
2 =="2" #true
2 === 2 #true

#Logical Operators
#py: 
and, or, not
#js:
&&, ||, !

#Type Operators
#py: type(smth)
print(type(1)) #<class 'int'>
print(type(False)) #<class 'bool'>
print(type(None)) #<class 'NoneType'>
print(type("")) #<class 'str'>
print(type(null)) #NameError: name 'null' is not defined
print(type(1,2)) #TypeError: type() takes 1 or 3 arguments
print(type(1.2)) #<class 'float'>

#js: typeof smth
console.log(typeof 1); #number
console.log(typeof false); #boolean
console.log(typeof None); #undefined
console.log(typeof ""); #string
console.log(typeof null); #object
console.log(typeof 1,2); #number
console.log(typeof 1.2); #number

#################################################   


# 6. Input/Output

#Input
#py:
input('message') 
login_input = input('Username')
#js:
window.prompt('message');
let loginInput = window.prompt('Username');

#Output
#py:
print()
#js:
console.log();
#print() in js will lead to print dialog


#################################################   


# 7. Conditional Statements

#IF
#py - if condition:
i = 0
if i >= 0:
    i += 1
    print(i)

#js - if (condition){}  
let i = 0 
if (i >=0){
    i++;
    console.log(i);    
}

#IF/ELSE
#py
i = -1
if i >= 0:
    i += 1
    print(i)
else:
    print(i + 1)

#js   
let i = -1 
if (i >= 0) {
    i++;
    console.log(i);    
} else {
    console.log(i + 1);
}

#ELIF
#py
i = 5
if i == 0:
    i += 1
    print(i)
elif i > 10:
    print("Več kot deset")
elif i < -10:
    print("Manj kot minus deset")
else:
    print(i - 1)

#js
let i = 5 
if (i === 0){
    i++;
    console.log(i);    
} else if (i > 10) {
    console.log("Več kot deset"); 
} else if (i < -10) {
    console.log("Manj kot minus deset"); 
} else {
    console.log(i - 1);
}

#SWITCH
#py does not have such type of built-in structure

#js - switch:
switch (new Date().getDay()) {
  case 0:
    day = "Nedelja";
    break;
  case 1:
    day = "Ponedeljek";
    break;
  case 2:
    day = "Torek";
    break;
  case 3:
    day = "Sreda";
    break;
  case 4:
    day = "Četrtek";
    break;
  case 5:
    day = "Petek";
    break;
  case  6:
    day = "Sobota";
    break;
}

#################################################   


# 8. For Loops and While Loops

#FOR
#py:
n = 10
for i in range(n):
    print(i)

#js:
let n = 10;
for (let i = 0; i < n; i++){
    console.log(i);
}

# For to iterate over the elements 
#py:
items = ["jabolko", "sonce", "kava", "knjiga"]
for item in items:
    print(item) 

#js:
let items = ["jabolko", "sonce", "kava", "knjiga"];
for (let i in items) {
    console.log(items[i]);
}

#WHILE
#py:
x = True
while x == True:
    print(False) 

#js:
let x = true;
while (x === true) {
    console.log(false);
}    

#DO...WHILE
#py does not have such a loop as do ... while

#js:
let i = 0;
do {
    console.log('Ciao!');
    i++;

} while (i < 5);

#################################################   


# 9. Functions

# Anonymous functions
#py:
#anonymos function in py aka lambda. Functions with name is defined using 'def', anonymous function is defined with 'lambda'
#syntax -> lambda arguments : expression
triple = lambda x: x * 3
print(triple(3)) #9

#js:
let triple = function (x){
  return x * 3;
}
console.log(triple(3)); #9

# Named functions
#py:
def triple(x):
    return x * 3
print(triple(4)) #12

#js:
#traditional named function
function triple(x) {
    return x * 3;
}
console.log(triple(4)); #12
# arrow named function
let triple = x => x * 3;
console.log(triple(4)); #12

#################################################   


# 10. Object-Oriented Programming

#Class, constructor, attributes, methods, and instances
#py:
class Person: #class 
  def __init__(self, surname, name, patronymic): #__init__ is a constructor that initializes the new instance
    self.surname = surname #use self to assign value to attribute
    self.name = name
    self.patronymic = patronymic
    

  def introduce_yourself_in_english(self): #method is defined with 'def' followed by name and params list which starts with self.
    print(f"Hello, my name is {self.name} {self.surname}.")

  def introduce_yourself_in_russian(self):

    print(f"Zdravstvujte, menja zovut {self.surname} {self.name} {self.patronymic}.")

name = Person("Shtante", "Olga", "Alexeevna") #instance of the class
name.introduce_yourself_in_english() #Hello, my name is Olga Shtante.
name.introduce_yourself_in_russian() #Zdravstvujte, menja zovut Shtante Olga Alexeevna.

#js:
class Person {

    constructor(surname, name, patronymic) {
        this.surname = surname;
        this.name = name;
        this.patronymic = patronymic;
    }

    introduceYourSelfInEnglish() {
        console.log(`Hello, my name is ${this.name} ${this.surname}.`);
    }

    introduceYourSelfInRussian() {
        console.log(`Zdravstvujte, menja zovut ${this.surname} ${this.name} ${this.patronymic}.`);
    }
}

const name = new Person("Shtante", "Olga", "Alexeevna"); 
name.introduceYourSelfInEnglish(); #Hello, my name is Olga Shtante.
name.introduceYourSelfInRussian(); #Zdravstvujte, menja zovut Shtante Olga Alexeevna.