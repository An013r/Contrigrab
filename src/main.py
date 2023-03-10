import sys
import gh_get as gh

if len(sys.argv) <= 1:
    print("Not Enough Arguments")
    print("contrigrab {{user}} [day]")
    exit(1)
loop = 0
user, arg = "", ""
for arg in sys.argv:
    if loop == 0 and arg[0] != "-":
        user = arg
    elif loop == 1 and arg[0] != "-":
        day = arg
