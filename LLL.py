from vector import vector
from gram_schmidt import gram_schmidt
from copy import deepcopy

d = 0.75

def mu(b_i, b_j):
	return b_i.dot_product(b_j) / b_j.dot_product(b_j)

def LLL(l_basis):
	ortho = gram_schmidt(l_basis)

	mu_i = vector(ortho[0])
	k = 1
	n = len(ortho)

	while k <= n:
		for j in range(k - 1, 0, -1):
			proj = mu(ortho[k], ortho[j])
			if abs(proj) > 1/2:
				ortho[k] = ortho[k] - int(round(proj)) * ortho[j]
		if ortho[k].dot_product(ortho[k]) >= d - mu(ortho[k], ortho[k-1]):
			k += 1
		else:
			b[k], b[k-1] = b[k-1], b[k]
			k = max(k - 1, 1)

if __name__ == "__main__":
	l_basis = [Vector((1, -1, 3)),\
		Vector((1, 0, 5)),\
		Vector((1, 2, 6))]
	
	print(LLL(l_basis))

