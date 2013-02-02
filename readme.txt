sorted_key_list.bf
==================

A brainfuck macro-language implementation of the algorithm described here:

    http://tapestryjava.blogspot.se/2013/02/crafting-code-in-clojure.html

(n.b. this gleefully misses the point of the post).


What it does
------------

1.  read a bunch of key:value pairs from stdin
2.  keep the keys and throw away the values
3.  sort the keys
4.  throw out duplicate keys
5.  print the keys, separated by ", ", ...
6.  ... but, if there are no keys, instead print "<none>"


Example
-------

    (assumes "apt-get install bf" ...)

    $ cat input.txt 
    fred:true wilma:false
    wilma:true
    fred:false barney:true
    thelma:true
    barney:false
    shaggy:true

    $ cat input.txt | bf sorted_key_list.bf 
    barney, fred, shaggy, thelma, wilma


Implementation details / limitations
------------------------------------

*   keys and values must not contain the following characters: ' ', ':', '\n'
*   the ':' character is used to bind keys to values, ie "key:value"
*   the ' ' and '\n' characters are used to separated key:value pairs
*   the maximum length of a key is 15 characters
*   sorting is done via bubble sort, so this will be excruciatingly slow
    for more than a small handful of input keys.


See also the comments on HN
---------------------------

    http://news.ycombinator.com/item?id=5153467

This source is compiled to brainfuck using
------------------------------------------

    https://github.com/fcostin/abfc_hs

