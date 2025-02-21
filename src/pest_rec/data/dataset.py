import torch
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms
from PIL import Image
import os

class PestDataset(Dataset):
    def __init__(self, root_dir, pest_classes, transform=None, split="train"):
        self.root_dir = root_dir
        self.pest_classes = pest_classes
        self.transform = transform
        self.split = split
        
        # Veri yollarını ve etiketleri topla
        self.samples = []
        for idx, pest in enumerate(pest_classes):
            pest_dir = os.path.join(root_dir, split, pest)
            for img_name in os.listdir(pest_dir):
                img_path = os.path.join(pest_dir, img_name)
                self.samples.append((img_path, idx))
                
    def __len__(self):
        return len(self.samples)
        
    def __getitem__(self, idx):
        img_path, label = self.samples[idx]
        image = Image.open(img_path).convert('RGB')
        
        if self.transform:
            image = self.transform(image)
            
        return image, label 

# Test için bir batch yükleyin
dataloader = DataLoader(PestDataset(root_dir="path/to/your/dataset", pest_classes=["class1", "class2", "class3"], transform=None, split="train"), batch_size=32, shuffle=True)
images, labels = next(iter(dataloader))
print(f"Batch shape: {images.shape}")
print(f"Labels: {labels}") 