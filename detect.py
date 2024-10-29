import cv2
import numpy as np

def detect_cones(img, output_file):
    # Pre-processing
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    img_hsv[:, :, 2] = cv2.equalizeHist(img_hsv[:, :, 2])

    def detect_color(color_name, lower_bound, upper_bound):
        mask = cv2.inRange(img_hsv, lower_bound, upper_bound)

        kernel = np.ones((5, 5), np.uint8)
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        if contours:
            # Sort contours in descending way
            contours = sorted(contours, key=cv2.contourArea, reverse=True)
            
            # Take the 2 bigger contours and merge them
            largest_contours = contours[:min(2, len(contours))]
            combined_contour = np.vstack(largest_contours)
            
            # Get bounding rectangle
            x, y, w, h = cv2.boundingRect(combined_contour)

            # Define color for the rectangle and text
            if color_name == "blue":
                color = (255, 0, 0)  # Blue
            elif color_name == "orange":
                color = (0, 165, 255) # Orange
            elif color_name == "yellow":
                color = (0, 255, 255) # Yellow
            else:
                color = (0, 255, 0) # Green (default)

            # Draw rectangle and text
            cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
            cv2.putText(img, f"Cone {color_name}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)
            
            return f"{color_name}: ({x}, {y}, {x+w}, {y+h})"
        else:
            return f"{color_name}: Not Found"
        
    lower_blue = np.array([20, 0, 0])
    upper_blue = np.array([200, 255, 255])
    lower_orange = np.array([5, 100, 80])
    upper_orange = np.array([15, 255, 255])
    lower_yellow = np.array([15, 80, 30]) 
    upper_yellow = np.array([20, 255, 255])

    with open(output_file, "w") as f:
        f.write(detect_color("blue", lower_blue, upper_blue) + "\n")
        f.write(detect_color("orange", lower_orange, upper_orange) + "\n")
        f.write(detect_color("yellow", lower_yellow, upper_yellow) + "\n")

    # cv2.imwrite("cone_boxed.png", img)

    return img