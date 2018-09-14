from vector import Vector
from fractions import Fraction

def gram_schmidt(*v, normalize=False, fraction = True, DENOM_LIMIT = 100):

    #Check to see if argument is of type list 
    if len(v) == 1 and type(v[0]) in [list, tuple]:
        v = v[0]
    
    if any([type(v_) != Vector for v_ in v]):
        raise TypeError("Argument array must all be of type 'Vector'")

    #By Gram-Schmidt, w_1 = v_1
    w_1 = v[0]
    w_n = w_1
    w_array = [Vector(w_n)]
    
    #Every vector w_1 ... w_n
    
    for n in range(1, len(v)):
        v_n = Vector(v[n])
        w_n = Vector(v_n)

        for j in range(n):
            w_n -= (Vector(v_n).dot_product(Vector(w_array[j]))
                    /(Vector(w_array[j])\
                      .dot_product(Vector(w_array[j]))))*Vector(w_array[j])
        w_array += [w_n]
        
        if fraction == True:
            w_array = [Vector(w).fraction_form(DENOM_LIMIT) for w in w_array]

        if normalize == True:
            w_array = [Vector(w).normalize() for w in w_array]
            
    return w_array

v1 = Vector([1, 0, 0, 1])
v2 = Vector([-1, 0, 2, 1])
v3 = Vector([0, 1, 2, 0])
v4 = Vector([0, 0, -1, 1])

print(gram_schmidt([v1, v2, v3, v4], fraction=True))
