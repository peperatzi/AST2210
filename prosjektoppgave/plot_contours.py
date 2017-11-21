# Simple contour plotting script for visualizing the lnL computed by
# cmb_likelihood.py. 
# For convenience, it takes as input either the .npy file or the .dat file.
# In the .dat case you also have to supply the number of grid points in each 
# direction so that we can define the grid correctly.

import numpy as np
import matplotlib.pyplot as plt
import sys

if __name__ == "__main__":
    if len(sys.argv)<2:
        print 'Wrong number if input arguments.'
        print 'Usage: python plot_contours.py resultfile.npy'
        print 'Or: python plot_contours.py resultfile.dat numpoints_Q numpoints_n'
        sys.exit()

    inputfile1 = sys.argv[1]
    if inputfile1[inputfile1.rfind('.'):]=='.npy':
        a = np.load(inputfile1)
        Q_values = a[0,:]
        n_values = a[1,:]
        lnL = a[2:,:]
        qgrid1, ngrid1 = np.meshgrid(Q_values,n_values, indexing='ij')

    inputfile2 = sys.argv[2]
    if inputfile2[inputfile2.rfind('.'):]=='.npy':
        a = np.load(inputfile2)
        Q_values = a[0,:]
        n_values = a[1,:]
        lnL = a[2:,:]
        qgrid2, ngrid2 = np.meshgrid(Q_values,n_values, indexing='ij')


    lnL -= np.amax(lnL) # arbitrarily "normalizing" to make the numbers more manageable

    # For a Gaussian distribution, the 1, 2 and 3 sigma (68%, 95% and
    # 99.7%) confidence regions correspond to where -2 lnL increases by
    # 2.3, 6.17 and 11.8 from its minimum value. 0.1 is close to the
    # peak. 
    fig, ax = plt.subplots()

    my_levels = [0.1, 2.3, 6.17, 11.8]
    cs1 = ax.contour(qgrid1,ngrid1, -2.*lnL, levels=my_levels, colors='r')
    ax.clabel(cs1, inline=1, fontsize=10)
#    plt.hold("on")
    cs2 = ax.contour(qgrid2,ngrid2, -2.*lnL, levels=my_levels, colors='g')
    ax.clabel(cs2, inline=1, fontsize=10)
    #plt.grid()

    #plt.legend(['$50 \ GHz$', '$90 \ GHz$'])

    lines = [ cs1.collections[0], cs2.collections[1]]
    labels = ['50 GHz','90 Ghzs']
    plt.legend(lines, labels)


    plt.show()




