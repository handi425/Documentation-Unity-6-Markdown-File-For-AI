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

#  [FrameDataView](Profiling.FrameDataView.html).GetUnityObjectInfo

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

public bool GetUnityObjectInfo(int instanceId, out
[Profiling.FrameDataView.UnityObjectInfo](Profiling.FrameDataView.UnityObjectInfo.html)
info);

### Parameters

instanceId | UnityEngine.Object instance identifier.  
---|---  
info | UnityEngine.Object information output struct with name and other attributes.  
  
### Returns

**bool** Returns true if instanceId exists in the frame and object information
is available.

### Description

Gets the UnityEngine.Object information for a given Instance ID.

Obtains information about the UnityEngine.Object instance in the profiler
capture.  
  
The Profiler sample can be associated with an instance of an object instance
that represents an Asset, a GameObject, or anything that is derived from
UnityEngine.Object.  
This information is available as a part of sample metadata. To get this
metadata you can use
[RawFrameDataView.GetSampleMetadataAsInt](Profiling.RawFrameDataView.GetSampleMetadataAsInt.html)
or
[HierarchyFrameDataView.GetItemInstanceID](Profiling.HierarchyFrameDataView.GetItemInstanceID.html).

    
    
    using UnityEditorInternal;
    using UnityEditor.Profiling;  
      
    public class Example
    {
        public static string GetInstanceName(int frame, int instanceId)
        {
            using (var frameData = ProfilerDriver.GetRawFrameDataView(frame, 0))
            {
                if (!frameData.GetUnityObjectInfo(instanceId, out var info))
                    return "N/A";
                return (frameData.GetUnityObjectNativeTypeInfo(info.nativeTypeIndex, out var typeInfo)) ? typeInfo.name + ": " + info.name : info.name;
            }
        }
    }
    

Additional resources:
[RawFrameDataView.GetSampleMetadataAsInt](Profiling.RawFrameDataView.GetSampleMetadataAsInt.html),
[HierarchyFrameDataView.GetItemInstanceID](Profiling.HierarchyFrameDataView.GetItemInstanceID.html),
[Object.GetInstanceID](Object.GetInstanceID.html).

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

