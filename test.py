def sums(arr,target):
    arr.sort()
    res = []

    def ss(ar, tmp):
        if sum(tmp)>target:
            return
        if sum(tmp) == target:
            res.append(tmp)
            return
        for i in range(len(ar)):
            if i>0 and ar[i] == ar[i-1]:
                continue
            ss(ar[i+1:], tmp + [ar[i]])
    ss(arr, [])
    return res


def merge(arr):

    res = []
    n = len(arr)

    def xx(ar, tmp):
        if len(tmp) == n:
            res.append(tmp)
            return
        for i in range(len(ar)):
            xx(ar[:i]+ar[i+1:], tmp+[ar[i]])
    xx(arr, [])
    return res


y = merge([1, 2, 3])
print(y)

x = sums([1,10,2,4,5,6,7],8)
print(x)

