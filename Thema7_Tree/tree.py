

class Tree:

    
    def __init__(self, value: str, right: "Tree" = None, left: "Tree" = None,):
        self.right = right
        self.left = left
        self.value = value 

tree = Tree(
    value=1,
    right=Tree(
        value=2,
        right=Tree(
            value=3
        ),
        left=Tree(
            value=4
        )
    ),
    left=Tree(
        value=5
    )
)

print(tree.left.value)
print(tree.right.left.value)
print(tree.value)