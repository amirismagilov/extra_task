def normalize(data, n):
    for i in range(n):
        ind_max = data.index(max(data))
        del data[ind_max]
        ind_min = data.index(min(data))
        del data[ind_min]
    return data

def uniq(data):
    result = []
    for element in data:
        if element not in result:
            result.append(element)
        else:
            ind = result.index(element)
            del result[ind]
    return result
