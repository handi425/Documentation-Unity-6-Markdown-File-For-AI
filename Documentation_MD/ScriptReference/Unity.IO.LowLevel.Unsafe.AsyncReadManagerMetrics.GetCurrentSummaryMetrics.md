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
[AsyncReadManagerMetrics](Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetrics.html).GetCurrentSummaryMetrics

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
[Unity.IO.LowLevel.Unsafe.AsyncReadManagerSummaryMetrics](Unity.IO.LowLevel.Unsafe.AsyncReadManagerSummaryMetrics.html)
GetCurrentSummaryMetrics([Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetrics.Flags](Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetrics.Flags.html)
flags);

### Parameters

flags | Flags to control the behavior, including clearing the underlying completed metrics after reading.  
---|---  
  
### Returns

**AsyncReadManagerSummaryMetrics** A summary of the current metrics data.

### Description

Gets a summary of the metrics collected for
[AsyncReadManager](Unity.IO.LowLevel.Unsafe.AsyncReadManager.html) read
operations since you started data collection or last cleared the metrics data.

The returned
[AsyncReadManagerSummaryMetrics](Unity.IO.LowLevel.Unsafe.AsyncReadManagerSummaryMetrics.html)
object provides overall statistics about the collected data. Call
[GetMetrics](Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetrics.GetMetrics.html)
to get the underlying metrics data used for the summary.  
  
Set the `flags` parameter to clear all data after returning the summary. This
has the same affect as calling
[ClearCompletedMetrics](Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetrics.ClearCompletedMetrics.html).

    
    
    using Unity.IO.LowLevel.Unsafe;
    using UnityEngine;
    public class AsyncReadManagerMetricsSample : [MonoBehaviour](MonoBehaviour.html)
    {
    #if ENABLE_PROFILER && UNITY_2020_2_OR_NEWER
        void Start()
        {
            [AsyncReadManagerMetrics.StartCollectingMetrics](Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetrics.StartCollectingMetrics.html)();
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            if ([Time.frameCount](Time-frameCount.html) == 10)
            {
                [AsyncReadManagerSummaryMetrics](Unity.IO.LowLevel.Unsafe.AsyncReadManagerSummaryMetrics.html) summaryOfMetrics = [AsyncReadManagerMetrics.GetCurrentSummaryMetrics](Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetrics.GetCurrentSummaryMetrics.html)([AsyncReadManagerMetrics.Flags.ClearOnRead](Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetrics.Flags.ClearOnRead.html));
                [Debug.LogFormat](Debug.LogFormat.html)($"Average bandwidth of every read over 10 frames: {summaryOfMetrics.AverageBandwidthMBPerSecond}MB/s");
                [Debug.LogFormat](Debug.LogFormat.html)($"Number of completed reads in 10 frames: {summaryOfMetrics.NumberOfCompletedRequests}");
                [Debug.LogFormat](Debug.LogFormat.html)($"Total number of requests in 10 frames: {summaryOfMetrics.TotalNumberOfRequests}");
                [Debug.LogFormat](Debug.LogFormat.html)($"Subsystem responsible for longest file read: {summaryOfMetrics.LongestReadSubsystem}");
                [Debug.LogFormat](Debug.LogFormat.html)($"[Asset](VersionControl.Asset.html) type responsible for longest wait: {summaryOfMetrics.LongestWaitAssetType}");
            }
        }  
      
    #endif
    }
    

* * *

## Declaration

public static
[Unity.IO.LowLevel.Unsafe.AsyncReadManagerSummaryMetrics](Unity.IO.LowLevel.Unsafe.AsyncReadManagerSummaryMetrics.html)
GetCurrentSummaryMetrics([Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetricsFilters](Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetricsFilters.html)
metricsFilters,
[Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetrics.Flags](Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetrics.Flags.html)
flags);

### Parameters

metricsFilters | The filters to apply to the metrics before calculating the summary.  
---|---  
flags | Flags to control the behavior, including clearing the underlying completed metrics after reading.  
  
### Returns

**AsyncReadManagerSummaryMetrics** A summary of the current metric data,
filtered by the specified `metricsFilters`.

### Description

Gets a filtered summary of the metrics collected for
[AsyncReadManager](Unity.IO.LowLevel.Unsafe.AsyncReadManager.html) read
operations since you started data collection or last cleared the metrics data.

This function filters the metrics collected for
[AsyncReadManager](Unity.IO.LowLevel.Unsafe.AsyncReadManager.html) read
operations and provides a summary based on the filtered data. See
AsyncReadManagerMetricsFilters.ctor for information about filter creation.

    
    
    using Unity.IO.LowLevel.Unsafe;
    using UnityEngine;  
      
    public class AsyncReadManagerMetricsSample : [MonoBehaviour](MonoBehaviour.html)
    {
    #if ENABLE_PROFILER && UNITY_2020_2_OR_NEWER
        [AsyncReadManagerMetricsFilters](Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetricsFilters.html) filters;
        void Start()
        {
            [AsyncReadManagerMetrics.StartCollectingMetrics](Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetrics.StartCollectingMetrics.html)();
            filters = new [AsyncReadManagerMetricsFilters](Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetricsFilters.html)();
            filters.SetPriorityFilter([Priority.PriorityHigh](Unity.IO.LowLevel.Unsafe.Priority.PriorityHigh.html));
            filters.SetSubsystemFilter([AssetLoadingSubsystem.Texture](Unity.IO.LowLevel.Unsafe.AssetLoadingSubsystem.Texture.html));
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            [AsyncReadManagerSummaryMetrics](Unity.IO.LowLevel.Unsafe.AsyncReadManagerSummaryMetrics.html) filteredSummaryOfMetrics = [AsyncReadManagerMetrics.GetCurrentSummaryMetrics](Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetrics.GetCurrentSummaryMetrics.html)(filters, [AsyncReadManagerMetrics.Flags.None](Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetrics.Flags.None.html));
            [Debug.LogFormat](Debug.LogFormat.html)($"Number of requests matching given filters: {filteredSummaryOfMetrics.TotalNumberOfRequests}");
            [Debug.LogFormat](Debug.LogFormat.html)($"Average bandwidth for textures in high priority queue: {filteredSummaryOfMetrics.AverageBandwidthMBPerSecond}MB/s");
            // Clear completed reads from metrics each frame to avoid rereading the same requests
            [AsyncReadManagerMetrics.ClearCompletedMetrics](Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetrics.ClearCompletedMetrics.html)();
        }  
      
    #endif
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

