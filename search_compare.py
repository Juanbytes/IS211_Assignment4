import time
import random

#It was very difficult for me

def sequential_search(a_list, a_item):


    start = time.time()
    pos = 0
    found = False
    while pos < len(a_list) and not found:
        if a_list[pos] == a_item:
            found = True
        else:
            pos = pos + 1
    end = time.time()
    return found, end - start


def ordered_sequential_search(a_list, a_item):


    start = time.time()
    pos = 0
    found = False
    stop = False
    a_list.sort()

    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == a_item:
            found = True
        else:
            if a_list[pos] > a_item:
                stop = True
            else:
                pos = pos + 1
    end = time.time()
    return found, end - start


def binary_search_iterative(a_list, a_item):


    start = time.time()
    first = 0
    last = len(a_list) - 1
    found = False
    a_list.sort()

    while first <= last and not found:
        midpoint = (first + last) // 2
        if a_list[midpoint] == a_item:
            found = True
        else:
            if a_item < a_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    end = time.time()
    return found, end - start


def binary_search_recursive(a_list, a_item, start=time.time()):

    if len(a_list) == 0:
        end = time.time()
        return False, end - start
    else:
        midpoint = len(a_list) // 2

    if a_list[midpoint] == a_item:
        end = time.time()
        return True, end - start
    else:
        if a_item < a_list[midpoint]:
            end = time.time()
            return binary_search_recursive(a_list[:midpoint], a_item, end - start)
        else:
            end = time.time()
            return binary_search_recursive(a_list[midpoint + 1:], a_item, end - start)


def main():
    list_a = random.sample(range(500), 500) * 100
    list_b = random.sample(range(1000), 1000) * 100
    list_c = random.sample(range(10000), 10000) * 100
    list_a.sort()
    list_b.sort()
    list_c.sort()

    sequential_search(list_a, -1)
    seqres1 = sequential_search(list_a, -1)[1]
    seqres2 = sequential_search(list_b, -1)[1]
    seqres3 = sequential_search(list_c, -1)[1]
    seqlist = [seqres1, seqres2, seqres3]
    sum1 = sum(seqlist)
    avg1 = sum1 / 3

    ordered_sequential_search(list_a, -1)
    ordseq1 = ordered_sequential_search(list_a, -1)[1]
    ordseq2 = ordered_sequential_search(list_b, -1)[1]
    ordseq3 = ordered_sequential_search(list_c, -1)[1]
    ordseqlist = [ordseq1, ordseq2, ordseq3]
    sum2 = sum(ordseqlist)
    avg2 = sum2 / 3

    binary_search_iterative(list_a, -1)
    biniter1 = binary_search_iterative(list_a, -1)[1]
    biniter2 = binary_search_iterative(list_b, -1)[1]
    biniter3 = binary_search_iterative(list_c, -1)[1]
    biniterlist = [biniter1, biniter2, biniter3]
    sum3 = sum(biniterlist)
    avg3 = sum3 / 3

    binary_search_recursive(list_a, -1)
    binrec1 = binary_search_recursive(list_a, -1)[1]
    binrec2 = binary_search_recursive(list_b, -1)[1]
    binrec3 = binary_search_recursive(list_c, -1)[1]
    binreclist = [binrec1, binrec2, binrec3]
    sum4 = sum(binreclist)
    avg4 = sum4 / 3

    print("Sequential search took {:.7f}".format(avg1), "seconds to run, on average")
    print("Ordered sequential search took {:.7f}".format(avg2), "seconds to run, on average")
    print("Binary iterative search took {:.7f}".format(avg3), "seconds to run, on average")
    print("Binary recursive search took {:.7f}".format(avg4), "seconds to run, on average")


if __name__ == "__main__":
    main()
