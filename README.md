The restored image is not the original one as color correction was not done given the two samples.
The image was just brought to have the same filter.
Detection of the three cones with the location of the boxes was still done.

For the reconstruction of the image in the file shift_image.py was done using the contours and identifying the longest horizontal contour present in the image.

To bring the two parts of the image with the same filter into the color_change.py file was manually adjusted by trying to enter values of the three RBG channels until they were equal (initially observing that there were constant differences between the pixels).

For object detection in the detect.py file of the cones, three ranges of the color space were set for each cone. Then the two largest obtainable boxes were searched and joined (to bipass the white strip in the middle of the cone).
