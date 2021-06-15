# LIFO(Last In First Out)

'''Basic Operations of Stack
There are some basic operations that allow us to perform different actions on a stack.

Push: Add an element to the top of a stack
Pop: Remove an element from the top of a stack
IsEmpty: Check if the stack is empty
IsFull: Check if the stack is full
Peek: Get the value of the top element without removing it
Working of Stack Data Structure
The operations work as follows:

A pointer called TOP is used to keep track of the top element in the stack.
When initializing the stack, we set its value to -1 so that we can check if the stack is empty by 
comparing TOP == -1.
On pushing an element, we increase the value of TOP and place the new element in the position pointed 
to by TOP.
On popping an element, we return the element pointed to by TOP and reduce its value.
Before pushing, we check if the stack is already full
Before popping, we check if the stack is already empty

Applications of Stack Data Structure
Although stack is a simple data structure to implement, it is very powerful. The most common uses of a 
stack are:

To reverse a word - Put all the letters in a stack and pop them out. Because of the LIFO order of stack, 
you will get the letters in reverse order.
In compilers - Compilers use the stack to calculate the value of expressions like 2 + 4 / 5 * (7 - 9) 
by converting the expression to prefix or postfix form.
In browsers - The back button in a browser saves all the URLs you have visited previously in a stack.
 Each time you visit a new page, it is added on top of the stack. When you press the back button, the 
 current URL is removed from the stack, and the previous URL is accessed.
'''

# Stack implementation in python


# Creating a stack
def create_stack():
    stack = []
    return stack


# Creating an empty stack
def check_empty(stack):
    return len(stack) == 0


# Adding items into the stack
def push(stack, item):
    stack.append(item)
    print("pushed item: " + item)


# Removing an element from the stack
def pop(stack):
    if (check_empty(stack)):
        return "stack is empty"

    return stack.pop()


stack = create_stack()
push(stack, str(1))
push(stack, str(2))
print("popped item: " + pop(stack))
push(stack, str(3))
push(stack, str(4))
print("popped item: " + pop(stack))
print("stack after popping an element: " + str(stack))
