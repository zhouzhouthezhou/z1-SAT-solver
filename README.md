# z1-SAT-solver
Not as good as z3, not good enough to be z2

See Example.py for a basic Knights vs Knaves application of z1

## Known Issues
* Only works for booleans
* Does not support predicate logic
* ~Does not support parenthesis~
* ~Negation does not work on statements~

## Documentation
### Solver
**add(phrase)**  
*string phrase*:  
Adds a popositional statement and its variables to the Solver instance  

**check()**:  
Checks if the current Solver instance is `SAT`  

**model()**:  
Returns the solution to the current Solver instance if **check()** returns `SAT`, otherwise it returns `None`  

### Propositional Operations

**Bool(a)**  
*string a*:  
Returns a z1 boolean variable  

**And(a,b)**  
*Bool a*,  
*Bool b*:  
Returns the conjunction between two z1 boolean statement 

**Or(a,b)**  
*Bool a*,  
*Bool b*:   
Returns the disjunction between two z1 boolean statement

**Not(a)**  
*Bool a*:  
Returns the negation of a z1 boolean statement

**Equal(a,b)**  
*Bool a*,  
*Bool b*:  
Returns the bicondition of two z1 boolean statements 

**Imply(a,b)**  
*Bool a*,  
*Bool b*:  
Returns the implication of two z1 boolean variables (a -> b)  
