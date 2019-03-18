from vector import vector
from gram_schmidt import gram_schmidt
from copy import deepcopy

d = 0.25

def LLL(l_basis):
	ortho = gram_schmidt(l_basis)

	mu_i = vector(ortho[0])
	k = 1
	n = len(ortho)

	while k <= n:
		for j in range(k - 1, 0, -1):
			