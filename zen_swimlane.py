from zen_issue import Issue
from zen_item import Item

class SwimLane(Item):
    def __init__(self, data):

        self.name = data['name']
        self.id = data['id']
        self.issues = []
        for item in data['issues']:
            self.Issues.append(Issue(item))
