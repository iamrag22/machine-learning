# Om sri Sai Ragana
# Hyperparameters
# Data dependent hyperparameters
# Learnable parameters
# Why do we extend nn.Module
    # It keeeps track of weights tensor, gradient tensor for every layer
# Pytorch layers are callable. So the forward methods are not directly invoked. 
#  Instead the network instance is passed with input tensor for each layer
# Disable Dynamic computation graph feature by setting torch.set_grad_enabled(False)
# loss.backward()  accumulates gradients

# Disable gradient tracking while eval with torch.zero_grad()

# Concat vs Stack
#  Concat combines tensors without creating a new axes
# Eg torch.cat((t1,t2), dim=0) =>  combines  along dim0
# torch.cat((t1,t2), dim=1) => combines along dim 1 ( Note we cant concat along an axis > rank of tensor)

# Stack will create a new axes and then concat tensors along the dimension

