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
[AsyncReadManagerMetrics](Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetrics.html).GetSummaryOfMetrics

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
GetSummaryOfMetrics(AsyncReadManagerRequestMetric[] metrics);

## Declaration

public static
[Unity.IO.LowLevel.Unsafe.AsyncReadManagerSummaryMetrics](Unity.IO.LowLevel.Unsafe.AsyncReadManagerSummaryMetrics.html)
GetSummaryOfMetrics(List<AsyncReadManagerRequestMetric> metrics);

### Parameters

metrics | Array of previously collected AsyncReadManagerRequestMetrics.  
---|---  
  
### Returns

**AsyncReadManagerSummaryMetrics** Calculated summary of the given metrics.

### Description

Summarizes an array containing
[AsyncReadManagerRequestMetric](Unity.IO.LowLevel.Unsafe.AsyncReadManagerRequestMetric.html)
records.

You can access the metrics collected for
[AsyncReadManager](Unity.IO.LowLevel.Unsafe.AsyncReadManager.html) read
operations by calling
[GetMetrics](Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetrics.GetMetrics.html).

* * *

## Declaration

public static
[Unity.IO.LowLevel.Unsafe.AsyncReadManagerSummaryMetrics](Unity.IO.LowLevel.Unsafe.AsyncReadManagerSummaryMetrics.html)
GetSummaryOfMetrics(AsyncReadManagerRequestMetric[] metrics,
[Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetricsFilters](Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetricsFilters.html)
metricsFilters);

## Declaration

public static
[Unity.IO.LowLevel.Unsafe.AsyncReadManagerSummaryMetrics](Unity.IO.LowLevel.Unsafe.AsyncReadManagerSummaryMetrics.html)
GetSummaryOfMetrics(List<AsyncReadManagerRequestMetric> metrics,
[Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetricsFilters](Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetricsFilters.html)
metricsFilters);

### Parameters

metrics | List of previously collected AsyncReadManagerRequestMetrics.  
---|---  
metricsFilters |  [Filters](Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetricsFilters.html) to apply to the data used in calculating the summary.  
  
### Returns

**AsyncReadManagerSummaryMetrics** Calculated summary of given metrics that
match the filters.

### Description

Summarizes
[AsyncReadManagerRequestMetric](Unity.IO.LowLevel.Unsafe.AsyncReadManagerRequestMetric.html)
records that match the specified filter.

The summary returned is calculated from any data in the specified `metrics`
list that matches the `metricsFilters`. See
AsyncReadManagerMetricsFilters.ctor for information about filter creation. You
can access the metrics collected for
[AsyncReadManager](Unity.IO.LowLevel.Unsafe.AsyncReadManager.html) read
operations by calling
[GetMetrics](Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetrics.GetMetrics.html).

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

