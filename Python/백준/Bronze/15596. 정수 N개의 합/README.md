# [Bronze II] 정수 N개의 합 - 15596 

[문제 링크](https://www.acmicpc.net/problem/15596) 

### 성능 요약

메모리: 339868 KB, 시간: 24 ms

### 분류

수학, 구현, 사칙연산

### 제출 일자

2025년 9월 5일 14:44:46

### 문제 설명

<p style="user-select: auto !important;">정수 n개가 주어졌을 때, n개의 합을 구하는 함수를 작성하시오.</p>

<p style="user-select: auto !important;">작성해야 하는 함수는 다음과 같다.</p>

<ul style="user-select: auto !important;">
	<li style="user-select: auto !important;">C, C11, C (Clang), C11 (Clang): <code style="user-select: auto !important;">long long sum(int *a, int n);</code>

	<ul style="user-select: auto !important;">
		<li style="user-select: auto !important;"><code style="user-select: auto !important;">a</code>: 합을 구해야 하는 정수 <code style="user-select: auto !important;">n</code>개가 저장되어 있는 배열 (0 ≤ a[i] ≤ 1,000,000, 1 ≤ n ≤ 3,000,000)</li>
		<li style="user-select: auto !important;"><code style="user-select: auto !important;">n</code>: 합을 구해야 하는 정수의 개수</li>
		<li style="user-select: auto !important;">리턴값: a에 포함되어 있는 정수 <code style="user-select: auto !important;">n</code>개의 합</li>
	</ul>
	</li>
	<li style="user-select: auto !important;">C++, C++11, C++14, C++17, C++ (Clang), C++11 (Clang), C++14 (Clang), C++17 (Clang): <code style="user-select: auto !important;">long long sum(std::vector<int> &a);</code>
	<ul style="user-select: auto !important;">
		<li style="user-select: auto !important;"><code style="user-select: auto !important;">a</code>: 합을 구해야 하는 정수 <code style="user-select: auto !important;">n</code>개가 저장되어 있는 배열 (0 ≤ a[i] ≤ 1,000,000, 1 ≤ n ≤ 3,000,000)</li>
		<li style="user-select: auto !important;">리턴값: <code style="user-select: auto !important;">a</code>에 포함되어 있는 정수 <code style="user-select: auto !important;">n</code>개의 합</li>
	</ul>
	</li>
	<li style="user-select: auto !important;">Python 2, Python 3, PyPy, PyPy3: <code style="user-select: auto !important;">def solve(a: list) -> int</code>
	<ul style="user-select: auto !important;">
		<li style="user-select: auto !important;"><code style="user-select: auto !important;">a</code>: 합을 구해야 하는 정수 <code style="user-select: auto !important;">n</code>개가 저장되어 있는 리스트 (0 ≤ a[i] ≤ 1,000,000, 1 ≤ n ≤ 3,000,000)</li>
		<li style="user-select: auto !important;">리턴값: <code style="user-select: auto !important;">a</code>에 포함되어 있는 정수 <code style="user-select: auto !important;">n</code>개의 합 (정수)</li>
	</ul>
	</li>
	<li style="user-select: auto !important;">Java: <code style="user-select: auto !important;">long sum(int[] a);</code> (클래스 이름: Test)
	<ul style="user-select: auto !important;">
		<li style="user-select: auto !important;"><code style="user-select: auto !important;">a</code>: 합을 구해야 하는 정수 <code style="user-select: auto !important;">n</code>개가 저장되어 있는 배열 (0 ≤ a[i] ≤ 1,000,000, 1 ≤ n ≤ 3,000,000)</li>
		<li style="user-select: auto !important;">리턴값: <code style="user-select: auto !important;">a</code>에 포함되어 있는 정수 <code style="user-select: auto !important;">n</code>개의 합</li>
	</ul>
	</li>
	<li style="user-select: auto !important;">Go: <code style="user-select: auto !important;">sum(a []int) int</code>
	<ul style="user-select: auto !important;">
		<li style="user-select: auto !important;"><code style="user-select: auto !important;">a</code>: 합을 구해야 하는 정수 <code style="user-select: auto !important;">n</code>개가 저장되어 있는 배열 (0 ≤ a[i] ≤ 1,000,000, 1 ≤ n ≤ 3,000,000)</li>
		<li style="user-select: auto !important;">리턴값: <code style="user-select: auto !important;">a</code>에 포함되어 있는 정수 <code style="user-select: auto !important;">n</code>개의 합</li>
	</ul>
	</li>
</ul>

### 입력 

 Empty

### 출력 

 Empty

