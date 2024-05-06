
import torch
import torchvision
from torch.utils.data import Dataset, DataLoader
import numpy as np
import math
import pandas as pd
import os
from skimage import io
import geopandas as gpd
import matplotlib.pyplot as plt

class data_loader_persistence_img(Dataset):

    def __init__(self,geo_file_path,root_dir,transform=None):
        self.annotations = gpd.read_file(geo_file_path)
        self.root_dir = root_dir
        self.transform = transform



        # self.variable_names = [name for name in os.listdir(root_dir) if not name.startswith('.')]


        # dictionary to store image paths for each variable name
        # self.image_paths = {variable_name: [] for variable_name in self.variable_names}
        

        # # Collect paths of all images in each variable name folder
        # for variable_name in self.variable_names:
        #     variable_folder = os.path.join(root_dir, variable_name)
        #     # image_names = os.listdir(variable_folder)
        #     image_names = [f for f in os.listdir(variable_folder) if not f.startswith('.')]
        #     # image_names = [f for f in os.listdir(variable_folder) 
        #             #    if os.path.isdir(os.path.join(variable_folder, f)) and not f.startswith('.')]
        #     for image_name in image_names:
        #         image_path = os.path.join(variable_folder, image_name)
        #         self.image_paths[variable_name].append(image_path)

    def __len__(self):
        # return sum(len(paths) for paths in self.image_paths.values())
        pass
    
    def __getitem__(self,index):

        img_path = os.path.join(self.root_dir, self.annotations.iloc[index, 0])
        img = io.imread(img_path)
        y_label = torch.tensor(int(self.annotations.iloc[index, 1]))

        if self.transform:
            img = self.transform(img)

        return (img, y_label)
        

        # temp_dict = {}
        pass

        # for variable_name, paths in self.image_paths.items():
        #     if index < 95:
        #         image_path = paths[index]
        #         image = io.imread(image_path)

        #         if self.transform:
        #             image = self.transform(image)

        #         #store variable name and image in a dictionary
        #         temp_dict[variable_name] = image

        #     else:
        #         raise IndexError('Index out of bounds')
        
        # return temp_dict



# # Create custom dataset
# custom_dataset = data_loader_persistence_img(geo_file_path='/Users/h6x/ORNL/git/opioid-risk-modeling/tennessee/data/processed data/SVI with HepVu census tracts/SVI2018 TN census tracts with death rate HepVu/SVI2018_TN_census_tracts_with_death_rate_HepVu.shp',
#     root_dir='/Users/h6x/ORNL/git/opioid-risk-modeling/tennessee/results/persistence images/percentiles/H0H1/EP_POV')


#single_observation = custom_dataset[94]
