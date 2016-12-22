#!/usr/bin/python

from door import reverse

def cabinet(number):
	return lambda student: lambda door: reverse(door) if student(number) else door

def student(number):
	return lambda cabinet: cabinet % number == 0

def students(*student):
	return lambda cabinet: len(filter(lambda s: s(cabinet), student)) % 2 != 0

def all_students(student_count):
	return students(*map(lambda sn: student(sn), xrange(1, student_count + 1)))

def all_cabinets(cabinet_count):
	return map(lambda cn: cabinet(cn), xrange(1, cabinet_count + 1))

def all_door(cabinet_count, student_count):
	students = all_students(student_count)
	cabinets = [cabinet(students) for cabinet in all_cabinets(cabinet_count)]
	return lambda init: [cabinet(init) for cabinet in cabinets]


import unittest

class TestDoor(unittest.TestCase):

	def test_student1_open_cabinet1(self):
		self.assertEqual(cabinet(1)(student(1))('close'), 'open')

	def test_student2_ignore_cabinet1(self):
		self.assertEqual(cabinet(1)(student(2))('open'), 'open')

	def test_student2_close_cabinet2(self):
		self.assertEqual(cabinet(2)(student(2))('open'), 'close')

	def test_student1_open_cabinet2_then_student2_close(self):
		self.assertEqual(cabinet(2)(students(student(1), student(2)))('close'), 'close')

	def test_all_students(self):
		self.assertEqual(cabinet(1)(all_students(100))('close'), 'open')
		self.assertEqual(cabinet(2)(all_students(100))('close'), 'close')

	def test_all_cabinets(self):
		doors = all_door(100, 100)('close')
		self.assertEqual(100, len(doors))
		self.assertEqual('open', doors[0])
		self.assertEqual('close', doors[1])

if __name__ == '__main__':
	unittest.main()
