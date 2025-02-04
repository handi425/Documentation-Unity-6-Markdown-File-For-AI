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

# ProfilerRecorder Constructor

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

public ProfilerRecorder(string categoryName, string statName, int capacity,
[Unity.Profiling.ProfilerRecorderOptions](Unity.Profiling.ProfilerRecorderOptions.html)
options);

## Declaration

public
ProfilerRecorder([Unity.Profiling.ProfilerCategory](Unity.Profiling.ProfilerCategory.html)
category, string statName, int capacity,
[Unity.Profiling.ProfilerRecorderOptions](Unity.Profiling.ProfilerRecorderOptions.html)
options);

### Parameters

categoryName | Profiler category name.  
---|---  
statName | Profiler marker or counter name.  
capacity | Maximum amount of samples to be collected.  
options | Profiler recorder options.  
category | Profiler category identifier.  
  
### Description

Constructs ProfilerRecorder instance with a Profiler metric name and category.

Use to initialize ProfilerRecorder and associate it with a specific Profiler
metric.  
  
By default, ProfilerRecorder does not start collecting data immediately. Use
[ProfilerRecorderOptions.StartImmediately](Unity.Profiling.ProfilerRecorderOptions.StartImmediately.html)
to enable collection together with ProfilerRecorder construction.
Alternatively, use [Start](Unity.Profiling.ProfilerRecorder.Start.html) method
after construction. If the
[CurrentValue](Unity.Profiling.ProfilerRecorder.CurrentValue.html) is the only
data you are interested in, you do not need to start ProfilerRecorder or
allocate sample storage. In this case, use 0 as a _capacity_ parameter when
creating ProfilerRecorder.  
  
Using a negative number as a _capacity_ parameter throws ArgumentException.  
  
**Note:**  
ProfilerRecorder allocates memory and must be disposed when it is no longer
needed.

    
    
    using Unity.Profiling;
    using UnityEngine;  
      
    public class ExampleScript : [MonoBehaviour](MonoBehaviour.html)
    {
        [ProfilerRecorder](Unity.Profiling.ProfilerRecorder.html) systemMemoryRecorder;
        [ProfilerRecorder](Unity.Profiling.ProfilerRecorder.html) gcMemoryRecorder;
        [ProfilerRecorder](Unity.Profiling.ProfilerRecorder.html) mainThreadTimeRecorder;  
      
        void OnEnable()
        {
            systemMemoryRecorder = new [ProfilerRecorder](Unity.Profiling.ProfilerRecorder.html)([ProfilerCategory.Memory](Unity.Profiling.ProfilerCategory.Memory.html), "[System](Rendering.VirtualTexturing.System.html) Used Memory", 1, [ProfilerRecorderOptions.Default](Unity.Profiling.ProfilerRecorderOptions.Default.html) | [ProfilerRecorderOptions.StartImmediately](Unity.Profiling.ProfilerRecorderOptions.StartImmediately.html));
            gcMemoryRecorder = new [ProfilerRecorder](Unity.Profiling.ProfilerRecorder.html)([ProfilerCategory.Memory](Unity.Profiling.ProfilerCategory.Memory.html), "GC Reserved Memory", 1, [ProfilerRecorderOptions.Default](Unity.Profiling.ProfilerRecorderOptions.Default.html) | [ProfilerRecorderOptions.StartImmediately](Unity.Profiling.ProfilerRecorderOptions.StartImmediately.html));
            mainThreadTimeRecorder = new [ProfilerRecorder](Unity.Profiling.ProfilerRecorder.html)([ProfilerCategory.Internal](Unity.Profiling.ProfilerCategory.Internal.html), "Main Thread", 15);
            mainThreadTimeRecorder.Start();
        }  
      
        void OnDisable()
        {
            systemMemoryRecorder.Dispose();
            gcMemoryRecorder.Dispose();
            mainThreadTimeRecorder.Dispose();
        }
    }
    

Additional resources:
[StartNew](Unity.Profiling.ProfilerRecorder.StartNew.html).

* * *

## Declaration

public ProfilerRecorder(string statName, int capacity,
[Unity.Profiling.ProfilerRecorderOptions](Unity.Profiling.ProfilerRecorderOptions.html)
options);

### Parameters

statName | Profiler marker or counter name.  
---|---  
capacity | Maximum amount of samples to be collected.  
options | Profiler recorder options.  
  
### Description

Constructs ProfilerRecorder instance with a Profiler metric name.

Use to initialize ProfilerRecorder with a metric name only. Unity searches for
the metric name across all categories, and as such, initialization is slower
than if you specify a category.

* * *

## Declaration

public
ProfilerRecorder([Unity.Profiling.ProfilerCategory](Unity.Profiling.ProfilerCategory.html)
category, char* statName, int statNameLen, int capacity,
[Unity.Profiling.ProfilerRecorderOptions](Unity.Profiling.ProfilerRecorderOptions.html)
options);

## Declaration

public
ProfilerRecorder([Unity.Profiling.ProfilerMarker](Unity.Profiling.ProfilerMarker.html)
marker, int capacity,
[Unity.Profiling.ProfilerRecorderOptions](Unity.Profiling.ProfilerRecorderOptions.html)
options);

## Declaration

public
ProfilerRecorder([Unity.Profiling.LowLevel.Unsafe.ProfilerRecorderHandle](Unity.Profiling.LowLevel.Unsafe.ProfilerRecorderHandle.html)
statHandle, int capacity,
[Unity.Profiling.ProfilerRecorderOptions](Unity.Profiling.ProfilerRecorderOptions.html)
options);

### Parameters

category | Profiler category identifier.  
---|---  
statName | Profiler marker or counter name pointer.  
statNameLen | Profiler marker or counter name length.  
capacity | Maximum amount of samples to be collected.  
options | Profiler recorder options.  
marker | Profiler marker instance.  
statHandle | Profiler recorder handle.  
  
### Description

Constructs ProfilerRecorder instance with a Profiler metric name pointer or
other unsafe handles.

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

