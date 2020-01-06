import sys
import matplotlib
import numpy as np
import pandas as pd
import calmap
from matplotlib import pyplot as plt
import mpld3

# Ensure correct usage and CSV file is supplied
if(len(sys.argv) < 2):
	print("Usage: python csvtoheatmap.py [csv file]")
	exit()

file = sys.argv[1]

# Use try block to ensure file exists
try:
    f = open(file, "r")
    ws = pd.read_csv(file,delimiter="\t")
    ws['Date'] = ws['Date'].astype('datetime64[ns]')

    # Transform CSV into readable format for CalMap
    events = pd.Series(ws['Number'].tolist(), index=ws['Date'].tolist())

    # Use CalMap to generate a heatmap with matplotlib
    calmap.calendarplot(events, cmap="Greens", vmax=120, vmin=0)
    matplotlib.pyplot.show()
    print(mpld3.fig_to_html(plt))
    
except IOError:
    print("File not accessible")


