graph={'A':['B','C'],'B':['D','E','F'],'C':['G','H'],'D':['I','J'],'E':['K','L'],'F':['M'],'G':['N','O'],'H':['P','Q'],}

def depth_limited_search(graph,start,goal,limit):
 
 explored=set()

 def recursive_dls(node,depth):
  if depth<0:
   return None
  if node==goal:
   return [node]
  explored.add(node)
  for neighbor in graph[node]:
   if neighbor not in explored:
    path=recursive_dls(neighbor,depth-1)
    if path is not None:
     return[node]+path
  return None
 return recursive_dls(start,limit-1)

print(depth_limited_search(graph,'A','G',3))
print(depth_limited_search(graph,'A','I',4))