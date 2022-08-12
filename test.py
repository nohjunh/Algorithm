

max_value= 100000
graph_matrix=[0 for _ in range(max_value+1)]
graph_matrix[N]= 1 # 수빈이의 현재 위치 check
ans_list=[]

def BFS_adj_list(graph_matrix, N):
    queue = deque()
    queue.append( N )
    while queue:
        N = queue.popleft()

        # 방향을 검사
        if N==K: #수빈이가 동생 위치로 갔다면
            global ans_list
            ans_list.append(graph_matrix[N])
        
        if (0<= N+1 <= max_value) and (graph_matrix[N+1]==0):
            graph_matrix[N+1]= graph_matrix[N]+1
            queue.append( N+1 )
        if (0<= N-1 <= max_value) and (graph_matrix[N-1]==0):
            graph_matrix[N-1]= graph_matrix[N]+1 
            queue.append( N-1 )
        if (0<= 2*N <= max_value) and (graph_matrix[2*N]==0):
            graph_matrix[2*N]= graph_matrix[N]+1 
            queue.append( 2*N )

BFS_adj_list(graph_matrix, N)
print(min(ans_list)-1)