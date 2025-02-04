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

#  [MeshUpdateFlags](Rendering.MeshUpdateFlags.html).DontResetBoneBounds

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

Indicates that Unity should not reset skinned mesh bone bounds when you modify
Mesh data using [Mesh.SetVertexBufferData](Mesh.SetVertexBufferData.html) or
[Mesh.SetIndexBufferData](Mesh.SetIndexBufferData.html).

When you modify Skinned Mesh vertex position or index buffer data, Unity's
default behaviour is to reset the internal data structure that contains the
cached bounding boxes of each bone, and then recalculate these bounds from the
new vertex and index buffer data.  
  
You can make Unity skip this behaviour by using the
`MeshUpdateFlags.DontResetBoneBounds` flag. This can be beneficial to
performance when you know that many mesh modifications will happen before the
bone bounds need an update, or when you know that bone bounds do not need to
be recalculated.  
  
You can use this flag with the
[Mesh.SetVertexBufferData](Mesh.SetVertexBufferData.html) and
[Mesh.SetIndexBufferData](Mesh.SetIndexBufferData.html) methods.

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

