import torch

ckpt_path = "./checkpoint/resnet34_test_2025Dec19_14.49"  # adjust path
ckpt = torch.load(ckpt_path, map_location="cpu")

print(type(ckpt))
print(ckpt.keys())