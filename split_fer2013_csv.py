import pandas as pd
import os

INPUT_CSV = "./saved/data/fer2013/fer2013.csv"
OUTPUT_DIR = "saved/data/fer2013"

os.makedirs(OUTPUT_DIR, exist_ok=True)

df = pd.read_csv(INPUT_CSV)

train_df = df[df["Usage"] == "Training"]
val_df = df[df["Usage"] == "PublicTest"]
test_df = df[df["Usage"] == "PrivateTest"]

train_df.to_csv(os.path.join(OUTPUT_DIR, "train.csv"), index=False)
val_df.to_csv(os.path.join(OUTPUT_DIR, "val.csv"), index=False)
test_df.to_csv(os.path.join(OUTPUT_DIR, "test.csv"), index=False)

print("✅ train.csv, val.csv, test.csv created")
print("Train:", len(train_df))
print("Val:", len(val_df))
print("Test:", len(test_df))