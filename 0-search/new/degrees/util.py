class Node():
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action


class StackFrontier():
    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node


class QueueFrontier(StackFrontier):

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node
    
    def print_frontier(self):
        """Prints the states contained in the frontier in order."""
        print("--- Queue Frontier (FIFO) ---")
        if self.empty():
            print("The frontier is empty.")
            return

        # Create a list of state values for clean printing
        state_list = [node.state for node in self.frontier]

        # Print the states, showing which is next to be removed (front)
        print(f"Frontier: {state_list}")

        if state_list:
             print(f"Next to Remove: {state_list[0]} (Front of Queue)")
        print("-----------------------------\n")


    def print_frontier_full(self):
        """Prints the full state, parent, and action for every node in the frontier."""
        print("\n====================================")
        print("  Queue Frontier Contents (FIFO)")
        print("====================================")

        if self.empty():
            print("The frontier is currently empty.")
            return

        print(f"Total Nodes: {len(self.frontier)}")
        print(f"  (Node to be removed NEXT is the first one listed)\n")

        # Iterate through all nodes currently in the frontier
        for i, node in enumerate(self.frontier):
            # Get the parent state (use 'None' if the node has no parent, like the start node)
            parent_state = node.parent.state if node.parent else '--- START ---'

            # Use 'None' for the action if it's the start node
            action_taken = node.action if node.action else '--- N/A ---'

            # Print the detailed information
            print(f"[{i + 1}]")
            print(f"  State:  {node.state}")
            print(f"  Parent: {parent_state}")
            print(f"  Action: {action_taken}")
            print("---")

        print("====================================\n")
