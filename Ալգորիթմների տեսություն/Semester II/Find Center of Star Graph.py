def find(edges):
    cheched = []
    for edge in edges:
        for centre in edge:
            if centre not in cheched:
                cheched.append(centre)
            else:
                return centre

print(f"ex 1 =  {find([[1,2],[2,3],[4,2]])}")
print(f"ex 2 = {find([[1,2],[5,1],[1,3],[1,4]])}")

