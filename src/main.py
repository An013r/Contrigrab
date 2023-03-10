import sys
import gh_get as gh

if len(sys.argv) <= 1:
    print("Not Enough Arguments")
    print("contrigrab {{user}} [day]\n\nday must be in mm-dd format(ex: 02-21 for February 21st)\nif a day is not specified, it will print it in the style that github presents it")
    exit(1)
fnd = 0
loop = 0
user, arg = "", ""
# TODO: Add argument to print it out in an easily parsable way, eg CONT=0;DAY="03-06" etc.
for arg in sys.argv:
    if loop == 0:
        loop += 1
        continue
    if fnd == 0 and arg[0] != "-":
        user = arg
        fnd += 1
    elif fnd == 1 and arg[0] != "-":
        day = arg
if day == "":
    # TODO: Implement this
    NUL
else:
    #print("Contributions on day ")
    cont, fday = gh.getcont(user, day=day, returnformalday=True)
    print("User " + user + " has contributed " + str(cont) + " times on " + fday)