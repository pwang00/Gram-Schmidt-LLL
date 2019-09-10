from vector import vector
from gram_schmidt import gram_schmidt
from copy import deepcopy

d = 0.25

def mu(b_i, b_j):
	return b_i.dot_product(b_j) / b_j.dot_product(b_j)

def LLL(l_basis):
	ortho = gram_schmidt(l_basis)

	mu_i = vector(ortho[0])
	k = 1
	n = len(ortho)

	while k <= n:
		for j in range(k - 1, 0, -1):
			b_j, b_k = ortho[j], ortho[k]
