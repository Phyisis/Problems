n_lim = int(1e7)
phi = [i for i in range(n_lim+2)]

for p in phi[2:]:
    if phi[p] == p:
        phi[p] = p - 1
        for i in range(2 * p, n_lim + 1, p):
            phi[i] = (phi[i] // p) * (p - 1)

n_min = 2
for i in range(2, n_lim + 1):
    if i / phi[i] < n_min / phi[n_min]:
        if sorted(str(i)) == sorted(str(phi[i])):
            n_min = i

print(n_min) 