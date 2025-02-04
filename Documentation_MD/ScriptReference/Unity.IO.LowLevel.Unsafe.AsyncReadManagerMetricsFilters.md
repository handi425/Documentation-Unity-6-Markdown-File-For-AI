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

# AsyncReadManagerMetricsFilters

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

Defines a filter for selecting specific categories of data when summarizing
[AsyncReadManager](Unity.IO.LowLevel.Unsafe.AsyncReadManager.html) metrics.

Pass a filter to
[AsyncReadManagerMetrics.GetCurrentSummaryMetrics](Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetrics.GetCurrentSummaryMetrics.html)
or
[AsyncReadManagerMetrics.GetSummaryOfMetrics](Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetrics.GetSummaryOfMetrics.html)
to limit the summary to the categories of data specified in the filter. For
each category supported by the `AsyncReadManagerMetricsFilters`, you can
specify either a single value or an array of values.

    
    
    using Unity.IO.LowLevel.Unsafe;
    using UnityEngine;  
      
    public class GetMetricsSummarySample : [MonoBehaviour](MonoBehaviour.html)
    {
    #if ENABLE_PROFILER && UNITY_2020_2_OR_NEWER
        [AsyncReadManagerMetricsFilters](Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetricsFilters.html) m_SummaryFilter;  
      
        public void Start()
        {
            [AsyncReadManagerMetrics.StartCollectingMetrics](Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetrics.StartCollectingMetrics.html)();
            // Create a filter for mesh and texture file reads that have been completed or failed
            [AssetLoadingSubsystem](Unity.IO.LowLevel.Unsafe.AssetLoadingSubsystem.html)[] assetLoadingSubsystems = new [AssetLoadingSubsystem](Unity.IO.LowLevel.Unsafe.AssetLoadingSubsystem.html)[] { [AssetLoadingSubsystem.Texture](Unity.IO.LowLevel.Unsafe.AssetLoadingSubsystem.Texture.html), [AssetLoadingSubsystem.Mesh](Unity.IO.LowLevel.Unsafe.AssetLoadingSubsystem.Mesh.html) };
            m_SummaryFilter = new [AsyncReadManagerMetricsFilters](Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetricsFilters.html)(assetLoadingSubsystems);
            m_SummaryFilter.SetStateFilter(new [ProcessingState](Unity.IO.LowLevel.Unsafe.ProcessingState.html)[] { [ProcessingState.Completed](Unity.IO.LowLevel.Unsafe.ProcessingState.Completed.html), [ProcessingState.Failed](Unity.IO.LowLevel.Unsafe.ProcessingState.Failed.html) });
        }  
      
        public void [Update](PlayerLoop.Update.html)()
        {
            if ([Time.frameCount](Time-frameCount.html) == 10)
            {
                [AsyncReadManagerSummaryMetrics](Unity.IO.LowLevel.Unsafe.AsyncReadManagerSummaryMetrics.html) summary = [AsyncReadManagerMetrics.GetCurrentSummaryMetrics](Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetrics.GetCurrentSummaryMetrics.html)(m_SummaryFilter, [AsyncReadManagerMetrics.Flags.ClearOnRead](Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetrics.Flags.ClearOnRead.html));
                [Debug.Log](Debug.Log.html)($"Average bandwidth for Completed or Failed reads of Textures or Meshes: {summary.AverageBandwidthMBPerSecond} MB/s.");
            }
        }  
      
    #endif
    }
    

### Constructors

[AsyncReadManagerMetricsFilters](Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetricsFilters-
ctor.html)| Constructor for an instance of the Summary Metrics Filters, used
to filter the metrics data that is included in the calculation of a summary.  
---|---  
  
### Public Methods

[ClearFilters](Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetricsFilters.ClearFilters.html)|
Clears all the filters on an existing AsyncReadManagerMetricsFilters instance.  
---|---  
[RemovePriorityFilter](Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetricsFilters.RemovePriorityFilter.html)|
Remove the Priority filters from an existing SummaryMetricsFilters instance.  
[RemoveReadTypeFilter](Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetricsFilters.RemoveReadTypeFilter.html)|
Remove the ReadType filters from an existing SummaryMetricsFilters instance.  
[RemoveStateFilter](Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetricsFilters.RemoveStateFilter.html)|
Remove the State filters from an existing SummaryMetricsFilters instance.  
[RemoveSubsystemFilter](Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetricsFilters.RemoveSubsystemFilter.html)|
Remove the Subsystem filters from an existing SummaryMetricsFilters instance.  
[RemoveTypeIDFilter](Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetricsFilters.RemoveTypeIDFilter.html)|
Remove the TypeID filters from an existing SummaryMetricsFilters instance.  
[SetPriorityFilter](Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetricsFilters.SetPriorityFilter.html)|
Set Priority filters on an existing SummaryMetricsFilters instance.  
[SetReadTypeFilter](Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetricsFilters.SetReadTypeFilter.html)|
Set FileReadType filters on an existing SummaryMetricsFilters instance.  
[SetStateFilter](Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetricsFilters.SetStateFilter.html)|
Set ProcessingState filters on an existing SummaryMetricsFilters instance.  
[SetSubsystemFilter](Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetricsFilters.SetSubsystemFilter.html)|
Set AssetLoadingSubsystem filters on an existing SummaryMetricsFilters
instance.  
[SetTypeIDFilter](Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetricsFilters.SetTypeIDFilter.html)|
Set TypeID filters on an existing SummaryMetricsFilters instance.  
  
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

