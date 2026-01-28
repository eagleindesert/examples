import heapq


def main():
    heap = []

    heapq.heappush(heap, 50)
    heapq.heappush(heap, 10)
    heapq.heappush(heap, 20)

    print(heapq.heappop(heap))
    print(heapq.heappop(heap))
    print(heapq.heappop(heap))

    print("##############################")
    #############################################################
    
    heapq.heappush(heap, (-50, 50))
    heapq.heappush(heap, (-10, 10))
    heapq.heappush(heap, (-20, 20))

    print(heapq.heappop(heap)[1])
    print(heapq.heappop(heap)[1])
    print(heapq.heappop(heap)[1])


main()
