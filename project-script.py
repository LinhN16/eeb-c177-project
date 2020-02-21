def dynamic_plot(): 
    xx= input ("Which column do you want to plot: ")
    x = Data[:,int(xx)]
    plt.hist(x, bins = 50)
    yy= input ("What's the x axis label: ")
    plt.xlabel(str(yy))
    zz= input ("What's the y axis label: ")
    plt.ylabel(str(zz))
    aa= input ("What's the graph title: ")
    plt.title (str(aa))
    plt.show()
