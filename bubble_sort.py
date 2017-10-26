'''
page20
'''

def bubble_sort(l, n):
    for i in range(n-1):
        for j in range(n-1):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]

if __name__ == "__main__":
    l = [23,1,3,2,15]
    bubble_sort(l, len(l))
    print(l)