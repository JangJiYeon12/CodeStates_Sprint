def selectionSort(li) :
    for i in range(len(li) - 1):
        max_idx = i
        for j in range(i + 1, len(li)):
            if li[j] > li[max_idx]:
                max_idx = j
        li[i], li[max_idx] = li[max_idx], li[i]

    return li


def bubbleSort(li) :
    for i in range(len(li) - 1, 0, -1):
        for j in range(i):
            if li[j] < li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]
    return li


def insertionSort(li):
    for end in range(1, len(li)):
        for i in range(end, 0, -1):
            if li[i - 1] < li[i]:
                li[i - 1], li[i] = li[i], li[i - 1]

    return li