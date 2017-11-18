# PARAMETER FILE FOR CMB_LIKELIHOOD

# Basic run parameters
#debug_mode = True # or False. debug_mode prints lnL to .dat file in-loop, and prints time usage
debug_mode = False
nside      = 16
#lmax       = 5
lmax       = 47
band       = 53 # or 90, in GHz
#band       = 90

# Grid specifications
q_min      =   1.
q_max      =  50.
q_numpoint =  40
n_min      =  -1.
n_max      =   3.
n_numpoint =  40


# MCMC specifications
num_mcmc_iterations = 2*1e3
q_guess = 1
n_guess = -1
q_step = (q_max - q_min)/q_numpoint
n_step = (n_max - n_min)/n_numpoint


# Input and output file paths
cmbfile    = 'data/cobe_dmr_%dGHz_n%d.npy'%(band,nside)
beamfile   = 'data/cobe_dmr_beam.npy'
pixwinfile = 'data/pixwin_n%d.npy'%nside

resultfile = 'cobe_dmr_%dghz_lnL.npy'%band


