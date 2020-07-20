# Chatper 2
## General notes

There are two basic ways to store mutliple items: arrays and linked lists.

### Arrays

Stored in memory consequtively and if size of array outgrows memory space allocated, all items must be moved to new allocated memory (computationally expensive). This will keep happening if the array size increases above the allocated size.

You know where all items in an array are stored and therefore you can read random elements effortlessly and easily.

### Linked Lists

Items can be anywhere in memory, with the pervious item contianing the address of the next item. It's like a treasure hunt, you go to the first address and then it tells you where the next is (and so on.)

You remove the issue of not having enough consequtive memory to allocate an array with a linked list. 

The problem with linked lists is if you don't want to be looking through the whole list, you don't have a choice. You have to keep jumpoing from item 1 to 2 to 3...until you get the 10th item.


