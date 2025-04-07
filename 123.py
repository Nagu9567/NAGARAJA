from collections import deque
def bfs(graph,start):
  queue=deque([start])
  visited=set()
  visited.add(start)
  print("Starting BFS from node:",start)
  print("step-by-step BFS:")
  while queue:
   node=queue.popleft()
   print(f"Visiting node:{node}")
   neighbors=graph.get(node,[])
   print(f"Neighbors of node {node}: {neighbors}")
   for neighbor in neighbors:
     if neighbor-+ not in visited:
        print(f"Queueing neighbors: {neighbor}")
        queue.append(neighbor)
        visited.add(neighbor)
     print("Queue state:",list(queue))
     print("Visited nodes:",list(visited))
     print("_"*40)
graph={
    'A':['B','C'],
    'B':['A','D','E'],
    'C':['A','F'],
    'D':['B'],
    'E':['B','F'],
    'F':['C','E']
    }
bfs(graph,'A')