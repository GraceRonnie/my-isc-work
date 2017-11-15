def calc_hypo(a, b):
    if type(a) not in (int, float) or type(b) not in (int, float): #here we're stating the values for this function to work have to be numbers, they cannot be strings of numbers of letters so show bad argument instead of error
        print "Bad argument"
        return False  #therefore do not return a value
    if a <= 0 or b <= 0: #the valuesx also must be greater than 0, you cannot have a negative length of a triangle side, this can be applied to many mathematical arguments 
        print "Bad argument"
        return False
    hypo = (a**2 + b**2)**0.5
    return hypo  #need to tell it to print

calc_hypo(0, -2)
calc_hypo("hi", "bye")