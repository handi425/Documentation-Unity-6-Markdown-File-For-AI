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

#  [Mesh](Mesh.html).MarkModified

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

public void MarkModified();

### Description

Notify [Renderer](Renderer.html) components of mesh geometry change.

By default, whenever Mesh data changes that could affect the geometry of the
mesh, all [Renderer](Renderer.html) components that use this mesh get
notified. For example, [MeshRenderer](MeshRenderer.html) components
recalculate their bounding boxes, and
[ShapeModule](ParticleSystem.ShapeModule.html) rebuild internal data used for
mesh surface emission.  
  
However a
[MeshUpdateFlags.DontNotifyMeshUsers](Rendering.MeshUpdateFlags.DontNotifyMeshUsers.html)
flag can be used in [Mesh.SetVertexBufferData](Mesh.SetVertexBufferData.html),
[Mesh.SetIndexBufferData](Mesh.SetIndexBufferData.html) or
[Mesh.SetSubMesh](Mesh.SetSubMesh.html) in order to skip this notification.
This can be beneficial when you know that many mesh modifications will happen
before the renderer components will need to actually update. A manual call to
`MarkModified` can be used later to notify the dependent renderer components
of a mesh geometry change.  
  
`MarkModified` function only needs to be called if you actually use the
`DontNotifyMeshUsers` flag. In all other cases the mesh change notifications
happen automatically.  
  
Additional resources:
[Mesh.SetVertexBufferData](Mesh.SetVertexBufferData.html),
[Mesh.SetIndexBufferData](Mesh.SetIndexBufferData.html),
[Mesh.SetSubMesh](Mesh.SetSubMesh.html).

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

