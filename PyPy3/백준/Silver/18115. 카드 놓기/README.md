# [Silver III] 카드 놓기 - 18115 

[문제 링크](https://www.acmicpc.net/problem/18115) 

### 성능 요약

메모리: 234044 KB, 시간: 412 ms

### 분류

자료 구조, 덱

### 제출 일자

2025년 9월 17일 12:06:39

### 문제 설명

<p style="user-select: auto !important;">수현이는 카드 기술을 연습하고 있다. 수현이의 손에 들린 카드를 하나씩 내려놓아 바닥에 쌓으려고 한다. 수현이가 쓸 수 있는 기술은 다음 3가지다.</p>

<ol style="user-select: auto !important;">
	<li style="user-select: auto !important;">제일 위의 카드 1장을 바닥에 내려놓는다.</li>
	<li style="user-select: auto !important;">위에서 두 번째 카드를 바닥에 내려놓는다. 카드가 2장 이상일 때만 쓸 수 있다.</li>
	<li style="user-select: auto !important;">제일 밑에 있는 카드를 바닥에 내려놓는다. 카드가 2장 이상일 때만 쓸 수 있다.</li>
</ol>

<p style="user-select: auto !important;">수현이는 처음에 카드 <em style="user-select: auto !important;">N</em>장을 들고 있다. 카드에는 1부터 <em style="user-select: auto !important;">N</em>까지의 정수가 중복되지 않게 적혀 있다. 기술을 <em style="user-select: auto !important;">N</em>번 사용하여 카드를 다 내려놓았을 때, 놓여 있는 카드들을 확인했더니 위에서부터 순서대로 1, 2, …, <em style="user-select: auto !important;">N</em>이 적혀 있었다!</p>

<p style="user-select: auto !important;">놀란 수현이는 처음에 카드가 어떻게 배치되어 있었는지 궁금해졌다. 처음 카드의 상태를 출력하여라.</p>

### 입력 

 <p style="user-select: auto !important;">첫 번째 줄에는 <em style="user-select: auto !important;">N </em>(1 ≤ <em style="user-select: auto !important;">N</em> ≤ 10<sup style="user-select: auto !important;">6</sup>)이 주어진다.</p>

<p style="user-select: auto !important;">두 번째 줄에는 길이가 <em style="user-select: auto !important;">N</em>인 수열 <em style="user-select: auto !important;">A</em>가 주어진다. <em style="user-select: auto !important;">A<sub style="user-select: auto !important;">i</sub></em>가 <em style="user-select: auto !important;">x</em>이면, <em style="user-select: auto !important;">i</em>번째로 카드를 내려놓을 때 <em style="user-select: auto !important;">x</em>번 기술을 썼다는 뜻이다. <em style="user-select: auto !important;">A<sub style="user-select: auto !important;">i</sub></em>는 1, 2, 3 중 하나이며, <em style="user-select: auto !important;">A<sub style="user-select: auto !important;">n</sub></em>은 항상 1이다.</p>

### 출력 

 <p style="user-select: auto !important;">초기 카드의 상태를 위에서부터 순서대로 출력하여라.</p>

