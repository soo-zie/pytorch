# # Tensor Concatenation
first_1 = torch.randn(2,5)
print(first_1)
second_1 = torch.randn(3,5)
print(second_1)
# Concatenation along the 0 dimension (concatenate rows)
conc_0 = torch.cat([first_1,second_1])
print(conc_0)
print(conc_0.shape)
# Concatenation along the 1 dimension (concatenate columns)
first_2 = torch.rand(2,3)
print(first_2)
second_2 = torch.rand(2,6)
print(second_2)
conc_1 = torch.cat([first_2,second_2], 1)
print(conc_1)
print(conc_1.shape) 
