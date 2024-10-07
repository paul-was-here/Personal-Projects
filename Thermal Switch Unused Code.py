# Break at UNUSED CODE:
exit()

coords = list(zip(wa,ta))

def valueWithin15(value):
    return round(1/value) - 1/value <= 0.05

def filterFn(coord):
    return valueWithin15(coord[0]) and valueWithin15(coord[1])

sortedlist = list(filter(filterFn, coords))
for item in sortedlist:
    #print(str(item[0])+'\t|\t'+str(item[1]))
    if item[0] > 0 and item[1] > 0:
        print('1/'+str(round(1/item[0],1))+'\t|\t1/'+str(round(1/item[1],1)))
        xlabel = "1/"+str(round(1/round(1/item[0],2),2))
        ylabel = "1/"+str(round(1/round(1/item[1],2),2))
        plt.gca().annotate(("↙ "+xlabel+", "+ylabel), (item[0], item[1]))