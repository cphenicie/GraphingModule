#!/usr/bin/python
import matplotlib.pyplot as plt

def niceplot(xdata, ydata, xlabel, ylabel, legEntry, linestylestr):

    bordersize = 3
    tickwidth = bordersize
    ticklength = bordersize*2
    ticklabelsize = 5*bordersize

    linewidth = 4
    markersize = 10
    labelfontsize = ticklabelsize+4
    #titlefontsize = labelfontsize+4
    #textfontsize = 16

    plt.figure(num=None, figsize=(8, 6), dpi=100, facecolor='w', edgecolor='k')
    plt.plot(xdata, ydata, linewidth=linewidth, linestyle=linestylestr, label=legEntry)
    plt.xlabel(xlabel, fontsize=labelfontsize)
    plt.ylabel(ylabel, fontsize=labelfontsize)
    if legEntry:
        legend = plt.legend(loc='best', shadow=True)

        for label in legend.get_texts():
            label.set_fontsize('large')

        for label in legend.get_lines():
            label.set_linewidth(linewidth)  # the legend line width


    ax = plt.gca()
    ax.tick_params(axis='both', which='major', width=tickwidth, length=ticklength, labelsize=ticklabelsize)
    for pos in ['top','bottom','left','right']:
      ax.spines[pos].set_linewidth(bordersize)

    plt.show()


def niceplot_err(xdata, ydata, yerr, xlabel, ylabel, plotlabel, linestylestr):
    bordersize = 3
    tickwidth = bordersize
    ticklength = bordersize * 2
    ticklabelsize = 5 * bordersize

    linewidth = 4
    markersize = 10
    labelfontsize = ticklabelsize + 4
    # titlefontsize = labelfontsize+4
    # textfontsize = 16

    plt.figure(num=None, figsize=(8, 6), dpi=100, facecolor='w', edgecolor='k')
    plt.errorbar(xdata, ydata, yerr, linewidth=linewidth, linestyle=linestylestr, label=plotlabel)
    plt.ylabel(xlabel, fontsize=labelfontsize)
    plt.xlabel(ylabel, fontsize=labelfontsize)
    legend = plt.legend(loc='best', shadow=True)

    for label in legend.get_texts():
        label.set_fontsize('large')

    for label in legend.get_lines():
        label.set_linewidth(linewidth)  # the legend line width

    ax = plt.gca()
    ax.tick_params(axis='both', which='major', width=tickwidth, length=ticklength, labelsize=ticklabelsize)
    for pos in ['top', 'bottom', 'left', 'right']:
        ax.spines[pos].set_linewidth(bordersize)

    plt.show()

def multiNiceplot(xdata, ydatas, xlabel, ylabel, legEntrys, linestylestr, markerstr):

    bordersize = 3
    tickwidth = bordersize
    ticklength = bordersize * 2
    ticklabelsize = 5 * bordersize

    linewidth = 3
    markersize = 10
    labelfontsize = ticklabelsize + 4
    # titlefontsize = labelfontsize+4
    # textfontsize = 16
    plt.figure(num=None, figsize=(8, 6), dpi=100, facecolor='w', edgecolor='k')
    for ydata, legEntry in zip(ydatas, legEntrys):
        plt.plot(xdata, ydata, linewidth=linewidth, linestyle=linestylestr, marker=markerstr, markersize=markersize, label=legEntry)
        plt.xlabel(xlabel, fontsize=labelfontsize)
        plt.ylabel(ylabel, fontsize=labelfontsize)
        if legEntry:
            legend = plt.legend(loc='best', shadow=True)

            for label in legend.get_texts():
                label.set_fontsize('large')

            for label in legend.get_lines():
                label.set_linewidth(linewidth)  # the legend line width

        ax = plt.gca()
        ax.tick_params(axis='both', which='major', width=tickwidth, length=ticklength, labelsize=ticklabelsize)
        for pos in ['top', 'bottom', 'left', 'right']:
            ax.spines[pos].set_linewidth(bordersize)

    plt.show()



        #if __name__ == '__main__':
#    niceplot(xdata, ydata, xlabel, ylabel, plotlabel, linestylestr)