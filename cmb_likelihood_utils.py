# ****************************************************************
#       Utility module for cmb_likelihood.py
# ****************************************************************
#
#   The module contains the following functions, usage being
#   returned_quantity = function(arguments)
#
#  +    N_cov    = get_noise_cov(rms)
#       F_cov    = get_foreground_cov(x,y,z)
#  +    C_ell    = get_C_ell_model(Q,n,lmax)
#       polys    = get_legendre_coeff(lmax)
#       P_ell_ij = get_legendre_mat(lmax,x,y,z)
#  +    S_cov    = get_signal_cov()
#  +    lnL      = get_lnL()
#
#
#  Routines marked by (*) are only partially implemented, and must be completed
#  before the program becomes functional.
#

import numpy as np
from scipy.special import legendre
import scipy.linalg as spl
from scipy.special import factorial
from scipy.special import gamma

def get_noise_cov(rms):
    """
    To be completed: (DONE!)
    Compute the noise covariance matrix from the pixel standard deviations
    """
    # 1: Compute a matrix with element (i,i) = sigma_i^2

    #N_cov = (rms**2)*np.kron(len(rms),len(rms))
    N_cov = np.diag(np.power(rms,2))

    # Test cov
    #for i in range(len(N_cov)):
    #    for j in range(len(N_cov[0])):
    #        val = N_cov[i,j]
    #        if i!=j and val!=0:
    #            print "ZERO DETECTED!"
    #        if i==j:
    #            print val

    return N_cov


def get_foreground_cov(x,y,z):
    """
    Computing the foreground template covariance matrix, to marginalize over
    any monopole and dipole components in the map
    F_cov = large_value * sum(template_cov), where
    template_cov = np.outer(f, f^t). 
    For the monopole template, f is a constant.
    To account for a dipole of any orientation, we use each of the unit vector 
    components as a dipole template.
    """
    large_value = 1.0e3
    monopole = np.ones((len(x),len(x)))
    dipole = np.outer(x,x) + np.outer(y,y) + np.outer(z,z)
    return large_value * (monopole + dipole)

#def gamma(n):
#    return factorial(n-1)

def get_C_ell_model(Q,n,lmax):
    """
    To be completed:
    Recursively compute a model power spectrum, C_ell, given the amplitude and
    spectral index parameters Q and n, on the range ell in [0,lmax],
    but with monopole and dipole terms set to 0.
    """
    # 1: Define array for power spectrum
    C_ell = np.zeros(lmax+1)
    # 2: Compute quadrupole (ell=2) term
    C_ell[2] = 4.*np.pi/5.*np.power(Q,2)

    #d 3: Compute multipoles 3 through lmax recursively
    for l in range(3,lmax+1):
        C_ell[l] = C_ell[l-1]*(2.*l + n-1.)/(2.*l+5.-n)

    return C_ell

def get_legendre_coeff(lmax):
    '''
    Helper routine for get_legendre_full. Computes Legendre polynomial
    coefficients for each multipole l, using scipy.special.legendre.
    Stores the result in a list of poly1d objects.
    Each such object returns the polynomial value when called with a 
    cos(theta) argument: P_ell = pol[l](costheta)
    '''
    leg = []
    for l in range(lmax+1):
        leg.append(legendre(l))
    return leg

def get_legendre_mat(lmax,x,y,z):
    '''
    Computing the full set of Legendre polynomial values needed to build the 
    signal covariance matrix.
    Uses helper function get_legendre_coeff for polynomial coefficients, and
    assembles a matrix of dimensions (ndata, ndata, lmax+1)
    '''
    leg = get_legendre_coeff(lmax)
    pos_vec = np.vstack([x,y,z]).T
    costheta =  np.dot(pos_vec,pos_vec.T)

    ndata = len(x)
    p_ell_ij = np.zeros((ndata,ndata,lmax+1))
    for l in range(lmax+1):
        p_ell_ij[:,:,l] = leg[l](costheta)
        
    return p_ell_ij


def get_signal_cov(C_ell, beam, pixwin, p_ell_ij):
    '''
    To be completed:
    Compute a (ndata,ndata) signal covariance matrix using the
    model power spectrum, instrument beam and pixel window function, and
    precomputed Legendre polynomials as input

    Hint: This can be done using a triple for-loop, but it is not necessary.
    Using NumPy array operations may get you a significant speed-up.
    '''
    lmax = len(C_ell) - 1


    #print S_cov

    # The "lamer-way":
    #S_ij = np.zeros_like(p_ell_ij[:,:,0])
    #for i in range(len(S_ij)):
    #    for j in range(len(S_ij[0])):
    #        for l in range(lmax):
    #            S_ij[i,j] += (2.0*l + 1)*((beam[l]*pixwin[l])**2)*C_ell[l]*p_ell_ij[i,j,l]
    #print S_ij

    # The "dude-way":
    S_cov = np.zeros_like(p_ell_ij[:,:,0])
    #l = np.arange(lmax+1)
    for l in range(lmax):
        S_cov[:,:] += (2.*l + 1.)*(np.power(beam[l]*pixwin[l],2))*C_ell[l]*p_ell_ij[:,:,l]

    S_cov /= (4.*np.pi)

    #print S_cov


    # Test S_cov
    #for i in range(len(S_cov)):
    #    for j in range(len(S_cov[0])):
    #        val = S_cov[i,j]
    #        if i!=j:
    #            print val


    # Debugging the size of the matrix
    #print "Size of S_ij-matrix: %gx%g" % (len(S_cov),(len(S_cov[0])))

    # 1: Compute all the elements of the sum over ell, as arrays

    # 2: Assemble a single array with all the ell terms which are independent of (i,j)

    # 3: Compute the covariance matrix by an appropriate inner product

    return S_cov

def get_lnL(data, cov):
    '''
    To be completed:
    Compute the quantity -2*lnL using the complete covariance matrix
    C = S+N+F, and the input data vector.

    Hint: This can be done directly by inverting the covariance matrix
    and computing a determinant, calling suitable NumPy or SciPy routines.
    Significant speedup can be gained by rather using the Cholesky decomposition
    method discussed in the project description notes.
    '''

    #print "Coveriance-matrix in get_lnL():"

    # Test cov
    #for i in range(len(cov)):
    #    for j in range(len(cov[0])):
    #        val = cov[i,j]
    #        if val==0:
    #            print "ZERO DETECTED!"
    #        if i==j and val<=0:
    #            print "DIAGONAL VALUES FAILD!"

    # 1: Cholesky-decompose C into a lower triangular matrix L, using scipy.linalg.cholesky
    L = spl.cholesky( cov )

    # 2: Compute log(det(C)) from L
    logdet = np.linalg.slogdet(L)[1]*2

    # 3: Solve for L^-1 d using scipy.linalg.solve_triangular
    x = spl.solve_triangular(L, np.identity(len(L)))

    # 4: Assemble -2*lnL using the components just computed
    C_inv = np.dot(np.transpose(x),x)
    d_C_d = np.dot(np.transpose(data),np.dot(C_inv,data))
        
    result = (d_C_d + logdet)

    print "Result = %g" % (result)

    return result

