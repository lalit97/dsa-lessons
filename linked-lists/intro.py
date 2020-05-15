
Time / Space 

CA  

| Information | | x| y| z| 1  |2 | 3  |4  |5 | 6| | | | | | | | |
200 |  204  |208| 212 |216 |220| 224

Hard disk -> 100 GB 
RAM -> 8 GB
Segmentation


Array -> contiguous memory locations 

arr = [1,10,2,3,4,5] -> 200 
arr[3]  O(1)

insertion -> O(n)
deletion -> O(n)

use: fixed amount of data
######################################################################
Linked list --> 

use: when amount of data is not fixed 
random memory locations 

linked_list = {1,2,3,4}
next, prev 

| |(1, 220)| | | |(2, 254) | | | | |(3, 300) |  (4, 408)|   |    |     |    5, |
  204            220                254        300                         408
  (head) 

loss -> random access not present
linkedlist[3]  O(n)

from begging
insertion -> O(1)
deletion -> O(1)