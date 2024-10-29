def color_change(img,mid):
    
    image = img
    
    # Iterate through pixels in the top half
    for y in range(mid+2):
        for x in range(image.shape[1]):
            # Get BGR values of the pixel
            blue, green, red = image[y, x]

            # Modify the color values, ensuring they stay within 0-255
            red = max(0, red - 5)   # Subtract 5 from red, minimum 0
            green = min(255, green + 15) # Add 15 to green, maximum 255
            blue = max(0, blue - 30)  # Subtract 30 from blue, minimum 0
            
            # Update the pixel value in the image
            image[y, x] = [blue, green, red] 
    
    # cv2.imwrite("restored.png", image)

    return image