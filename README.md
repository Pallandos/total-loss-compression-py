# tlcPy : Total Loss Compression

## Usage

```py
from tlcpy import compress, unzip

GEMINI_KEY = "your_google_gemini_api_key_here"
OPENAI_KEY = "your_openai_api_key_here"

# 1. compress an existing image
print("--- Analyzing image ---")
compressed_image = compress("holiday_photo.jpg", GEMINI_KEY)
print(compressed_image)

# 2. unzip the previously compressed image
result = unzip(
    description=compressed_image, 
    openai_api_key=OPENAI_KEY,
    save_path="holiday.png"
)
print(result)
```