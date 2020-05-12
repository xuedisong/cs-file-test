import sys
import xgboost as xgb
import os

sys.path.extend(['C:\\Python27\\Lib\\site-packages'])

# this script demonstrate how to fit generalDMatrixed linear model in xgboost
# basically, we are using linear model, instead of tree for our boosters

# change booster to gblinear, so that we are fitting a linear model
# alpha is the L1 regularizer
# lambda is the L2 regularizer
# you can also set lambda_bias which is L2 regularizer on the bias term
os.environ["OMP_NUM_THREADS"] = "1"
param = {'silent': 1, 'objective': 'binary:logistic', 'booster': 'gbtree',
         'alpha': 0.001, 'lambda': 1, 'eval_metric': 'auc',
         'n_jobs': 4}

# load data
dtrain = xgb.DMatrix(
    'libsvm_samples/train_{0}.txt'.format(data_version))  # train_targetA_7days_group3_order_info_v2.txt')
dtest = xgb.DMatrix('libsvm_samples/test_{0}.txt'.format(data_version))  # test_targetA_7days_group3_order_info_v2.txt')

# normally, you do not need to set eta (step_size)
# XGBoost uses a parallel coordinate descent algorithm (shotgun),
# there could be affection on convergence with parallelization on certain cases
# setting eta to be smaller value, e.g 0.5 can make the optimization more stable
# param['eta'] = 1

##
# the rest of settings are the same
watchlist = [(dtest, 'eval'), (dtrain, 'train')]
# watchlist = [(dtrain, 'train')]
num_round = 150
bst = xgb.train(param, dtrain, num_round, watchlist)

# dump model
bst.save_model('models/{0}-{1}.model'.format(model_date, data_version))
