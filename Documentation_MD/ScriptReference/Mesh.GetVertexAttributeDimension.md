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

#  [Mesh](Mesh.html).GetVertexAttributeDimension

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

public int
GetVertexAttributeDimension([Rendering.VertexAttribute](Rendering.VertexAttribute.html)
attr);

### Parameters

attr | Vertex data attribute to check for.  
---|---  
  
### Returns

**int** Dimensionality of the data attribute, or zero if it is not present.

### Description

Get dimension of a specific vertex data attribute on this Mesh.

Meshes usually use a known format for data layout, for example, a position is
always a 3-component Vector, and a tangent is always a 4-component Vector.
But, in some cases (usually regarding texture coordinates), the data layout
can be of different dimensionality. For example, [SetUVs](Mesh.SetUVs.html)
accepts either a 2D, 3D or 4D texture coordinates. You can use this function
to query this layout.  
  
Additional resources: [VertexAttribute](Rendering.VertexAttribute.html),
[HasVertexAttribute](Mesh.HasVertexAttribute.html),
[GetVertexAttributeFormat](Mesh.GetVertexAttributeFormat.html),
[GetVertexAttributes](Mesh.GetVertexAttributes.html).

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

