import cv2
import numpy as np
from find_monitor_sizes import monitorSizes

objMonitor = monitorSizes()
objMonitor.setMonitorConfig([])
screenStatsArr = objMonitor.getChosenMonitorStats(1)
screenWidth, screenHeight = screenStatsArr[0], screenStatsArr[1]

def resize_image(srcImgPath, newImgPath, sizeMult):
    image1 = cv2.imread(srcImgPath)
    
    new_width = image1.shape[1] * sizeMult
    new_height = image1.shape[0] * sizeMult
    new_size = (new_width, new_height)

    # Resize the image using INTER_CUBIC or INTER_LANCZOS4 interpolation
    resized_image_cubic = cv2.resize(image1, new_size, interpolation=cv2.INTER_CUBIC)
    # resized_image_lanczos = cv2.resize(srcImgPath, new_size, interpolation=cv2.INTER_LANCZOS4)


    # Save the resized images
    cv2.imwrite(newImgPath, resized_image_cubic)
    # cv2.imwrite(newImgPath, resized_image_lanczos)
    
# resize_image('./images/escape_pod_images/building-with-inground-container_1.png', './images/escape_pod_images/resized-building.png', 6)

# Load the images
curMinimap = cv2.imread('./images/escape_pod_images/better-escape-pod-minimap_1.png')
ingroundContainer_image1 = cv2.imread('./images/escape_pod_images/bigger-building.png')

# convert to greyscale
curMinimap_bw = cv2.cvtColor(curMinimap,cv2.COLOR_BGR2GRAY)
ingroundContainer_image1_bw = cv2.cvtColor(ingroundContainer_image1,cv2.COLOR_BGR2GRAY)


# # Perform template matching
# result = cv2.matchTemplate(curMinimap_bw, rotateTest, cv2.TM_CCOEFF_NORMED)

# # Threshold the result to find matches
# threshold = 0.8
# locations = np.where(result >= threshold)

# # Draw rectangles around the matches
# for pt in zip(*locations[::-1]):
#     cv2.rectangle(curMinimap, pt, (pt[0] + rotateTest.shape[1], pt[1] + rotateTest.shape[0]), (0, 0, 255), 2)

# # Display the result
# cv2.imshow('Detected Objects', curMinimap)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# Create an ORB detector
orb = cv2.ORB_create()
# surf = cv2.xfeatures2d.SURF_create(400)

# Find keypoints and descriptors
keypoints1, descriptors1 = orb.detectAndCompute(curMinimap_bw, None)
keypoints2, descriptors2 = orb.detectAndCompute(ingroundContainer_image1_bw, None)

# Create a Brute-Force matcher
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=False)

# Match descriptors
matches = bf.match(descriptors1, descriptors2)

# Sort matches by distance
matches = sorted(matches, key = lambda x:x.distance)

# Draw the top N matches
N = 50
image_matches = cv2.drawMatches(curMinimap, keypoints1, ingroundContainer_image1, keypoints2, matches[:N], None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

# Display the result
cv2.imshow('Matches', image_matches)
cv2.waitKey(0)
cv2.destroyAllWindows()