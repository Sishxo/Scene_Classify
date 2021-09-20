# Resnet50训练及预测工程文件使用方法
---
* 帧划分
    getFrameImg.py 用于从视频中抽帧得到图片，这些图片将用于后续模型的训练
    ```
    56 readPath = "/home/sishxo/project/scene/清洁卫生不合格"
    57 #if not os.path.exists(readPath):
    58 #    os.makedirs(readPath)
    59 savePath = "/home/sishxo/project/scene/clear_no_image"
    60 if not os.path.exists(savePath):
    61    os.makedirs(savePath)
    62 getFrameInVideo(readPath, savePath, 10)
    ```
    截自代码中56行到59行
    其中 **readPath** 填写的是需要进行抽帧处理的视频所在的文件夹路径，将会把这个目录下所有的视频进行帧的抽取
    其中 **savePath** 填写的是放置抽取得到的图片写入的路径，如果不存在这个路径会自动创建
    第62行调用的**getFrameVideo(readPath,savePath,interval)**，最后一个参数表示你想要隔多少帧抽一张照片，目前文件下的视频都是30帧每秒的手机拍摄视频，源代码中填了10，也就是一秒钟获取三张照片
---

* 训练
    main.py 用于模型的训练和保存
    config.py 中填写了训练所需要的一些初始参数
    一般来说训练无需对 main.py 进行操作，只需要对 config.py进行修改
    ```
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

    ```
    如注释所言，比较详细

    **此外，还有数据集的划分**
    在上一步进行视频抽帧得到图片，或者得到了直接的图片原始数据后，需要将他们进行数据集的划分。
    简单而言，将他们中一部分选为训练集，另一部分选为验证集，可以随机划分，其中训练集和验证集又分别下属自己的类别，以清洁与否这两种情况为例，训练集下属525张清洁的图片，和525张不清洁的图片；而验证集一般要比训练集少很多，这里我的验证集下属89张清洁图片，和89张不清洁图片。
    之后进行训练，将能得到一个训练好的模型，之后进行预测。
---

* 预测
    predict.py 用于利用训练好的模型进行预测
    ```
    10 model_dir = './trained_models/clean-2_record.pth'
    11 img_dir = './origin_data/工地整洁度识别-地面没有清扫'
    ```
    **model_dir** 变量填写的是你所用来预测的模型文件，也就是上一步训练得到的模型
    **img_dir** 变量填写的是你要用来预测的图片所在的文件夹路径
    这部分代码中我添加了对于判断结果的统计，将会输出输入预测的图片多少判为了清洁，多少判为了不清洁，用来提供给开发者进行预测效果的分析
---
BY Sun Shichu