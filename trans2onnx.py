import torch
import os
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

path="./trained_models/clean-2_record.pth"
file_name=os.path.split(path)[1].split('.')[0]
print(file_name)
model = torch.load(path) # pytorch模型加载
batch_size = 32  #批处理大小
input_shape = (3, 256,256)   #输入数据,改成自己的输入shape

# #set the model to inference mode
model.eval()
#print("break")
x = torch.randn(batch_size, *input_shape)   # 生成张量
x = x.to(device)
export_onnx_file = "./trained_models/"+file_name+".onnx"	# 目的ONNX文件名
torch.onnx.export(model,
                    x,
                    export_onnx_file,
                    opset_version=10,
                    do_constant_folding=True,	# 是否执行常量折叠优化
                    input_names=["input"],	# 输入名
                    output_names=["output"],	# 输出名
                    dynamic_axes={"input":{0:"batch_size"},  # 批处理变量
                                    "output":{0:"batch_size"}})