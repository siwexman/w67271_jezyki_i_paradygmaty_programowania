def knapsack_procedural(items, capacity):
    n = len(items)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            item_weight, item_value = items[i - 1]
            if item_weight <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - item_weight] + item_value)
            else:
                dp[i][w] = dp[i - 1][w]

    result_value = dp[n][capacity]
    result_items = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            result_items.append(items[i - 1])
            w -= items[i - 1][0]

    return result_value, result_items

def knapsack_recursive(items, capacity, n):
    if n == 0 or capacity == 0:
        return 0, []

    item_weight, item_value = items[n - 1]

    if item_weight > capacity:
        return knapsack_recursive(items, capacity, n - 1)
    else:
        without_item_value, without_item_items = knapsack_recursive(items, capacity, n - 1)

        with_item_value, with_item_items = knapsack_recursive(items, capacity - item_weight, n - 1)
        with_item_value += item_value

        if with_item_value > without_item_value:
            return with_item_value, with_item_items + [items[n - 1]]
        else:
            return without_item_value, without_item_items

def knapsack_functional(items, capacity):
    return knapsack_recursive(items, capacity, len(items))

items = [(2, 3), (3, 4), (4, 5), (5, 6)]
capacity = 5

result = knapsack_procedural(items, capacity)
print("Maksymalna wartość (proceduralnie):", result[0])
print("Wybrane przedmioty:", result[1])

result = knapsack_functional(items, capacity)
print("Maksymalna wartość (funkcyjnie):", result[0])
print("Wybrane przedmioty:", result[1])