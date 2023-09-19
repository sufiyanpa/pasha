def binarysearch(a,key):
    low=0
    high=len(a)-1
    while low<=high:
        mid=(high+low)//2
        if a[mid]==key:
            return mid
        elif key<a[mid]:
            high=mid-1
        else:
            low=mid+1
    return -1
a=[34,55,67,21,3]
print("the elements are:",a)
k=int(input("enter the element to search:-"))
r=binarysearch(a,k)
if r==-1:
    print("search unsuccessful")
else:
    print("search successful key found at key location",r+1)
    