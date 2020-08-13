import resnet

model = resnet.ResNet101(input_shape=(224,224,3), attention_input_shape=(224,224,3))
model.summary()