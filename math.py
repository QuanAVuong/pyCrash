# 1 Find the probabilities of the following rocks rounded to the nearest hundredth:
rocks = {
  "sedimentary": 58,
  "metamorphic": 213,
  "igneous": 522,
}
# Expected ouput:
#  There is 0.07 probability of the sedimentary rock 
#  There is 0.27 probability of the metamorphic rock 
#  There is 0.66 probability of the igneous rock 

[ print(f" There is {round( value / sum(rocks.values() ), 2)} probability of the {key} rock ")
    for key, value in rocks.items() ]


# 2 X is a discrete random variable. The table below defines a probability distribution for X. What is the expected value of X?

x = [10, 20, 30, 40]
p = [.2, .3, .15, .35]
e = 0

for x, p in zip(x, p):
    print(f"{x} * {p} = {x*p} + ")
    e += x*p     
print(f"Expected Value: {e}")


# 3 Find standard deviation given mean and pdf
from math import sqrt 
pdf = {
    200: .999,
    -99800: .001,
}

e = 100
variance = 0

for rv, p in pdf.items():
    variance += (rv - e)**2 * p
print(sqrt(variance))


# 4 Calculate & Plot Normal Cumulative Distribution Function
# print(norm.__doc__)
# https://docs.scipy.org/doc/scipy/reference/tutorial/stats.html
# https://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.stats.norm.html
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.rv_continuous.html#scipy.stats.rv_continuous
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.truncnorm.html
from scipy.stats import truncnorm, norm
import matplotlib.pyplot as plt

def normalCdf(lower=truncnorm.a, upper=truncnorm.b, mean=0, sd=1):
	X = truncnorm( (lower - mean) / sd,
									(upper - mean) / sd,
									loc=mean, scale=sd )

	N = norm(loc=mean, scale=sd)
	truncdf = N.cdf(upper) - N.cdf(lower)
	print(truncdf)

	fig, ax = plt.subplots(2, sharex=True)
	ax[0].hist(N.rvs(1000000), normed=True)
	ax[1].hist(X.rvs(1000000), normed=True)

	xmin, xmax = plt.xlim()
	ymin, ymax = plt.ylim()

	plt.annotate(f"CDF= {truncdf}", xy=(upper, .5*ymax), xytext=(upper + (xmax - xmin)/4, .75*ymax),
								arrowprops=dict(facecolor="red", shrink=0.05, connectionstyle="angle3") )

	plt.show()

normalCdf(-999999, 0, 8, 10)
