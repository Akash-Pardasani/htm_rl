import numpy

class temporal_memory(self, input_space, num_iter, columns, syn_perm_up, syn_perm_down, num_distals, num_cells, default_perm = 0.1, perm_threshold = 0.5, input_sequence):
	self.input_sequence = input_sequence
	self.num_iter = num_iter
	self.input_space = input_space
	self.num_inputs = self.input_space.prod()
	self.columns = columns
	self.num_columns = self.columns.prod()
	self.num_column_cells = num_cells
	self.default_perm = default_perm
	self.perm_threshold = perm_threshold
	self.syn_perm_up = syn_perm_up
	self.num_distals = num_distals
	self.syn_perm_down = syn_perm_down
	self.distal_columns = numpy.array(self.num_columns, self.num_distals, 2)
	self.column_space = numpy.array(self.num_columns, self.num_column_cells)
	self.column_setup()
	self.learn_sequence(self.input_sequence)

	def column_setup(self):
		for i in xrange(self.num_columns):	
			for k in xrange(self.num_column_cells)
			distal = random.sample(xrange(self.num_columns), self.num_distals)
			for j in xrange(self.num_distals):
				self.distal_columns[i][j][0] = distal[j]
				self.distal_columns[i][j][1] = self.default_perm	


	def learn_sequence(self, input_sequence):
		for i in xrange(num_iter):
			for j in input_sequence:
				if j != input_sequence[0]:
					for k in j:                   # on sdr columns of the input sdr
						for m in num_distals: # match if these columns are also distally connected to a column
							if 
