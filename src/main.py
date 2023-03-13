import sys
import gh_get as gh

if len(sys.argv) <= 1:
    print("Not Enough Arguments")
    print("contrigrab {user} {day}\n\nday must be in mm-dd format(ex: 02-21 for February 21st) or yy-mm-dd(ex: 23-02-21 for February 21st, 2023), this won't never work for the years before the last year, only this year and the previous year will work")
    exit(1)
fnd = 0
loop = 0
user, day = "", ""
parsable = False
for arg in sys.argv:
    if loop == 0:
        loop += 1
        continue
    if fnd == 0 and arg[0] != "-":
        user = arg
        fnd += 1
    elif fnd == 1 and arg[0] != "-":
        day = arg
    elif arg == "-P" or arg == "--parse":
        parsable = True
else:
    if not parsable:
        cont, fday = gh.getcont(user, day=day, returnformalday=True)
        print("User " + user + " has contributed " + str(cont) + " times on " + fday)
    elif parsable:
        cont, fday = gh.getcont(user, day=day, returnformalday=True)
        print(str(cont))
