there should be two objects in this project:

1. the Block object, which is the task object, it has the following attributes:
	- id
	- title
	- description
	- duration
	- completed [bool]
	- the order of the block (an integer, the first task of the day has order of 0, and we keep increment it based on the order)

### it has the following methods:
	- modify title
	- modify description
	- modify order 
	- modify duration



2. the Schedule object, which is basically a list of all the blocks
this class contain the block objects, it's not a block, but a container for the blocks

its main attribute is this:
	- block list (contains block objects)

### it has the following methods:
	- add block
	- delete block	
	- display block title/order
	
