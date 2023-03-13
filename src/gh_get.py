import os, sys, requests

def getcont(user, day, returnformalday=False):
    page = requests.get("https://github.com/" + user).text
    # Removes everything in the HTML file thats not needed 
    page = page[page.find("js-calendar-graph-svg"):page.find("</g>  </svg>")]
    page = page.split("\n")

    for ln in page:
        if not day in ln:
            continue

        cont = int(ln[ln.find("data-level=\"") + 12:ln.find("rx=") - 2])
        if returnformalday == False:
            return cont

        else:
            formalday = ln[ln.find("contributions on ") + 17:ln.find("</rect>")]
            return cont, formalday

