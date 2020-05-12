import xgboost as xgb
import pandas as pd
param = {'silent': 1, 'objective': 'reg:linear', 'booster': 'gbtree',
         'alpha': 0.001, 'lambda': 1, 'eval_metric': 'auc',
         'n_jobs': 4}
file_folder = "/Users/zhangshupei/Documents/workspace/dms/bto_turing_engine/output/ML-配送时长源数据.xlsx"
train = pd.read_excel(file_folder, head=0,
                      converters={'dest_poi': str, 'dest_address': str})
target = train['delivery_time']
train = train.drop(['delivery_time'], axis=1)
# load data
dtrain = xgb.DMatrix(train.values, target.values)
dtest = xgb.DMatrix(train.values, target.values)

watchlist = [(dtest, 'eval'), (dtrain, 'train')]
num_round = 150
bst = xgb.train(param, dtrain, num_round, watchlist)

bst.save_model('/Users/zhangshupei/Documents/workspace/dms/bto_turing_engine/output/1.model')