def calc_hypo(a, b):
    hypo = (a**2 + b**2)**0.5 #NB: not (a**0.5 + b**0.5), these are not equivalent
    return hypo
print calc_hypo(3, 4)

#here we are defining a function called calc_hypo to calculate the value of the hypotenuse via Pythagoras' theorem such that it can be applied to different sets of input values 