## **1. Types of Memory in C#**

C# memory is divided into two main areas:

- **Stack** (for value types and method calls)
- **Heap** (for reference types and dynamically allocated objects)

### **Stack Memory**

- Stores value types (`int`, `char`, `float`, `struct`, etc.).
- Uses **LIFO (Last In, First Out)** allocation.
- Memory is automatically freed when the method returns.

### **Heap Memory**

- Stores reference types (`class`, `object`, `array`, `string`, etc.).
- Requires garbage collection to reclaim unused memory.
- Allocates memory dynamically at runtime.

---

## **2. Garbage Collection in C#**

The **Garbage Collector (GC)** in C# automatically reclaims memory used by objects that are no longer accessible. It runs in the background and helps prevent memory leaks.

### **Generations in GC**

The GC organizes memory into **three generations** to optimize performance:

1. **Gen 0** – New objects are allocated here. GC frequently cleans this.
2. **Gen 1** – Objects that survive Gen 0 collection move here.
3. **Gen 2** – Long-lived objects like static variables or large objects.

GC runs **more frequently** in Gen 0 and **less frequently** in Gen 2.

### **Garbage Collection Triggers**

GC is triggered automatically when:

- Available memory is low.
- An object survives multiple collections and moves to an older generation.
- You explicitly call `GC.Collect()` (not recommended in most cases).

---

## **3. Memory Management Best Practices**

### ✅ **Use `using` with IDisposable**

- Ensures resources like file handles, database connections, and sockets are released properly.
- Example: 
```
using (StreamReader reader = new StreamReader("file.txt"))
{
    string content = reader.ReadToEnd();
}  // reader is disposed automatically here

```