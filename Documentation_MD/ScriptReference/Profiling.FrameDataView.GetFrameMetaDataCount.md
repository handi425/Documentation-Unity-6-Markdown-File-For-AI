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

#  [FrameDataView](Profiling.FrameDataView.html).GetFrameMetaDataCount

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

public int GetFrameMetaDataCount(Guid id, int tag);

### Parameters

id | Project or package identifier.  
---|---  
tag | Data stream index.  
  
### Returns

**int** Returns count of metadata chunks.

### Description

Gets the total number of metadata chunks for each _id_ and _tag_ pair in the
frame.

Use the _GetSessionMetaDataCount_ method to retrieve the total number of
metadata arrays available in this session.  
  
When there are multiple
[Profiler.EmitFrameMetaData](Profiling.Profiler.EmitFrameMetaData.html) calls
in the same frame, it results in multiple metadata arrays that are associated
with the frame for a given _id_ , _tag_ pair. This information can be used to
write data to the stream in small portions, which reduces the amount of memory
needed to hold generated data.  
  
Use _id_ to identify the metadata from your project or package.  
Use _tag_ to distinguish between different data streams.  
  
Additional resources:
[GetFrameMetaData](Profiling.FrameDataView.GetFrameMetaData.html),
[Profiler.EmitFrameMetaData](Profiling.Profiler.EmitFrameMetaData.html).

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

