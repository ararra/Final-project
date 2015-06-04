import matplotlib.pyplot as pl

def plotzor(grid, polly, graphic, index):
    pl.plot(grid, polly, graphic)
    pl.savefig('BestApprox{}.png'.format(index), dpi=1080)
