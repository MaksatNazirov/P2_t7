# For the given integer X print 1 if it's positive, -1 if it's negative, or 0 if it's equal
# to zero.Try to use the cascade if-elif-else for it.

#

x = int(input("введите число: "))
if x >= 1:
    print('positive')
elif x <= -1:
    print('negatif')
elif x == 0:
#     print('equal')
# else:
    print('it\'s equal to zero')
