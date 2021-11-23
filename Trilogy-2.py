#Given an array arr[] of size N and two integers M and K, the task is to find the array element at the Kth index after performing following M operations on the given array.

#In a single operation, a new array is formed whose elements have the Bitwise XOR values of the adjacent elements of the current array.

def kthXOR(M,N,K,arr):
    if N<0 or M>N:
        return -1
    if K>=N-M or K<0:
        return -1
    for _ in range(M):   #For performing iterations
        temp=[]
        for i in range(len(arr)-1):
            value=arr[i]^arr[i+1]
            temp.append(value)
        arr=temp[:]
    ans=arr[K]
    return ans

if __name__ == '__main__':
    M=2
    N=3
    K=0
    arr = [1, 2, 1]
 
    print(kthXOR(M,N,K,arr))

    