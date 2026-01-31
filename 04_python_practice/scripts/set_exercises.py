from collections import defaultdict

def unique_words(s):
    return set(s.lower().split(' '))
assert unique_words("Red red BLUE blue") == {"red","blue"}


def is_pangram(s):
    return set(s.replace(' ', '').lower()) == set('abcdefghijklmnopqrstuvwxyz')
assert is_pangram("The quick brown fox jumps over a lazy dog")

def disjoint(a_tags, b_tags):
    return a_tags.isdisjoint(b_tags)
assert disjoint({"sql","python"}, {"go"}) is True
assert disjoint({"sql","python"}, {"python","go"}) is False

def set_ops(a: set, b: set):
    """Return dict with union, intersection, diff_a_b, diff_b_a, symdiff."""
    return {"union": a.union(b),
            "intersection": a.intersection(b),
            "diff_a_b": a.difference(b),
            "diff_b_a": b.difference(a),
            "symdiff": a.symmetric_difference(b)}
d = set_ops({1,2,3},{3,4})
assert d["union"] == {1,2,3,4} and d["symdiff"] == {1,2,4}

def dedupe_keep_first(xs):
    out, seen = [], set()
    for x in xs:
        if x not in seen:
            out.append(x)
            seen.add(x)  
    return out
assert dedupe_keep_first([1,2,1,3,2,4]) == [1,2,3,4]


def invert_index(items):
    """
    items: list of (item_id, tags_iterable).
    Return dict: tag -> set({item_id,...})
    """
    dct = defaultdict(set)
    for value, letters in items:
        for letter in letters:
            dct[letter].add(value)
    return dct
ii = invert_index([(1,{"a","b"}),(2,{"b"}),(3,{"a"})])
assert ii == {"a":{1,3}, "b":{1,2}}


def canonical_edge(a, b):
    """Return frozenset representing undirected edge."""
    return frozenset((a, b))
assert canonical_edge("A","B") == frozenset({"A","B"})

def first_missing_positive(xs):
    """Return smallest missing positive integer."""
    xs = list(filter(lambda x: x>0, xs))
    return min(list(set([x for x in range(min(xs), max(xs)+1)]) - set(xs)))
assert first_missing_positive([3,4,-1,1]) == 2
assert first_missing_positive([1,2,0,5]) == 3

def has_triangle(edges):
    """
    edges is iterable of pairs (u,v). Return True if there exists
    a triangle u-v-w-u. Use sets for adjacency.
    """ 
    # Build adjacency list using sets
    adj = {}
    for u, v in edges:
        if u not in adj:
            adj[u] = set()
        if v not in adj:
            adj[v] = set()
        adj[u].add(v)
        adj[v].add(u)
    
    # Check for triangles: for each edge (u,v), check if they have a common neighbor
    for u, v in edges:
        # Find common neighbors of u and v
        if adj[u] & adj[v]:  # Set intersection
            return True
    
    return False
assert has_triangle([("a","b"),("b","c"),("c","a")]) is True
assert has_triangle([("a","b"),("b","c")]) is False