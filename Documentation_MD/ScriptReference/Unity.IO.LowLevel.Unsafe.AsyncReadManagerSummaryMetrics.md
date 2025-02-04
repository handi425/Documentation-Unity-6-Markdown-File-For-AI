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

# AsyncReadManagerSummaryMetrics

class in Unity.IO.LowLevel.Unsafe

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

A summary of the metrics collected for
[AsyncReadManager](Unity.IO.LowLevel.Unsafe.AsyncReadManager.html) read
operations.

Get a summary of the current metrics by calling
[AsyncReadManagerMetrics.GetCurrentSummaryMetrics](Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetrics.GetCurrentSummaryMetrics.html).
This function summarizes all metrics recorded since you started metrics
collection or last cleared your metrics data. Get a summary of an existing set
of
[AsyncReadManagerRequestMetric](Unity.IO.LowLevel.Unsafe.AsyncReadManagerRequestMetric.html)
records by calling
[AsyncReadManagerMetrics.GetSummaryOfMetrics](Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetrics.GetSummaryOfMetrics.html).
You can get these records by calling
[AsyncReadManagerMetrics.GetMetrics](Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetrics.GetMetrics.html).
In both cases, you can filter the data with
[AsyncReadManagerMetricsFilters](Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetricsFilters.html)
in order to focus the summary on the particular categories of data you want to
analyze. Additional resources:
[AsyncReadManagerMetrics](Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetrics.html).

    
    
    using Unity.IO.LowLevel.Unsafe;
    using UnityEngine;  
      
    public class GetMetricsSummary : [MonoBehaviour](MonoBehaviour.html)
    {
    #if ENABLE_PROFILER && UNITY_2020_2_OR_NEWER
        [AsyncReadManagerMetricsFilters](Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetricsFilters.html) m_Filter;
        [AsyncReadManagerSummaryMetrics](Unity.IO.LowLevel.Unsafe.AsyncReadManagerSummaryMetrics.html) m_Summary;
        public void Start()
        {
            // Create a filter for texture file reads that have been completed
            m_Filter = new [AsyncReadManagerMetricsFilters](Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetricsFilters.html)();
            m_Filter.SetStateFilter([ProcessingState.Completed](Unity.IO.LowLevel.Unsafe.ProcessingState.Completed.html));
        }  
      
        public void [Update](PlayerLoop.Update.html)()
        {
            m_Summary = [AsyncReadManagerMetrics.GetCurrentSummaryMetrics](Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetrics.GetCurrentSummaryMetrics.html)(m_Filter, [AsyncReadManagerMetrics.Flags.ClearOnRead](Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetrics.Flags.ClearOnRead.html));
            [Debug.Log](Debug.Log.html)($"Last frame bandwidth: {m_Summary.AverageBandwidthMBPerSecond} MB/s.");
        }  
      
    #endif
    }
    

### Properties

