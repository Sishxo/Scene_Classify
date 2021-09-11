# 数据集的类别
NUM_CLASSES = 2

# 训练时batch的大小
BATCH_SIZE = 32

# 训练轮数
NUM_EPOCHS = 25

#预训练模型路径
PRETRAINED_MODEL = './resnet50-19c8e357.pth'

# 训练完成后，权重文件的保存路径
TRAINED_MODEL = 'trained_models/clean-2_record.pth'

# 数据集存放位置
TRAIN_DATASET_DIR = './clean_status/train'
VALID_DATASET_DIR = './clean_status/val'
