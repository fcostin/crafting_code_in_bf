sorted\_key\_list.bf
==================

A brainfuck macro-language implementation of the algorithm described here:

<http://tapestryjava.blogspot.se/2013/02/crafting-code-in-clojure.html>

This demonstrates that the job can be done trivially as a one-liner in brainfuck:

    $ wc -l sorted_key_list.bf 
    1 sorted_key_list.bf
    $ wc -c sorted_key_list.bf 
    112848 sorted_key_list.bf


What it does
------------

1.  reads a bunch of key:value pairs from stdin
2.  keep the keys and throw away the values
3.  sort the keys
4.  throw out duplicate keys
5.  print the keys, separated by `", "`, ...
6.  ... but, if there are no keys, instead print `<"none>"`


Example
-------

Assuming you have `apt-get install bf` or similar:

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

*   keys and values must not contain the following characters: `' '`, `':'`, `'\n'`
*   the `':'` character is used to bind keys to values, ie `"key:value"`
*   the `' '` and `'\n'` characters are used to separate `"key:value"` pairs
*   the maximum length of a key is 15 characters
*   sorting is done via bubble sort, so this will be excruciatingly slow
    for more than a small handful of input keys.


See also
--------

*   [discussion on HN](http://news.ycombinator.com/item?id=5153467)
*   [abfc\_hs (used here to generate bf code from macros)](https://github.com/fcostin/abfc_hs)

