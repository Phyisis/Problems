from helpers.primes import isPerfectPower, baillie_psw, nextPrime, brentRho
from helpers.integers import iroot, ilog, isqrt, legendre, mod_sqrt, mod_inv
from math import log,gcd,prod

def mpqs(n):
    # When the bound proves insufficiently large, we throw out all our work and start over.
    # TODO: When this happens, get more data, but don't trash what we already have.
    # TODO: Rewrite to get a few more relations before proceeding to the linear algebra.
    # TODO: When we need to increase the bound, what is the optimal increment?
    
    # Special cases: this function poorly handles primes and perfect powers:
    m = isPerfectPower(n)
    if m[1]!=1: return m
    if baillie_psw(n): return n
    
    root_n, root_2n = isqrt(n), isqrt(2*n)
    bound = ilog(n**6, 10)**2  # formula chosen by experiment
    
    while True:
        try:
            primesList, mod_root, log_p, num_prime = [], [], [], 0
            
            # find a number of small primes for which n is a quadratic residue
            p = 2
            while p < bound or num_prime < 3:
                leg = legendre(n%p, p)
                if leg == 1:
                    primesList += [p]
                    mod_root += [mod_sqrt(n, p)]    # the rhs was [int(mod_sqrt(n, p))].  If we get errors, put it back.
                    log_p += [log(p, 10)]
                    num_prime += 1
                elif leg == 0: return p
                p = nextPrime(p)
            
            x_max = len(primesList)*60    # size of the sieve
            
            m_val = (x_max * root_2n) >> 1    # maximum value on the sieved range
            
            # fudging the threshold down a bit makes it easier to find powers of primes as factors
            # as well as partial-partial relationships, but it also makes the smoothness check slower.
            # there's a happy medium somewhere, depending on how efficient the smoothness check is
            thresh = log(m_val, 10) * 0.735
            
            # skip small primes. they contribute very little to the log sum
            # and add a lot of unnecessary entries to the table
            # instead, fudge the threshold down a bit, assuming ~1/4 of them pass
            min_prime = thresh*3
            fudge = sum(log_p[i] for i,p in enumerate(primesList) if p < min_prime)/4
            thresh -= fudge
            
            smooth, used_prime, partial = [], set(), {}
            num_smooth, num_used_prime, num_partial, num_poly, root_A = 0, 0, 0, 0, isqrt(root_2n / x_max)
            
            while num_smooth <= num_used_prime:
                # find an integer value A such that:
                # A is =~ sqrt(2*n) / x_max
                # A is a perfect square
                # sqrt(A) is prime, and n is a quadratic residue mod sqrt(A)
                while True:
                    root_A = nextPrime(root_A)
                    leg = legendre(n, root_A)
                    if leg == 1: break
                    elif leg == 0: return root_A
                
                A = root_A**2
                
                # solve for an adequate B
                # B*B is a quadratic residue mod n, such that B*B-A*C = n
                # this is unsolvable if n is not a quadratic residue mod sqrt(A)
                b = mod_sqrt(n, root_A)
                B = (b + (n - b*b) * mod_inv(b + b, root_A))%A
                C = (B*B - n) / A        # B*B-A*C = n <=> C = (B*B-n)/A
                
                num_poly += 1
                
                # sieve for prime factors
                sums, i = [0.0]*(2*x_max), 0
                for p in primesList:
                    if p < min_prime:
                        i += 1
                        continue
                    logp = log_p[i]
                    inv_A = mod_inv(A, p)
                    # modular root of the quadratic
                    a, b, k = ((mod_root[i] - B) * inv_A)%p, ((p - mod_root[i] - B) * inv_A)%p, 0
                    while k < x_max:
                        if k+a < x_max: sums[k+a] += logp
                        if k+b < x_max: sums[k+b] += logp
                        if k:
                            sums[k-a+x_max] += logp
                            sums[k-b+x_max] += logp
                        k += p
                    i += 1
                
                # check for smooths
                i = 0
                for v in sums:
                    if v > thresh:
                        x, vec, sqr = x_max-i if i > x_max else i, set(), []
                        # because B*B-n = A*C
                        # (A*x+B)^2 - n = A*A*x*x+2*A*B*x + B*B - n
                        #               = A*(A*x*x+2*B*x+C)
                        # gives the congruency
                        # (A*x+B)^2 = A*(A*x*x+2*B*x+C) (mod n)
                        # because A is chosen to be square, it doesn't need to be sieved
                        val = sieve_val = (A*x + 2*B)*x + C
                        if sieve_val < 0: vec, sieve_val = {-1}, -sieve_val
                        
                        for p in primesList:
                            while sieve_val%p == 0:
                                if p in vec: sqr += [p] # track perfect sqr facs to avoid sqrting something huge at the end
                                vec ^= {p}
                                sieve_val = sieve_val // p
                        if sieve_val == 1: # smooth
                            smooth += [(vec, (sqr, (A*x+B), root_A))]
                            used_prime |= vec
                        elif sieve_val in partial:
                            # combine two partials to make a (xor) smooth
                            # that is, every prime factor with an odd power is in our factor base
                            pair_vec, pair_vals = partial[sieve_val]
                            sqr += list(vec & pair_vec) + [sieve_val]
                            vec ^= pair_vec
                            smooth += [(vec, (sqr + pair_vals[0], (A*x+B)*pair_vals[1], root_A*pair_vals[2]))]
                            used_prime |= vec
                            num_partial += 1
                        else: partial[sieve_val] = (vec, (sqr, A*x+B, root_A))      # save partial for later pairing
                    i += 1
                
                num_smooth, num_used_prime = len(smooth), len(used_prime)
            
            used_prime = sorted(list(used_prime))
            
            # set up bit fields for gaussian elimination
            masks, mask, bitfields = [], 1, [0]*num_used_prime
            for vec, vals in smooth:
                masks += [mask]
                i = 0
                for p in used_prime:
                    if p in vec: bitfields[i] |= mask
                    i += 1
                mask <<= 1
            
            # row echelon form
            offset = 0
            null_cols = []
            for col in range(num_smooth):
                pivot = bitfields[col-offset] & masks[col] == 0 # This occasionally throws IndexErrors.
                # TODO: figure out why it throws errors and fix it.
                for row in range(col+1-offset, num_used_prime):
                    if bitfields[row] & masks[col]:
                        if pivot: bitfields[col-offset], bitfields[row], pivot = bitfields[row], bitfields[col-offset], False
                        else: bitfields[row] ^= bitfields[col-offset]
                if pivot:
                    null_cols += [col]
                    offset += 1
            
            # reduced row echelon form
            for row in range(num_used_prime):
                mask = bitfields[row] & -bitfields[row]        # lowest set bit
                for up_row in range(row):
                    if bitfields[up_row] & mask: bitfields[up_row] ^= bitfields[row]
            
            # check for non-trivial congruencies
            # TODO: if none exist, check combinations of null space columns...
            # if _still_ none exist, sieve more values
            for col in null_cols:
                all_vec, (lh, rh, rA) = smooth[col]
                lhs = lh   # sieved values (left hand side)
                rhs = [rh] # sieved values - n (right hand side)
                rAs = [rA] # root_As (cofactor of lhs)
                i = 0
                for field in bitfields:
                    if field & masks[col]:
                        vec, (lh, rh, rA) = smooth[i]
                        lhs += list(all_vec & vec) + lh
                        all_vec ^= vec
                        rhs += [rh]
                        rAs += [rA]
                    i += 1
                factor = gcd(prod(map(int,rAs))*prod(map(int,lhs)) - prod(map(int,rhs)), n)
                if 1 < factor < n: return factor
        except IndexError: print("pass"); pass
        bound *= 1.2

def quadraticSieve(n):    
    if n == 1: return []
    if n%2==0: return [2] + quadraticSieve(n//2)
    if baillie_psw(n): return [n]
    d = mpqs(n)
    return [d] + quadraticSieve(n//d)

