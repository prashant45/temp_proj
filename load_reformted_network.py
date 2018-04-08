import pickle
import scipy.io as sio

model = sio.loadmat('Network_weights.mat', struct_as_record=True)['model_weights']

model_dict = {}

for i in range(model.size):

    model_dict['layer_' + str(i + 1)] = {
        'weights': {
            'filters': model[0][i][0][0][0][0][0],
            'bias': model[0][i][0][0][0][0][1]
        },
        'msq': model[0][i][0][0][1][0],
        'm': {
            'filters': model[0][i][0][0][2][0][0],
            'bias': model[0][i][0][0][2][0][1]
        },
        'v': {
            'filters': model[0][i][0][0][3][0][0],
            'bias': model[0][i][0][0][3][0][1]
        }
    }

with open('Network_weights.pickle', 'wb') as handle:
    pickle.dump(model_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)
