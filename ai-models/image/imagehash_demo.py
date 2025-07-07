from PIL import Image
import imagehash

# Load two images (original and possibly stolen/edited)
img1 = Image.open("test-data/img1.jpg")
img2 = Image.open("test-data/img2.jpg")

# Generate perceptual hashes
hash1 = imagehash.phash(img1)
hash2 = imagehash.phash(img2)

# Print hash values and difference
print("Hash 1:", hash1)
print("Hash 2:", hash2)
print("Hash Difference:", abs(hash1 - hash2))

# Check similarity
if abs(hash1 - hash2) <= 10:
    print("Likely Same / Reused")
else:
    print("Probably Different Images")
