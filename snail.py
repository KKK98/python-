import numpy as np

am = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
ab = np.array([[1,2,3],[4,5,6],[7,8,9]])
a = np.array([[1,2],[3,4]])
c = np.array([])
k = len(a)


if k%2 == 0:
    for i in range(0,k-2):
        c = np.hstack((c,snail_map[i,i:k-i-1],snail_map[i:k-i-1,k-i-1],snail_map[k-i-1,-i-1:i-k:-1],snail_map[-i-1:i-k:-1,i]))
        #np.concatenate((snail_map[i,i:k-i-1],snail_map[i:k-i-1,k-i-1],snail_map[k-i-1,-i-1:i-k:-1],snail_map[-i-1:i-k:-1,i]),axis = 0)
        i = i + 1
if k%2 == 1:
    for i in range(0,k-2):
        c = np.hstack((c,snail_map[i,i:k-i-1],snail_map[i:k-i-1,k-i-1],snail_map[k-i-1,-i-1:i-k:-1],snail_map[-i-1:i-k:-1,i]))
        i = i + 1

    m = int((k-1)/2)
    c = np.append(c,snail_map[m,m])

print(c)
