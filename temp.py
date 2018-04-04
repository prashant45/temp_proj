import numpy as np
import pickle
import scipy.io as sio

model = sio.loadmat('Net.mat')
model = model['net']
model_dict = {}
#model_dict['layer_' + str(i)]

layers = model[0][0][0]
for i in range(layers.size):
    temp = layers[0, i]
    temp_dict = {}
    temp_dict['type'] = temp[0][0][0][0]

    if i%2 == 0:
        temp_dict['stride'] = temp[0][0][2].item()
        temp_dict['pad'] = temp[0][0][3].item()
        #m_tmp = [ temp[[0][0][5][0,0], temp[0][0][5][0,1] ]
        temp_dict['m'] = {
            'filters': temp[0][0][5][0,0],
            'bias': temp[0][0][5][0,1]
        }
        temp_dict['v'] = {
            'filters': temp[0][0][6][0,0],
            'bias': temp[0][0][6][0,1]
        }

    model_dict['layer_' + str(i+1)] = temp_dict

print(model_dict['layer_1']['m'].keys())
