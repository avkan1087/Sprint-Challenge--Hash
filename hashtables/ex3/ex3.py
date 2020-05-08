def intersection(arrays):

    items_count = {}
    result = []

    for i, num_list in enumerate(arrays):
        for y in num_list:
            if items_count.get(y) != None and i > 0:
                items_count[y] = items_count[y] + 1
            elif items_count.get(y) is None and i == 0:
                items_count[y] = 1
            else:
                continue

    for num in items_count:
        if items_count[num] == len(arrays):
            result.append(num)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
