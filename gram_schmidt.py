from vector import vector
from fractions import Fraction
from copy import deepcopy

def gram_schmidt(*v, normalize=False, fraction=False, DENOM_LIMIT=100):

    #Check to see if argument is of type list 
    if len(v) == 1 and type(v[0]) in [list, tuple]:
        v = v[0]
    
    if any([type(v_) != vector for v_ in v]):
        raise TypeError("Argument array must all be of type 'Vector'")

    #By Gram-Schmidt, w_1 = v_1
    w_1 = v[0]
    w_n = w_1
    w_array = [deepcopy(vector(w_n))]
    
    #Every vector w_1 ... w_n
    for n in range(1, len(v)):
        v_n = vector(v[n])
        w_n = vector(v_n)

        for j in range(n):
            w_j = deepcopy(w_array[j])
            if not any(w_j):
                continue
            w_n -= v_n.dot_product(w_j) / w_j.dot_product(w_j)*w_j
        
        w_array += [w_n]
        
    if fraction == True:
        w_array = [vector(w).fraction_form(DENOM_LIMIT) for w in w_array]

    if normalize == True:
        w_array = [vector(w).normalize() for w in w_array]
            
    return w_array

if __name__ == "__main__":
    v1 = vector([0, 0, 4])
    v2 = vector([0, 0, 1])
    v3 = vector([1, 1, 3])
    print(gram_schmidt([v1, v2, v3]))
