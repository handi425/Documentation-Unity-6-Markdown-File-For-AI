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

#  [FrameDataView](Profiling.FrameDataView.html).GetMarkerId

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

public int GetMarkerId(string markerName);

### Parameters

markerName | Marker name.  
---|---  
  
### Returns

**int** Returns marker identifier as integer. Returns _invalidMarkerId_ if
there is no such marker in the capture.

### Description

Get Profiler marker identifier for a specific name.

Use marker identifier to avoid string allocations when traversing Profiler
data.  
  
The Profiler uses a unique identifier for each marker it creates during a
profiling session. The markers can generate many samples which
[HierarchyFrameDataView](Profiling.HierarchyFrameDataView.html) and
[RawFrameDataView](Profiling.RawFrameDataView.html) can access.  
All samples that the same marker generates have the same integer marker
identifier and the same name.  
  
Marker identifiers are persistent for the entire profiling session.

    
    
    using [System](Rendering.VirtualTexturing.System.html);
    using Unity.Collections;
    using UnityEditor.Profiling;
    using UnityEditorInternal;
    using UnityEngine;
    using UnityEngine.Profiling;  
      
    public class Example
    {
        public static long GetGCAllocs(int frameIndex)
        {
            long totalGcAllocSize = 0;  
      
            int gcAllocMarkerId = [FrameDataView.invalidMarkerId](Profiling.FrameDataView-invalidMarkerId.html);  
      
            for (int threadIndex = 0;; ++threadIndex)
            {
                using ([RawFrameDataView](Profiling.RawFrameDataView.html) frameData = ProfilerDriver.GetRawFrameDataView(frameIndex, threadIndex))
                {
                    if (!frameData.valid)
                        break;  
      
                    if (gcAllocMarkerId == [FrameDataView.invalidMarkerId](Profiling.FrameDataView-invalidMarkerId.html))
                    {
                        gcAllocMarkerId = frameData.GetMarkerId("GC.Alloc");
                        if (gcAllocMarkerId == [FrameDataView.invalidMarkerId](Profiling.FrameDataView-invalidMarkerId.html))
                            break;
                    }  
      
                    int sampleCount = frameData.sampleCount;
                    for (int i = 0; i < sampleCount; ++i)
                    {
                        if (gcAllocMarkerId != frameData.GetSampleMarkerId(i))
                            continue;  
      
                        long gcAllocSize = frameData.GetSampleMetadataAsLong(i, 0);
                        totalGcAllocSize += gcAllocSize;
                    }
                }
            }  
      
            return totalGcAllocSize;
        }
    }
    

Additional resources:
[GetMarkerName](Profiling.FrameDataView.GetMarkerName.html),
[HierarchyFrameDataView.GetItemMarkerID](Profiling.HierarchyFrameDataView.GetItemMarkerID.html),
[RawFrameDataView.GetSampleMarkerId](Profiling.RawFrameDataView.GetSampleMarkerId.html).

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

