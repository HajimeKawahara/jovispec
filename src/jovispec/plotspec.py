import matplotlib.pyplot as plt


def plot_prediction3(wav, spe, spc, spw, la, fpl, fpr):
    fig = plt.figure(figsize=(20, 10))
    ax = fig.add_subplot(311)
    ax.plot(wav, spe, lw=3, color="black", alpha=0.5)
    ax.plot(la, fpr[0], lw=3, alpha=0.5, color="blue", ls="dashed")
    ax.plot(la, fpl[0], lw=3, alpha=0.5, color="blue")
    plt.title("Prediction: East")
    plt.legend(["Input", "Ridge", "Lasso"])
    ax = fig.add_subplot(312)
    ax.plot(wav, spc, lw=3, color="black", alpha=0.5)
    ax.plot(la, fpr[1], lw=3, alpha=0.5, color="blue", ls="dashed")
    ax.plot(la, fpl[1], lw=3, alpha=0.5, color="blue")
    plt.title("Prediction: Center")
    ax = fig.add_subplot(313)
    ax.plot(wav, spw, lw=3, color="black", alpha=0.5)
    ax.plot(la, fpr[2], lw=3, alpha=0.5, color="blue", ls="dashed")
    ax.plot(la, fpl[2], lw=3, alpha=0.5, color="blue")
    plt.title("Prediction: West")
    plt.show()


def plot_each3(
    mrlamb_input, mrspece_input, mrspecc_input, mrspecw_input, la, efplt, efplp, efpls
):
    fig = plt.figure(figsize=(20, 10))
    ax = fig.add_subplot(311)
    # ax.plot(la,hfe,lw=3,color="black",alpha=0.5)
    ax.plot(mrlamb_input, mrspece_input, lw=3, alpha=0.5, color="gray")
    ax.plot(la, efplt[0], lw=3, alpha=0.5)
    ax.plot(la, efplp[0], lw=3, alpha=0.5)
    ax.plot(la, efpls[0], lw=3, alpha=0.5)
    plt.title("Prediction: East")
    plt.legend(["Input", "Telluric", "Planet", "Stellar"])
    ax = fig.add_subplot(312)
    ax.plot(mrlamb_input, mrspecc_input, lw=3, alpha=0.5, color="gray")
    ax.plot(la, efplt[1], lw=3, alpha=0.5)
    ax.plot(la, efplp[1], lw=3, alpha=0.5)
    ax.plot(la, efpls[1], lw=3, alpha=0.5)
    plt.title("Prediction: Center")
    ax = fig.add_subplot(313)
    ax.plot(mrlamb_input, mrspecw_input, lw=3, alpha=0.5, color="gray")
    # ax.plot(la,hfw,lw=3,color="black",alpha=0.5)
    ax.plot(la, efplt[2], lw=3, alpha=0.5)
    ax.plot(la, efplp[2], lw=3, alpha=0.5)
    ax.plot(la, efpls[2], lw=3, alpha=0.5)
    plt.title("Prediction: West")
    plt.show()
