import numpy as np


def generate_abc_design_matrix(deltav, K):
    """
    _summary_

    Args:
        deltav (_type_): _description_
        K (_type_): _description_

    Returns:
        _type_: _description_
    """
    P, Q = np.shape(deltav)
    N = K * P
    M = K * Q
    Wij = np.zeros((N, M))
    print("I used 4 for loops!! Please modify my code anyone!!!")
    # naive computation
    for p in range(0, P):
        for q in range(0, Q):
            print(p, "/", P, "-", q, "/", Q)
            for k in range(0, K):
                for kd in range(0, K):
                    i = K * p + kd
                    j = K * q + k
                    if kd - k - deltav[p, q] == 0:
                        Wij[i, j] = 1.0

    return Wij
