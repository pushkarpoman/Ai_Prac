import heapq

V = int(input("Enter number of vertices"))
E = int(input("Enter number of edges"))
graph = {i : [] for i in range(V)}

print("Enter each edge in format U V W")
for _ in range(E):
    u,v,w = map(int, input().split())
    graph[u].append((v,w))
    graph[v].append((u,w))

visited = [False]*V
min_heap = [(0,0)]
total_cost = 0 

print("Edge:Cost")
while min_heap:
    cost,current = heapq.heappop(min_heap)
    if visited[current]:
        continue
    visited[current] = True
    total_cost+=cost
    for v, weight in graph[current]:
        if not visited[v]:
            heapq.heappush(min_heap,(weight,v))
print(total_cost)

