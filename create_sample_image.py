import cv2
import numpy as np

canvas = np.full((500,800,3), 245, dtype=np.uint8)

cv2.rectangle(
    canvas,
    (70, 110),
    (330, 380),
    (255, 0, 0),
    thickness=-1,
)

cv2.circle(
    canvas,
    (570, 245),
    115,
    (0, 255, 0),
    thickness=-1,
)

cv2.imwrite("sample_shapes.png", canvas)

print("Created sample_shapes.png")