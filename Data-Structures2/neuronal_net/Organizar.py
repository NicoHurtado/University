def quickSort(data):
    if len(data) <= 1:
        return data
    pivote = data[len(data)//2]
    greaterData = [item for item in data if item > pivote]
    equalData = [item for item in data if item == pivote]
    lowerData = [item for item in data if item < pivote]
    return  quickSort(lowerData) + equalData + quickSort(greaterData)

def OrdenarEstados(list):
    SortedList = quickSort(list)
    return SortedList

