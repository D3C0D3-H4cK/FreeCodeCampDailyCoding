def golf_score(par, strokes):
    if strokes == 1:
        print('Hole in one!')
    elif par == strokes:
        print('Par')
    elif strokes - par == 2 and strokes > par:
        print('Double bogey')
    elif strokes - par == 1 and par < strokes:
        print('Bogey')
    elif par - strokes == 2 and strokes < par:
        print('Eagle')
    elif par - strokes == 1 and par > strokes:
        print('Birdie')
    
golf_score(4, 3)