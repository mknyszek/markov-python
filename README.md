markov-python
=============

A simple implementation of an nth-order markov chain generator in Python.

markov.py should be compatible with Python 2.7+ and 3.0+, though any version of Python with shlex should work alright.

Step 1
-------

Import the module. (naturally)

Ex: <code>import markov</code>

Step 2
-------

Create a Markov object with desired delimiter and order.

Ex: <code>w = markov.Markov(' ', 2)</code> (Sets up a 2nd order markov chain with a space as the delimiter)

Step 3
-------

Teach your Markov object.

Ex: Input text data <code>w.learn("the quick brown fox jumps over the lazy dog")</code>

Ex: Read text data from a file <code>w.learn_file("kingjames.txt")</code>

Step 4: 
-------

Query your Markov object!

Ex: Query using standard empty seed <code>w.query()</code>
  
Ex: Query with a specific seed <code>w.ask(["jumps", "over"])</code>
