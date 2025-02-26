import numpy as np

def fractions(start, end, sum_func):
    values = np.arange(start, end)
    return sum_func(1 / values)
    #21.300481501347903 for 1.000.000.000
    #1.000.000.000 in c: 21.30048150134 85497843248595017939805984497070312500000000000000000
    #10.000.000.000 in c: 21.6441175934619209897391556296497583389282226562500000000000000000



def custom_sum(values):
    return np.sum(values)

def main():
    start = 1
    end = 1_000_000_000
    result = fractions(start, end, custom_sum)
    print(result)

if __name__ == "__main__":
    main()