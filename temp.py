import pickle

with open('Network_weights.pickle', 'rb') as handle:
    b = pickle.load(handle)

print(b['layer_4']['v']['bias'])