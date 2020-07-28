# Chatper 2
## General notes

There are two basic ways to store mutliple items: arrays and linked lists.

The position of an element is called the **index**, so correct terminology would be "20 is at index 1"

Run times for common operations:

        | Arrays | Lists
Reading|O(1)|O(n)
Insertion|O(n)|O(1)

key: O(n) - will take as many steps as elements of data | O(1) - will take the same number of steps no matter how large the number of elements.

 To break down this table, assume we have a lot of data (elements): It is very fast to either read an array or insert into a list, but it would take a lot longer (with lots of data) to either read all the items of a list or insert into an array.

We can extend the table with deletion too, it follows the same rule as insertion.

        | Arrays | Lists
Reading|O(1)|O(n)
Insertion|O(n)|O(1)
Deletion|0(n)|)(1)

Arrays are used a lot more because they allow random access. There are two types of access: *random access* and *sequential access*. Linked lists can only do sequential access.

### Arrays

Stored in memory consequtively and if size of array outgrows memory space allocated, all items must be moved to new allocated memory (computationally expensive). This will keep happening if the array size increases above the allocated size.

You know where all items in an array are stored and therefore you can read random elements effortlessly and easily.

### Linked Lists

Items can be anywhere in memory, with the pervious item contianing the address of the next item. It's like a treasure hunt, you go to the first address and then it tells you where the next is (and so on.)

You remove the issue of not having enough consequtive memory to allocate an array with a linked list. 

The problem with linked lists is if you don't want to be looking through the whole list, you don't have a choice. You have to keep jumpoing from item 1 to 2 to 3...until you get the 10th item.

Linked lists are okay if you are reading all items as well, they are a lot slower on random reads for the reasons set out above.

Lists are also better for inserations in the middle as you can just change where the previous item points to. The same goes for deleting
