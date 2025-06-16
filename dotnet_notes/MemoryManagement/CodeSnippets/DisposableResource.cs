using System;

public class DisposableResource : IDisposable
{
    private bool disposed;
    private IntPtr unmanagedHandle;

    public DisposableResource()
    {
        unmanagedHandle = new IntPtr(123); // Simulated handle
    }

    public void Dispose()
    {
        if (!disposed)
        {
            disposed = true;
            GC.SuppressFinalize(this);
        }
    }

    ~DisposableResource()
    {
        Dispose();
    }
}
