"""

markov.py

NTH-ORDER MARKOV CHAIN IMPLEMENTATION

Author: Michael A. Knyszek

"""

import random, shlex

class Markov:
    """An nth-Order Markov Chain class with some lexical processing elements."""
    def __init__(self, delim, order):
        """Initialized with a delimiting character (usually a space) and the order of the Markov chain."""
        self.states = {}
        self.delim = delim
        if order > 0:
            self.order = order
        else:
            raise Exception('Markov Chain order cannot be negative or zero.')

    def init_chain(self):
        """Helper function to generate the correct initial chain value."""
        init = []
        for i in range(self.order):
            init.append('');
        return tuple(init)

    def step(self, a, e):
        """Helper function that pops the end of tuple 'a' and tags on str 'e'."""
        d = a[1:] + (e,)
        return d
    
    def learn(self, sample):
        """Adds states to the dictionary; works best with sentences."""
        prev = self.init_chain()
        tokens = sample.split(self.delim)
        for t in tokens:
            if not prev in self.states:
                self.states[prev] = []
            curr = self.step(prev, t)
            self.states[prev].append(curr)
            prev = curr

    def learn_file(self, url):
        """Parses a text document sentence-wise using shlex and 'learns' each sentence."""
        f = open(url, 'r')
        s = shlex.shlex(f)
        t = s.get_token()
        sent = ''
        while t != None and t != '':
            t = t.replace('"', '').replace("'", '') \
                .replace('(','').replace(')','').replace('[','') \
                .replace(']','')
            if t.endswith('.') or t.endswith('!') or t.endswith('?'):
                sent = sent + t
                sent = sent + self.delim
                self.learn(sent)
                sent = ''
            else:
                sent = sent + t
                sent = sent + self.delim
            t = s.get_token()
        f.close()

    def query(self):
        """Queries the Markov chain with the default seed (defined by init_chain)."""
        tmp = self.init_chain()
        t = self.states[tmp][random.randint(0, len(self.states[tmp])-1)]
        sent = ''
        first = True
        while t in self.states and t != tmp and t != None:
            if not first:
                sent = sent + self.delim
            sent = sent + t[len(t)-1]
            t = self.states[t][random.randint(0, len(self.states[t])-1)]
            first = False
        return sent + self.delim + t[len(t)-1]

    def ask(self, seed):
        """Queries the Markov chain with the seed of your choice (make sure it is an n-element list/tuple where n is the order of the chain)."""
        tmp = seed
        if not tmp in states:
            tmp = self.init_chain()
        t = self.states[tmp][random.randint(0, len(self.states[tmp])-1)]
        sent = ''
        first = True
        while t in self.states and t != tmp and t != None:
            if not first:
                sent = sent + self.delim
            sent = sent + t[len(t)-1]
            t = self.states[t][random.randint(0, len(self.states[t])-1)]
            first = False
        return sent + self.delim + t[len(t)-1]
