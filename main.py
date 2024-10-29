import cv2
from shift_image import shift_image
from color_chage import color_change
from detect import detect_cones

image = cv2.imread("corrupted.png")
coordinates = [(128, 541), (564, 267)]

swapped, lower, upper, y = shift_image(image)

original_pixel_B = [250, 158, 3]
original_pixel_Y = [40, 195, 240]

restored = color_change(swapped, y)

# restored_2 = color_restore(restored_1, coordinates[0], coordinates[1], original_pixel_B, original_pixel_Y)

output_file = 'bounding_boxes.txt'
final_img = detect_cones(restored, output_file)
# final_img = object_detection(restored)

cv2.imshow('Original Image', image)
# cv2.imshow('Swapped', swapped)
# cv2.imshow('Restored', restored)
cv2.imshow('Final Image', final_img)

cv2.waitKey(0)
cv2.destroyAllWindows()

