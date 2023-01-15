from collections import defaultdict, deque
def bfs_and_node_count(del_line, n, wire_dict): 
    count = 1  # 연결된 노드 수
    visited = [False] * (n + 1)  # 방문여부 체크
    visited[del_line[0]] = True  # 시작 노드 방문 처리
    queue = deque([del_line[0]])

    while queue:  # bfs 수행
        curr = queue.popleft()
        for i in wire_dict[curr]:  # curr 노드와 연결된 노드에 대해서
            if visited[i] or i == del_line[1]:  
                continue
            count += 1
            queue.append(i)
            visited[i] = True
    return count


def solution(n, wires):
    answer = 1000
    data = defaultdict(set)  # 각 노드별 연결된 노드 정보
    for a, b in wires:
        data[a].add(b)
        data[b].add(a)

    for w in wires:
        # 해당 와이어를 끊었을 때 한쪽 영역의 노드 수 구하기
        temp = bfs_and_node_count(w, n, data)

        answer = min(answer, abs(n - temp - temp))
    return answer