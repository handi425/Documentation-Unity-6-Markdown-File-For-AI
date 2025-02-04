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

#  [SystemInfo](SystemInfo.html).SupportsVertexAttributeFormat

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

public static bool
SupportsVertexAttributeFormat([Rendering.VertexAttributeFormat](Rendering.VertexAttributeFormat.html)
format, int dimension);

### Parameters

format | The [VertexAttributeFormat](Rendering.VertexAttributeFormat.html) format to look up.  
---|---  
dimension | The dimension of vertex data to check for.  
  
### Returns

**bool** True if the format with the given dimension is supported.

### Description

Indicates whether the given combination of a vertex attribute format and
dimension is supported on this device.

Not all [VertexAttributeFormat](Rendering.VertexAttributeFormat.html) and
dimension combinations are supported. The most common restriction is that
format and dimension data size must be a multiple of 4 bytes, so for example
[VertexAttributeFormat.UNorm8](Rendering.VertexAttributeFormat.UNorm8.html)
with dimensions below 4 are not supported. Some platforms or devices might
have more limitations, for example
[VertexAttributeFormat.Float16](Rendering.VertexAttributeFormat.Float16.html)
is not supported by some mobile phones.  
  
Additional resources:
[VertexAttributeFormat](Rendering.VertexAttributeFormat.html),
[VertexAttributeDescriptor](Rendering.VertexAttributeDescriptor.html).

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

