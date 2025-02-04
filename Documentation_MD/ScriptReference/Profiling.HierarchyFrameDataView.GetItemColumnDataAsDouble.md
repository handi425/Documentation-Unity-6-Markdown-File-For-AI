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
[HierarchyFrameDataView](Profiling.HierarchyFrameDataView.html).GetItemColumnDataAsDouble

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

public double GetItemColumnDataAsDouble(int id, int column);

### Parameters

id | Hierarchy item identifier.  
---|---  
column | Column identifier.  
  
### Returns

**double** Value of the correspnding column as double.

### Description

Returns double representation of hierarchy item value associated with the
column.

Use to retrieve value with high precision for columns such as
[HierarchyFrameDataView.columnStartTime](Profiling.HierarchyFrameDataView-
columnStartTime.html) which represents sample start time in milliseconds.

    
    
    using System.Collections.Generic;
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.Profiling;
    using UnityEditorInternal;  
      
    class Example
    {
        static List<int> childrenIdCache = new List<int>();  
      
        static int FindChildItemByFunctionName([HierarchyFrameDataView](Profiling.HierarchyFrameDataView.html) frameData, int parentId, string functionName)
        {
            frameData.GetItemChildren(parentId, childrenIdCache);
            foreach (var childId in childrenIdCache)
            {
                var name = frameData.GetItemName(childId);
                if (name == functionName)
                    return childId;
            }  
      
            return [HierarchyFrameDataView.invalidSampleId](Profiling.HierarchyFrameDataView-invalidSampleId.html);
        }  
      
        static double GetSampleStartTime(string sampleName)
        {
            using (var frameData = ProfilerDriver.GetHierarchyFrameDataView(ProfilerDriver.lastFrameIndex, 0, [HierarchyFrameDataView.ViewModes.Default](Profiling.HierarchyFrameDataView.ViewModes.Default.html), [HierarchyFrameDataView.columnDontSort](Profiling.HierarchyFrameDataView-columnDontSort.html), false))
            {
                var sampleId = FindChildItemByFunctionName(frameData, frameData.GetRootItemID(), sampleName);
                if ([HierarchyFrameDataView.invalidSampleId](Profiling.HierarchyFrameDataView-invalidSampleId.html) == sampleId)
                    return 0;  
      
                double startTime = frameData.GetItemColumnDataAsDouble(sampleId, [HierarchyFrameDataView.columnStartTime](Profiling.HierarchyFrameDataView-columnStartTime.html));
                return startTime;
            }
        }
    }
    

Additional resources:
[HierarchyFrameDataView.GetItemColumnData](Profiling.HierarchyFrameDataView.GetItemColumnData.html),
[HierarchyFrameDataView.GetItemColumnDataAsFloat](Profiling.HierarchyFrameDataView.GetItemColumnDataAsFloat.html).

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

