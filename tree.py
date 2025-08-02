class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, node):
        self.children.append(node)

    def dfs(self):
        print(self.value)
        for child in self.children:
            child.dfs()