[AverageBandwidthMBPerSecond](Unity.IO.LowLevel.Unsafe.AsyncReadManagerSummaryMetrics.AverageBandwidthMBPerSecond.html)|
The mean rate of reading of data (bandwidth), in Mbps, for read request
metrics included in the summary calculation.  
---|---  
[AverageReadSizeInBytes](Unity.IO.LowLevel.Unsafe.AsyncReadManagerSummaryMetrics.AverageReadSizeInBytes.html)|
The mean size of data read, in bytes, for read request metrics included in the
summary calculation.  
[AverageReadTimeMicroseconds](Unity.IO.LowLevel.Unsafe.AsyncReadManagerSummaryMetrics.AverageReadTimeMicroseconds.html)|
The mean time taken for reading (excluding queue time), in microseconds, for
read request metrics included in the summary calculation.  
[AverageThroughputMBPerSecond](Unity.IO.LowLevel.Unsafe.AsyncReadManagerSummaryMetrics.AverageThroughputMBPerSecond.html)|
The mean rate of request throughput, in Mbps, for read request metrics
included in the summary calculation.  
[AverageTotalRequestTimeMicroseconds](Unity.IO.LowLevel.Unsafe.AsyncReadManagerSummaryMetrics.AverageTotalRequestTimeMicroseconds.html)|
The mean time taken from request to completion, in microseconds, for completed
read request metrics included in the summary calculation.  
[AverageWaitTimeMicroseconds](Unity.IO.LowLevel.Unsafe.AsyncReadManagerSummaryMetrics.AverageWaitTimeMicroseconds.html)|
The mean time taken from request to the start of reading, in microseconds, for
read request metrics included in the summary calculation.  
[LongestReadAssetType](Unity.IO.LowLevel.Unsafe.AsyncReadManagerSummaryMetrics.LongestReadAssetType.html)|
The asset type ID for the longest read included in the summary calculation.  
[LongestReadSubsystem](Unity.IO.LowLevel.Unsafe.AsyncReadManagerSummaryMetrics.LongestReadSubsystem.html)|
The Subsystem tag for the longest read included in the summary calculation.  
[LongestReadTimeMicroseconds](Unity.IO.LowLevel.Unsafe.AsyncReadManagerSummaryMetrics.LongestReadTimeMicroseconds.html)|
The longest read time (not including time in queue) included in the summary
calculation in microseconds.  
[LongestWaitAssetType](Unity.IO.LowLevel.Unsafe.AsyncReadManagerSummaryMetrics.LongestWaitAssetType.html)|
The asset type ID for the longest wait time included in the summary
calculation.  
[LongestWaitSubsystem](Unity.IO.LowLevel.Unsafe.AsyncReadManagerSummaryMetrics.LongestWaitSubsystem.html)|
The Subsystem tag for the longest wait time included in the summary
calculation.  
[LongestWaitTimeMicroseconds](Unity.IO.LowLevel.Unsafe.AsyncReadManagerSummaryMetrics.LongestWaitTimeMicroseconds.html)|
The longest time spent waiting of metrics included in the summary calculation,
in microseconds.  
[NumberOfAsyncReads](Unity.IO.LowLevel.Unsafe.AsyncReadManagerSummaryMetrics.NumberOfAsyncReads.html)|
The total number of Async reads in the metrics included in the summary
calculation.  
[NumberOfCachedReads](Unity.IO.LowLevel.Unsafe.AsyncReadManagerSummaryMetrics.NumberOfCachedReads.html)|
The total number of cached reads (so read time was zero) in the metrics
included in the summary calculation.  
[NumberOfCanceledRequests](Unity.IO.LowLevel.Unsafe.AsyncReadManagerSummaryMetrics.NumberOfCanceledRequests.html)|
The total number of canceled requests in the metrics included in the summary
calculation.  
[NumberOfCompletedRequests](Unity.IO.LowLevel.Unsafe.AsyncReadManagerSummaryMetrics.NumberOfCompletedRequests.html)|
The total number of completed requests in the metrics included in the summary
calculation.  
[NumberOfFailedRequests](Unity.IO.LowLevel.Unsafe.AsyncReadManagerSummaryMetrics.NumberOfFailedRequests.html)|
The total number of failed requests in the metrics included in the summary
calculation.  
[NumberOfInProgressRequests](Unity.IO.LowLevel.Unsafe.AsyncReadManagerSummaryMetrics.NumberOfInProgressRequests.html)|
The total number of in progress requests in the metrics included in the
summary calculation.  
[NumberOfSyncReads](Unity.IO.LowLevel.Unsafe.AsyncReadManagerSummaryMetrics.NumberOfSyncReads.html)|
The total number of Sync reads in the metrics included in the summary
calculation.  
[NumberOfWaitingRequests](Unity.IO.LowLevel.Unsafe.AsyncReadManagerSummaryMetrics.NumberOfWaitingRequests.html)|
The total number of waiting requests in the metrics included in the summary
calculation.  
[TotalBytesRead](Unity.IO.LowLevel.Unsafe.AsyncReadManagerSummaryMetrics.TotalBytesRead.html)|
The total number of bytes read in the metrics included in the summary
calculation.  
[TotalNumberOfRequests](Unity.IO.LowLevel.Unsafe.AsyncReadManagerSummaryMetrics.TotalNumberOfRequests.html)|
The total number of read requests included in the summary calculation.  
  
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

