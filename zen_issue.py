from zen_item import Item


class Issue(Item):
    def __init__(self, data={}):
        self.tags = []
        self.name = data['name'] if 'name' in data else ''
        self.id = data['id'] if 'id' in data else ''
        self.estimates = data['estimate']['value'] if 'estimate' in data else 0
        self.tags = [t.name for t in data['tags']] if 'tags' in data else []
