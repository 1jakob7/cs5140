import numpy as np
import matplotlib.pyplot as plt
import time


n = 200

m = 300

def generate_rand_until_full(size):
    count = 0

    domain = dict()
    for i in range(size):
        domain[i] = 1
    rNum = np.random.randint(0, size)
    while len(domain) > 0:
        if rNum in domain:
            del domain[rNum]
        rNum = np.random.randint(0, size)
        count += 1
    return count

def plot_timed_experiments():
    fig, ax = plt.subplots(figsize=(8, 4))
    mList = list(range(1, 10002, 2000))
    for i in range(500, 2001, 500): # m
        timeCounts = []
        for j in mList: # n
            tic = time.perf_counter()
            for k in range(i):
                trialCounts.append(generate_rand_until_full(j))
            toc = time.perf_counter()
            timeCounts.append(toc - tic)
        ax.plot(mList, timeCounts, 'o-', label=f'm={i}')
    
    # tidy up the figure
    ax.grid(True)
    ax.legend(loc='right')
    ax.set_title('Timing Plots')
    ax.set_xlabel('range of random numbers - n')
    ax.set_ylabel('time taken to complete')

    plt.show()

if __name__ == '__main__':
    print(f'it took {generate_rand_until_full(n)} random trials')

    trialCounts = []

    # attempt 'm' experiments and record elapsed time
    tic = time.perf_counter()
    for i in range(m):
        trialCounts.append(generate_rand_until_full(n))
    toc = time.perf_counter()
    print(f'{m} experiments took {toc - tic:0.4f} seconds')

    fig, ax = plt.subplots(figsize=(8, 4))
    # plot cumulative histogram
    n, bins, patches = ax.hist(trialCounts, m, density=True, histtype='step', cumulative=True) #, label='Empirical')
    # tidy up the figure
    ax.grid(True)
    ax.legend(loc='right')
    ax.set_title('Cumulative (Step) Density Plot')
    ax.set_xlabel('required trials - k')
    ax.set_ylabel('fraction of experiments w/ filled domain after k trials')

    plt.show()

    estimate = sum(trialCounts) / m
    print('Expected number of k-random trials before generating every number: ' + str(estimate))

    # more timed experiments w/ increasing 'n' and 'm'
    plot_timed_experiments()