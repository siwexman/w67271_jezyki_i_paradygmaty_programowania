from functools import reduce

def procedural_scheduling(tasks):
    tasks.sort(key=lambda x: x[0])

    total_wait_time = 0
    total_reward = 0
    current_time = 0
    
    for time, reward in tasks:
        current_time += time
        total_wait_time += current_time
        total_reward += reward
    
    return tasks, total_wait_time, total_reward

def functional_scheduling(tasks):
    sorted_tasks = sorted(tasks, key=lambda x: x[0])

    completion_times = list(map(lambda x: sum([task[0] for task in sorted_tasks[:x+1]]), range(len(sorted_tasks))))
    
    total_wait_time = reduce(lambda acc, x: acc + x, completion_times, 0)
    
    total_reward = reduce(lambda acc, task: acc + task[1], sorted_tasks, 0)
    
    return sorted_tasks, total_wait_time, total_reward

tasks = [(3, 50), (1, 30), (2, 40), (4, 20)]
result = procedural_scheduling(tasks)
print("Optymalna kolejność zadań (proceduralnie):", result[0])
print("Całkowity czas oczekiwania:", result[1])
print("Całkowita nagroda:", result[2])

result = functional_scheduling(tasks)
print("Optymalna kolejność zadań (funkcyjnie):", result[0])
print("Całkowity czas oczekiwania:", result[1])
print("Całkowita nagroda:", result[2])