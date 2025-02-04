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

# RawFrameDataView

class in UnityEditor.Profiling

/

Inherits from:[Profiling.FrameDataView](Profiling.FrameDataView.html)

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

Provides access to the Profiler data for a specific frame and thread.

Use _RawFrameDataView_ to retrieve unstructured Profiler samples data for the
particular frame.  
The order of samples is determined by the order they are generated in the
code.  
  
_RawFrameDataView_ can quickly iterate over all samples in the frame without
any internal allocations.

    
    
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
    

Additional resources: [FrameDataView](Profiling.FrameDataView.html),
[HierarchyFrameDataView](Profiling.HierarchyFrameDataView.html).

### Static Properties

[invalidSampleIndex](Profiling.RawFrameDataView-invalidSampleIndex.html)| This
constant defines a sample index that does not match any valid Profiler Sample.  
---|---  
  
### Public Methods

[GetFlowEvents](Profiling.RawFrameDataView.GetFlowEvents.html)| Gets all flow
events for the current frame and thread.  
---|---  
[GetSampleCallstack](Profiling.RawFrameDataView.GetSampleCallstack.html)| Gets
the callstack associated with the specified sample.  
[GetSampleCategoryIndex](Profiling.RawFrameDataView.GetSampleCategoryIndex.html)|
Gets Profiler marker category for the specific sample.  
[GetSampleChildrenCount](Profiling.RawFrameDataView.GetSampleChildrenCount.html)|
Gets amount of child samples for the specific sample.  
[GetSampleChildrenCountRecursive](Profiling.RawFrameDataView.GetSampleChildrenCountRecursive.html)|
Gets amount of direct and indirect child samples for the specific sample.  
[GetSampleFlags](Profiling.RawFrameDataView.GetSampleFlags.html)| Gets
Profiler marker flags for the specific sample.  
[GetSampleFlowEvents](Profiling.RawFrameDataView.GetSampleFlowEvents.html)|
Gets the flow events that originate from the specific sample.  
[GetSampleMarkerId](Profiling.RawFrameDataView.GetSampleMarkerId.html)| Gets
Profiler marker indentifier which uniquely identifies sample name.  
[GetSampleMetadataAsDouble](Profiling.RawFrameDataView.GetSampleMetadataAsDouble.html)|
Gets sample metadata value as double.  
[GetSampleMetadataAsFloat](Profiling.RawFrameDataView.GetSampleMetadataAsFloat.html)|
Gets sample metadata value as float.  
[GetSampleMetadataAsInt](Profiling.RawFrameDataView.GetSampleMetadataAsInt.html)|
Gets sample metadata value as integer.  
[GetSampleMetadataAsLong](Profiling.RawFrameDataView.GetSampleMetadataAsLong.html)|
Gets sample metadata value as long.  
[GetSampleMetadataAsSpan](Profiling.RawFrameDataView.GetSampleMetadataAsSpan.html)|
Returns Span<T> representation of sample metadata.  
[GetSampleMetadataAsString](Profiling.RawFrameDataView.GetSampleMetadataAsString.html)|
Gets sample metadata value as string.  
[GetSampleMetadataCount](Profiling.RawFrameDataView.GetSampleMetadataCount.html)|
Gets metadata count associated with the specific sample.  
[GetSampleName](Profiling.RawFrameDataView.GetSampleName.html)| Gets the name
of the specific sample.  
[GetSampleStartTimeMs](Profiling.RawFrameDataView.GetSampleStartTimeMs.html)|
Gets the start time of the sample. The amount of time is expressed in
milliseconds.  
[GetSampleStartTimeNs](Profiling.RawFrameDataView.GetSampleStartTimeNs.html)|
Gets the start time of the sample. The amount of time is expressed in
nanoseconds.  
[GetSampleTimeMs](Profiling.RawFrameDataView.GetSampleTimeMs.html)| Gets the
duration of sample. The amount of time is expressed in milliseconds.  
[GetSampleTimeNs](Profiling.RawFrameDataView.GetSampleTimeNs.html)| Gets the
duration of sample. The amount of time is expressed in nanoseconds.  
  
### Inherited Members

### Static Properties

[invalidMarkerId](Profiling.FrameDataView-invalidMarkerId.html)| Identifier of
the invalid marker.  
---|---  
[invalidThreadId](Profiling.FrameDataView-invalidThreadId.html)| This constant
defines a thread id that does not match any valid thread's id.  
[invalidThreadIndex](Profiling.FrameDataView-invalidThreadIndex.html)| This
constant defines a thread index that does not match any valid thread's index.  
  
### Properties

