import cv2

# Load both images in grayscale
img1 = cv2.imread("test-data/img1.jpg", 0)
img2 = cv2.imread("test-data/img2.jpg", 0)

# Create SIFT detector
sift = cv2.SIFT_create()

# Detect keypoints and descriptors
kp1, des1 = sift.detectAndCompute(img1, None)
kp2, des2 = sift.detectAndCompute(img2, None)

print("Keypoints in Image 1:", len(kp1))
print("Keypoints in Image 2:", len(kp2))

# Match descriptors using Brute-Force Matcher + KNN
bf = cv2.BFMatcher()
matches = bf.knnMatch(des1, des2, k=2)

# Apply Lowe's ratio test
good_matches = []
for m, n in matches:
    if m.distance < 0.75 * n.distance:
        good_matches.append([m])

# Count good matches
num_good_matches = len(good_matches)
print("Number of Good Matches:", num_good_matches)

# Define threshold to decide relatedness
threshold = 20  # You can tune this number as needed

if num_good_matches > threshold:
    print("✅ Result: The two images are likely RELATED (similar or modified version).")
else:
    print("❌ Result: The two images are DIFFERENT (not matching well).")
