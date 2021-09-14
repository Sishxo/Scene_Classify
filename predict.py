import torch
torch.backends.cudnn.benchmark=True                 
import torch.nn as nn
import torchvision.models as models
import torchvision.transforms as transforms
from PIL import Image
import numpy as np
import os

model_dir = './trained_models/clean-2_record.pth'
img_dir = './origin_data/工地整洁度识别-地面没有清扫'

mean = [0.485, 0.456, 0.406]
std = [0.229, 0.224, 0.225]
data_transforms = transforms.Compose(
        [transforms.RandomResizedCrop(size=256,scale=(0.8,1.0)),
        transforms.RandomRotation(degrees=15),
        transforms.RandomHorizontalFlip(),
        transforms.CenterCrop(size=224),
        transforms.ToTensor(),
        transforms.Normalize([0.485,0.456,0.406],
                             [0.229,0.224,0.225])
])
'''class Model(nn.Module):
    def __init__(self):
        super().__init__()
        self.model = models.resnet50(pretrained=False)
        for param in self.model.parameters():
            #with torch.no_grad():
            param.requires_grad = False 
 
        self.model.fc = nn.Linear(self.model.fc.in_features,2,bias=False)
    def forward(self, x):
        x = self.model(x)
        return x
'''
#my_model = Model()
my_model=torch.load(model_dir) 
my_model = my_model.cuda()   #use gpu to run the model
my_model.eval()

sum=0
no_count=0
for path,dir_list,file_list in os.walk(img_dir):
    for file_name in file_list:
        img = Image.open(os.path.join(img_dir,file_name)).convert('RGB')
        #change the shape of image to fit in the model
        img = data_transforms(img)  
        img = img.unsqueeze(0)
        #print('img.shape:',img.shape)
            
        outputs = my_model(img.cuda())
        _, preds = torch.max(outputs.data,1)
        #I use the gpu0 to run the model, so I should use '.cpu()' before using '.numpy()'
        a = preds.data.cpu().numpy()
        sum+=1
        if(a[0]==0):
            no_count+=1
        tag_list=['clean_no','clean_ok'] 
        print('preds:',file_name,' ',tag_list[a[0]])
print("no_accuracy:",no_count/sum*100,'%')
print("ok_accuracy:",(sum-no_count)/sum*100,'%')