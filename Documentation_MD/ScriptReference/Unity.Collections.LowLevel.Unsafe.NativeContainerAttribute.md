[ ]()

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

LanguageEnglish

  * [English]()

  * C#

[ ](https://docs.unity3d.com)

## Scripting API

Version: Unity 6 Select a different version

LanguageEnglish

  * [English]()

# NativeContainerAttribute

class in Unity.Collections.LowLevel.Unsafe

/

Implemented in:[UnityEngine.CoreModule](UnityEngine.CoreModule.html)

Leave feedback

Suggest a change

## Success!

Thank you for helping us improve the quality of Unity Documentation. Although
we cannot accept all submissions, we do read each suggested change from our
users and will make updates where applicable.

Close

## Submission failed

For some reason your suggested change could not be submitted. Please <a>try
again</a> in a few minutes. And thank you for taking the time to help us
improve the quality of Unity Documentation.

Close

Your name Your email Suggestion* Submit suggestion

Cancel

[ ]()

### Description

Allows you to create your own custom native container.

Native containers let you create new container types, which don't allocate any
GC memory and give explicit control over allocations. The data contained must
be blittable. You can also use native containers in jobs. The job debugger
makes sure that all access to native containers is safe and throws exceptions
if any code contains race conditions or non-deterministic behavior.  
  
Native containers must embed an
[AtomicSafetyHandle](Unity.Collections.LowLevel.Unsafe.AtomicSafetyHandle.html)
to ensure that the job debugging system can detect any possible race
conditions, and leak tracking happens automatically whenever
[UnsafeUtility.MallocTracked](Unity.Collections.LowLevel.Unsafe.UnsafeUtility.MallocTracked.html)
is called.  
  
To create your own custom container use the following code example. You should
add test coverage for all scenarios, particularly for the integration into
jobs, to ensure that all race conditions are prevented. If you implement a
custom container incorrectly, it might crash Unity without throwing an
exception.  
  
You can also use the Collections package to create a registered custom
allocator to allocate your own custom container. For more information, see the
Collections documentation on [Custom
allocators](https://docs.unity3d.com/Packages/com.unity.collections@latest/index.html?subfolder=/manual/allocator-
custom-define.html).

    
    
    using System.Diagnostics;
    using [System](Rendering.VirtualTexturing.System.html);
    using Unity.Collections.LowLevel.Unsafe;
    using Unity.Collections;
    using Unity.Burst;  
      
    // Marks our struct as a NativeContainer.
    // If ENABLE_UNITY_COLLECTIONS_CHECKS is enabled,
    // it is required that m_Safety with exactly this name.
    [NativeContainer]
    // The [NativeContainerSupportsMinMaxWriteRestriction] enables
    // a common jobification pattern where an [IJobParallelFor](Unity.Jobs.IJobParallelFor.html) is split into ranges
    // And the job is only allowed to access the index range being Executed by that worker thread.
    // Effectively limiting access of the array to the specific index passed into the Execute(int index) method
    // This attribute requires m_MinIndex & m_MaxIndex to exist.
    // and the container is expected to perform out of bounds checks against it.
    // m_MinIndex & m_MaxIndex will be set by the job scheduler before Execute is called on the worker thread.
    [NativeContainerSupportsMinMaxWriteRestriction]
    // It is recommended to always implement a Debugger proxy
    // to visualize the contents of the array in VisualStudio and other tools.
    [DebuggerDisplay("[Length](UIElements.Length.html) = {[Length](UIElements.Length.html)}")]
    [DebuggerTypeProxy(typeof(NativeCustomArrayDebugView<>))]
    public unsafe struct NativeCustomArray<T> : IDisposable where T : unmanaged
    {
        internal void* m_Buffer;
        internal int m_Length;  
      
    #if ENABLE_UNITY_COLLECTIONS_CHECKS
        internal int m_MinIndex;
        internal int m_MaxIndex;
        internal [AtomicSafetyHandle](Unity.Collections.LowLevel.Unsafe.AtomicSafetyHandle.html) m_Safety;
        internal static readonly SharedStatic<int> s_staticSafetyId = SharedStatic<int>.GetOrCreate<NativeCustomArray<T>>();
    #endif  
      
        internal [Allocator](Unity.Collections.Allocator.html) m_AllocatorLabel;  
      
        public NativeCustomArray(int length, [Allocator](Unity.Collections.Allocator.html) allocator)
        {
            int totalSize = [UnsafeUtility.SizeOf](Unity.Collections.LowLevel.Unsafe.UnsafeUtility.SizeOf.html)<T>() * length;  
      
    #if ENABLE_UNITY_COLLECTIONS_CHECKS
            // Native allocation is only valid for Temp, TempJob, Persistent or registered custom allocator
            if (allocator <= [Allocator.None](Unity.Collections.Allocator.None.html))
                throw new ArgumentException("[Allocator](Unity.Collections.Allocator.html) must be Temp, TempJob, Persistent or registered custom allcoator", "allocator");
            if (length < 0)
                throw new ArgumentOutOfRangeException("length", "[Length](UIElements.Length.html) must be >= 0");
            if (![UnsafeUtility.IsBlittable](Unity.Collections.LowLevel.Unsafe.UnsafeUtility.IsBlittable.html)<T>())
                throw new ArgumentException(string.Format("{0} used in NativeCustomArray<{0}> must be blittable", typeof(T)));
    #endif  
      
            m_Buffer = AllocatorManager.Allocate(allocator, totalSize, [UnsafeUtility.AlignOf](Unity.Collections.LowLevel.Unsafe.UnsafeUtility.AlignOf.html)<T>());
            [UnsafeUtility.MemClear](Unity.Collections.LowLevel.Unsafe.UnsafeUtility.MemClear.html)(m_Buffer, totalSize);  
      
            m_Length = length;
            m_AllocatorLabel = allocator;  
      
    #if ENABLE_UNITY_COLLECTIONS_CHECKS
            m_MinIndex = 0;
            m_MaxIndex = length - 1;
            m_Safety = CollectionHelper.CreateSafetyHandle(allocator);
            CollectionHelper.SetStaticSafetyId<NativeCustomArray<T>>(ref m_Safety, ref s_staticSafetyId.Data);
    #endif
        }  
      
        public int [Length](UIElements.Length.html) { get { return m_Length; } }  
      
        public unsafe T this[int index]
        {
            get
            {
    #if ENABLE_UNITY_COLLECTIONS_CHECKS
                // If the container is currently not allowed to read from the buffer
                // then this will throw an exception.
                // This handles all cases, from already disposed containers
                // to safe multithreaded access.
                [AtomicSafetyHandle.CheckReadAndThrow](Unity.Collections.LowLevel.Unsafe.AtomicSafetyHandle.CheckReadAndThrow.html)(m_Safety);  
      
                // Perform out of range checks based on
                // the NativeContainerSupportsMinMaxWriteRestriction policy
                if (index < m_MinIndex || index > m_MaxIndex)
                    FailOutOfRangeError(index);
    #endif
                // Read the element from the allocated native memory
                return [UnsafeUtility.ReadArrayElement](Unity.Collections.LowLevel.Unsafe.UnsafeUtility.ReadArrayElement.html)<T>(m_Buffer, index);
            }  
      
            set
            {
    #if ENABLE_UNITY_COLLECTIONS_CHECKS
                // If the container is currently not allowed to write to the buffer
                // then this will throw an exception.
                // This handles all cases, from already disposed containers
                // to safe multithreaded access.
                [AtomicSafetyHandle.CheckWriteAndThrow](Unity.Collections.LowLevel.Unsafe.AtomicSafetyHandle.CheckWriteAndThrow.html)(m_Safety);  
      
                // Perform out of range checks based on
                // the NativeContainerSupportsMinMaxWriteRestriction policy
                if (index < m_MinIndex || index > m_MaxIndex)
                    FailOutOfRangeError(index);
    #endif
                // Writes value to the allocated native memory
                [UnsafeUtility.WriteArrayElement](Unity.Collections.LowLevel.Unsafe.UnsafeUtility.WriteArrayElement.html)(m_Buffer, index, value);
            }
        }  
      
        public T[] ToArray()
        {
    #if ENABLE_UNITY_COLLECTIONS_CHECKS
            [AtomicSafetyHandle.CheckReadAndThrow](Unity.Collections.LowLevel.Unsafe.AtomicSafetyHandle.CheckReadAndThrow.html)(m_Safety);
    #endif  
      
            var array = new T[[Length](UIElements.Length.html)];
            for (var i = 0; i < [Length](UIElements.Length.html); i++)
                array[i] = [UnsafeUtility.ReadArrayElement](Unity.Collections.LowLevel.Unsafe.UnsafeUtility.ReadArrayElement.html)<T>(m_Buffer, i);
            return array;
        }  
      
        public bool IsCreated
        {
            get { return m_Buffer != null; }
        }  
      
        public void Dispose()
        {
    #if ENABLE_UNITY_COLLECTIONS_CHECKS
            CollectionHelper.DisposeSafetyHandle(ref m_Safety);
    #endif  
      
            AllocatorManager.Free(m_AllocatorLabel, m_Buffer);
            m_Buffer = null;
            m_Length = 0;
        }  
      
    #if ENABLE_UNITY_COLLECTIONS_CHECKS
        private void FailOutOfRangeError(int index)
        {
            if (index < [Length](UIElements.Length.html) && (m_MinIndex != 0 || m_MaxIndex != [Length](UIElements.Length.html) - 1))
                throw new IndexOutOfRangeException(string.Format(
                    "Index {0} is out of restricted [IJobParallelFor](Unity.Jobs.IJobParallelFor.html) range [{1}...{2}] in ReadWriteBuffer.\n" +
                    "ReadWriteBuffers are restricted to only read & write the element at the job index. " +
                    "You can use double buffering strategies to avoid race conditions due to " +
                    "reading & writing in parallel to the same elements from a job.",
                    index, m_MinIndex, m_MaxIndex));  
      
            throw new IndexOutOfRangeException(string.Format("Index {0} is out of range of '{1}' [Length](UIElements.Length.html).", index, [Length](UIElements.Length.html)));
        }  
      
    #endif
    }  
      
    // Visualizes the custom array in the C# debugger
    internal sealed class NativeCustomArrayDebugView<T> where T : unmanaged
    {
        private NativeCustomArray<T> m_Array;  
      
        public NativeCustomArrayDebugView(NativeCustomArray<T> array)
        {
            m_Array = array;
        }  
      
        public T[] Items
        {
            get { return m_Array.ToArray(); }
        }
    }
    

Is something described here not working as you expect it to? It might be a
**Known Issue**. Please check with the Issue Tracker at
[issuetracker.unity3d.com](https://issuetracker.unity3d.com).

Copyright ©2005-2025 Unity Technologies. All rights reserved. Built from:
6000.0.36f1 (02b661dc617c). Built on: 2025-01-14.

[Tutorials](https://unity3d.com/learn) [Community
Answers](https://answers.unity3d.com) [Knowledge
Base](https://support.unity3d.com/hc/en-us)
[Forums](https://forum.unity3d.com) [Asset Store](https://unity3d.com/asset-
store) [Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)
[Legal](https://unity.com/legal) [Privacy
Policy](https://unity.com/legal/privacy-policy)
[Cookies](https://unity.com/legal/cookie-policy) [Do Not Sell or Share My
Personal Information](https://unity.com/legal/do-not-sell-my-personal-
information)

[Your Privacy Choices (Cookie Settings)](javascript:void\(0\);)

