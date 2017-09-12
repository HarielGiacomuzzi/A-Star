/**********************************************************************
 *  Hyrule's maze readme.txt template
 **********************************************************************/


Name: Hariel Giacomuzzi
Student ID: 1314441-4


Hours to complete assignment (optional): 4 Days


/**********************************************************************
 *  Explain briefly how you implemented the datatype for states.
 **********************************************************************/
the states are represented as a list of nodes that I must explore plus a list of nodes that does not matter any more.




/**********************************************************************
 *  Explain briefly how you represented a search node
 *  (state + number of moves + previous search node).
 **********************************************************************/

the search node is a class created by me for reasons of commodity and it cary the suns of a node as well as his father and the distance from that node to the goal as well as the X and Y positions.





/**********************************************************************
 *  Explain briefly how you detected unsolvable problems.
 **********************************************************************/


I have runned the algorithm and as since as there's no connection to the nodes wich leaves to the goal I stopped 


/**********************************************************************
 *  If you wanted to solve random $10^6$ problem, which would you 
 * prefer:  more time (say, 2x as much), more memory (say 2x as much), 
 * a better priority queue (say, 2x as fast), or a better priority 
 * function (say, one on the order of improvement from Hamming to 
 * Manhattan)? Why?
 **********************************************************************/


probably a more time because priority queue is not soo hard to optimaze and more memory will in most cases not be as usefull as a good algorithm



/**********************************************************************
 *  If you did the extra credit, describe your algorithm briefly and
 *  state the order of growth of the running time (in the worst case)
 *  for isSolvable().
 **********************************************************************/

As i worked on the algorithm i notice that if we put the next movements in such fashion that it will be at least kind of ordered this can make the algorithm a lot faster and as the running time was fast enought I decide to use this in the get sovable method, since the algorithm will stop as soon as it notice that the player is on a dead end. and as it is the simple implementation of the A* with a few improvments the O notation stills the same but with the mark of most of times pull this mark of O(lgH(n)) where H is the heuristic function and the n is the cost from the start point to the objective.


/**********************************************************************
 *  Known bugs / limitations.
 **********************************************************************/

The implementation I provided probably has some for loops that can be optimazed but don't have enough time to make this

/**********************************************************************
 *  Describe whatever help (if any) that you received.
 *  Don't include readings, lectures, and precepts, but do
 *  include any help from people (including staff, classmates, and 
 *  friends) and attribute them by name.
 **********************************************************************/

I have talked a lot With Leonardo Gubert, Matheus Redecker and also with Lucas Schuler, but in most we talked about how to make the algorithm runs faster until I figure out a little trick that make my code runs in 1.2 seconds in a 500x500 problem, in the end the trick was to get a ordered list of next movements while inserting it on the queue.



/**********************************************************************
 *  Describe any serious problems you encountered.                    
 **********************************************************************/

don't find any problem at all, in the end the biggest problem was optmization but I was able to make it faster


/**********************************************************************
 *  List any other comments here. Feel free to provide any feedback   
 *  on how much you learned from doing the assignment, and whether    
 *  you enjoyed doing it.                                             
 **********************************************************************/

 the only thing i think was odd was to understood the professors implementation of methods and how to use it but reading the description a lot of time I was able (or at least I think i was) to figure out.
