# import heapq


# def mystery(list):
#     min_h = []

#     for i, lst in enumerate(list):
#         if lst:
#             heapq.heappush(min_h, (lst[0], i, 0))

#     res_lst = []

#     while min_h:
#         value, list_idx, element_idx = heapq.heappop(min_h)
#         res_lst.append(value)
#         next_idx = element_idx + 1
#         if next_idx < len(list[list_idx]):
#             heapq.heappush(
#                 min_h, (list[list_idx][next_idx], list_idx, next_idx))

#     return res_lst


# res = mystery([[1, 3], [2, 4]])
# print(res)

from collections import deque


def proces_element(elements):
    que = deque()
    stk = []

    for element in elements:
        que.append(element)
    while que:
        item = que.popleft()
        stk.append(item)

        if len(stk) % 2 == 0 and que:
            stk.pop()
    return list(stk)


res = proces_element([1, 2, 3, 4, 5])
print(res)
