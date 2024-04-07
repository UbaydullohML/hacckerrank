n = int(input())
country_set = set()
for _ in range(n):
    countryn = input()
    country_set.add(countryn)

print(len(country_set))


# Input Format
# The first line contains an integer N, the total number of country stamps.
# The next N lines contains the name of the country where the stamp is from.

# Test Input:
# 7
# UK
# Bangladesh
# USA
# France
# Canada
# UK
# France 

# Test Output:
# 5
