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

# Target

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

The intended targets for GraphicsBuffer.

Provide the intended targets ([target](GraphicsBuffer-target.html)) when
creating a GraphicsBuffer. For example, pass
[GraphicsBuffer.Target.Index](GraphicsBuffer.Target.Index.html) for a buffer
to be usable as a geometry index buffer.  
  
Different platforms and devices might or might not support different targets.
Any target values different from [Vertex](GraphicsBuffer.Target.Vertex.html),
[Index](GraphicsBuffer.Target.Index.html) or
[Constant](GraphicsBuffer.Target.Constant.html) require the compute shader
support (see [SystemInfo.supportsComputeShaders](SystemInfo-
supportsComputeShaders.html)).  
  
You can combine values in this enum. For example, `GraphicsBuffer.Target.Index | GraphicsBuffer.Target.Raw` creates a buffer that can be used both as an index buffer in a [Graphics.DrawProcedural](Graphics.DrawProcedural.html) call, and as a raw byte address buffer in a compute shader.  
  
DirectX 11 does not allow [Index](GraphicsBuffer.Target.Index.html) or
[Vertex](GraphicsBuffer.Target.Vertex.html) buffers to also be
[Structured](GraphicsBuffer.Target.Structured.html). For compute shader mesh
data access with DirectX 11 compatibility, use
[Raw](GraphicsBuffer.Target.Raw.html).  
  
Additional resources: [GraphicsBuffer](GraphicsBuffer.html) class,
[GraphicsBuffer constructor](GraphicsBuffer-ctor.html),
[Mesh.vertexBufferTarget](Mesh-vertexBufferTarget.html),
[Mesh.indexBufferTarget](Mesh-indexBufferTarget.html).

### Properties

[Vertex](GraphicsBuffer.Target.Vertex.html)| GraphicsBuffer can be used as a
vertex buffer.  
---|---  
[Index](GraphicsBuffer.Target.Index.html)| GraphicsBuffer can be used as an
index buffer.  
[CopySource](GraphicsBuffer.Target.CopySource.html)| GraphicsBuffer can be
used as a source for CopyBuffer.  
[CopyDestination](GraphicsBuffer.Target.CopyDestination.html)| GraphicsBuffer
can be used as a destination for CopyBuffer.  
[Structured](GraphicsBuffer.Target.Structured.html)| GraphicsBuffer can be
used as a structured buffer.  
[Raw](GraphicsBuffer.Target.Raw.html)| GraphicsBuffer can be used as a raw
byte-address buffer.  
[Append](GraphicsBuffer.Target.Append.html)| GraphicsBuffer can be used as an
append-consume buffer.  
[Counter](GraphicsBuffer.Target.Counter.html)| GraphicsBuffer with an internal
counter.  
[IndirectArguments](GraphicsBuffer.Target.IndirectArguments.html)|
GraphicsBuffer can be used as an indirect argument buffer for indirect draws
and dispatches.  
[Constant](GraphicsBuffer.Target.Constant.html)| GraphicsBuffer can be used as
a constant buffer (uniform buffer).  
  
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

