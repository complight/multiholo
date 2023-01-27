import torch
import odak
from torchvision import transforms
from torch.utils.data import Dataset


class hologram_dataset(Dataset):
    """
    A class to load hologram datasets generated by Kavaklı et al. "Realistic Defocus Blur for Multiplane Computer-Generated Holography".
    """
    def __init__(self, directory='./dataset/train', key='*.pt', device=None):
        self.filenames = odak.tools.list_files(directory, key=key)
        self.device = device
        if isinstance(self.device, type(None)):
            self.device = torch.device('cpu')

        
    def __getitem__(self, index):
        self.filename = self.filenames[index]
        data = torch.load(self.filename).to(self.device)
        data = (data - 0.5) * 2
        return data


    def __len__(self):
        return len(self.filenames)
