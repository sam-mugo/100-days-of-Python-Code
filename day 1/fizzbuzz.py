# if a factor of 3 print fizz
#if a factor of 5 print buzz
#if a factor of 3 and 5 print fizzbuzz
#if not factor of 3 or 5 print not fizz, not buzz


def fizz_buzz(number):
    if number % 3 == 0 and number % 5 == 0:
        print("fizzbuzz")
    elif number % 3 == 0:
        print("fizz")
    elif number % 5 == 0:
        print("buzz")
    else:
        print("Not a fizz, buzz or fizzbuzz")
    
fizz_buzz(75)    