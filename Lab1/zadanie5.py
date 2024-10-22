from functools import reduce

def activity_selection_procedural(tasks):
    tasks.sort(key=lambda x: x[1])

    selected_tasks = []
    total_reward = 0

    last_end_time = 0

    for task in tasks:
        start, end, reward = task
        if start >= last_end_time:
            selected_tasks.append(task)
            total_reward += reward
            last_end_time = end

    return total_reward, selected_tasks



def activity_selection_functional(tasks):
    sorted_tasks = sorted(tasks, key=lambda x: x[1])

    def select_task(acc, task):
        selected_tasks, last_end_time, total_reward = acc
        start, end, reward = task
        if start >= last_end_time:
            return (selected_tasks + [task], end, total_reward + reward)
        else:
            return acc

    result = reduce(select_task, sorted_tasks, ([], 0, 0))

    selected_tasks, _, total_reward = result
    return total_reward, selected_tasks

tasks = [(1, 3, 50), (2, 5, 20), (4, 6, 30), (6, 8, 25), (5, 7, 60)]
result = activity_selection_procedural(tasks)
print("Maksymalna możliwa nagroda (proceduralnie):", result[0])
print("Optymalny harmonogram zadań:", result[1])

result = activity_selection_functional(tasks)
print("Maksymalna możliwa nagroda (funkcyjnie):", result[0])
print("Optymalny harmonogram zadań:", result[1])
