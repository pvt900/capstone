from pandas import *

dat_in = read_csv('historical_data.csv', header = None, sep = '\t')
dat_in.to_csv(r'C:\Users\Will G\OneDrive - Wartburg College\CSCI\Capstone\hist.csv')
