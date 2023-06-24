import torchvision
import torchvision.transforms as T


# Convert Image to Array or Tensor
Image = torchvision.io.read_image("jokowi.jpeg")

# show result image of array
print(Image.shape)

# Visualize Image
torchImage = T.ToPILImage()(Image)
torchImage.show()
