# define the job scheduling function
def job_scheduling(jobs):
    jobs = sorted(jobs, key=lambda x: x[2], reverse=True)
    slots = [-1] * len(jobs)
    for i in range(len(jobs)):
        for j in range(min(jobs[i][1]-1, len(jobs)-1), -1, -1):
            if slots[j] == -1:
                slots[j] = i
                break
    scheduled_jobs = []
    for i in range(len(slots)):
        if slots[i] != -1:
            scheduled_jobs.append((jobs[slots[i]][0], jobs[slots[i]][2]))
    return scheduled_jobs
jobs = [
    (1, 3, 35),
    (2, 4, 25),
    (3, 2, 20),
    (4, 3, 15),
    (5, 1, 12),
]
scheduled_jobs = job_scheduling(jobs)
print(scheduled_jobs)
