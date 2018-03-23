print("Hello world")
print 'what\'s up?'
print 'Let\'s get started...'

#####asking name#####

spy_name = input("Welcome to spy chat, you must tell me your spy name first: ")
if len(spy_name) > 0:
   spy_name=input("What is your name?")
   print 'Welcome ' + spy_name + '. Glad to have you back with us.'

   #####providing salutation######
   spy_salutation = input("What should we call you (Mr. or Ms.)?")
   spy_salutation + " " + spy_name

   spy_name = spy_salutation + " " + spy_name
   print(spy_name)
   print "Alright " + " " + spy_name +". I'd like to know a little bit more about you before we proceed..."
else:
    print "A spy needs to have a valid name. Try again please."

#####further details#####
spy_age = 0
spy_rating = 0.0
spy_is_online = False
#####asking age#####
spy_age = input("What is your age?")
if spy_age > 12 and spy_age < 50:
    spy_rating = float(input("What is your spy rating?"))
else:
    print 'Sorry you are not of the correct age to be a spy'
if spy_rating > 4.5:
    print 'Great ace!'
elif spy_rating > 3.5 and spy_rating <= 4.5:
    print 'You are one of the good ones.'
elif spy_rating >= 2.5 and spy_rating <= 3.5:
    print 'You can always do better'
else:
    print 'We can always use somebody to help in the office.'
spy_is_online = True
print 'Authentication complete. Welcome ', spy_name
print 'Your age =' , spy_age
print 'Your spy rating=',spy_rating