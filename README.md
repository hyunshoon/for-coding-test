# for-coding-test




## 코딩 테스트 플랫폼
- 백준, 프로그래머스, 리트코드
- Softeer: 현대그룹 코딩테스트. input을 직접 해야 하고 여기서 시간 단축을 위해 input()이 아닌 sys.stdin.readline()으로 입력 받아야 한다.
- 프로그래머스: 에러 발생 시 출력 내용을 볼 수 없어서 디버깅이 번거로움. IDE 사용 가능 한 시험에는 필수적으로 사용하고 불가능한 경우에는 구현하며 주기적으로 print를 찍어 디버깅 시간을 줄여주자.

## 코딩 테스트 전략

![image](https://user-images.githubusercontent.com/28949162/216966360-01f4c02b-9c5e-4c60-84e9-9e37a631a0d4.png)

0. 주석을 쓰면서 하자.

Point, Caution, Solution 으로 분리하여 문제를 체계적으로 푸는게 경험상 가장 빠르고 정확하다.

1. 문제 풀이 컨셉을 정한 뒤 구현하기 전 여러 케이스를 대입해보고 문제가 없으면 구현한다.

구현부터 하고 나중에 잘못된 방법인걸 깨달으면 시간 소모가 크다.

2. 예외 처리 리스트

- 입력값이 0, null 인 경우
- 경계 값 항상 체크

3. 시간과 메모리는 트레이드 오프 관계이다

시간초과가 발생하는 경우, 메모리를 사용(DP, Stack, Queue, Dictionary 등 자료구조를 먼저 떠올리자)하여 타계할 생각을 가지자! 

## 다루는 알고리즘
- 구현
- 정렬
- 완전탐색
- BFS, DFS
- 그리디
- DP
- 슬라이딩 윈도우
- 최단 경로
- 문자열
- 이진 탐색

### 바이너리 서치

정렬된 배열에서 타겟을 서치하는 O(logN)시간 복잡도를 가지는 검색 알고리즘.

#### 파라메트릭 서치: 최적화 문제를 결정 문제로 바꾸어 해결하는 기법

예시) 특정한 조건을 만족하는 가장 알맞은 값을 빠르게 찾는 최적화 문제

대표문제
- Softeer: 코딩테스트 세트

### set 자료형

방문처리 같은 경우 리스트를 만들어 리스트안에 원소가 있는지 판별하는 경우가 있다.
리스트인 경우 O(N)을 가진다.
이를 줄이기 위해 set() 자료구조를 사용하면 O(1)만에 찾을 수 있다. set은 해시테이블을 사용하기 때문이다.

### defaultdict 자료형
```python
from collections import defaultdict
my_dict = defaultdict(list)  #list 자료형으로 딕셔너리를 초기화
```
defaultdict를 사용하면 키 값을 초기화하지 않았을 때 디폴트 자료형으로 초기화 하는 것.
위와 같이 사용하면 my_dict['ex']를 초기화 하지 않았을 때 디폴트로 빈 리스트를 가진다.

### BFS: 큐로 구현

1. 탐색 시작 노드를 큐에 삽입하고 방문 처리
2. 큐에서 노드를 꺼낸 뒤에 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문처리

방문기준: 번호가 낮은 순서

#### 구현 예시
임의의 그래프에서 특정 지점과 하나의 트리 형태로 연결되어있는 노드 수를 구하는 문제라고 가정
중복 탐색을 막기 위한 방문 visit 자료형 구현 해야 함(상황에 따라 자료형은 달라 질 수 있다)
graph = {1:[2,3], 2:[1,4], 3:[1], 4:[2]}

```python
from collections import deque
def BFS(graph):
  queue = deque()
  queue.append(graph[0][0]) #출발지를 임의로 지정
  visit = set()
  while queue:
    node = queue.popleft()
    for next_node in graph[node]:
      if next_node in visit: continue
      else:
        visit.add(next_node)
        queue.append(next_node)
  return len(visit)
```

