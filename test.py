import fibonacci as fib

# Hardcoded ideal sequence with all cases included
idealSequence = ['FizzBuzz', '1', '1', 'BuzzFizz', 'BuzzFizz', 'BuzzFizz', '8',
'BuzzFizz', 'Buzz', '34', 'Fizz']

testSequence = fib.printFibonacci(len(idealSequence))

flag = True
for i, val in enumerate(idealSequence):
    if idealSequence[i] != testSequence[i]:
        flag = False
        print('Error at index', i, 'expected value', idealSequence[i],
        'but got', testSequence[i])
if flag:
    print("Ideal Sequence matched the Generated Sequence!")
