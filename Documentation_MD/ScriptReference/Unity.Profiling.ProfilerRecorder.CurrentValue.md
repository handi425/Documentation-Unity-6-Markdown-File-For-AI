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

#  [ProfilerRecorder](Unity.Profiling.ProfilerRecorder.html).CurrentValue

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

public long CurrentValue;

### Description

Gets current value of the Profiler metric.

Use to obtain immediate profiler counter value or marker timing. If the
current value is the only data you are interested in, there is no need to
start ProfilerRecorder or allocate sample storage. In this case use 0 as a
capacity parameter when creating ProfilerRecorder.

    
    
    using UnityEngine;
    using Unity.Profiling;  
      
    public class Example
    {
        public static void LogCurrentSystemMemoryUsage()
        {
            var systemMemoryRecorder = new [ProfilerRecorder](Unity.Profiling.ProfilerRecorder.html)([ProfilerCategory.Memory](Unity.Profiling.ProfilerCategory.Memory.html), "[System](Rendering.VirtualTexturing.System.html) Used Memory", 0);
            [Debug.Log](Debug.Log.html)("[System](Rendering.VirtualTexturing.System.html) Used Memory (bytes): " + systemMemoryRecorder.CurrentValue);
        }
    }
    

Use _CurrentValue_ to retrieve timings of a code tagged with
[ProfilerMarker.Auto](Unity.Profiling.ProfilerMarker.Auto.html).

    
    
    using UnityEngine;
    using Unity.Profiling;  
      
    public class Example
    {
        static readonly [ProfilerMarker](Unity.Profiling.ProfilerMarker.html) k_MyMarker = new [ProfilerMarker](Unity.Profiling.ProfilerMarker.html)([ProfilerCategory.Scripts](Unity.Profiling.ProfilerCategory.Scripts.html), "MyMarker");  
      
        public static void TimeSynchronousMethodWithMarkers()
        {
            using (var recorder = [ProfilerRecorder.StartNew](Unity.Profiling.ProfilerRecorder.StartNew.html)([ProfilerCategory.Scripts](Unity.Profiling.ProfilerCategory.Scripts.html), "MyMarker"))
            {
                using (k_MyMarker.Auto())
                {
                    // ...
                }  
      
                [Debug.Log](Debug.Log.html)("MyMarker total time, ns:  " + recorder.CurrentValue);
            }
        }
    }
    

**Note:**  
[Stop](Unity.Profiling.ProfilerRecorder.Stop.html) resets _CurrentValue_ to
zero.

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

