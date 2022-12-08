# day 7 notes

`7:46pm: after two unsuccessful attempts`

I'm definitely overcomplicating my solution.
the input itself is an ordered, DFS traversal of a tree.
the task is to build a correct tree out of the traversal output.

(I have the sum algorithm already ok -- I think-- but that assumes a CORRECT file tree.)

the reason my solution is incorrect -- I think -- is 
because I missed the fact that directory names are NOT unique. 

and the anytree/Node datastructure uses the name as a unique identifier. so I think I'm overwriting nodes and parents as soon as I encounter a dir (like `lcgv`) a second, third time in a different place in the tree.

the long input has 200 directory names. 
what if I just manually changed the names of all the duplicates? 
to ensure that all 200 dir names are unique? 

part one, at least, doesn't care about tracking dir names, just the size counts. 


There are 5 dirs used multiple times:
```
Dir lcgv was seen 15 times.
Dir nmbfwc was seen 6 times.
Dir wqdlv was seen 14 times.
Dir zmflq was seen 10 times.
Dir rfzrwc was seen 8 times.
```