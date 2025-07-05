import cv2
import numpy as np

# Step 1: Read the image
img = cv2.imread("/Users/vedmangal/Downloads/best.jpeg")

# Step 2: Flip the image horizontally
flipped = np.fliplr(img)

# Step 3: Crop a region from image
cropped = img[100:300, 200:400]  # rows, cols

# Step 4: Remove Red color from image
no_red = img.copy()
no_red[:, :, 2] = 0  # channel 2 = Red

# Step 5: Make top half of image black
black_top = img.copy()
black_top[:img.shape[0] // 2, :] = 0

# Step 6: Show all modified images
cv2.imshow("Original", img)
cv2.imshow("Flipped", flipped)
cv2.imshow("Cropped", cropped)
cv2.imshow("No Red", no_red)
cv2.imshow("Top Half Black", black_top)
 
# Step 7: Save final image
cv2.imwrite("output_blacktop.jpg", black_top)

# Step 8: Wait for key press and close
cv2.waitKey(0)