def job_scheduling(jobs):
    # sort the jobs in decreasing order of their profits
    jobs = sorted(jobs, key=lambda x: x[2], reverse=True)
    
    # create a list to keep track of the time slots
    slots = [-1] * len(jobs)
    
    # loop through the jobs and assign them to time slots
    for i in range(len(jobs)):
        # loop through the time slots in reverse order
        for j in range(min(jobs[i][1]-1, len(jobs)-1), -1, -1):
            # if the time slot is empty, assign the job to that slot
            if slots[j] == -1:
                slots[j] = i
                break
                
    # create a list of the scheduled jobs and their profits
    scheduled_jobs = []
    for i in range(len(slots)):
        if slots[i] != -1:
            scheduled_jobs.append((jobs[slots[i]][0], jobs[slots[i]][2]))
            
    return scheduled_jobs

# example usage
jobs = [(1, 4, 20), (2, 1, 10), (3, 1, 40), (4, 1, 30)]
scheduled_jobs = job_scheduling(jobs)
print(scheduled_jobs)
