import numpy as np
import matplotlib.pyplot as plt
import sys


if __name__ == '__main__':
    if len(sys.argv)<2:
        print 'Wrong number if input arguments.'
        print 'Usage: python plot_mcmc.py resultfile.npy'
        sys.exit()

    # Get file data
    inputfile = sys.argv[1]
    
    # Load file
    a = np.load(inputfile)

    # Decompose
    q_values = a[0,:]
    n_values = a[1,:]
    #lnL = a[2:,:]  # won't really be neeing this, will we.. 

    # 
    num_q_values = len(q_values)
    num_n_values = len(n_values)

    print "len(q_values): %g" % (num_q_values)
    print "len(n_values): %g" % (num_n_values)

    #print Q_values

    res = 30.

    #
    q_steps = int(float(num_q_values)/res)
    n_steps = int(float(num_n_values)/res)

    #dq = float(num_q_values)/q_steps
    #dn = float(num_n_values)/n_steps

    min_q = np.min(q_values)
    print "min_q: %g" % (min_q)
    max_q = np.max(q_values)
    print "max_q: %g" % (max_q)

    min_n = np.min(n_values)
    print "min_n: %g" % (min_n)
    max_n = np.max(n_values)
    print "max_n: %g" % (max_n)

    q = np.linspace(min_q, max_q, q_steps)
    n = np.linspace(min_n, max_n, n_steps)
    
    dq = q[1] - q[0]
    dn = n[1] - n[0]

    dist = np.zeros((q_steps, n_steps))
    
    for i in range(num_q_values):
        q_index = np.argmin(np.abs(q-q_values[i]))
        n_index = np.argmin(np.abs(n-n_values[i]))
        
        dist[q_index, n_index] += 1.
    

    # Numerical integration .. really hard work..
    #dist /= num_q_values*dq
    q_dist = np.sum(dist, axis=0)
    n_dist = np.sum(dist, axis=1)

    # Normalize
    q_dist = q_dist / (np.sum(q_dist)*dq)
    n_dist = n_dist / (np.sum(n_dist)*dn)

    # 
    plt.pcolor(q, n, dist)
    plt.title("Distribution of Q and n values")
    plt.xlabel("n")
    plt.ylabel("Q")
    plt.colorbar()
    plt.show()

    # 
    plt.plot(n, n_dist)
    plt.title("Distribution of n values")
    plt.xlabel("n")
    plt.ylabel("P(n)")
    plt.show()

    # 
    plt.plot(q, q_dist)
    plt.title("Distribution of Q values")
    plt.xlabel("Q")
    plt.ylabel("P(Q)")
    plt.show()








