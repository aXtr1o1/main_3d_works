import torch
print(torch.__version__)
print(torch.version.cuda)

print(torch.cuda.get_device_name(0))
print(torch.cuda.current_device())
from torch.utils.cpp_extension import CUDA_HOME
print(CUDA_HOME)
