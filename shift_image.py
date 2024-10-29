import numpy as np
import cv2

def shift_image(image):
    
    # find the edges
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blurred, 50, 150)

    # find the largest horizontal line from the edges
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, threshold=100, minLineLength=100, maxLineGap=10)
    longest_horizontal_line = None
    longest_length = 0
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            if abs(y1 - y2) < 10:
                length = np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
                if length > longest_length:
                    longest_length = length
                    longest_horizontal_line = (x1, y1, x2, y2)
    if longest_horizontal_line is not None:
        x1, y1, x2, y2 = longest_horizontal_line
        if y1 == y2:
            upper_part = image[:y1]
            lower_part = image[y1:]
            swapped = np.vstack((lower_part, upper_part))
    else:
        print("No orizontal line found")

    y = y1

    # cv2.imwrite("swapped.png", swapped)
    
    return swapped, upper_part, lower_part, y