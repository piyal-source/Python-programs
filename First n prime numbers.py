n = 12
num_arr = [_ for _ in range(2,n+1)]
visited = [0]*(n-1)

prime_index = 0
while True:
    for i in range(num_arr[prime_index]*num_arr[prime_index],n+1):
        if i % num_arr[prime_index] == 0:
            visited[num_arr.index(i)] = 1
    if visited[prime_index+1:n+1].count(0)==0:
        break
    else:
        prime_index = visited.index(0,prime_index+1,n-1)
# print(f'{num_arr}\n{visited}\n')
for i in range(n-1):
    if visited[i]==0:
        print(num_arr[i], end=" ")
