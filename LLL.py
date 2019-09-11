from vector import vector
from gram_schmidt import gram_schmidt
from copy import deepcopy

d = 0.75

def mu(b_i, b_j):
	return b_i.dot_product(b_j) / b_j.dot_product(b_j) if b_j.dot_product(b_j) != 0 else 0

def LLL(l_basis):

	ortho = [vector(i) for i in gram_schmidt(l_basis)]

	k = 1
	n = len(ortho)

	while k < n:
		for j in range(k - 1, -1, -1):
			proj = mu(l_basis[k], ortho[j])
			if abs(proj) > 1/2:
				l_basis[k] = l_basis[k] - l_basis[j] * round(proj)
				ortho = gram_schmidt(l_basis)
		
		if ortho[k].dot_product(ortho[k]) >= (d - mu(l_basis[k], ortho[k-1])**2)* (ortho[k-1].dot_product(ortho[k-1])):
			k += 1

		else:
			l_basis[k], l_basis[k-1] = l_basis[k-1], l_basis[k]
			ortho = gram_schmidt(l_basis)
			k = max(k - 1, 1)

	return l_basis

if __name__ == "__main__":
	l_basis = [vector((3, 4, 5)),\
		vector((6, 7, 8)),\
		vector((9, 10, 11))]
	
	print(LLL(l_basis))

