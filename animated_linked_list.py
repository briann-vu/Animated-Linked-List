'''File: animated_linked_list.py
    Author: Brian Vu
    Purpose: Program asks for integer inputs and inserts/creates
        a linked list with them. The program prints out a
        text-based list in the console and prints out an updated
        one each time a node is inserted. The program also draws
        a graphical version of the list. Each time a node is inserted,
        an updated list gets drawn making an animation since the
        drawing changes each time; the inserted node is also highlighted
        in green. graphics.py is imported in order to draw the images,
        list_node.py is imported to create list node objects for the
        linked list, lasty sys is imported for the standard input
        of the numbers.
'''

import sys
from graphics import *
from list_node import *

def main():
    win = graphics(700, 400, "Animated Linked List")
    win.rectangle(0,0,700,400,'grey')
    array = []
    for line in sys.stdin:
        win.update_frame(2)
        line = line.split()
        for num in line:
            try:
                num = int(num)
            except:
                continue
            #  accounts for negative ints^
            array.append(num)
            head = create_head(sorted(array))
            linked_list = create_list(head, sorted(array))
            draw_list(array, win, num)
            print('After insertion, the list is now:', linked_list)


def create_head(array):
    '''
    Creates the head of the linked list

    array: sorted list of integer inputs
    '''
    head = ListNode(array[0])
    return head

def create_list(head, array):
    '''
    Creates the rest of the linked list by taking a sorted array
    of the integer inputs and creates a new list node object for
    each of them and connects them all together with the head node
    of the list.

    head: head of a linked list
    array: sorted list of integer inputs
    '''
    cur = head
    for x in range(1,len(array)):
        cur.next = ListNode(array[x])
        cur = cur.next
    return head

def draw_list(array, win, node):
    '''
    Draws the the linked list and spaces the nodes based on a
    calculated distance. Specifically draws circles, lines and
    text.

    array: sorted list of integer inputs
    win: graphics object for the canvas
    node: node to be inserted
    '''
    win.clear()
    win.rectangle(0,0,700,400,'grey')
    distance = 700 / (len(array) + 1)
    #  distance between nodes based on how many nodes there are
    #  to draw
    y = 200
    x = distance
    count = 0
    count_2 = 0
    for num in sorted(array):
        if len(array) > 1 and count != len(array) - 1:
            win.line(x + 25, y, x + 25 + distance, y, 'black', 5)
            count += 1
        if num == node and count_2 == 0:
            win.ellipse(x, y, 60, 60, 'green')
            win.ellipse(x, y, 50, 50, 'white')
            count_2 += 1
            #  an extra circle to highlight the inserted node
        else:
            win.ellipse(x, y, 50, 50, 'white')
        if len(str(num)) == 1:
            win.text(x - 5, y - 10, str(num), 'black', 20)
        elif len(str(num)) == 2:
            win.text(x - 10, y - 10, str(num), 'black', 20)
        elif len(str(num)) == 3:
            win.text(x - 15, y - 10, str(num), 'black', 20)
        else:
            win.text(x - 20, y - 20, str(num), 'black', 20)
        #  centers the text based on the length of it^
        x += distance
    win.update_frame(2)

main()


