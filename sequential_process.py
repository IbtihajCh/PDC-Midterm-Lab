import os
import time
from PIL import Image, ImageDraw, ImageFont

input_dir = r"C:\University\Parallel and Distributed Computing\Mid Term Lab\data_set"
output_dir = r"C:\University\Parallel and Distributed Computing\Mid Term Lab\output_seq"

def add_watermark(image, text="© IBTIHAJ"):
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()
    draw.text((10, 10), text, fill=(255, 255, 255))
    return image

def process_image(src_path, dst_path):
    img = Image.open(src_path).convert("RGB")
    img = img.resize((128, 128))
    img = add_watermark(img)
    img.save(dst_path)

def main():
    print("\nSequential Image Processing Started...\n")
    start = time.perf_counter()
    
    total_images = sum(len(files) for _, _, files in os.walk(input_dir))
    processed = 0

    for root, _, files in os.walk(input_dir):
        for f in files:
            if f.lower().endswith((".jpg", ".png", ".jpeg")):
                rel_path = os.path.relpath(root, input_dir)
                out_folder = os.path.join(output_dir, rel_path)
                os.makedirs(out_folder, exist_ok=True)
                
                src = os.path.join(root, f)
                dst = os.path.join(out_folder, f)
                process_image(src, dst)
                processed += 1
    
    end = time.perf_counter()
    total_time = end - start

    
    print("\n" + "=" * 50)
    print("SEQUENTIAL PROCESSING SUMMARY")
    print("=" * 50)
    print(f"Input Folder : {input_dir}")
    print(f"Output Folder: {output_dir}")
    print(f"Total Images : {total_images}")
    print(f"Total Time   : {total_time:.2f} seconds")
    print("=" * 50)
    print("Task Completed Successfully!\n")

if __name__ == "__main__":
    main()
