import os
import time
from multiprocessing import Process, Manager
from PIL import Image, ImageDraw, ImageFont

input_dir = r"C:\University\Parallel and Distributed Computing\Mid Term Lab\data_set"
output_dir = r"C:\University\Parallel and Distributed Computing\Mid Term Lab\output_distributed"

def add_watermark(image, text="© IBTIHAJ"):
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()
    draw.text((10, 10), text, fill=(255, 255, 255))
    return image

def process_image(src, dst):
    img = Image.open(src).convert("RGB")
    img = img.resize((128, 128))
    img = add_watermark(img)
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    img.save(dst)

def node_worker(images, node_name, return_dict):
    start = time.perf_counter()
    for i, (src, dst) in enumerate(images, 1):
        process_image(src, dst)
        print(f"{node_name}: Processed {i}/{len(images)} images", end="\r")
    duration = time.perf_counter() - start
    return_dict[node_name] = duration
    print(f"\n{node_name} finished: {len(images)} images in {duration:.2f}s")

def main():
    print("\nSimulated Distributed Image Processing Started...\n")

    paths = []
    for root, _, files in os.walk(input_dir):
        for f in files:
            if f.lower().endswith((".jpg", ".png", ".jpeg")):
                rel = os.path.relpath(root, input_dir)
                out_path = os.path.join(output_dir, rel, f)
                paths.append((os.path.join(root, f), out_path))

    total_images = len(paths)
    
    mid = total_images // 2
    node1_imgs, node2_imgs = paths[:mid], paths[mid:]

    manager = Manager()
    times = manager.dict()

    p1 = Process(target=node_worker, args=(node1_imgs, "Node 1 (CPU)", times))
    p2 = Process(target=node_worker, args=(node2_imgs, "Node 2 (CPU)", times))

    start_total = time.perf_counter()
    p1.start(); p2.start()
    p1.join();  p2.join()
    end_total = time.perf_counter()

    total_time = end_total - start_total
    seq_sim = sum(times.values())
    efficiency = seq_sim / total_time if total_time > 0 else 0

    print("\n" + "=" * 55)
    print("DISTRIBUTED PROCESSING SUMMARY")
    print("=" * 55)
    print(f"Input Folder : {input_dir}")
    print(f"Output Folder: {output_dir}")
    print(f"Total Images : {total_images}")
    print("-" * 55)
    for node, t in times.items():
        print(f"{node:<15} → {t:.2f} seconds")
    print("-" * 55)
    print(f"Total Distributed Time : {total_time:.2f} seconds")
    print(f"Efficiency (Speedup)   : {efficiency:.2f}× over sequential")
    print("=" * 55)
    print("Simulation Completed Successfully!\n")

# ---------- Run ----------
if __name__ == "__main__":
    main()
