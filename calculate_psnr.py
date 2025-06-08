import os
import sys
import numpy as np
from PIL import Image
import math

def calculate_psnr(img1, img2):
    mse = np.mean((np.array(img1, dtype=np.float32) - np.array(img2, dtype=np.float32)) ** 2)
    if mse == 0:
        return float('inf')
    max_pixel = 255.0
    psnr = 20 * math.log10(max_pixel / math.sqrt(mse))
    return psnr

def main(dir1, dir2):
    files = sorted(f for f in os.listdir(dir1) if f.endswith('.png'))

    psnr_values = []
    for file in files:
        path1 = os.path.join(dir1, file)
        path2 = os.path.join(dir2, file)

        if not os.path.exists(path2):
            print(f"File {file} not found in {dir2}, skipping.")
            continue

        img1 = Image.open(path1).convert('RGB')
        img2 = Image.open(path2).convert('RGB')

        if img1.size != img2.size:
            print(f"Skipping {file} due to different sizes.")
            continue

        psnr = calculate_psnr(img1, img2)
        psnr_values.append(psnr)
        print(f"{file}: PSNR = {psnr:.2f} dB")

    if psnr_values:
        avg_psnr = sum(psnr_values) / len(psnr_values)
        print(f"\nAverage PSNR: {avg_psnr:.2f} dB")
    else:
        print("No comparable PNG files found.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python compare_png_psnr.py <dir1> <dir2>")
        sys.exit(1)

    dir1 = sys.argv[1]
    dir2 = sys.argv[2]
    main(dir1, dir2)
