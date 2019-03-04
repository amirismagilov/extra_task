def normalize(data, n):
    for i in range(n):
        ind_max = data.index(max(data))
        del data[ind_max]
        ind_min = data.index(min(data))
        del data[ind_min]

    return data
