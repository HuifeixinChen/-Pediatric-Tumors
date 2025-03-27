import torch
import hiddenlayer as hl
from nnunetv2.training.network.nnUNetTrainer import nnUNetTrainer
from nnunetv2.paths import nnUNet_results
from nnunetv2.utilities.label_handling.label_handling import LabelManager
from nnunetv2.utilities.plans_handling.plans_handler import PlansManager
from batchgenerators.utilities.file_and_folder_operations import join, load_json

# 指定任务信息
task = "Dataset999_BraTSPED"
fold = "fold_0"
config = "3d_fullres"
trainer = "nnUNetTrainer"

# 加载 Trainer（用于构建网络）
trainer_path = join(nnUNet_results, task, f"{trainer}__{config}", fold)
plans_path = join(trainer_path, "plans.json")
dataset_json_path = join(trainer_path, "dataset.json")

plans = PlansManager(plans_path)
dataset_json = load_json(dataset_json_path)

# 获取 patch 大小和输入通道数等信息
configuration = plans.get_configuration(config)
in_channels = len(configuration['normalization_schemes'])
num_classes = len(plans.label_manager.foreground_labels) + 1
patch_size = [1] + configuration['patch_size']  # shape: C, D, H, W

# 构建网络
net = plans.get_network(configuration, dataset_json)

# 构造输入
dummy_input = torch.zeros([1] + patch_size).float()

# 可视化
g = hl.build_graph(net, dummy_input)
g.save("network_architecture_fold0.svg")
print("网络结构图已保存为 network_architecture_fold0.svg")
