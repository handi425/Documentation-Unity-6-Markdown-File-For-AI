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

#  [ProfilerRecorder](Unity.Profiling.ProfilerRecorder.html).StartNew

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

public static
[Unity.Profiling.ProfilerRecorder](Unity.Profiling.ProfilerRecorder.html)
StartNew([Unity.Profiling.ProfilerCategory](Unity.Profiling.ProfilerCategory.html)
category, string statName, int capacity,
[Unity.Profiling.ProfilerRecorderOptions](Unity.Profiling.ProfilerRecorderOptions.html)
options);

### Parameters

category | Profiler category.  
---|---  
statName | Profiler marker or counter name.  
capacity | Maximum amount of samples to be collect. Must be greater than 0.  
options | ProfilerRecorder options.  
  
### Returns

**ProfilerRecorder** Returns new enabled recorder instance.

### Description

Initialize a new instance of ProfilerRecorder and start data collection.

For a list of built-in Profiler markers available, see the User Manual
documentation on [Common Profiler markers](../Manual/profiler-markers.html).  
  
**Note:** _capacity_ paramether must be greater than 0, otherwise StartNew
throws an exception.

    
    
    using Unity.Profiling;
    using UnityEngine;  
      
    public class ExampleScript : [MonoBehaviour](MonoBehaviour.html)
    {
        [ProfilerRecorder](Unity.Profiling.ProfilerRecorder.html) systemMemoryRecorder;
        [ProfilerRecorder](Unity.Profiling.ProfilerRecorder.html) gcMemoryRecorder;
        [ProfilerRecorder](Unity.Profiling.ProfilerRecorder.html) mainThreadTimeRecorder;  
      
        void OnEnable()
        {
            systemMemoryRecorder = [ProfilerRecorder.StartNew](Unity.Profiling.ProfilerRecorder.StartNew.html)([ProfilerCategory.Memory](Unity.Profiling.ProfilerCategory.Memory.html), "[System](Rendering.VirtualTexturing.System.html) Used Memory");
            gcMemoryRecorder = [ProfilerRecorder.StartNew](Unity.Profiling.ProfilerRecorder.StartNew.html)([ProfilerCategory.Memory](Unity.Profiling.ProfilerCategory.Memory.html), "GC Reserved Memory");
            mainThreadTimeRecorder = [ProfilerRecorder.StartNew](Unity.Profiling.ProfilerRecorder.StartNew.html)([ProfilerCategory.Internal](Unity.Profiling.ProfilerCategory.Internal.html), "Main Thread", 15);
        }  
      
        void OnDisable()
        {
            systemMemoryRecorder.Dispose();
            gcMemoryRecorder.Dispose();
            mainThreadTimeRecorder.Dispose();
        }
    }
    

Additional resources: [ctor](Unity.Profiling.ProfilerRecorder-ctor.html).

* * *

## Declaration

public static
[Unity.Profiling.ProfilerRecorder](Unity.Profiling.ProfilerRecorder.html)
StartNew([Unity.Profiling.ProfilerMarker](Unity.Profiling.ProfilerMarker.html)
marker, int capacity,
[Unity.Profiling.ProfilerRecorderOptions](Unity.Profiling.ProfilerRecorderOptions.html)
options);

### Parameters

capacity | Maximum amount of samples to be collected. Must be greater than 0.  
---|---  
options | Profiler recorder options.  
marker | Profiler marker instance.  
  
### Returns

**ProfilerRecorder** Returns new enabled recorder instance.

### Description

Initialize a new instance of ProfilerRecorder for ProfilerMarker and start
data collection.

Additional resources:: [ProfilerMarker](Unity.Profiling.ProfilerMarker.html).

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

