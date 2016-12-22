#!/usr/bin/python

from door import reverse

def all_door(cabinet_count, student_count):
	def state(init):
		door = [init] * (cabinet_count + 1)
		for cabinet in xrange(1, cabinet_count + 1):
			for student in xrange(1, student_count + 1):
				if cabinet % student == 0:
					door[cabinet] = reverse(door[cabinet])
		return door[1:]
	return state

if __name__ == '__main__':
	all_door(100, 100)('close')