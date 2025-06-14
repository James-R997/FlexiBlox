class Block:
    def __init__(self, title:str, description:str, duration:int):
        '''
        Represents a time block for a specific task.

        Args:
            title (str): The title of the task.
            description (str): The description of the task.
            duration (int): The duration of the task (in minutes).
        '''
        self.title       = title
        self.description = description
        self.duration    = duration

        self.completed   = False
    
    def mark_completed(self):
        self.completed = True
    
    def mark_incomplete(self):
        self.completed = False

    def modify_title(self, newTitle):
        self.title = newTitle
    
    def modify_description(self, newDescription):
        self.description = newDescription
    
    def adjust_duration(self, newDuration:int):
        self.duration = newDuration
    

    def __str__(self):
        return f"-- The block [{self.title}] ({self.description}) has a duration of {self.duration} minutes. --"

class Schedule:
    '''
    A Schedule is a list of blocks
    '''

    def __init__(self):
        self.blocks = []

    def add_block(self, title, description, duration):
        task = Block(title, description, duration)
        self.blocks.append(task)
    
    def delete_block(self, title):
        self.blocks = [b for b in self.blocks if b.title != title]

    def adjust_order(self, oldOrder, newOrder):
        b = self.blocks.pop(oldOrder)
        self.blocks.insert(newOrder, b)
    
    def get_all_blocks(self):
        return self.blocks

    def __str__(self):
        return f"-- This Schedule has {len(self.blocks)} block. --"
