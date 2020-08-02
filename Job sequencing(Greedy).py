profits = [10,15, 20, 5, 1]
deadlines = [1, 2, 2, 3, 3]
num_jobs = len(profits)
total_profit = 0
jobs = []
d = dict()
for i in range(max(deadlines)):
    jobs.append(None)
rem = len(jobs)
for i in range(num_jobs):
    d[profits[i]] = deadlines[i]
profits.sort(reverse=True)
for i in range(num_jobs):
    if rem > 0:
        for j in range(d[profits[i]]-1, -1, -1):
            if jobs[j] is None:
                jobs[j] = i+1
                rem -= 1
                total_profit += profits[i]
                break
    else:
        break
print(jobs)
print(total_profit)