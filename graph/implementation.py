def add_edge(mat, i, j):
  
    # Add an edge between two vertices
    mat[i][j] = 1  # Graph is 
    mat[j][i] = 1  # Undirected

def display_matrix(mat):
  
    # Display the adjacency matrix
    for row in mat:
        print(" ".join(map(str, row)))  

# Main function to run the program
if __name__ == "__main__":
    V = 4  # Number of vertices
    mat = [[0] * V for _ in range(V)]  
    print("mat", mat)

    # Add edges to the graph
    add_edge(mat, 0, 1)
    add_edge(mat, 0, 2)
    add_edge(mat, 1, 2)
    add_edge(mat, 2, 3)

    # Optionally, initialize matrix directly
    """
    mat = [
        [0, 1, 0, 0],
        [1, 0, 1, 0],
        [0, 1, 0, 1],
        [0, 0, 1, 0]
    ]
    """

    # Display adjacency matrix
    print("Adjacency Matrix:")
    display_matrix(mat)


from collections import deque

# 1. Графыг тодорхойлох (Dictionary ашиглан)
# 'A' орой 'B' ба 'C'-тэй холбоотой гэх мэт
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

def bfs(graph, start_node):
    visited = set()          # Зочилсон оройнуудыг хадгалах олонлог
    queue = deque([start_node]) # Дараалал (Queue) үүсгэж, эхлэх оройг хийх
    visited.add(start_node)
    
    print(f"BFS эхэллээ (Эхлэл: {start_node}):")
    
    while queue:
        # Дарааллын урд талын оройг авна
        current_node = queue.popleft()
        print(current_node, end=" -> ")
        
        # Тухайн оройн бүх хөршүүдийг шалгах
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    print("Дууслаа")

# Алгоритмыг ажиллуулах
bfs(graph, 'A')

# 1. Графыг тодорхойлох (Dictionary)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Зочилсон оройнуудыг бүртгэх олонлог
visited = set()

def dfs(visited, graph, node):
    if node not in visited:
        print(node, end=" ") # Орой дээр очсоноо хэвлэх
        visited.add(node)    # Зочилсон гэж тэмдэглэх
        
        # Тухайн оройн бүх хөршүүд рүү гүн рүү нь орж хайх
        for neighbor in graph[node]:
            dfs(visited, graph, neighbor)

print("DFS хайлтын дараалал:")
dfs(visited, graph, 'A')

import heapq

# 1. Жинтэй графыг тодорхойлох
# Орой бүрийн хөршүүд болон тэдгээрийн хоорондох зай (жин)
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 1, 'D': 5},
    'C': {'A': 2, 'B': 1, 'D': 8, 'E': 10},
    'D': {'B': 5, 'C': 8, 'E': 2, 'F': 6},
    'E': {'C': 10, 'D': 2, 'F': 3},
    'F': {'D': 6, 'E': 3}
}

def dijkstra(graph, start):
    # Орой бүр хүртэлх хамгийн богино зайг хадгалах (эхлээд хязгааргүй гэж үзнэ)
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    
    # Priority queue: (зай, орой)
    priority_queue = [(0, start)]
    
    while priority_queue:
        # Хамгийн бага зайтай оройг сонгож авах
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # Хэрэв олсон зам нь өмнөхөөсөө их бол алгасна
        if current_distance > distances[current_node]:
            continue
            
        # Хөрш оройнуудыг шалгах
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            # Хэрэв шинэ зам нь өмнөхөөс богино байвал шинэчилнэ
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
                
    return distances

# Алгоритмыг ажиллуулах
start_node = 'A'
result = dijkstra(graph, start_node)

print(f"'{start_node}' оройноос бусад орой хүртэлх хамгийн богино зайнүүд:")
for node, dist in result.items():
    print(f"{node} хүртэл: {dist}")