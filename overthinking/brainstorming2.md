there should be two objects in this project:

1. the Block object, which is the task object, it has the following attributes:
	- title
	- description
	- duration
	- completed [bool]

### it has the following methods:
	- mark completed
	- mark incomplete
	- modify title
	- modify description
	- modify duration



2. the Schedule object, which is basically a list of all the blocks for a specific day (we can make the block different based on the day)
this class contain the block objects, it's not a block, but a container for the blocks

its main attribute is this:
	- block list (contains block objects)

### it has the following methods:
	- add block
	- delete block	
	- modify the order of the block	
	- list all blocks
