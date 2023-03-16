import os, sys, requests

def getcont(user, day, returnformalday=False):
    page = requests.get("https://github.com/" + user).text
    # Removes everything in the HTML file thats not needed
    page = page[page.find("js-calendar-graph-svg"):page.find("</g>  </svg>")]
    page = page.split("\n")

    for ln in page:
        if not day in ln:
            continue

        cont = ln[ln.find("\">") + 2:ln.find("contribution")]
        try:
            cont = int(cont)
        except:
            cont = 0
        if returnformalday == False:
            return cont

        else:
            formalday = ln[ln.find("contribution") + 16:ln.find("</rect>")]
            return cont, formalday

