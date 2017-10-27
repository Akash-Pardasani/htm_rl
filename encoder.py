import math
import numpy
import random
import copy

DEFAULT_RES = 1

class encoder:
	def __init__(self, offset, n = 400, w = 21, res = DEFAULT_RES, maxOverlap = 2):
		self.res = res
 		self.w = w
		self.n = n
		self.maxOverlap = maxOverlap
		self.init_Buckets(offset)

	def init_Buckets(self, offset):
		self.offset = offset
		self.BucketMap = {}
		self.init_Ind = 0
		self.minInd = self.init_Ind	
		self.maxInd = self.init_Ind
		#self.MaptoInd(offset, minInd)
		self.BucketMap[self.minInd] = random.sample(range(1, self.n + 1), self.w)
		print 'offset:', self.offset
	#	print self.BucketMap[0]
	def MapINPUTtoRep(self,x):
		bucketInd = int(round((x - self.offset)/self.res))
		
	#	print 'x:', x, 'bucketInd:', bucketInd	
	#	print x
		self.createRep(bucketInd)
		output = self.MaptoRep(bucketInd)
		#print output
		return output
		
	
	def MaptoRep(self, index):
		fakeInd = index + abs(self.minInd)
	#	print fakeInd		
	#	print self.BucketMap
		return self.BucketMap[fakeInd]

	def createRep(self, index):
		fakeInd = index + abs(self.minInd)		
		if index > 0:
			if index > self.maxInd:
				self.maxInd = index
	#		print '*', self.maxInd
			if (fakeInd - 1) in self.BucketMap.keys():		
	#			print '*'				
				self.createNewMap(index)
			else:
				self.createRep(index-1)
				self.createRep(index)
		elif index < 0:
			if index < self.minInd:
				for key in reversed(self.BucketMap.keys()):
					self.BucketMap[key + (self.minInd-index)] = self.BucketMap[key]
				self.minInd = index

		#	print '&', self.minInd
			if (fakeInd + 1) in self.BucketMap.keys():		
		#		print index
				self.createNewMap(index)
			else:
				self.createRep(index+1)
				self.createRep(index)
	
	def createNewMap(self, index):
		fakeInd = index + abs(self.minInd)
		if index > 0:
			temp = self.BucketMap[fakeInd - 1]
			newMap = self.BucketMap[fakeInd - 1][:]
			#print 'x'
			#print '&&', newMap
			ch_bit = (index-1) % self.w
		#	print '$', index, ch_bit
			newBit = random.randint(1,self.n)
			newMap[ch_bit] = newBit
		#	print '&&', newMap
			while newBit in temp or not self.newRepOK(newMap, index):	
				
				newBit = random.randint(1,self.n)	
				newMap[ch_bit] = newBit
			#	print '$', newMap
			m = max(list(self.BucketMap.keys()))
			self.BucketMap[m+1] = newMap
			#print self.BucketMap
			#print "done"
		elif index < 0:
			
		#	print fakeInd + 1
		#	print self.BucketMap			
			temp = self.BucketMap[fakeInd + 1]
			newMap = self.BucketMap[fakeInd + 1][:]
			ch_bit = self.w - 1 - (abs(index+1) % self.w)	
		#	print 'ch', ch_bit
			newBit = random.randint(1,self.n)
			newMap[ch_bit] = newBit
		#	print '^', newMap
			while newBit in temp or not self.newRepOK(newMap, index):	
				newBit = random.randint(1,self.n)	
				newMap[ch_bit] = newBit
			self.BucketMap[fakeInd] = newMap
		#	print 'abc', self.BucketMap

	def newRepOK(self, newRep, index):
			fakeInd = index + abs(self.minInd)
			fakeInit = self.init_Ind + abs(self.minInd)
			
			if index > 0:	
				tot_overlap = self.countOverlap(self.BucketMap[self.init_Ind], newRep)
				if not self.OverlapOK(self.init_Ind, index, tot_overlap):
			#	print total_overlap
					return False
				for i in range(self.init_Ind + 1, index):
				#	print '%', i					
					ch_bit = (i-1) % self.w
					I = i + abs(self.minInd)
					if self.BucketMap[I-1][ch_bit] in newRep:		
				#		print "#"						
						tot_overlap -= 1
					if self.BucketMap[I][ch_bit] in newRep:
				#		print "$"						
						tot_overlap += 1

					if not self.OverlapOK(i, index, tot_overlap):
						return False
	
			else:
				m_1 = max(list(self.BucketMap.keys()))
				#print 'woah', m_1
				tot_overlap = self.countOverlap(self.BucketMap[m_1], newRep)
				if not self.OverlapOK(m_1 - abs(self.minInd), index, tot_overlap):
				#	print 'total_overlap'
					return False				
				for i in range(m_1 - abs(self.minInd) - 1, index, -1):
					ch_bit = self.w - 1 - (abs(i+1) % self.w)
					I = i + abs(self.minInd)
					if self.BucketMap[I+1][ch_bit] in newRep:
						tot_overlap -= 1
					if self.BucketMap[I][ch_bit] in newRep:
						tot_overlap += 1
				
					if not self.OverlapOK(i, index, tot_overlap):
						return False
			return True

	def countOverlap(self, Rep, NewRep):
		counter = 0	
		for i in Rep:
			if i in NewRep:	
				counter += 1
		return counter

	def OverlapOK(self, ind1, ind2, overlap):
		if abs(ind1 - ind2) >=self.w:
			if overlap <= self.maxOverlap:
				return True
			else:
				return False
		else:
			if overlap == self.w - abs(ind1 - ind2):
				return True	
			else:
				return False
		
			

en1 = encoder(1, 40, 6)	
for i in range(1, 15):
	m = en1.MapINPUTtoRep(i)
	print m

print "%%%%%%"
for i in range(1,15):
	count = en1.countOverlap(en1.MapINPUTtoRep(i), en1.MapINPUTtoRep(15))	

	print count

					
		
