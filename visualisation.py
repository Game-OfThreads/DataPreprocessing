import matplotlib.pyplot as plt
import numpy as np

estimated = [0.040006721,0.072009505,0.060010082,0.068014691,0.368216511,0.592666157,0.220065139,0.092022453,0.504478245,0.4122721,0.212072105,0.144034568,0.01200024]
ILIrate = [0.069150797,0.073073121,0.084506484,0.079204384,0.090427218,0.156828177,0.188491793,0.223705257,0.215099465,0.184673114,0.138395522,0.105329457,0.072901458]

week = [35,36,37,38,39,40,41,42,43,44,45,46,47]
#pearson correlation

pearson = str(np.corrcoef(estimated,ILIrate))

plt.plot(week, estimated, color='g')
plt.plot(week, ILIrate, color='orange')
plt.xlabel('Flu season week')
plt.ylabel('Flu rate per 1000')
plt.title('Estimated tweet flu incidence vs CDC ILI incidence')
plt.text(35, 0.26, "r = 0.56")
plt.show()

