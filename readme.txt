A brainfuck macro-language implementation of the algorithm described here:

    http://tapestryjava.blogspot.se/2013/02/crafting-code-in-clojure.html

n.b. this gleefully misses the point of the post.


What this program does:

    reads a bunch of key:value pairs from stdin
    keep the keys and throw away the values
    sort the keys
    throw out duplicate keys
    print the keys, separated by ", "
    but, if there are no keys, instead print "<none>"

Implementation details:

*   keys and values must not contain the following characters: ' ', ':', '\n'
*   the ':' character is used to bind keys to values, ie "key:value"
*   the ' ' and '\n' characters are used to separated key:value pairs
*   the maximum length of a key is 15 characters
*   sorting is done via bubble sort, so this will be excruciatingly slow
    for more than a small handful of input keys.

See also the comments on HN:

    http://news.ycombinator.com/item?id=5153467

This source is compiled to brainfuck using:

    https://github.com/fcostin/abfc_hs

