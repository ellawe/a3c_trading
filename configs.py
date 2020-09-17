# Directories
TENSORBOARD_DIR = '/mnt/a3c_data/tb/'
MODEL_DIR = 'model'
DATA_DIR = '/mnt/a3c_data/data/'
PLOTS_DIR = '/mnt/a3c_data/plots/'

# Data files
postfix = "[_RTS-12.15_]"
test_postfix = "[_RTS-3.16_, _RTS-6.16_]"
postfix_real = "[_RTS-12.15_]"
test_postfix_real = "[_RTS-3.16_, _RTS-6.16_]"

# Network architechture
EXTRA_DENSE = False
N_HIDDEN = 64
DROPOUT = True
training = False
COOL_V = True
COOL_A = False
dep = 1
gamma = .8
load_model = True
LR = 1e-4
comission = 20  # rubls
PRICE_MAG = 1 / 5000  # среднне различие между макс и мин ценой за 5000 шагов
TRAIN_DATA = 'data\[_RTS-3.16_, _RTS-6.16_]'
FRAMES_STACKED = 1
NUM_WORKERS = 2
USE_DEVICE = "cpu:0"