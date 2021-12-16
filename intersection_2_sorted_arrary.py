"""
Time Complexity: O(max(m, n))
Space Complexity: O(min(m, n))
"""
def find_intersection(input1, input2):

    if not input1 or not input2:
        return []

    commons = []

    if len(input1) > len(input2):
        input1, input2 = input2, input1

    
    for i in input1:
        index = 0
        for indx, j in enumerate(input2[index:], start = index):

            if j > i:
                index = indx
                break

            if i == j:
                commons.append(i)

            index = indx

    return commons


print(find_intersection(input1, input2))