import os, sys, requests

def getcont(user, day="0", returnformalday=False):
    page = requests.get("https://github.com/" + user).text
    page = page[page.find("js-calendar-graph-svg"):page.find("</g>  </svg>")]
    page = page.split("\n")
    if day != "0":
        loop = 0
        for ln in page:
            #print("okx2")
            if day in ln:
                cont = int(page[loop][page[loop].find("data-level=\"") + 12:page[loop].find("rx=") - 2])
                if returnformalday == False:
                    return cont
                else:
                    formalday = ln[ln.find("contributions on ") + 17:ln.find("</rect>")]
                    print(formalday)
                    return cont, formalday
            else:
                loop += 1