import struct
import numpy as np
import matplotlib.pyplot as plt
import os
from scipy.special import expit

liczba_epok = 100

def wczytaj_dane():
    with open('train-labels.idx1-ubyte', 'rb') as labels:
        magic, n = struct.unpack('>II', labels.read(8))
        train_labels = np.fromfile(labels, dtype=np.uint8)
    with open('train-images.idx3-ubyte', 'rb') as imgs:
        magic, num, nrows, ncols = struct.unpack('>IIII', imgs.read(16))
        train_images = np.fromfile(imgs, dtype=np.uint8).reshape(num,784)
    with open('t10k-labels.idx1-ubyte', 'rb') as labels:
        magic, n = struct.unpack('>II', labels.read(8))
        test_labels = np.fromfile(labels, dtype=np.uint8)
    with open('t10k-images.idx3-ubyte', 'rb') as imgs:
        magic, num, nrows, ncols = struct.unpack('>IIII', imgs.read(16))
        test_images = np.fromfile(imgs, dtype=np.uint8).reshape(num,784)
    return train_images, train_labels, test_images, test_labels

def wizualizacja_data(img_array, label_array):
    fig, ax = plt.subplots(nrows=8, ncols=8, sharex=True, sharey=True)
    ax = ax.flatten()
    for i in range(64):
        img = img_array[label_array==7][i].reshape(28,28)
        ax[i].imshow(img, cmap='Greys', interpolation='nearest')
    plt.show()

def konwersja_na_wektor(y, num_labels=10):
    one_hot = np.zeros((num_labels, y.shape[0]))
    for i, val in enumerate(y):
        one_hot[val,i] = 1.0
    return one_hot

def sigmoid(z):
    return(1 / (1 + np.exp(-z)))

def sigmoid_gradient(z):
    s = sigmoid(z)
    return s * (1 - s)

def wizualizacja_sigmoid():
    x = np.arange(-10, 10, 0.1)
    y = sigmoid(x)
    fig, ax = plt.subplots()
    ax.plot(x,y)
    plt.show()

def oblicz_koszt(y_enc, outpt):
    t1 = -y_enc * np.log(outpt)
    t2 = (1 - y_enc)*np.log(1-outpt)
    cost = np.sum(t1 - t2)
    return cost

def dodaj_wsp_b(X, miejsce):
    if miejsce == 'kolumna':
        noweX = np.ones((X.shape[0], X.shape[1] + 1))
        noweX[:, 1:] = X
    elif miejsce == 'wiersz':
        noweX = np.ones((X.shape[0] + 1, X.shape[1]))
        noweX[1:, :] = X
    return noweX

def inicjalizacja_wag(n_features, n_hidden, n_output):
    w1 = np.random.uniform(-1.0, 1.0, size=n_hidden*(n_features+1))
    w1 = w1.reshape(n_hidden, n_features+1)
    w2 = np.random.uniform(-1.0, 1.0, size=n_hidden*(n_hidden+1))
    w2 = w2.reshape(n_hidden, n_hidden+1)
    w3 = np.random.uniform(-1.0, 1.0, size=n_output*(n_hidden+1))
    w3 = w3.reshape(n_output, n_hidden+1)
    return w1, w2, w3

def sprzezenie_w_przod(x, w1, w2, w3):
    # dodaj wsp b
    a1 = dodaj_wsp_b(x, miejsce='kolumna')
    z2 = w1.dot(a1.T)
    a2 = sigmoid(z2)
    # po transpozycji
    a2 = dodaj_wsp_b(a2, miejsce='wiersz')
    z3 = w2.dot(a2)
    a3 = sigmoid(z3)
    a3 = dodaj_wsp_b(a3, miejsce='wiersz')
    z4 = w3.dot(a3)
    a4 = sigmoid(z4)

    return a1, z2, a2, z3, a3, z4, a4

def przewidywanie(x, w1, w2, w3):
    a1, z2, a2, z3, a3, z4, a4 = sprzezenie_w_przod(x, w1, w2, w3)
    y_pred = np.argmax(a4, axis=0)
    return y_pred

