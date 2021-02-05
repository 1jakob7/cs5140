import numpy as np
import matplotlib.pyplot as plt
import time


n = 3000 # range of random numbers

m = 200 # number of experiments

def generate_rand_until_match(range):
    count = 0
    numbers = dict()
    rNum = np.random.randint(0, range+1)
    while rNum not in numbers.keys():
        numbers[rNum] = 1
        count += 1
        rNum = np.random.randint(0, range+1)
    return count

def plot_timed_experiments():
    fig, ax = plt.subplots(figsize=(8, 4))
    mList = list(range(100000, 1000001, 100000))
    for i in range(3000, 9001, 3000): # m
        timeCounts = []
        for j in mList: # n
            tic = time.perf_counter()
            for k in range(i):
                trialCounts.append(generate_rand_until_match(j))
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
    #print('it took: ' + str(generate_rand_until_match()) + ' random trials')
    trialCounts = []

    # attempt 'm' experiments and record elapsed time
    tic = time.perf_counter()
    for i in range(m):
        trialCounts.append(generate_rand_until_match(n))
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
    ax.set_ylabel('fraction of experiments w/ collision after k trials')

    plt.show()

    estimate = sum(trialCounts) / m
    print('Expected number of k-random trials before collision: ' + str(estimate))

    # more timed experiments w/ increasing 'n' and 'm'
    plot_timed_experiments()