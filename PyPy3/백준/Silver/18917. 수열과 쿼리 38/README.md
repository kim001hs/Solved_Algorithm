# [Silver III] 수열과 쿼리 38 - 18917 

[문제 링크](https://www.acmicpc.net/problem/18917) 

### 성능 요약

메모리: 113340 KB, 시간: 284 ms

### 분류

수학, 구현

### 제출 일자

2025년 9월 17일 11:33:59

### 문제 설명

<p style="user-select: auto !important;">처음에 0이 하나 포함되어있는 배열 A가 있다. 이때, 다음 쿼리를 수행해야 한다.</p>

<ul style="user-select: auto !important;">
	<li style="user-select: auto !important;"><code style="user-select: auto !important;">1 x</code>: A의 가장 뒤에 <code style="user-select: auto !important;">x</code>를 추가한다.</li>
	<li style="user-select: auto !important;"><code style="user-select: auto !important;">2 x</code>: A에서 <code style="user-select: auto !important;">x</code>를 제거한다. A에 <code style="user-select: auto !important;">x</code>가 두 개 이상 있는 경우에는 가장 앞에 있는 하나만 제거한다. 항상 A에 <code style="user-select: auto !important;">x</code>가 있는 쿼리만 주어진다.</li>
	<li style="user-select: auto !important;"><code style="user-select: auto !important;">3</code>: A에 포함된 모든 원소를 더한 값을 출력한다.</li>
	<li style="user-select: auto !important;"><code style="user-select: auto !important;">4</code>: A에 포함된 모든 원소를 XOR한 값을 출력한다.</li>
</ul>

### 입력 

 <p style="user-select: auto !important;">첫째 줄에는 쿼리의 개수 M이 주어진다. 둘째 줄부터 다음 M 개의 줄에 쿼리가 주어진다.</p>

### 출력 

 <p style="user-select: auto !important;">3번 혹은 4번 쿼리가 등장할 때마다, 답을 한 줄에 하나씩 출력한다.</p>

