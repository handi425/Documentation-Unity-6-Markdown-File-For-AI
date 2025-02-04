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

# AsyncReadManagerMetricsFilters Constructor

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

public AsyncReadManagerMetricsFilters();

## Declaration

public AsyncReadManagerMetricsFilters(ulong typeID);

## Declaration

public
AsyncReadManagerMetricsFilters([Unity.IO.LowLevel.Unsafe.ProcessingState](Unity.IO.LowLevel.Unsafe.ProcessingState.html)
state);

## Declaration

public
AsyncReadManagerMetricsFilters([Unity.IO.LowLevel.Unsafe.FileReadType](Unity.IO.LowLevel.Unsafe.FileReadType.html)
readType);

## Declaration

public
AsyncReadManagerMetricsFilters([Unity.IO.LowLevel.Unsafe.Priority](Unity.IO.LowLevel.Unsafe.Priority.html)
priorityLevel);

## Declaration

public
AsyncReadManagerMetricsFilters([Unity.IO.LowLevel.Unsafe.AssetLoadingSubsystem](Unity.IO.LowLevel.Unsafe.AssetLoadingSubsystem.html)
subsystem);

### Parameters

typeID | The YAML Class ID for the asset type to include in the summary calculations. See the [YAML Class ID Reference](../Manual/ClassIDReference.html) page.  
---|---  
state | The Processing State to include in the summary calculations.  
readType | The type of file read (async or sync) to include in the summary calculations.  
priorityLevel | The priority level to include in the summary calculations.  
subsystem | The Subsystem 'tag' to include in the summary calculations.  
  
### Description

Constructor for an instance of the Summary Metrics Filters, used to filter the
metrics data that is included in the calculation of a summary.

The constructor takes one value of a filter. To take multiple values for the
same filter, you can use the array constructor (below). For multiple filters,
use the Set method for additional required filter types.

    
    
    using Unity.IO.LowLevel.Unsafe;
    using UnityEngine;  
      
    public class GetMetricsSummary : [MonoBehaviour](MonoBehaviour.html)
    {
    #if ENABLE_PROFILER && UNITY_2020_2_OR_NEWER
        public void Start()
        {
            // Create a filter for texture file reads that have been completed
            [AsyncReadManagerMetricsFilters](Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetricsFilters.html) m_TextureFilter = new [AsyncReadManagerMetricsFilters](Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetricsFilters.html)([AssetLoadingSubsystem.Texture](Unity.IO.LowLevel.Unsafe.AssetLoadingSubsystem.Texture.html));
            m_TextureFilter.SetStateFilter([ProcessingState.Completed](Unity.IO.LowLevel.Unsafe.ProcessingState.Completed.html));
        }  
      
    #endif
    }
    

* * *

## Declaration

public AsyncReadManagerMetricsFilters(ulong[] typeIDs, ProcessingState[]
states, FileReadType[] readTypes, Priority[] priorityLevels,
AssetLoadingSubsystem[] subsystems);

## Declaration

public AsyncReadManagerMetricsFilters(ulong[] typeIDs);

## Declaration

public AsyncReadManagerMetricsFilters(ProcessingState[] states);

## Declaration

public AsyncReadManagerMetricsFilters(FileReadType[] readTypes);

## Declaration

public AsyncReadManagerMetricsFilters(Priority[] priorityLevels);

## Declaration

public AsyncReadManagerMetricsFilters(AssetLoadingSubsystem[] subsystems);

### Parameters

typeIDs | An array of all the [TypeIDs](../Manual/ClassIDReference.html) to include in the summary calculations.  
---|---  
states | An array of all the ProcessingStates to include in the summary calculations.  
readTypes | An array of all the FileReadTypes to include in the summary calculations. As there are only two options, this is generally unnecesary.  
priorityLevels | An array of all the Priority levels to include in the summary calculations. As there are only two options, this is generally unnecesary.  
subsystems | An array of all the Subsystem 'tags' to include in the summary calculations.  
  
### Description

Constructor for an instance of the Summary Metrics Filters, used to filter the
metrics data that is included in the calculation of a summary.

The constructor takes an array of values for a single filter, or for all of
the filters. For multiple filters, but not all, use the Set method for
additional required filter types.

    
    
    using Unity.IO.LowLevel.Unsafe;
    using UnityEngine;  
      
    public class GetMetricsSummary : [MonoBehaviour](MonoBehaviour.html)
    {
    #if ENABLE_PROFILER && UNITY_2020_2_OR_NEWER
        public void Start()
        {
            // Create a filter for mesh and texture file reads that have been completed or failed
            [AssetLoadingSubsystem](Unity.IO.LowLevel.Unsafe.AssetLoadingSubsystem.html)[] assetLoadingSubsystems = new [AssetLoadingSubsystem](Unity.IO.LowLevel.Unsafe.AssetLoadingSubsystem.html)[] {[AssetLoadingSubsystem.Texture](Unity.IO.LowLevel.Unsafe.AssetLoadingSubsystem.Texture.html), [AssetLoadingSubsystem.Mesh](Unity.IO.LowLevel.Unsafe.AssetLoadingSubsystem.Mesh.html)};
            [AsyncReadManagerMetricsFilters](Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetricsFilters.html) m_SummaryFilter = new [AsyncReadManagerMetricsFilters](Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetricsFilters.html)(assetLoadingSubsystems);
            m_SummaryFilter.SetStateFilter(new [ProcessingState](Unity.IO.LowLevel.Unsafe.ProcessingState.html)[] { [ProcessingState.Completed](Unity.IO.LowLevel.Unsafe.ProcessingState.Completed.html), [ProcessingState.Failed](Unity.IO.LowLevel.Unsafe.ProcessingState.Failed.html) });
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