[frameFps](Profiling.FrameDataView-frameFps.html)| The current frames per
second (FPS) for the frame.  
---|---  
[frameGpuTimeMs](Profiling.FrameDataView-frameGpuTimeMs.html)| The amount of
GPU frame time in milliseconds.  
[frameGpuTimeNs](Profiling.FrameDataView-frameGpuTimeNs.html)| The amount of
GPU frame time in nanoseconds.  
[frameIndex](Profiling.FrameDataView-frameIndex.html)| The frame index for the
FrameDataView.  
[frameStartTimeMs](Profiling.FrameDataView-frameStartTimeMs.html)| The start
time of CPU frame in milliseconds.  
[frameStartTimeNs](Profiling.FrameDataView-frameStartTimeNs.html)| The start
time of CPU frame in nanoseconds.  
[frameTimeMs](Profiling.FrameDataView-frameTimeMs.html)| The amount of CPU
frame time in milliseconds.  
[frameTimeNs](Profiling.FrameDataView-frameTimeNs.html)| The amount of CPU
frame time in nanoseconds.  
[maxDepth](Profiling.FrameDataView-maxDepth.html)| Maximum child samples
levels in the thread data.  
[sampleCount](Profiling.FrameDataView-sampleCount.html)| The amount of samples
in the frame for the thread.  
[threadGroupName](Profiling.FrameDataView-threadGroupName.html)| The name of
the group that the thread belongs to.  
[threadId](Profiling.FrameDataView-threadId.html)| Persistent identifier
associated with the thread.  
[threadIndex](Profiling.FrameDataView-threadIndex.html)| The index of the
thread in the current frame.  
[threadName](Profiling.FrameDataView-threadName.html)| Name of the thread.  
[valid](Profiling.FrameDataView-valid.html)| True after the frame data for the
thread is processed and ready for retrieval.  
  
### Public Methods

[GetAllCategories](Profiling.FrameDataView.GetAllCategories.html)| Gets all
the available Profiler Categories for the current profiling session.  
---|---  
[GetCategoryInfo](Profiling.FrameDataView.GetCategoryInfo.html)| Gets the
Profiler category information for a given category ID.  
[GetCounterValueAsDouble](Profiling.FrameDataView.GetCounterValueAsDouble.html)|
Gets the last value of a counter marker in the frame as a double data type'.  
[GetCounterValueAsFloat](Profiling.FrameDataView.GetCounterValueAsFloat.html)|
Gets the last value of a counter marker in the frame as a float data type'.  
[GetCounterValueAsInt](Profiling.FrameDataView.GetCounterValueAsInt.html)|
Gets the last value of a counter marker in the frame as an int data type'.  
[GetCounterValueAsLong](Profiling.FrameDataView.GetCounterValueAsLong.html)|
Gets the last value of a counter marker in the frame as a long data type.  
[GetCounterValuePtr](Profiling.FrameDataView.GetCounterValuePtr.html)| Gets
unsafe pointer to the last value of a counter marker in the frame.  
[GetFrameMetaData](Profiling.FrameDataView.GetFrameMetaData.html)| Retrieves
metadata associated with the frame.  
[GetFrameMetaDataCount](Profiling.FrameDataView.GetFrameMetaDataCount.html)|
Gets the total number of metadata chunks for each id and tag pair in the
frame.  
[GetGfxResourceInfo](Profiling.FrameDataView.GetGfxResourceInfo.html)| Gets
information for a given graphics resource identifier.  
[GetMarkerCategoryIndex](Profiling.FrameDataView.GetMarkerCategoryIndex.html)|
Gets Profiler marker category for the specific marker identifier.  
[GetMarkerFlags](Profiling.FrameDataView.GetMarkerFlags.html)| Gets Profiler
marker flags for the specific marker identifier.  
[GetMarkerId](Profiling.FrameDataView.GetMarkerId.html)| Get Profiler marker
identifier for a specific name.  
[GetMarkerMetadataInfo](Profiling.FrameDataView.GetMarkerMetadataInfo.html)|
Gets Profiler marker metadata information for the specific marker identifier.  
[GetMarkerName](Profiling.FrameDataView.GetMarkerName.html)| Gets Profiler
marker name for the specific marker identifier.  
[GetMarkers](Profiling.FrameDataView.GetMarkers.html)| Gets all available
markers for the current profiling session.  
[GetSessionMetaData](Profiling.FrameDataView.GetSessionMetaData.html)|
Retrieves the metadata of the session this frame occurred in as a NativeArray.  
[GetSessionMetaDataCount](Profiling.FrameDataView.GetSessionMetaDataCount.html)|
Gets the total number of metadata chunks for each id and tag pair in the
Profiler session.  
[GetUnityObjectInfo](Profiling.FrameDataView.GetUnityObjectInfo.html)| Gets
the UnityEngine.Object information for a given Instance ID.  
[GetUnityObjectNativeTypeInfo](Profiling.FrameDataView.GetUnityObjectNativeTypeInfo.html)|
Gets native Unity type intormation.  
[GetUnityObjectNativeTypeInfoCount](Profiling.FrameDataView.GetUnityObjectNativeTypeInfoCount.html)|
Returns native types count in the capture.  
[HasCounterValue](Profiling.FrameDataView.HasCounterValue.html)| Returns true
for a marker that includes a counter in the active frame.  
[ResolveMethodInfo](Profiling.FrameDataView.ResolveMethodInfo.html)| Returns
method name and location information for the specified method address.  
  
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

