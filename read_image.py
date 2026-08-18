import cv2

image = cv2.imread("sample_shapes.png")

if image is None:
    raise FileNotFoundError

print(image.shape)
print(image.dtype)
print(image[150, 100])