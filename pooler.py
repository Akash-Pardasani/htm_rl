import math
import numpy
import random
import heapq

class pooler:
	def __init__(self, in_n = (6, 6), in_w = 4, n = (15, 15), pool = 0.5, thres_volt = 0.6, max_volt = 0.8, sparse = 10, perm_up = 0.1, perm_down = 0.1):

		self.in_n = numpy.array(in_n)
		self.num_inputs = self.in_n.prod()
		self.in_w = in_w #number of on bits
		self.n = numpy.array(n)
		self.num_columns = self.n.prod()
		self.pool = pool #potential pool, % of input bits a column is connected to
		self.thres_volt = thres_volt
		self.sparse = sparse #number of on columns
		self.perm_up = perm_up
		self.perm_down = perm_down
		self.max_volt = max_volt
		self.num_synapse = int(self.pool*self.num_inputs) # no of bits a column is connected to
		self.space = self.setup_space()
		
	
	def setup_space(self):
				
		columns = numpy.zeros((self.num_columns, self.num_inputs, 3))
		for i in xrange(0, self.num_columns):
			counter = 0
			#print random.sample(xrange(self.num_inputs), self.num_synapse)
			# print pool_bits			
			for j in random.sample(xrange(self.num_inputs), self.num_synapse):
				columns[i][j][0] = 1
				columns[i][j][1] = random.uniform(0, self.max_volt)	
#				print columns[i][j][1]
				if columns[i][j][1] >= self.thres_volt:
					counter += 1
					columns[i][j][2] = 1
		#	print counter
		return columns

	def MapInput(self, in_SDR, learning):
		in_binary = numpy.zeros((1, self.num_inputs))	
		pool_map = numpy.zeros((1, self.num_columns))
		counter = numpy.zeros((1, self.num_columns))
		for i in in_SDR:
			print '**', i
			in_binary[0][i] = 1	
		print in_binary
		print '**'
	
		for k in range(0, self.num_columns):		
			for j in range(0, self.num_inputs):
				#print k, j, '*'
				#print self.space[k][j][2]				
				if self.space[k][j][2] and in_binary[0][j]:
					 counter[0][k] += 1

		print counter
		print "woah"
		m = (-counter).argsort()
		for i in m:
			max_index = i[:self.sparse]
		print max_index
		print "woah"
		for k in max_index:
			print k
			pool_map[0][k] = 1
			if learning:
				for b in xrange(self.num_inputs):		
					if in_binary[0][b]:
					#	print "*", b					
						self.space[k][b][1] += self.perm_up
					else:
						if self.space[k][b][2]:						
							self.space[k][b][1] -= self.perm_down		
					if self.space[k][b][1] >= self.thres_volt:
						self.space[k][b][2] = 1
						print '*', b
		pool_map.resize(self.n[0], self.n[1])
		return pool_map

p = pooler()
for i in range(10):
	out = p.MapInput([2, 14, 16, 21], 1)

print out

					
		

