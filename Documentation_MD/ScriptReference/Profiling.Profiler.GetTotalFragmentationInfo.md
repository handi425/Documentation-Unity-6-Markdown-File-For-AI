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

#  [Profiler](Profiling.Profiler.html).GetTotalFragmentationInfo

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

## Declaration

public static long GetTotalFragmentationInfo(NativeArray<int> stats);

### Parameters

stats | An array to receive the count of free blocks grouped by power of two sizes. Given a small array, Unity counts the larger free blocks together in the final array element.  
---|---  
  
### Returns

**long** Returns the total number of free blocks in the dynamic heap.

### Description

Returns heap memory fragmentation information.

Heap fragmentation is a measure of how much space is potentially unusable in
the dynamic heap. If your application has too much heap fragmentation it can
lead to memory allocation failures.  
  
There might be more total free memory than your application needs for an
allocation, but because this free memory is composed of two or more separate
smaller memory blocks, then the allocation might fail.  
  
Some memory usage patterns at runtime can cause the number of free blocks to
grow over time, which results in fragmentation of the heap.  
  
As an example, consider when Unity frees a large allocation, a single large
free block is returned to the heap. This large free block could then later be
used to satisfy many more smaller allocations if no smaller blocks are
available.  
  
If all these small allocations other than a single allocation in the middle of
this block are freed, then the heap now has two smaller free blocks either
side of the single remaining allocation. A new allocation of the original
large size might fail if there are no larger blocks available to use.  
  
As Unity dynamically allocates and frees memory, it manages the heap area by
keeping track of free memory blocks. Internally, Unity groups these free
memory blocks into lists of similar sizes - grouped in power of two sizes,
between one power of two and the next, specifically [ (2^n) .. (2^(n+1) - 1)
].  
  
e.g. blocks of sizes [1], [2..3], [4..7], [8..15], [16..31], [32..63],
[64..127], [128..256] ... bytes.  
  
This design gives quick and constant time allocator performance for all
allocations regardless of allocation size or heap capacity.  
  
You can use
[Profiler.GetTotalFragmentationInfo](Profiling.Profiler.GetTotalFragmentationInfo.html)
to keep track of the heap's free memory blocks over time.

    
    
    using Unity.Collections;
    using UnityEngine;
    using UnityEngine.Profiling;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        const int kFreeBlockPow2Buckets = 24;  
      
        void [Update](PlayerLoop.Update.html)()
        {
            var freeStats = new NativeArray<int>(kFreeBlockPow2Buckets, [Allocator.Temp](Unity.Collections.Allocator.Temp.html));
            var freeBlocks = [Profiler.GetTotalFragmentationInfo](Profiling.Profiler.GetTotalFragmentationInfo.html)(freeStats);  
      
            [Debug.Log](Debug.Log.html)(string.Format("Total Free Blocks: {0}", freeBlocks));
            for (int i = 0; i < kFreeBlockPow2Buckets; i++)
            {
                [Debug.Log](Debug.Log.html)(string.Format(" size[2^{0}] = {1} blocks", i, freeStats[i]));
            }
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

