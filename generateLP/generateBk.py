import sys
import scipy.stats as stats

Btype=sys.argv[1]
K=3785

if Btype=='ones':
  vals=[1]*K
  f=open('../../small_dataset/Bk_ones.csv', 'w+')
  for v in vals:
    f.write(str(v) + '\n')
else:
  Bminus=float(sys.argv[2])
  Bplus=float(sys.argv[3])

  mu=(Bplus+Bminus)/2.0
  sigma=(Bplus-Bminus)/6.0
  dist=stats.truncnorm((Bplus-mu)/sigma, (Bminus-mu)/sigma, loc=mu, scale=sigma)
  vals=dist.rvs(K)
  f=open('../../small_dataset/Bk_' + str(Bminus) + '_' + str(Bplus) + '.csv', 'w+')
  for v in vals:
    f.write(str(v) + '\n')
