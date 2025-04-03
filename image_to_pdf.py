import os
import re
import argparse
from typing import List
from PIL import Image

def has_number(filename: str) -> re.Match | None:
    """Check if filename contains a number."""
    return re.search(r'\d+', filename)

def extract_number(filename: str) -> int:
    """Extract first number from filename for sorting."""
    match = re.search(r'\d+', filename)
    return int(match.group()) if match else float('inf')

def convert_images_to_pdf(image_folder: str, order: bool = True, pdf_folder: str = None) -> None:
    """
    Convert images in a folder to PDFs.
    - `order`: If True, merge labeled images into one PDF.
    - `pdf_folder`: Output folder. If None, defaults to image folder.
    """
    image_files: List[str] = [
        f for f in os.listdir(image_folder)
        if f.lower().endswith(('.png', '.jpg', '.jpeg'))
    ]

    if not image_files:
        print("No image files found.")
        return

    labeled_images = [f for f in image_files if has_number(f)]
    non_labeled_images = [f for f in image_files if not has_number(f)]

    labeled_paths = [os.path.join(image_folder, f) for f in labeled_images]
    non_labeled_paths = [os.path.join(image_folder, f) for f in non_labeled_images]

    # Use provided pdf_folder, or default to image folder
    output_folder = pdf_folder if pdf_folder else image_folder

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    if order:
        # Merge numbered images into one PDF
        if labeled_images:
            labeled_paths.sort(key=lambda x: extract_number(os.path.basename(x)))
            images: List[Image.Image] = []
            for img_path in labeled_paths:
                try:
                    img = Image.open(img_path).convert('RGB')
                    images.append(img)
                except Exception as e:
                    print(f"❌ Failed to open {img_path}: {e}")

            if images:
                output_path = os.path.join(output_folder, "combined_output.pdf")
                images[0].save(output_path, save_all=True, append_images=images[1:])
                print(f"✅ Combined PDF saved at: {output_path}")
            else:
                print("⚠️ No valid labeled images to combine.")

        # Save individual PDFs for non-labeled images
        for img_path in non_labeled_paths:
            try:
                img = Image.open(img_path).convert('RGB')
                base = os.path.splitext(os.path.basename(img_path))[0]
                output_path = os.path.join(output_folder, f"{base}.pdf")
                img.save(output_path)
                print(f"📄 Saved individual PDF: {output_path}")
            except Exception as e:
                print(f"❌ Failed to open {img_path}: {e}")
    else:
        # Save all images individually
        for img_path in labeled_paths + non_labeled_paths:
            try:
                img = Image.open(img_path).convert('RGB')
                base = os.path.splitext(os.path.basename(img_path))[0]
                output_path = os.path.join(output_folder, f"{base}.pdf")
                img.save(output_path)
                print(f"📄 Saved individual PDF: {output_path}")
            except Exception as e:
                print(f"❌ Failed to open {img_path}: {e}")

def main():
    parser = argparse.ArgumentParser(description="Convert images to PDF(s).")
    parser.add_argument("--order", type=bool, default=True, help="Merge labeled images into one PDF (default: True)")
    parser.add_argument("--pdf_folder", type=str, help="Optional path to save PDFs (default: same as image folder)")

    args = parser.parse_args()

    # 🔧 Set your image folder (fixed)
    image_folder = "./images_to_pdfs/"

    convert_images_to_pdf(image_folder=image_folder, order=args.order, pdf_folder=args.pdf_folder)

if __name__ == "__main__":
    main()