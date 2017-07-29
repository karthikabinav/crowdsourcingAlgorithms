import sys
import scipy.stats as stats

dist=sys.argv[1]
T=int(sys.argv[2])
J=0
f=open('../../small_dataset/RHSvertices_withTags.csv', 'r')
for line in f:
  J+=1
print J
if dist =='uniform':
  pjt=[1.0/(J)]*J*T  
  f=open('../../small_dataset/pjt_uniform.csv', 'w+')
  for p in pjt:
    f.write(str(p) + '\n')
else:
  a=1
  b=100
  nop=float(sys.argv[3])
  mu=(a+b)/2.0
  sigma=(b-a)/6.0

  dist2=stats.truncnorm((b-mu)/sigma, (a-mu)/sigma, loc=mu, scale=sigma)
  vals=dist2.rvs(J*T)
  
  sums=list()
  c=0
  csum = 0
  for v in vals:
    if c==J:
      sums.append(csum)
      csum=0
      c=0
    csum+=v
    c+=1
  sums.append(csum)
  pjt=list()
  c=0
  for v in vals:
    pjt.append(v/(sums[c/J]+nop))
    c+=1

  f=open('../../small_dataset/pjt_normal_' + str(nop) + '.csv', 'w+')
  for p in pjt:
    f.write(str(p) + '\n')
