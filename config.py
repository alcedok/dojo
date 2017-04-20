# modules used for easier display of data
from IPython.display import display
from IPython.core.display import HTML
display(HTML("<style>.container { width:100% !important; }</style>"))

# these are variables that will be constant for this kata

#  52Hz
sampling_freq = 52.0 

# number of participants
p_num = 15

# number of activities to be classified
act_num = 7

#  columns names
cols = ['sequential_number', 'x_acceleration', 'y_acceleration', 'z_acceleration', 'label' ]

# labels
labels_list =['Working at Computer','Standing Up,Walking and Going up/down stairs',
              'Standing','Walking','Going Up/Down Stairs','Walking and Talking with Someone',
              'Talking while Standing']

labels_dict = {n+1:i for n,i in enumerate(labels_list)}
