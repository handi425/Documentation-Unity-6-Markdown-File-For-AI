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

#  [MeshUpdateFlags](Rendering.MeshUpdateFlags.html).DontNotifyMeshUsers

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

Indicates that Unity should not notify [Renderer](Renderer.html) components
about a possible [Mesh](Mesh.html) bounds change, when you modify Mesh data.

When you modify Mesh data that could affect the geometry of the mesh, Unity's
default behaviour is to notify all [Renderer](Renderer.html) components that
use this mesh, so that they can perform recalculations based on the new data
that are typically desirable. For example, [MeshRenderer](MeshRenderer.html)
components recalculate their bounding boxes, and the
[ShapeModule](ParticleSystem.ShapeModule.html) rebuilds internal data used for
mesh surface emission.  
  
If you supply the `MeshUpdateFlags.DontNotifyMeshUsers` flag when using the
"advanced" Mesh API, Unity will omit these notifications. This can be
beneficial to performance when you know that many mesh modifications will
happen before the renderer components actually need to update.  
  
You must therefore make sure that you call
[Mesh.MarkModified](Mesh.MarkModified.html) at a later point to notify the
dependent renderer components that they should perform their recalculations.  
  
You can use this flag with the following "advanced" mesh API:
[Mesh.SetVertexBufferData](Mesh.SetVertexBufferData.html),
[Mesh.SetIndexBufferData](Mesh.SetIndexBufferData.html) or
[Mesh.SetSubMesh](Mesh.SetSubMesh.html)  
  
For information about the difference between the simpler and more advanced
methods of assigning data to a Mesh from script, see the notes on the
[Mesh](Mesh.html) page.  
  

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

