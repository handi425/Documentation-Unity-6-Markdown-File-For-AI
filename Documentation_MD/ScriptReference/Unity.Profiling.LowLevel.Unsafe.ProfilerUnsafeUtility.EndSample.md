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

#
[ProfilerUnsafeUtility](Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.html).EndSample

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

public static void EndSample(IntPtr markerPtr);

### Parameters

markerPtr | Marker handle.  
---|---  
  
### Description

End profiling a piece of code marked with a custom name defined by this
instance of [ProfilerMarker](Unity.Profiling.ProfilerMarker.html).

Code marked with
[BeginSample](Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.BeginSample.html)
and
[EndSample](Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.EndSample.html)
shows up in the Profiler hierarchy. Always use
[BeginSample](Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.BeginSample.html)
or
[BeginSampleWithMetadata](Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.BeginSampleWithMetadata.html)
to start a section of the instrumented code.  
  
  
**Note:**
[EndSample](Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.EndSample.html)
is thread safe and can be used in jobified code.  
The low level Profiler API is included in a Release Build.

    
    
    using Unity.Collections.LowLevel.Unsafe;
    using Unity.Profiling.LowLevel;
    using Unity.Profiling.LowLevel.Unsafe;
    using [System](Rendering.VirtualTexturing.System.html);  
      
    class Example
    {
        static readonly IntPtr markerHandle = [ProfilerUnsafeUtility.CreateMarker](Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.CreateMarker.html)("MyMarker", [ProfilerUnsafeUtility.CategoryScripts](Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.CategoryScripts.html), [MarkerFlags.Default](Unity.Profiling.LowLevel.MarkerFlags.Default.html), 0);
        static unsafe void DoWork(int num)
        {
            [ProfilerUnsafeUtility.BeginSample](Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.BeginSample.html)(markerHandle);
            //...
            [ProfilerUnsafeUtility.EndSample](Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.EndSample.html)(markerHandle);
        }
    }
    

Additional resources:
[BeginSample](Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.BeginSample.html),
[BeginSampleWithMetadata](Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.BeginSampleWithMetadata.html),
[Recorder](Profiling.Recorder.html),
[ProfilerCPU](../Manual/ProfilerCPU.html).

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

