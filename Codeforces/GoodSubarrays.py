from collections import defaultdict
t = int(input())
for _ in range(t):
	arr_len = int(input())
	arr = [ord(i) - ord("0") for i in input()]
	pref_arr = [0] + arr
	for i in range(1, len(pref_arr)):
		pref_arr[i] += pref_arr[i - 1]
 
	sum_dist = defaultdict(int)
	for i in range(len(pref_arr)):
		sum_dist[pref_arr[i] - i] += 1
	good_arrays = 0
	for f in sum_dist.values():
		good_arrays += f * (f - 1) // 2
	print(good_arrays)