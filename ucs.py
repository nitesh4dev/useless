import heapq
def uniform_cost_search(graph,start,goal):
 visited=set()
 queue = [(0,start,[])]
 while queue:
  (cost,node,path)=heapq.heappop(queue)
  if node not in visited:
   visited.add(node)
  path=path+[node]
  if node == goal:
   return (cost,path)
  for (next_node,c) in graph[node]:
   if next_node not in visited:
    heapq.heappush(queue,(cost + c,next_node,path))
 return float("inf")


graph= {
 'A':[('B',1),('C',3),('D',7)],
 'B':[('D',5)],
 'C':[('D',12)]
}
cost,path = uniform_cost_search(graph,'A','D')
print(f"Path: {path},Cost: {cost}")
