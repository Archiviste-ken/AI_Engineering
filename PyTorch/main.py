import demo
import torch

model = demo.MyModel()

# linear layer expects an input with 3 features
input_tensor = torch.tensor([5.0, 5.0, 5.0])

print(model(input_tensor))