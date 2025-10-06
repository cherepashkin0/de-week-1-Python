from functools import reduce


def window_sums(xs, k):
    """Return sums for each contiguous window of length k."""
    lst = []
    for i in range(len(xs)-k+1):
        sm = sum(xs[i:i+k])
        lst.append(sm)
    return lst

def window_sums2(xs, k):
    """Return sums for each contiguous window of length k."""
    # Generate all windows of length k
    windows = map(lambda i: xs[i:i+k], range(len(xs)-k+1))
    # Sum each window
    return list(map(sum, windows))

def calc_tax(lst):
    return reduce(lambda x, acc: acc + x, map(lambda x: x[0]*x[1], lst), 0)

def main():
    # window_sums(xs, k)
    assert window_sums([1,2,3,4,5], 3) == [6,9,12]
    assert window_sums([1,2], 3) == []
    assert calc_tax([(50000, 0.08), (100000, 0.10), (150000, 0.15)]) == 36500.0

if __name__ == "__main__":
    main()
