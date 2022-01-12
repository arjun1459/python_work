# You're given a number N.
# If N is divisible by 5 or 11 but not both then print "ONE"(without quotes).
# If N is divisible by both 5 and 11 then print "BOTH"(without quotes).
# If N is not divisible by 5 or 11 then print "NONE"(without quotes).

number = int(input())

if number % 11 == 0 and number % 5 == 0:
    print("BOTH")
elif number % 11 != 0 and number % 5 != 0:
    print("NONE")
else:
    print("ONE")
