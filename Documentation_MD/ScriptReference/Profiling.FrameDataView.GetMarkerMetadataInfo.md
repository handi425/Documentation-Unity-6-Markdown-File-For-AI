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

#  [FrameDataView](Profiling.FrameDataView.html).GetMarkerMetadataInfo

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

public MarkerMetadataInfo[] GetMarkerMetadataInfo(int markerId);

### Parameters

markerId | Marker identifier.  
---|---  
  
### Returns

**MarkerMetadataInfo[]** Returns an array of metadata information structures.

### Description

Gets Profiler marker metadata information for the specific marker identifier.

Use to get name, unit type and value type for the metadata parameters which
can be passed together with a Profiler sample associated with the identifier.

    
    
    using System.Text;
    using UnityEditor.Profiling;  
      
    public class Example
    {
        public static string GetFormattedMetadata([HierarchyFrameDataView](Profiling.HierarchyFrameDataView.html) frameDataView, int itemId, int mergedSampleIndex)
        {
            int sampleMetadataCount = frameDataView.GetItemMergedSamplesMetadataCount(itemId, mergedSampleIndex);
            if (sampleMetadataCount == 0)
                return null;  
      
            var metadataInfo = frameDataView.GetMarkerMetadataInfo(frameDataView.GetItemMarkerID(itemId));
            var sb = new StringBuilder();
            for (var i = 0; i < sampleMetadataCount; ++i)
            {
                if (metadataInfo != null && i < metadataInfo.Length)
                    sb.Append(metadataInfo[i].name);
                else
                    sb.Append(i);
                sb.Append(": ");
                sb.Append(frameDataView.GetItemMergedSamplesMetadata(itemId, mergedSampleIndex, i));
                sb.Append('\n');
            }  
      
            return sb.ToString();
        }
    }
    

**Throws:**  
_System.ArgumentException_ if _markerId_ is invalid.

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

