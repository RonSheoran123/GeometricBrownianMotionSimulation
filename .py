def plot_gbm(gbm):
  fig, ax=plt.subplots(1,1,figsize=(8,4))
  for path in gbm:
    ax.plot(path)
  ax.set_xlabel("Time")
  ax.set_ylabel("Asset Price")
  plt.show()
