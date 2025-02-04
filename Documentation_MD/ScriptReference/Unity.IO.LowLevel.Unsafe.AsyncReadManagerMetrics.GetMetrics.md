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
[AsyncReadManagerMetrics](Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetrics.html).GetMetrics

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

public static AsyncReadManagerRequestMetric[]
GetMetrics([Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetrics.Flags](Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetrics.Flags.html)
flags);

## Declaration

public static AsyncReadManagerRequestMetric[]
GetMetrics([Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetricsFilters](Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetricsFilters.html)
filters,
[Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetrics.Flags](Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetrics.Flags.html)
flags);

### Parameters

flags | Flags to control the behaviour, including clearing the underlying completed metrics after reading.  
---|---  
filters | (Optional) The [filters](Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetricsFilters.html) to control the data returned.  
  
### Returns

**AsyncReadManagerRequestMetric[]** Array of [read request
metrics](Unity.IO.LowLevel.Unsafe.AsyncReadManagerRequestMetric.html)
currently stored in the AsyncReadManager, which can be filtered by passing
[AsyncReadManagerMetricsFilters](Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetricsFilters.html).

### Description

Returns the current
[AsyncReadManager](Unity.IO.LowLevel.Unsafe.AsyncReadManager.html) metrics.

This function can filter the metrics collected by passing
[AsyncReadManagerMetricsFilters](Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetricsFilters.html).
See AsyncReadManagerMetricsFilters.ctor for information about filter creation.

    
    
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
            [AsyncReadManagerRequestMetric](Unity.IO.LowLevel.Unsafe.AsyncReadManagerRequestMetric.html)[] thisFrameMetrics = [AsyncReadManagerMetrics.GetMetrics](Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetrics.GetMetrics.html)([AsyncReadManagerMetrics.Flags.ClearOnRead](Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetrics.Flags.ClearOnRead.html));
            foreach ([AsyncReadManagerRequestMetric](Unity.IO.LowLevel.Unsafe.AsyncReadManagerRequestMetric.html) metric in thisFrameMetrics)
            {
                if (metric.State == [ProcessingState.Completed](Unity.IO.LowLevel.Unsafe.ProcessingState.Completed.html))
                {
                    double bandwidthMBPerSecond = metric.SizeBytes / (metric.TotalTimeMicroseconds - metric.TimeInQueueMicroseconds);
                    [Debug.LogFormat](Debug.LogFormat.html)($"[Asset](VersionControl.Asset.html) name:\"{metric.AssetName}\", bandwidth = {bandwidthMBPerSecond}MB/s");
                }
            }
        }  
      
    #endif
    }
    

* * *

## Declaration

public static void GetMetrics(List<AsyncReadManagerRequestMetric> outMetrics,
[Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetrics.Flags](Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetrics.Flags.html)
flags);

## Declaration

public static void GetMetrics(List<AsyncReadManagerRequestMetric> outMetrics,
[Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetricsFilters](Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetricsFilters.html)
filters,
[Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetrics.Flags](Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetrics.Flags.html)
flags);

### Parameters

outMetrics | The pre-allocated list to store the metrics in.  
---|---  
flags | Flags to control the behaviour, including clearing the underlying completed metrics after reading.  
filters | (Optional) The [filters](Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetricsFilters.html) to control the data returned.  
  
### Description

Writes the current
[AsyncReadManager](Unity.IO.LowLevel.Unsafe.AsyncReadManager.html) metrics
into the given List.

This function can filter the metrics collected by passing
[AsyncReadManagerMetricsFilters](Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetricsFilters.html).
See AsyncReadManagerMetricsFilters.ctor for information about filter creation.

    
    
    using Unity.IO.LowLevel.Unsafe;
    using System.Collections.Generic;
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
            List<[AsyncReadManagerRequestMetric](Unity.IO.LowLevel.Unsafe.AsyncReadManagerRequestMetric.html)> thisFrameMetrics = new List<[AsyncReadManagerRequestMetric](Unity.IO.LowLevel.Unsafe.AsyncReadManagerRequestMetric.html)>();
            [AsyncReadManagerMetrics.GetMetrics](Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetrics.GetMetrics.html)(thisFrameMetrics, [AsyncReadManagerMetrics.Flags.ClearOnRead](Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetrics.Flags.ClearOnRead.html));
            foreach ([AsyncReadManagerRequestMetric](Unity.IO.LowLevel.Unsafe.AsyncReadManagerRequestMetric.html) metric in thisFrameMetrics)
            {
                if (metric.State == [ProcessingState.Completed](Unity.IO.LowLevel.Unsafe.ProcessingState.Completed.html))
                {
                    double bandwidthMBPerSecond = metric.SizeBytes / (metric.TotalTimeMicroseconds - metric.TimeInQueueMicroseconds);
                    [Debug.LogFormat](Debug.LogFormat.html)($"[Asset](VersionControl.Asset.html) name:\"{metric.AssetName}\", bandwidth = {bandwidthMBPerSecond}MB/s");
                }
            }
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

