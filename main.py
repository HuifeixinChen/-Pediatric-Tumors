# main.py

import torch
from TransBTS.models import TransBTSModel
from TransBTS.utils import load_data, preprocess_data

def main():
    # 实例化 TransBTS 模型（根据仓库中的实际接口调整参数）
    model = TransBTSModel()
    
    # 如果有预训练权重，可以加载
    # weight_path = "path/to/weights.pth"
    # model.load_state_dict(torch.load(weight_path, map_location=torch.device('cpu')))
    
    model.eval()
    
    # 指定数据文件路径（请替换为实际路径）
    data_path = "data/train/sample_image.nii.gz"
    
    # 加载并预处理数据
    raw_data = load_data(data_path)
    input_data = preprocess_data(raw_data)
    
    # 转换为 PyTorch Tensor，增加 batch 维度
    input_tensor = torch.tensor(input_data).unsqueeze(0)
    
    with torch.no_grad():
        output = model(input_tensor)
    
    print("预测结果：", output)

if __name__ == "__main__":
    main()