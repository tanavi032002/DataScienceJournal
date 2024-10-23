class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

# Function to add a new node at the start of the list
def insert_at_head(head_ref, new_value):
    # Create a new node
    new_node = ListNode(new_value)
    # Link the current head to the new node
    new_node.next = head_ref
    # Update the head to be the new node
    return new_node

# Function to find the middle element of the linked list
def find_middle(head):
    slow_ptr = head
    fast_ptr = head
    # Iterate through the linked list with two pointers
    while fast_ptr and fast_ptr.next:
        slow_ptr = slow_ptr.next           # Moves one step
        fast_ptr = fast_ptr.next.next      # Moves two steps
    # slow_ptr will be at the middle when fast_ptr reaches the end
    return slow_ptr.value if slow_ptr else None

# Driver code
head = None
# Insert values 8 to 1 at the head
for i in range(8, 0, -1):
    head = insert_at_head(head, i)

# Print the middle element of the linked list
print("The middle element of the linked list is:", find_middle(head))
