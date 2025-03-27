import os

def generate_train_txt(base_dir, output_file="train.txt"):
    """
    生成 train.txt，列出 Train/BraTS-PED 目录下的所有病例文件夹。

    :param base_dir: 训练数据集的根目录，例如 "/Users/joshuafxxx/Desktop/Pediatric-Tumors/Data/Train"
    :param output_file: 生成的 train.txt 文件路径
    """
    # 确保路径正确
    braTS_ped_path = os.path.join(base_dir, "BraTS-PED")  # 进入 BraTS-PED 目录

    if not os.path.exists(braTS_ped_path):
        print(f"❌ 错误: 目录 {braTS_ped_path} 不存在，请检查路径是否正确！")
        return

    # 获取 BraTS-PED/ 目录下的所有病例
    cases = sorted(os.listdir(braTS_ped_path))
    cases = [case for case in cases if os.path.isdir(os.path.join(braTS_ped_path, case))]  # 仅保留文件夹

    if not cases:
        print(f"⚠️  警告: 目录 {braTS_ped_path} 下未找到任何病例文件夹，请检查数据集结构！")
        return

    # 生成 train.txt
    with open(output_file, "w") as f:
        for case in cases:
            f.write(f"BraTS-PED/{case}\n")  # 加上 BraTS-PED/ 前缀

    print(f"✅ {output_file} 生成成功！总计 {len(cases)} 个病例，路径: {os.path.abspath(output_file)}")

if __name__ == "__main__":
    # ✅ **修改为你的实际数据集路径**
    base_dir = "/Users/joshuafxxx/Desktop/Pediatric-Tumors/Data/Train"
    
    # 生成 train.txt
    generate_train_txt(base_dir, "train.txt")