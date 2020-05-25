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


# Pytorch
# Tensors = nd arrays ( Covers all dimensions including scalar(0))
# Tensor Attributes
#  Rank => Number of dimensions.
#       => Number of indices required to access an element.
#  Axes => A specific dimension through which elements run
#          Number of dimensions = Number of axes
#  Shape => Encodes all the information about tensor
#        => It is tuple. 
#             Number of elements in the tuple = number of axes/indices/rank
#             value of each element in the tuple = length of each axes
#       => (length of axes 1, length of axes 2) 

# Reshaping does not change the number of dimensions/rank/numel

