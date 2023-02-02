# for-coding-test

## 참고 강의
- https://youtube.com/playlist?list=PLRx0vPvlEmdAghTr5mXQxGpHjWqSz0dgC : 이코테2021(동빈나)

## 참고 서적
- 파이썬 알고리즘 인터뷰: 95가지 알고리즘 문제 풀이로 완성하는 코딩 테스트

## 코딩 테스트 플랫폼
- 백준, 프로그래머스, 리트코드

## 코딩 테스트 전략

1. 예외 처리 리스트
- 입력값이 0, null 인 경우

2. 문제 당 제한 시간을 정해두자. 문제를 잘못 이해했거나, 잘못된 알고리즘으로 푸는 등 잘못 접근했을 때 이를 방지하기 위한 방법으로 시간제한을 둔다. 

3. REPL 도구로 코드를 검증하자.

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

### set 자료형

방문처리 같은 경우 리스트를 만들어 리스트안에 원소가 있는지 판별하는 경우가 있다.
리스트인 경우 O(N)을 가진다.
이를 줄이기 위해 set() 자료구조를 사용하면 O(1)만에 찾을 수 있다. set은 해시테이블을 사용하기 때문이다.

### defaultdict 자료형

from collections import defaultdict
my_dict = defaultdict(list)  <- list 자료형으로 딕셔너리를 초기화

defaultdict를 사용하면 키 값을 초기화하지 않았을 때 디폴트 자료형으로 초기화 하는 것.
위와 같이 사용하면 my_dict['ex']를 초기화 하지 않았을 때 디폴트로 빈 리스트를 가진다.
