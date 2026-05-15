-- Behind the scene of loops in python --
iteration tool (for) this goes to :- useing iter()
iterable objects (lists, file) points to strat point of the memory and returns the next
response __next__ also written as next() next is getting means there are other more values too. and when end is reached, stop exception is hited.

files have their own iter() tool/method

iter(any iterable object here)
ex. 
myList = [1, 2, 3, 4]
I - iter(myList)
I
it gives this ;- 
<list_iterator object at 0x0102f4f430> i.e it gives the memory posiotn

but in the case of files, python bydefault does this thing iter(myFile) i.e it stores the location of the strat of the file.
example:-
f = open('filename.txt')
iter(f) is f
true (this is the result)

but if done same for array, example :- 
myNewList = [1, 2, 3]
iter(myNewList) is myNewList
False (this is the result)

// conclusion
when file is stored ina variable, then it is a iterable object in its own.
but in case of list, then it is not its iterable object, just the refrence of the actual object.

dictionary and range is also iterable.


-- closure --
jab hum kisi fuction ki puri defication ko hi return karate hai to uss function k sath associated jitne bhi sare refrences and values hai vo sare jate hai and isiko bolte hai closure
closure ko factory function bhi bolte hai 

---- oops ----
in class 'self' use hota hai yeh btane k liye ki jo bhi var use hoga vo isi class ka hoga naki iske bahar ka koi variable
like :- self.varname

__init__ yeh python class ka constructor function hota hai yahi jb class call hoti hai to yahi function chlta hai

super() keyword use hota hai jb kisi class ko inherit karte hai, iska use krk hum uss upr wali claass ki chije access kar skte hai

__varname # for encapsulation we use __ in front of var name, it makes the variable private i.e, now it is accessable only in the class and not in the objects. for accessing such vars we make methods for it.

same setter bhi hota hai, setter yani esa method jo private vars ko safely update karta hai
---

-- Static Methods --
In python, static methods vo hote hai jinhe objects access na kar paye only class kar sake.
They dont requrire self parameter since objects to access hi nahi kar sakte

property decorator use krte hai jab attribute ko readonly banana ho 
also method ko variable ki tarah access kar sakte hai