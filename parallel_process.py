import os
import time
from PIL import Image, ImageDraw, ImageFont
from concurrent.futures import ProcessPoolExecutor

input_dir = r"C:\University\Parallel and Distributed Computing\Mid Term Lab\data_set"
output_dir = r"C:\University\Parallel and Distributed Computing\Mid Term Lab\output_parallel"

def add_watermark(image, text="© IBTIHAJ"):
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()
    draw.text((10, 10), text, fill=(255, 255, 255))
    return image

def process_image(paths):
    src, dst = paths
    img = Image.open(src).convert("RGB")
    img = img.resize((128, 128))
    img = add_watermark(img)
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    img.save(dst)

def run_parallel(workers):
    start = time.perf_counter()
    paths = []
    for root, _, files in os.walk(input_dir):
        for f in files:
            if f.lower().endswith((".jpg", ".png", ".jpeg")):
                rel = os.path.relpath(root, input_dir)
                out = os.path.join(output_dir, rel, f)
                paths.append((os.path.join(root, f), out))
    with ProcessPoolExecutor(max_workers=workers) as ex:
        ex.map(process_image, paths)
    return time.perf_counter() - start

if __name__ == "__main__":
    print("\nPARALLEL IMAGE PROCESSING STARTED\n")
    seq_time = run_parallel(1)
    results = [(1, seq_time, 1.00)]
    for w in [2, 4, 8, 10]:
        t = run_parallel(w)
        results.append((w, t, seq_time / t))

    print("=" * 45)
    print("PARALLEL PROCESSING PERFORMANCE SUMMARY")
    print("=" * 45)
    print(f"{'Workers':<10} | {'Time (s)':<10} | {'Speedup':<10}")
    print("-" * 45)
    for w, t, s in results:
        print(f"{w:<10} | {t:<10.2f} | {s:<10.2f}x")
    print("=" * 45)
    best = min(results, key=lambda x: x[1])
    print(f"Best Configuration: {best[0]} workers ({best[2]:.2f}x faster)\n")
