from rmn import RMN
import cv2

# Initialize the model
m = RMN()

# Detect emotions from an image
image = cv2.imread(r"c:\dataset\c2.jpg")
results = m.detect_emotion_for_single_frame(image)
print(results)

# Draw results on the image
image = m.draw(image, results)
cv2.imwrite("output.png", image)

best_face = max(results, key=lambda r: r["emo_proba"])
print(best_face["emo_label"], best_face["emo_proba"])