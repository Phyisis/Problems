#Find the smallest cube for which exactly five permutations of its digits are cube.
cubes = {"1":[1,1]}

def search():
    i = 1
    while True:
        nextCube = ''.join(sorted(str(i**3)))
        if nextCube in cubes:
            cubes[nextCube][0] += 1
            cubes[nextCube].append(i)
            if cubes[nextCube][0] == 5:
                return cubes[nextCube]
        else:
            cubes[nextCube] = [1,i]
        i += 1

result = search()
print(result)
print(result[1]**3)