import json
import matplotlib.pyplot as plt

class Teacher:
    def __init__(self, name, subject, subject_code, score):
        self.name = name
        self.subject = subject
        self.subject_code = subject_code
        self.score = score
        self.ranking = None  # Ranking will be assigned later

    def __repr__(self):
        return f"{self.name} ({self.subject}, {self.subject_code}) - Score: {self.score}, Rank: {self.ranking}"

class TreeNode:
    def __init__(self, teacher):
        self.teacher = teacher
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, teacher):
        if not self.root:
            self.root = TreeNode(teacher)
        else:
            self._insert_recursive(self.root, teacher)

    def _insert_recursive(self, node, teacher):
        if teacher.score > node.teacher.score:  # Higher score goes to the left
            if node.left is None:
                node.left = TreeNode(teacher)
            else:
                self._insert_recursive(node.left, teacher)
        else:
            if node.right is None:
                node.right = TreeNode(teacher)
            else:
                self._insert_recursive(node.right, teacher)

    def assign_positions(self, node, pos_x=0, pos_y=0, dx=1):
        """Assign positions for the nodes in the tree."""
        if node is None:
            return []
        
        positions = []
        
        # Add current node
        positions.append((pos_x, pos_y, node))
        
        # Draw left child
        left_positions = self.assign_positions(node.left, pos_x - dx, pos_y - 1, dx / 2)
        positions.extend(left_positions)
        
        # Draw right child
        right_positions = self.assign_positions(node.right, pos_x + dx, pos_y - 1, dx / 2)
        positions.extend(right_positions)
        
        return positions

    def draw_tree(self):
        """Visualize the tree using matplotlib."""
        if self.root is None:
            print("Tree is empty!")
            return

        positions = self.assign_positions(self.root)

        # Create the plot
        plt.figure(figsize=(12, 8))  # Increase figure size for better visibility
        
        # Draw nodes
        for x, y, node in positions:
            plt.text(x, y, f"{node.teacher.name}\n{node.teacher.subject}\nScore: {node.teacher.score}\nRank: {node.teacher.ranking}",
                     ha='center', va='center', bbox=dict(boxstyle="round,pad=0.3", edgecolor='black', facecolor='lightblue'))

        # Draw lines
        for x, y, node in positions:
            if node.left:  # Check if the left child exists
                left_x = x - 0.5  # Adjust horizontal offset for left child
                left_y = y - 1    # Vertical offset for child
                plt.plot([x, left_x], [y, left_y], 'k-', linewidth=2)  # Thicker line for visibility
            if node.right:  # Check if the right child exists
                right_x = x + 0.5  # Adjust horizontal offset for right child
                right_y = y - 1    # Vertical offset for child
                plt.plot([x, right_x], [y, right_y], 'k-', linewidth=2)  # Thicker line for visibility

        plt.title("Binary Tree of Teachers Based on Scores", fontsize=16)
        plt.axis('off')  # Hide axes
        plt.tight_layout()
        plt.savefig("teacher_ranking_tree.png")  # Save the figure
        plt.show()  # Show the plot

def load_teachers_from_config(file_path):
    """Load teacher data from teacher.json."""
    with open(file_path, 'r') as file:
        data = json.load(file)
    return [Teacher(item["name"], item["subject"], item["subject_code"], item["score"]) for item in data["teachers"]]

def assign_rankings(teachers):
    """Assign rankings based on scores."""
    # Sort teachers by score in descending order
    sorted_teachers = sorted(teachers, key=lambda x: x.score, reverse=True)
    for rank, teacher in enumerate(sorted_teachers, start=1):
        teacher.ranking = rank

def main():
    # Load teachers from teacher.json
    teachers = load_teachers_from_config("teacher.json")
    
    # Assign rankings based on scores
    assign_rankings(teachers)
    
    # Initialize the binary tree and insert teachers based on score
    tree = BinaryTree()
    for teacher in teachers:
        tree.insert(teacher)
    
    # Draw the binary tree using matplotlib
    tree.draw_tree()

if __name__ == "__main__":
    main()
