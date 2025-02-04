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

#  [GraphicsBuffer.Target](GraphicsBuffer.Target.html).Index

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

GraphicsBuffer can be used as an index buffer.

Allows a buffer to be used as an index buffer for
[Graphics.DrawProcedural](Graphics.DrawProcedural.html) and similar low level
drawing APIs.  
  
When you construct a GraphicsBuffer of this type, the value of `stride` must
be either 2 (16-bit indices) or 4 (32-bit indices).  
  
DirectX 11 does not allow `Index` buffers to also be
[Structured](GraphicsBuffer.Target.Structured.html). For compute shader mesh
data access with DirectX 11 compatibility, it is best to use
[Raw](GraphicsBuffer.Target.Raw.html).  
  
Additional resources:
[Graphics.RenderPrimitivesIndexed](Graphics.RenderPrimitivesIndexed.html),
[Graphics.RenderPrimitivesIndexedIndirect](Graphics.RenderPrimitivesIndexedIndirect.html),
[CommandBuffer.DrawProcedural](Rendering.CommandBuffer.DrawProcedural.html),
[CommandBuffer.DrawProceduralIndirect](Rendering.CommandBuffer.DrawProceduralIndirect.html),
[Mesh.indexBufferTarget](Mesh-indexBufferTarget.html),
[Mesh.GetIndexBuffer](Mesh.GetIndexBuffer.html).

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

