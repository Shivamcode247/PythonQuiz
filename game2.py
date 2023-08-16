print('Welcome to PythonPlay Quiz')
answer = input('Are You Reeady To Play Quiz (yes/no)?:\n')
score= 0
total_questions = 3

if answer.lower():'yes'
answer= input('What is Your Favorite Programming Language?')
if answer.lower()=='python' or 'Python':
    score += 1
    print('Correct')
else :
    print('Wrong Answer :(')
answer= input('Which first Programming Language you hear first?\n')
if answer.lower()=='html' or 'HTML' :
    score += 1
    print('Correct')
else :
    print('Wrong Answer :(')
answer= input('Best Programming Language is easy to learn?\n')
if answer.lower()=='python' or 'Python':
    score += 1
    print('Correct')
elif answer.lower()=='c+' or 'C' :
      score += 1
      print('Correct')  
else :
    print('Wrong Answer :(')                   

print('Thankyou for Playing this small Quiz Game, You attemted',score,"questions correctly!")
mark=(score/total_questions)*100
print('Marks obtained:',mark)
print('BYE!')
print('Have a good day!')