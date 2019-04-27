#Basic SAT Solver
#Kyle Zhou
#April 2019

from collections import deque

class Solver:
	def __init__(self):
		self.varList = []
		self.varDict = dict()
		self.keywords = ['&', '|', '=']
		self.statement = []
		self.isChecked = False;

	#Adds a propositional phrase and its variables into the Solver object
	#@param phrase
	#The propositional phrase to be added (string_
	def add(self, phrases):
		self.isChecked = False;

		phrase = deque([])
		for c in phrases:
			phrase.append(c)

		builder = ''
		stack = []
		while phrase:
			c = phrase.popleft()
			if c not in self.keywords and c not in self.varList and c != '(' and c != ')':
				negate = False;
				while c == '~':
					negate = not negate
					c = phrase.popleft()
					
				if negate:
					builder = builder + '~'

				self.varList.append(c)
				self.varDict[c] = True
				builder = builder + c
			elif c in self.keywords or c == '(':
				stack.append(c)
			elif c == ')':
				t = stack.pop()
				while t != '(':
					builder = builder + t
					t = stack.pop()

		while stack:
			t = stack.pop()
			builder = builder + t
		print(builder)
					

	#Handles creating a negated variable
	#@param v
	#The symbolic variable ment to be converted into a boolean (string)
	def generateVar(self, v):
		if '~' in v:
			v = v.replace('~','')
			return not self.varDict[v]
		else:
			return self.varDict[v]

	#Determintes the SAT of a given propositional phrase
	#@param phrase
	#The propositional phrase to be evaluated (string)
	def old_evaluatePhrase(self, phrase):
		ans = True
		q = deque([])
		for c in phrase:
			q.append(c)
		v = deque([])
		while q:
			c = q.popleft()
			if c == '~':
				temp = q.popleft()
				n = 1
				while temp == '~':
					n = n + 1
					temp = q.popleft()
				
				if n % 2 == 1:
					temp = '~' + temp
				v.append(temp)
			elif c in self.keywords:
				temp = q.popleft()
				if temp == '~':
					temp = '~' + q.popleft()
					n = 1
					while temp == '~':
						n = n + 1
						temp = q.popleft()
					if n % 2 == 1:
						temp = '~' + temp
				v.append(temp)
				a = self.generateVar(v.popleft())
				b = self.generateVar(v.popleft())
				if c == '&':
					ans = ans and (a and b)
				elif c == '|':
					ans = ans and (a or b)
				elif c == '=':
					ans = ans and (a == b)
			else:
				v.append(c)
		return ans

	def evaluatePhrase(self, phrase):
		pass


	#Generates the nth line of the truth table representetive of the current amout of propositional variables
	#@param line
	#The nth line of the truth table you wish to generate (int)
	#@param n
	#The index of the current propositional variable that will be edited, should always be 0 when called (int)
	#@param layer
	#The current dividing layer of the truth table to compare against (int)
	def generateline(self, line, n, layer):
		if layer == 1:
			return
		
		threshold = layer//2
		if line <= threshold:
			self.varDict[self.varList[n]] = True
			self.generateline(line, n + 1, threshold)
		else:
			self.varDict[self.varList[n]] = False
			self.generateline(line - threshold, n + 1, threshold) 
	

	#Evaluates the current set of statements stored in the solver
	def evaluate(self):
		n = pow(2, len(self.varList))
		for i in range(n):
			self.generateline(i+1, 0, n)
			ans = True
			for s in self.statement:
				ans = ans and self.evaluatePhrase(s)
			if ans:
				return True
		return False
		
	#Checks the satisfiability of the current state of the Solver. Must be run before modeling
	def check(self):
		ans = self.evaluate()
		if ans:
			self.isChecked = True
			return 'sat'
		else:
			return 'unsat'
	
	#If the current state of Solver is SAT, print the dictionary containting the boolean values of the propositional variables
	def model(self):
		if self.isChecked:
			return self.varDict
		else:
			return None

#################################################################################################################################################

#returns conjunction
def And(a, b):
	temp = a + '&' + b
	return temp

#returns disjunction
def Or(a, b):
	temp = a + '|' + b
	return temp

#returns negation
def Not(a):
	temp = '~' + a
	return temp

#returns biconditional
def Equal(a, b):
	temp = a + '=' + b
	return temp

#returns implication
def Imply(a, b):
	temp = Or(Not(a), b)
	return temp

#returns a z1 boolean object
def Bool(a):
	return a
