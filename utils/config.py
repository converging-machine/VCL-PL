"""
Authors: Wouter Van Gansbeke, Simon Vandenhende
Licensed under the CC BY-NC 4.0 license (https://creativecommons.org/licenses/by-nc/4.0/)
"""
import os
import yaml
from easydict import EasyDict
from utils.utils import mkdir_if_missing

def create_config(config_file_env, config_file_exp, batch_size, epochs):
    # Config for environment path
    with open(config_file_env, 'r') as stream:
        root_dir = yaml.safe_load(stream)['root_dir']
   
    with open(config_file_exp, 'r') as stream:
        config = yaml.safe_load(stream)
    
    cfg = EasyDict()
   
    # Copy
    for k, v in config.items():
        cfg[k] = v

    # Set paths for pretext task (These directories are needed in every stage)
    base_dir = os.path.join(root_dir, cfg['train_db_name'])
    pretext_dir = os.path.join(base_dir, 'SimCLR-B' + str(batch_size))
    mkdir_if_missing(base_dir)
    mkdir_if_missing(pretext_dir)
    cfg['pretext_dir'] = pretext_dir
    cfg['pretext_checkpoint'] = os.path.join(pretext_dir, 'checkpoint.pth.tar')
    cfg['pretext_model'] = os.path.join(pretext_dir, 'model.pth.tar')
    cfg['topk_neighbors_train_path'] = os.path.join(pretext_dir, 'topk-train-neighbors.npy')
    cfg['topk_neighbors_val_path'] = os.path.join(pretext_dir, 'topk-val-neighbors.npy')
    return cfg 
