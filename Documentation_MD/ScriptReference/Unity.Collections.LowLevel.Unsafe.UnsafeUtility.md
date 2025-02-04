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

# UnsafeUtility

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

Contains unsafe utility methods.

### Static Methods

[AddressOf](Unity.Collections.LowLevel.Unsafe.UnsafeUtility.AddressOf.html)|
Gets the memory address of a struct.  
---|---  
[AlignOf](Unity.Collections.LowLevel.Unsafe.UnsafeUtility.AlignOf.html)| Gets
the minimum alignment of a struct.  
[ArrayElementAsRef](Unity.Collections.LowLevel.Unsafe.UnsafeUtility.ArrayElementAsRef.html)|
Gets a reference to an array element at its current location in memory.  
[As](Unity.Collections.LowLevel.Unsafe.UnsafeUtility.As.html)| Reinterprets
the reference as a reference of a different type.  
[AsRef](Unity.Collections.LowLevel.Unsafe.UnsafeUtility.AsRef.html)| Gets a
reference to the struct at its current location in memory.  
[CheckForLeaks](Unity.Collections.LowLevel.Unsafe.UnsafeUtility.CheckForLeaks.html)|
Gets a list of memory leaks.  
[CopyObjectAddressToPtr](Unity.Collections.LowLevel.Unsafe.UnsafeUtility.CopyObjectAddressToPtr.html)|
Assigns an object reference to a struct or pinned class.  
[CopyPtrToStructure](Unity.Collections.LowLevel.Unsafe.UnsafeUtility.CopyPtrToStructure.html)|
Copies sizeof(T) bytes from a memory pointer to a struct.  
[CopyStructureToPtr](Unity.Collections.LowLevel.Unsafe.UnsafeUtility.CopyStructureToPtr.html)|
Copies sizeof(T) bytes from a memory pointer to a struct.  
[EnumEquals](Unity.Collections.LowLevel.Unsafe.UnsafeUtility.EnumEquals.html)|
Determines whether specified enums are equal without boxing.  
[EnumToInt](Unity.Collections.LowLevel.Unsafe.UnsafeUtility.EnumToInt.html)|
Gets the integer representation of an enum value without boxing.  
[ForgiveLeaks](Unity.Collections.LowLevel.Unsafe.UnsafeUtility.ForgiveLeaks.html)|
Tells the leak checking system to ignore any memory allocations made up to
that point.  
[Free](Unity.Collections.LowLevel.Unsafe.UnsafeUtility.Free.html)| Free
memory.  
[FreeTracked](Unity.Collections.LowLevel.Unsafe.UnsafeUtility.FreeTracked.html)|
Free memory with leak tracking.  
[GetFieldOffset](Unity.Collections.LowLevel.Unsafe.UnsafeUtility.GetFieldOffset.html)|
Returns the offset of the field relative struct or class it is contained in.  
[GetLeakDetectionMode](Unity.Collections.LowLevel.Unsafe.UnsafeUtility.GetLeakDetectionMode.html)|
Gets the mode of memory leak detection.  
[IsBlittable](Unity.Collections.LowLevel.Unsafe.UnsafeUtility.IsBlittable.html)|
Gets whether a struct is blittable.  
[IsNativeContainerType](Unity.Collections.LowLevel.Unsafe.UnsafeUtility.IsNativeContainerType.html)|
Checks whether a struct or type is a NativeContainer.  
[IsUnmanaged](Unity.Collections.LowLevel.Unsafe.UnsafeUtility.IsUnmanaged.html)|
Checks whether the struct or type is unmanaged.  
[IsValidAllocator](Unity.Collections.LowLevel.Unsafe.UnsafeUtility.IsValidAllocator.html)|
Returns true if the allocator label is valid and can be used to allocate or
deallocate memory.  
[IsValidNativeContainerElementType](Unity.Collections.LowLevel.Unsafe.UnsafeUtility.IsValidNativeContainerElementType.html)|
Checks whether the type is acceptable as an element type in a native
container.  
[Malloc](Unity.Collections.LowLevel.Unsafe.UnsafeUtility.Malloc.html)|
Allocate memory.  
[MallocTracked](Unity.Collections.LowLevel.Unsafe.UnsafeUtility.MallocTracked.html)|
Allocate memory with leak tracking.  
[MemClear](Unity.Collections.LowLevel.Unsafe.UnsafeUtility.MemClear.html)|
Clear memory.  
[MemCmp](Unity.Collections.LowLevel.Unsafe.UnsafeUtility.MemCmp.html)| Checks
whether two memory regions are identical.  
[MemCpy](Unity.Collections.LowLevel.Unsafe.UnsafeUtility.MemCpy.html)| Copy
memory.  
[MemCpyReplicate](Unity.Collections.LowLevel.Unsafe.UnsafeUtility.MemCpyReplicate.html)|
Copy memory and replicate.  
[MemCpyStride](Unity.Collections.LowLevel.Unsafe.UnsafeUtility.MemCpyStride.html)|
Similar to UnsafeUtility.MemCpy but can skip bytes via desinationStride and
sourceStride.  
[MemMove](Unity.Collections.LowLevel.Unsafe.UnsafeUtility.MemMove.html)| Move
memory.  
[MemSet](Unity.Collections.LowLevel.Unsafe.UnsafeUtility.MemSet.html)| Set
memory to specified value.  
[MemSwap](Unity.Collections.LowLevel.Unsafe.UnsafeUtility.MemSwap.html)| Swap
the content of two memory buffers of the same size.  
[PinGCArrayAndGetDataAddress](Unity.Collections.LowLevel.Unsafe.UnsafeUtility.PinGCArrayAndGetDataAddress.html)|
Keeps a strong GC reference to an array and pins it.  
[PinGCObjectAndGetAddress](Unity.Collections.LowLevel.Unsafe.UnsafeUtility.PinGCObjectAndGetAddress.html)|
Keeps a strong GC reference to an object and pins it.  
[ReadArrayElement](Unity.Collections.LowLevel.Unsafe.UnsafeUtility.ReadArrayElement.html)|
Read array element.  
[ReadArrayElementWithStride](Unity.Collections.LowLevel.Unsafe.UnsafeUtility.ReadArrayElementWithStride.html)|
Read array element with stride.  
[ReleaseGCObject](Unity.Collections.LowLevel.Unsafe.UnsafeUtility.ReleaseGCObject.html)|
Releases a GC Object Handle, previously aquired by
UnsafeUtility.PinGCObjectAndGetAddress.  
[SetLeakDetectionMode](Unity.Collections.LowLevel.Unsafe.UnsafeUtility.SetLeakDetectionMode.html)|
Set the leak detection mode.  
[SizeOf](Unity.Collections.LowLevel.Unsafe.UnsafeUtility.SizeOf.html)| Get the
size of struct.  
[WriteArrayElement](Unity.Collections.LowLevel.Unsafe.UnsafeUtility.WriteArrayElement.html)|
Write array element.  
[WriteArrayElementWithStride](Unity.Collections.LowLevel.Unsafe.UnsafeUtility.WriteArrayElementWithStride.html)|
Write array element with stride.  
  
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

