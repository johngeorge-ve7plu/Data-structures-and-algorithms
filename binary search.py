def binary_search(l, target):
  start = 0
  end = len(l) - 1
  while start <= end:
    mid = (start + end) // 2
    if l[mid] == target:
      return mid
    elif l[mid] < target:
      start = mid + 1
    else:
      end = mid - 1
    
  return -1
  
  
l = list(map(int,input().split()))
target = int(input())
print(binary_search(l,target))