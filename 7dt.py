

d_eff_lsst = 6.423
d_lsst  = 8.4
d_7dt = 0.5
ro_7dt = 5.
ro_lsst = 2.


nexp_lsst = 2
etime_lsst = 15
lsst_sample = etime_lsst + ro_lsst

ntel_7dt = 20
sample_7dt = ntel_7dt * lsst_sample
etime_7dt = sample_7dt - ro_7dt

# comparison 
def relative_sn_17(source=False):

	source_lsst = 15
	sky_lsst = 15

	# 7dt telescopes start observing every 17 seconds
	
	source_7dt = 17
	sky_7dt = sample_7dt - ro_7dt

	if source:
		ans = numpy.sqrt(source_7dt / source_lsst)  * d_7dt/d_eff_lsst
	else:
		ans = source_7dt / source_lsst  / numpy.sqrt(sky_7dt/ sky_lsst) * d_7dt/d_eff_lsst
	return ans, 1/ans

relative_sn_17()
relative_sn_17(source=True)

def relative_sn_340(source=False):

	source_lsst = 15
	sky_lsst = 15

	# 7dt telescopes start observing every 17 seconds
	# first 20 observe n*17-5
	# 17 sum_n=1^20 n -20*5
	# ast 19 observe n * 17
	source_7dt = (20 + 9*20 + 10)*17 - 20*ro_7dt + 9*20 *17
	sky_7dt = 39*(sample_7dt - ro_7dt)

	if source:
		ans = numpy.sqrt(source_7dt / source_lsst)  * d_7dt/d_eff_lsst
	else:
		ans = source_7dt / source_lsst  / numpy.sqrt(sky_7dt/ sky_lsst) * d_7dt/d_eff_lsst
	return ans, 1/ans


relative_sn_340()
relative_sn_340(source=True)

def scintillation_noise():
	return ( numpy.sqrt((d_7dt / d_lsst)**(-4./3) / (etime_7dt/etime_lsst)),
		numpy.sqrt((numpy.sqrt(20)*d_7dt / d_lsst)**(-4./3) / (etime_7dt/etime_lsst))
		)

scintillation_noise()

