### **Memory Allocation**

- **Static Allocation**: Memory size is fixed at compile time.
- **Dynamic Allocation**: Memory is allocated during runtime using:
    - `malloc()`, `calloc()`, `realloc()` in C.
    - `new` and `delete` in C++.
    - Automatic garbage collection in languages like Java, Python, [[C-Sharp]]

### **Memory Management Techniques**

- **Paging**: Divides memory into fixed-size pages.
- **Segmentation**: Divides memory based on logical sections (e.g., code, stack, heap).
- **Paging + Segmentation**: A hybrid approach used in modern OS.

### **Memory Leaks & Garbage Collection**

- **Memory Leak**: Occurs when allocated memory is not freed, leading to wastage.
- **Garbage Collection (GC)**: Automatic memory management in high-level languages.
- **Manual Deallocation**: Required in languages like C and C++.
### **Common Memory Issues**

- **Segmentation Fault**: Accessing restricted memory areas.
- **Buffer Overflow**: Writing beyond allocated memory.
- **Dangling Pointers**: Pointers referencing freed memory.