def oblicz_gradient(a1, a2, a3, a4, z2, z3, z4, y_enc, w1, w2, w3):
    delta4 = a4 - y_enc
    z3 = dodaj_wsp_b(z3, miejsce='wiersz')
    delta3 = w3.T.dot(delta4)*sigmoid_gradient(z3)
    delta3 = delta3[1:, :]
    z2 = dodaj_wsp_b(z2, miejsce='wiersz')
    delta2 = w2.T.dot(delta3)*sigmoid_gradient(z2)
    delta2 = delta2[1:,:]

    grad1 = delta2.dot(a1)
    grad2 = delta3.dot(a2.T)
    grad3 = delta4.dot(a3.T)

    return grad1, grad2, grad3

def trenowanie_sieci(X, y, X_t, y_t):
    X_copy, y_copy = X.copy(), y.copy()
    y_enc = konwersja_na_wektor(y)
    batch = 50

    w1, w2, w3 = inicjalizacja_wag(784, 75, 10)

    alpha = 0.001
    eta = 0.001
    dec = 0.00001
    delta_w1_prev = np.zeros(w1.shape)
    delta_w2_prev = np.zeros(w2.shape)
    delta_w3_prev = np.zeros(w3.shape)
    calkowity_koszt = []
    pred_acc = np.zeros(liczba_epok)

    for i in range(liczba_epok):

        shuffle = np.random.permutation(y_copy.shape[0])
        X_copy, y_enc = X_copy[shuffle], y_enc[:, shuffle]
        eta /= (1 + dec*i)

        mini = np.array_split(range(y_copy.shape[0]), batch)

        for step in mini:
            # feed forward the model
            a1, z2, a2, z3, a3, z4, a4 = sprzezenie_w_przod(X_copy[step], w1, w2, w3)
            cost = oblicz_koszt(y_enc[:,step], a4)

            calkowity_koszt.append(cost)
            # back propagate
            grad1, grad2, grad3 = oblicz_gradient(a1, a2, a3, a4, z2, z3, z4, y_enc[:,step],
                                            w1, w2, w3)
            delta_w1, delta_w2, delta_w3 = eta * grad1, eta * grad2, eta * grad3

            w1 -= delta_w1 + alpha * delta_w1_prev
            w2 -= delta_w2 + alpha * delta_w2_prev
            w3 -= delta_w3 + alpha * delta_w3_prev

            delta_w1_prev, delta_w2_prev, delta_w3_prev = delta_w1, delta_w2, delta_w3_prev

        y_pred = przewidywanie(X_t, w1, w2, w3)
        pred_acc[i] = 100*np.sum(y_t == y_pred, axis=0) / X_t.shape[0]
        print('epoka #', i)
    return calkowity_koszt, pred_acc, y_pred

treningowe_x, treningowe_y, test_x, test_y = wczytaj_dane()

cost, acc, y_pred = trenowanie_sieci(treningowe_x, treningowe_y, test_x, test_y)

x_a = [i for i in range(acc.shape[0])]
x_c = [i for i in range(len(cost))]
print('ostateczna dokladnosc: ', acc[-1])
plt.subplot(221)
plt.plot(x_c, cost)
plt.subplot(222)
plt.plot(x_a, acc)
plt.show()

miscl_img = test_x[test_y != y_pred][:25]
correct_lab = test_y[test_y != y_pred][:25]
miscl_lab = y_pred[test_y != y_pred][:25]

fig, ax = plt.subplots(nrows=5, ncols=5, sharex=True, sharey=True)
ax = ax.flatten()
for i in range(25):
    img = miscl_img[i].reshape(28,28)
    ax[i].imshow(img, cmap='Greys', interpolation='nearest')
    ax[i].set_title('%d) t: %d p: %d' % (i + 1, correct_lab[i], miscl_lab[i]))
ax[0].set_xticks([])
ax[0].set_yticks([])
plt.tight_layout()
plt.show()
