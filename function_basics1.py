#1 i think it would try to return 5 food groups, but there isnt anyting inside the function, so nothing will print except for the number 5.
def number_of_food_groups():
    return 5
print(number_of_food_groups())


#2 nothing is in the function so it will just return 5. It wont print days of the week because its not a function outside of print. 
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())


#3 it will return 10 and then print 10 on the page, but not any specific books on hold because there arent any.
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())


#4 it will return and print 5 as the number of fingers
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())


#5 it will print 5, but then may be undefined for the function for lakes because there is nothing in it, and if x is printed then it cant show any data from it.
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)


#6 it will add the two strings together to make bc, and then print that. it will then print the two seperate sums added together
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))


#7 it will add the two strings from the return, and the bottom print will just put 2 and 5 together, not add and push out the sum.
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))

#8 there is nothing within the first function, so it may print none. it will then print 100 as b on the page. the if statement wont happen bvecause b is already greater, and the two conditions on the bottom will not be met.
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())


#9 b and c arent defined, and because of that I dont think anything will print, despite the numbers inside the print(s). the returns may come back but im not sure if it will come out if b and c arent set integers 
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))


#10 it will add b and c from the return, along with 10, unless it is overwritten. then it will print the addition function, which might add the 3 and 5, but they werent stated earlier, so idk.
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))


#11 500 will be printed, and then printed again as the string below, which is greater than or equal to 300. it will print 2 more times after that.
b = 500
print(b)
def foobar():
    b ="keyword operator from-rainbow">= 300
    print(b)
print(b)
foobar()
print(b)


#12 it will print 500 and then 300, because the value is changed. or it may not like the last function.
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)


#13
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)


#14 it will print 1, and then 2, and then 3.
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()


#15 it will print 1, and then 10, and then 3, 5, but not y
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)
