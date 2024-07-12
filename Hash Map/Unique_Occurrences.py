def uniqueOccurrences(arr):
    count = {}
    
    for num in arr:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
            
    occurrence_set = set(count.values())
    return len(occurrence_set) == len(count.values())
    
print(uniqueOccurrences([1,2,2,1,1,3]))
print(uniqueOccurrences([1,2]))
    