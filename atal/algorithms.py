# Esse metodo recebe uma lista com as matriculas dos alunos
# e retorna essa lista em ordem crescente de matriculas
def retorna_matriculas_decrescente(alist):
    return mergesort(alist)

 
def mergesort(alist):
    if len(alist) <= 4:
        return insertionsort(alist)
 
    middle = len(alist) // 2
    left = alist[:middle]
    right = alist[middle:]
 
    left = mergesort(left)
    right = mergesort(right)
    return list(merge(left, right))


def merge(left, right):
    result = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        # comparison is ">=" to sort in descending order
        if left[left_index] >= right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
 
    if left_index < len(left):
        result.extend(left[left_index:])
    if right_index < len(right):
        result.extend(right[right_index:])

    return result


def insertionsort(alist):
    for i in xrange(1, len(alist)):
        j = i-1 
        element = alist[i]

        # comparison is "<" to sort in descending order
        while (alist[j] < element) and (j >= 0):
           alist[j +1] = alist[j]
           j -= 1

        alist[j +1] = element
    
    return alist
