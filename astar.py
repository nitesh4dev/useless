graph={'A':{'B':6,'F':3},
 'B':{'C':3,'D':2},
 'C':{'E':5,'D':1},
 'D':{'E':8},
 'E':{'J':5},
 'F':{'G':1,'H':7},
 'G':{'I':3},
 'H':{'I':2},
 'I':{'E':5,'J':3},
 'J':{}}
state={'A':10,
 'B':8,
 'C':5,
 'D':7,
 'E':3,
 'F':6,
 'G':5,
 'H':3,
 'I':1,
 'J':0}
def A_star(graph, start_node,end_node,state):
 m={} 
 value=0
 if start_node==end_node:
  return  
 for node,v in graph[start_node].items():
  value=state[node]+v
  m[node]=value
 if(m != {}):
  path[min(m,key=m.get)]=value
  A_star(graph,min(m,key=m.get),end_node,state)
 return path
path={}
path['A']=0
bp=(A_star(graph,'A','J',state))
print(list(bp))
print("Total cost: {}".format(sum(bp.values())))
print(bp)