"""
Navigator

On October 28, 1994, Netscape Navigator was released, helping millions explore the early web.

Given an array of browser commands you executed on Netscape Navigator, return the current page you are on after executing all the commands using the following rules:

    You always start on the "Home" page, which will not be included in the commands array.
    Valid commands are:
        "Visit Page": Where "Page" is the name of the page you are visiting. For example, "Visit About" takes you to the "About" page. When you visit a new page, make sure to discard any forward history you have.
        "Back": Takes you to the previous page in your history or stays on the current page if there isn't one.
        "Forward": Takes you forward in the history to the page you came from or stays on the current page if there isn't one.

For example, given ["Visit About Us", "Back", "Forward"], return "About Us".

"""

def navigate(commands):
    History = ["Home"]
    puntero = 0
    
    for pages in commands:
        if "Back" in pages:
            if puntero > 0:
                puntero -= 1
        elif "Forward" in pages:
            if puntero < len(History) - 1:
                puntero -= 1
                
        else:
            page = pages[len("Visit "):]
            History = History[:puntero + 1]
            History.append(page)
            puntero += 1
    print(History, puntero)
navigate(["Visit About Us", "Visit Visit Us", "Forward", "Visit Contact Us", "Back"])

