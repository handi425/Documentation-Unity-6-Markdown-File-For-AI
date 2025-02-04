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

#  [Profiler](Profiling.Profiler.html).GetMonoUsedSizeLong

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

public static long GetMonoUsedSizeLong();

### Returns

**long** Returns a long integer value of the memory in use.

### Description

Gets the allocated managed memory for live objects and non-collected objects.

This function returns the amount of allocated managed-memory for all objects,
both live and non-collected. Always call GC.Collect before calling this
function, because non-referenced objects still take up space until the garbage
collector (GC) collects them. This returns an ever-increasing value until
GC.Collect is called.  
  
The size of
[Profiler.GetMonoHeapSizeLong](Profiling.Profiler.GetMonoHeapSizeLong.html)
might decrease after a subsequent GC.Collect is called, if the first
GC.Collect call collected all remaining objects in a heap section. Allocating
new memory might also implicitly re-trigger GC.Collect and if it finds more
objects that are ready to be collected since the first call, it might lower
the value that Profiler.GetMonoUsedSizeLong returns even further. Also, Unity
might allocate managed memory on threads, or threaded code might get rid of
pointers to managed allocations, so while it might look like no code should
have changed the amount of managed allocations between two points of
measurements, that is not necessarily the case.

    
    
    using UnityEngine;
    using System.Collections;
    using UnityEngine.Profiling;  
      
    class GetMonoExample : [MonoBehaviour](MonoBehaviour.html)
    {
        void [Update](PlayerLoop.Update.html)()
        {
            System.GC.Collect();
            System.GC.WaitForPendingFinalizers();
            [Debug.Log](Debug.Log.html)("Mono used size" + [Profiler.GetMonoUsedSizeLong](Profiling.Profiler.GetMonoUsedSizeLong.html)() + "Bytes");
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