### DFS: 깊은 부분을 우선적으로 탐색하는 알고리즘

스택 혹은 재귀를 이용하여 구체적인 동작 과정은 다음과 같다

1. 탐색 시작 노드를 스택에 삽입하고 방문 처리
2. 스택의 최상단 노드에 방문하지 않은 인접한 노드가 하나라도 있으면 그 노드를 스택에 넣고 방문처리. 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼낸다.
3. 더 이상 2번의 과정을 수행할 수 없을 때까지 반복.

### 우선순위 큐: 우선순위가 가장 높은 값을 가장 먼저 삭제하는 자료구조

우선순위에 따라 데이터를 처리하고 싶을 때 사용

우선순위 큐를 구현하는 방법

1. heap으로 구현하면 삽입과 삭제 시간의 시간복잡도를 O(logN) 으로 만들 수 있다.
2. list로 구현하면 삽입은 O(1) 이지만 삭제 시 O(N)이 걸린다.

#### Heap의 특징

- 완전 이진 트리 자료구조
- 루트 노드를 제거한다.
- 최소 힙
  - 루트 노드가 가장 작은 값을 가진다 -> 가장 작은 값이 삭제된다.
  - 부모는 자식보다 항상 작아야 한다
  - ![image](https://user-images.githubusercontent.com/28949162/216970261-3031e9bd-7e03-4406-8309-ff133be73800.png)
  - ![image](https://user-images.githubusercontent.com/28949162/216969454-1be99557-9f00-4d59-b26f-ab7d718029e6.png) 
  - 원소를 삽입할 때
  - ![image](https://user-images.githubusercontent.com/28949162/216969688-ae1cc199-d780-4711-8858-bd70d950e954.png)
  - ![image](https://user-images.githubusercontent.com/28949162/216969790-6bd97e31-4a9d-4b55-81d5-a34eb78566b3.png)
  - 원소를 삭제할 때

- 최대 힙
  - 루트 노드가 가장 큰 값을 가진다 -> 가장 큰 값이 삭제된다.
  - 원리는 최소 힙과 같다.

#### 힙 구현
```python
import heapq

def heqp(arr):
  heap_list = []
  for elem in arr:
    heqpq.heappush(heap_list, elem)# 힙에 원소 삽입
  for i in range(len(heap_list)):
    heqpq.heappop(heqp_list) # 힙에서 원소 pop
```

### Tree

계층적인 구조를 표현할 때 사용

기본적으로 트리의 노드가 N 일 때 간선의 개수는 N-1개이다.

#### 이진 탐색 트리

이진탐색이 동작할 수 있도록 고안된 자료구조

특징: 모든 왼쪽 자식노드 < 부모 노드 < 모든 오른쪽 자식 노드

![image](https://user-images.githubusercontent.com/28949162/219547389-dbe2b1a4-473a-45fc-a7ca-2bfc6db35647.png)

#### 트리의 순회

- 전위 순회: 루트를 먼저 방문
- 중위 순회: 왼쪽 자식을 방문한 뒤에 루트를 방문
- 후위 순회: 오른쪽 자식을 방문한 뒤에 루트를 방문

![image](https://user-images.githubusercontent.com/28949162/219547857-d566b830-43b0-4d41-a326-7778f69d1cda.png)

```python
Class Node:
  def __init__(self, root, left_node, right_node):
    self.root = root
    self.left_node = left_node
    self.right_node = rigth_node
```


## 다시볼만한 풀이

- Programmars: 아이템 줍기



## 참고 강의
- https://youtube.com/playlist?list=PLRx0vPvlEmdAghTr5mXQxGpHjWqSz0dgC : 이코테2021(동빈나)

## 참고 서적
- 파이썬 알고리즘 인터뷰: 95가지 알고리즘 문제 풀이로 완성하는 코딩 테스트
