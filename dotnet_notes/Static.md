# Summary: Static Class in C# (From Dot Net Tutorials)

## 🔹 What Is a Static Class in C#?

A static class in C# is declared using the `static` keyword. It:
- Can contain only static members (methods, properties, fields).
- Cannot be instantiated.
- Is accessed directly using the class name.

Static classes are typically used for utility or helper methods that don’t require maintaining state.

---

## 🔹 Key Characteristics

- **No Instantiation**: You cannot create an instance of a static class.
- **Static Members Only**: All members must be static.
- **No Inheritance**: Static classes are implicitly sealed and cannot be inherited.
- **Single Instance**: Loaded and initialized once per application lifetime.

---

## 🔹 Practical Example

The article shows a `CommonTask` static class used to:
- Provide utility functions like getting the current machine name.
- Be used across other classes such as `Customer` and `CountryMaster`.

---

## 🔹 Differences Between Static and Non-Static Classes

| Feature             | Static Class                            | Non-Static Class                             |
|---------------------|------------------------------------------|----------------------------------------------|
| Instantiation        | Not allowed                             | Allowed                                      |
| Members              | Only static members                     | Can have static and instance members         |
| Constructors         | Only static constructor                 | Can have static and instance constructors    |
| Inheritance          | Cannot inherit or be inherited          | Can inherit and be inherited                 |
| Access               | Accessed via class name                 | Accessed via object instances                |

---

## 🔹 Use Cases for Static Classes

- Utility or helper methods (e.g., math functions, string operations)
- Centralized configuration settings
- Logging mechanisms
- Extension methods

They are ideal when methods/properties don’t rely on object state and need global accessibility.

---

👉 **Read the full article**: [Static Class in C# – Dot Net Tutorials](https://dotnettutorials.net/lesson/static-class-in-csharp/)
