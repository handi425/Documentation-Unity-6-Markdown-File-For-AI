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

# MeshUpdateFlags

enumeration

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

Mesh data update flags.

Some advanced [Mesh](Mesh.html) functions like
[SetVertexBufferData](Mesh.SetVertexBufferData.html),
[SetIndexBufferData](Mesh.SetIndexBufferData.html),
[SetSubMesh](Mesh.SetSubMesh.html) take an optional `flags` parameter that
controls behavior of these functions. In particular, these flags allow you to
control what happens when a Mesh's data is updated.  
  
By default, Unity performs checks and validation on the data you supply when
using these methods - for example, to check whether the indices array has any
out-of-bounds values.  
  
These flags allow you to optionally omit some or all of these checks for the
purpose of increasing performance. If you choose to omit these checks, you
must ensure that the data you are supplying is valid.  
  
You can combine individual flags using the logical OR operator. For example: `MeshUpdateFlags.DontNotifyMeshUsers | MeshUpdateFlags.DontValidateIndices`.  
  
For information about the difference between the simpler and more advanced
methods of assigning data to a Mesh from script, see the notes on the
[Mesh](Mesh.html) page.

### Properties

[Default](Rendering.MeshUpdateFlags.Default.html)| Indicates that Unity should
perform the default checks and validation when you update a Mesh's data.  
---|---  
[DontValidateIndices](Rendering.MeshUpdateFlags.DontValidateIndices.html)|
Indicates that Unity should not check index values when you use
Mesh.SetIndexBufferData to modify a Mesh's data.  
[DontResetBoneBounds](Rendering.MeshUpdateFlags.DontResetBoneBounds.html)|
Indicates that Unity should not reset skinned mesh bone bounds when you modify
Mesh data using Mesh.SetVertexBufferData or Mesh.SetIndexBufferData.  
[DontNotifyMeshUsers](Rendering.MeshUpdateFlags.DontNotifyMeshUsers.html)|
Indicates that Unity should not notify Renderer components about a possible
Mesh bounds change, when you modify Mesh data.  
[DontRecalculateBounds](Rendering.MeshUpdateFlags.DontRecalculateBounds.html)|
Indicates that Unity should not recalculate the bounds when you set Mesh data
using Mesh.SetSubMesh.  
  
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

