def GenerateSyracusSequence(n):

    values = []
    while n > 1:

        values.append(int(n))

        if n % 2 == 0:
            n = n / 2

        elif n % 2 == 1:
            n = 3 * n + 1

        else:
            n *= 3 * n + 1

    return values


values = GenerateSyracusSequence(11)

print(values)

# if n > 1:
#     max = n
#     count = 1
#
#     while n > 1:
#         if n % 2 == 0:
#             n = n / 2
#
#         elif n % 2 == 1:
#             n = 3 * n + 1
#
#         else:
#             n *= 3 * n + 1
#
#     count = count + 1
#
#     if n > max:
#         max = n
#     print(n)
# print("nombre de termes dans la suite :" + str(count))
# print("valeur max de la suite :" + str(max))
