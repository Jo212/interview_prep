candies = [2,3,5,1,3]
extraCandies = 3
max_candy = max(candies)
result = []
for ind,candy in enumerate(candies):
    if candies[ind] + extraCandies >= max_candy:
        result.insert(ind, True)
    else:
        result.insert(ind, False)
print(result)