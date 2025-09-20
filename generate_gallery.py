import os

# --- SETTINGS ---
GITHUB_USER = "cardiff-caving"
REPO = "photos"  # your GitHub repo with images
BRANCH = "main"  # or 'master'
IMAGE_EXTENSIONS = (".jpg", ".jpeg", ".png", ".gif", ".webp")
OUTPUT_FILE = "gallery.html"

# --- SCRIPT ---
# Get raw GitHub URL prefix
GITHUB_RAW_URL = f"https://raw.githubusercontent.com/{GITHUB_USER}/{REPO}/{BRANCH}/"

# Scan current folder (or repo clone) for images
image_files = [f for f in os.listdir(".") if f.lower().endswith(IMAGE_EXTENSIONS)]

# Generate <img> tags
img_tags = "\n".join(
    f'  <img src="{GITHUB_RAW_URL}{f}" alt="{f}">'
    for f in sorted(image_files)
)

# Save to gallery.html
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write(img_tags)

print(f"✅ Gallery HTML saved as {OUTPUT_FILE}")
print("Copy and paste this into your main HTML file inside the <div class='gallery'>...</div> section.")
