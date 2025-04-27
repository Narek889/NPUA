def find_next (edges,num_vertices, index, from_node):
    max_weight = [0,0]
    for check in range(index, num_vertices):
        if edges[check][0] != from_node:
            for weight in range(1, edges[index][2]):
                if edges[check][2] > max_weight[0]:
                    max_weight[0] = edges[check][2]
                    max_weight[1] = index
    return max_weight

def jump(edges, num_vertices, start):
    distances = [float('inf')] * num_vertices
    distances[start] = 0

    jump_check = None
    for _ in range(num_vertices - 1):
        for index, (from_node, to_node, weight) in enumerate(edges):
            # if jump_check == None
            #     jump_check = from_node
            max_weight = find_next(edges, num_vertices,index, from_node)
            index = max_weight[1]
            from_node = max_weight[0]
            distances.append(index)
    return distances


nums = [2, 3, 1, 1, 4,5]

#region list_to_graph

edges = [] # from_node, to_node, weight
for i in range(len(nums)):
    print(f'i = {i}')
    for j in range(1, len(nums)-i):
        if j <= nums[i]:
            print(f'j = {j}')
            edges.append((i, i+j, j))

print(edges)

#endregion list_to_graph

start = 0
print(f'ex_1 = {jump(edges, len(nums), start)}')