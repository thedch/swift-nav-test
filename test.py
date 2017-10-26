import main as fib

idealSequence = ['FizzBuzz', '1', '1', 'BuzzFizz', 'BuzzFizz', 'BuzzFizz', '8',
'BuzzFizz', 'Buzz', '34', 'Fizz']

testSequence = fib.printFibonacci(len(idealSequence))

for i, val in enumerate(idealSequence):
	if idealSequence[i] != testSequence[i]:
		print('Error at index', i)