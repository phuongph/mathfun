from itertools import permutations


def get_int(list_a):
	n = len(list_a)
	num = 0
	for i in range(0, n):
		num += list_a[i] * 10 ** (n-1-i) 
	return num


def get_sum(per3, target=8):
	sum_9_l = list()
	for x in per3:
		if sum(x) == target:
			sum_9_l.append(x)
	return sum_9_l


def split_number3(per3):
	p3_combine = list()

	all  = list(all_digits)
	for p in per3:
		all.remove(p)

	per3_1 = list(permutations(all, 3))

	for p in per3_1:
		l3 = list(all)
		for u in p:
			l3.remove(u)
		
		per3_last = list(permutations(l3))
		for pl in per3_last:
	
			p3_combine.append([list(p), list(pl)])


	return p3_combine


def get_two_nums(per39):
	t = 0
	matched = 0

	for p in per39:
	
		total = list(p)
		total.insert(0, 1)
		tsum = get_int(total)
		
		p3_combine = split_number3(p)

		for combine in p3_combine:
			t += 1

			num1 = get_int(combine[0])
			num2 = get_int(combine[1])
			
			if num1 + num2 == tsum:
				matched += 1
				print "{} + {} = {}".format(num1, num2, tsum)

	print "Total permutations {}".format(t)
	print "Matched: {}".format(matched) 


if __name__ == '__main__':


	all_digits = [0, 2, 3, 4, 5 ,6 ,7 ,8, 9]

	per3 = list(permutations(all_digits, 3))


	per3_9 = get_sum(per3, target=8)

	print "Sum is 8"
	get_two_nums(per3_9)

	print "Sum is 17"
	per3_17 = get_sum(per3, target=17)
	get_two_nums(per3_17)
