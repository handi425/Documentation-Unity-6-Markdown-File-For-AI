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

#  [Mesh.MeshData](Mesh.MeshData.html).GetVertexAttributeFormat

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

[Switch to Manual](../Manual/class-Mesh.html "Go to Mesh Component in the
Manual")

## Declaration

public [Rendering.VertexAttributeFormat](Rendering.VertexAttributeFormat.html)
GetVertexAttributeFormat([Rendering.VertexAttribute](Rendering.VertexAttribute.html)
attr);

### Parameters

attr | The vertex attribute to check the format of.  
---|---  
  
### Returns

**VertexAttributeFormat** Returns the format of the given vertex attribute.

### Description

Gets the format of a given vertex attribute in the `MeshData`.

Most vertex attributes have a standard data format. For example, a position is
a [Vector3](Vector3.html). Some vertex attributes have more than one possible
data format. For example, [Mesh.colors32](Mesh-colors32.html) and
[Mesh.colors](Mesh-colors.html) are different formats for vertex colors. Use
this function to query the format of a given vertex attribute. Additional
resources:
[Mesh.GetVertexAttributeFormat](Mesh.GetVertexAttributeFormat.html),
[HasVertexAttribute](Mesh.MeshData.HasVertexAttribute.html),
[GetVertexAttributeDimension](Mesh.MeshData.GetVertexAttributeDimension.html).

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

