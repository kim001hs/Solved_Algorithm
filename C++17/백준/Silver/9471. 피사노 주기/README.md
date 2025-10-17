# [Silver IV] 피사노 주기 - 9471 

[문제 링크](https://www.acmicpc.net/problem/9471) 

### 성능 요약

메모리: 2020 KB, 시간: 28 ms

### 분류

수학, 브루트포스 알고리즘, 정수론, 피사노 주기

### 제출 일자

2025년 10월 17일 10:49:07

### 문제 설명

<p style="user-select: auto !important;">1960년, IBM의 직원 Donald Wall은 피보나치 수열을 m으로 나눈 나머지가 주기를 이룬다는 것을 증명했다.</p>

<p style="user-select: auto !important;">예를 들어, 피보나치 수열의 처음 10개를 11로 나눈 예는 다음과 같다.</p>

<table class="table table-bordered" style="width: 60%; user-select: auto !important;">
	<thead style="user-select: auto !important;">
		<tr style="user-select: auto !important;">
			<th style="user-select: auto !important;">n</th>
			<th style="user-select: auto !important;">1</th>
			<th style="user-select: auto !important;">2</th>
			<th style="user-select: auto !important;">3</th>
			<th style="user-select: auto !important;">4</th>
			<th style="user-select: auto !important;">5</th>
			<th style="user-select: auto !important;">6</th>
			<th style="user-select: auto !important;">7</th>
			<th style="user-select: auto !important;">8</th>
			<th style="user-select: auto !important;">9</th>
			<th style="user-select: auto !important;">10</th>
		</tr>
	</thead>
	<tbody style="user-select: auto !important;">
		<tr style="user-select: auto !important;">
			<th style="user-select: auto !important;">F(n)</th>
			<td style="user-select: auto !important;">1</td>
			<td style="user-select: auto !important;">1</td>
			<td style="user-select: auto !important;">2</td>
			<td style="user-select: auto !important;">3</td>
			<td style="user-select: auto !important;">5</td>
			<td style="user-select: auto !important;">8</td>
			<td style="user-select: auto !important;">13</td>
			<td style="user-select: auto !important;">21</td>
			<td style="user-select: auto !important;">34</td>
			<td style="user-select: auto !important;">55</td>
		</tr>
		<tr style="user-select: auto !important;">
			<th style="user-select: auto !important;">F(n) mod 11</th>
			<td style="user-select: auto !important;">1</td>
			<td style="user-select: auto !important;">1</td>
			<td style="user-select: auto !important;">2</td>
			<td style="user-select: auto !important;">3</td>
			<td style="user-select: auto !important;">5</td>
			<td style="user-select: auto !important;">8</td>
			<td style="user-select: auto !important;">2</td>
			<td style="user-select: auto !important;">10</td>
			<td style="user-select: auto !important;">1</td>
			<td style="user-select: auto !important;">0</td>
		</tr>
	</tbody>
</table>

<p style="user-select: auto !important;">나머지를 이용해서 만든 수열은 주기가 나타날 수 있다. k(m)을 반복하는 부분 수열의 길이라고 했을 때, k(11) = 10임을 알 수 있다.</p>

<p style="user-select: auto !important;">Wall은 아래와 같은 여러 가지 성질도 증명했다.</p>

<ul style="user-select: auto !important;">
	<li style="user-select: auto !important;">m > 2인 경우에 k(m)은 짝수이다.</li>
	<li style="user-select: auto !important;">임의의 짝수 정수 n > 2에 대해서, k(m) = n인 m이 항상 존재한다.</li>
	<li style="user-select: auto !important;">k(m) ≤ m<sup style="user-select: auto !important;">2</sup> - 1</li>
	<li style="user-select: auto !important;">k(2<sup style="user-select: auto !important;">n</sup>) = 3×2<sup style="user-select: auto !important;">(n-1)</sup></li>
	<li style="user-select: auto !important;">k(5<sup style="user-select: auto !important;">n</sup>) = 4×5<sup style="user-select: auto !important;">n</sup></li>
	<li style="user-select: auto !important;">k(2×5<sup style="user-select: auto !important;">n</sup>) = 6n</li>
	<li style="user-select: auto !important;">n > 2라면, k(10<sup style="user-select: auto !important;">n</sup>) = 15×10<sup style="user-select: auto !important;">(n-1)</sup></li>
</ul>

<p style="user-select: auto !important;">m이 주어졌을 때, k(m)을 구하는 프로그램을 작성하시오.</p>

### 입력 

 <p style="user-select: auto !important;">첫째 줄에 테스트 케이스의 개수 P가 주어진다. 각 테스트 케이스는 N과 M으로 이루어져 있다. N은 테스트 케이스의 번호이고, M은 문제에서 설명한 m이다.</p>

### 출력 

 <p style="user-select: auto !important;">각 테스트 케이스마다 테스트 케이스 번호를 출력하고 k(M)을 출력한다.</p>

