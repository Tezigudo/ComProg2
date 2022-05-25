# # def wrapper(func):
# #     def inner(*args):
# #         print('Hi Inner')
# #         func(*args)
# #     return inner


# # @wrapper
# # def banana(a):
# #     print(f'Yo {a}')


# # banana(6)

# # wrapper(banana)(6)

# # '''
# # f(g(x))
# # f(h(x))
# # f(j(x))
# # ...

# # @f
# # def g(x):
# # ...

# # @f
# # def h(x):
# # ...


# # '''

# def tracer(func):
#     def nothing(*args):
#         if len(args) == 1:
#             print(f'{func.__name__}{args}'.replace(',', ''))
#         else:
#             print(f'{func.__name__}{args}')
#         result = func(*args)
#         print(result)
#         return result

#     return nothing


# @tracer
# def fac(n):
#     if n <= 1:
#         return 1
#     return n*fac(n-1)


# # @tracer
# # def banana(a, b):
# #     return b, a

# print('4! is', fac(4))

# # print(banana(4, 8))
