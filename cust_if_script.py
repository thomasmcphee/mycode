#!/usr/bin/env python

message = 'Your score converted to letter grade is '

score = float(input("what score did you receive on your test? "))

if score >= 97:
    message = message + 'an A+.'
elif score >=93:
    message = message + 'an A.'
elif score >=90:
    message = message + 'an A-.'
elif score >=87:
    message = message + 'a B+.'
elif score >=83:
    message = message + 'a B.'
elif score >=80:
    message = message + 'a B-.'
elif score >=77:
    message = message + 'a C+.'
elif score >=73:
    message = message + 'a C.'
elif score >=70:
    message = message + 'a C-'
elif score >=67:
    message = message + 'a D+.'
elif score >=65:
    message = message + 'a D.'
elif score <=65:
    message = message + 'an F.'

print(message)
