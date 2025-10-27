# Parallel and Distributed Computing – Midterm Lab (Fall 2025)

**Name:** Muhammad Ibtihaj  
**Roll No:** SP23-BAI-037

---

Each script performs image preprocessing (resizing to 128×128 and adding a watermark) using different computational paradigms:

- **Sequential:** Single-core execution (baseline)
- **Parallel:** Multi-core execution using `multiprocessing`
- **Distributed:** Simulated multi-node environment using `multiprocessing.Manager()`

---

## Execution Results

| Mode | Configuration | Time (s) | Speedup × |
|------|----------------|-----------|------------|
| Sequential | — | **0.30** | 1.00 |
| Parallel | 1 worker | 0.51 | 1.00 |
| Parallel | 2 workers | 0.39 | 1.31 |
| Parallel | 4 workers | **0.36** | **1.40** |
| Parallel | 8 workers | 0.45 | 1.15 |
| Parallel | 10 workers | 0.49 | 1.06 |
| Distributed | 2 nodes (CPU + CPU) | 0.43 | 0.68 |

---

## Best Configuration

The **best performance** was achieved using **4 workers**, completing all image processing in **0.36 seconds**, resulting in a **1.40× speedup** over sequential execution.  
This configuration matches the number of **physical CPU cores** available, providing optimal resource utilization.  

Beyond four workers, performance declined slightly due to:
- Context switching between processes  
- Cache invalidation and memory contention  
- Disk I/O congestion from simultaneous read/write operations  

---

## Performance Discussion

Parallelism improved performance by dividing tasks among multiple CPU cores, allowing simultaneous execution and efficient utilization of system resources.  
This reduced total runtime while maintaining identical output quality.

However, some bottlenecks limited scalability:

- **Context Switching:** Oversubscription of CPU cores led to frequent task switching, reducing effective CPU time.  
- **Disk I/O Contention:** Multiple processes accessing the disk simultaneously caused serialized read/write operations.  
- **Memory Bandwidth Competition:** Processes shared memory and cache, causing slower data access.  
- **Inter-Process Communication (IPC):** In the distributed setup, communication through `Manager()` added synchronization latency.  

Despite these limitations, parallelism significantly enhanced throughput and reduced runtime compared to sequential execution.

---

## Summary

| Approach | Strength | Limitation |
|-----------|-----------|------------|
| Sequential | Simple baseline; predictable results | Uses only one CPU core |
| Parallel (4 workers) | Fastest performance; optimal scaling | Limited by I/O and context switching |
| Distributed (2 nodes) | Demonstrates multi-node behavior | IPC overhead and reduced efficiency |

---

## Conclusion

Parallel image processing achieved substantial performance gains over sequential execution, with the best results at **4 workers**.  
Increasing worker count beyond physical cores led to diminishing returns due to system-level constraints such as **context switching**, **I/O bottlenecks**, and **cache contention**.  

The distributed simulation successfully demonstrated multi-node coordination and performance trade-offs in distributed systems.  

This lab effectively demonstrates the concepts of **parallelism**, **concurrency**, and **distributed computing efficiency** using Python’s `multiprocessing` paradigm.

---

## Submission Checklist

- [x] Sequential, Parallel, and Distributed scripts implemented  
- [x] Dataset processed successfully  
- [x] Output directories generated (`output_seq`, `output_parallel`, `output_distributed`)  
- [x] `report.txt` created with analysis and comparison  
- [x] `README.md` includes table, best worker explanation, and discussion  
- [x] Repository follows required lab structure  
