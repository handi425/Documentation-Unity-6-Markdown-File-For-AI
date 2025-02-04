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

# VertexAttributeDescriptor

struct in UnityEngine.Rendering

/

Implemented in:[UnityEngine.CoreModule](UnityEngine.CoreModule.html)

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

Information about a single [VertexAttribute](Rendering.VertexAttribute.html)
of a Mesh vertex.

[Mesh](Mesh.html) vertex data comprised of different Vertex Attributes. For
example, a vertex can include a Position, Normal, TexCoord0, and Color. Meshes
usually use a known format for data layout, for example, a position is most
often a 3-component float vector ([Vector3](Vector3.html)), but you can also
specify non-standard data formats and their layout for a Mesh.  
  
You can use `VertexAttributeDescriptor` to specify custom mesh data layout in
[Mesh.SetVertexBufferParams](Mesh.SetVertexBufferParams.html).  
  
Vertex data is laid out in separate "streams" (each stream goes into a
separate vertex buffer in the underlying graphics API). Unity supports up to
four vertex streams, but you usually use only one stream. Separate streams are
most useful when some vertex attributes don't need to be processed, or you
need to give the vertex attributes a specific data layout.  
  
Within each stream, attributes of a vertex are laid out one after another, in
this order:
[VertexAttribute.Position](Rendering.VertexAttribute.Position.html),
[VertexAttribute.Normal](Rendering.VertexAttribute.Normal.html),
[VertexAttribute.Tangent](Rendering.VertexAttribute.Tangent.html),
[VertexAttribute.Color](Rendering.VertexAttribute.Color.html),
[VertexAttribute.TexCoord0](Rendering.VertexAttribute.TexCoord0.html), ...,
[VertexAttribute.TexCoord7](Rendering.VertexAttribute.TexCoord7.html),
[VertexAttribute.BlendWeight](Rendering.VertexAttribute.BlendWeight.html),
[VertexAttribute.BlendIndices](Rendering.VertexAttribute.BlendIndices.html).  
  
If you include `BlendWeight` or `BlendIndices` attributes in your vertex data,
use Unity's default stream layout so Unity doesn't reorder your vertex
attributes or incorrectly render your vertices in a
[SkinnedMeshRenderer](SkinnedMeshRenderer.html).

  1. In the first stream, add [VertexAttribute.Position](Rendering.VertexAttribute.Position.html), [VertexAttribute.Normal](Rendering.VertexAttribute.Normal.html) and [VertexAttribute.Tangent](Rendering.VertexAttribute.Tangent.html).
  2. In the second stream, add [VertexAttribute.Color](Rendering.VertexAttribute.Color.html), and [VertexAttribute.TexCoord0](Rendering.VertexAttribute.TexCoord0.html) to [VertexAttribute.TexCoord7](Rendering.VertexAttribute.TexCoord7.html).
  3. In the third stream, add [VertexAttribute.BlendWeight](Rendering.VertexAttribute.BlendWeight.html) and [VertexAttribute.BlendIndices](Rendering.VertexAttribute.BlendIndices.html).

All the attributes in the second stream are optional. If you don't include any
`Color` or `TexCoord` attributes, add `BlendWeight` and `BlendIndices` to the
second stream instead.  
  
Not all [format](Rendering.VertexAttributeDescriptor-format.html) and
[dimension](Rendering.VertexAttributeDescriptor-dimension.html) combinations
are valid. Specifically, the data size of a vertex attribute must be a
multiple of 4 bytes. For example, a
[VertexAttributeFormat.Float16](Rendering.VertexAttributeFormat.Float16.html)
format with dimension `3` is not valid. Additional resources:
[SystemInfo.SupportsVertexAttributeFormat](SystemInfo.SupportsVertexAttributeFormat.html).

    
    
    var mesh = new [Mesh](Mesh.html)();
    // specify vertex layout with:
    // - floating point positions,
    // - half-precision (FP16) normals with two components,
    // - low precision (UNorm8) tangents
    var layout = new[]
    {
        new [VertexAttributeDescriptor](Rendering.VertexAttributeDescriptor.html)([VertexAttribute.Position](Rendering.VertexAttribute.Position.html), [VertexAttributeFormat.Float32](Rendering.VertexAttributeFormat.Float32.html), 3),
        new [VertexAttributeDescriptor](Rendering.VertexAttributeDescriptor.html)([VertexAttribute.Normal](Rendering.VertexAttribute.Normal.html), [VertexAttributeFormat.Float16](Rendering.VertexAttributeFormat.Float16.html), 2),
        new [VertexAttributeDescriptor](Rendering.VertexAttributeDescriptor.html)([VertexAttribute.Tangent](Rendering.VertexAttribute.Tangent.html), [VertexAttributeFormat.UNorm8](Rendering.VertexAttributeFormat.UNorm8.html), 4),
    };
    var vertexCount = 10;
    mesh.SetVertexBufferParams(vertexCount, layout);

A C# struct (for use with
[Mesh.SetVertexBufferData](Mesh.SetVertexBufferData.html)) matching this
vertex layout could look like this:

    
    
    [System.Runtime.InteropServices.StructLayout(System.Runtime.InteropServices.LayoutKind.Sequential)]
    struct ExampleVertex
    {
        public [Vector3](Vector3.html) pos;
        public ushort normalX, normalY;
        public [Color32](Color32.html) tangent;
    }

Additional resources:
[Mesh.SetVertexBufferParams](Mesh.SetVertexBufferParams.html),
[Mesh.SetVertexBufferData](Mesh.SetVertexBufferData.html),
[Mesh.GetVertexAttributes](Mesh.GetVertexAttributes.html).

### Properties

[attribute](Rendering.VertexAttributeDescriptor-attribute.html)| The vertex
attribute.  
---|---  
[dimension](Rendering.VertexAttributeDescriptor-dimension.html)|
Dimensionality of the vertex attribute.  
[format](Rendering.VertexAttributeDescriptor-format.html)| Format of the
vertex attribute.  
[stream](Rendering.VertexAttributeDescriptor-stream.html)| Which vertex buffer
stream the attribute should be in.  
  
### Constructors

[VertexAttributeDescriptor](Rendering.VertexAttributeDescriptor-ctor.html)|
Create a VertexAttributeDescriptor structure.  
---|---  
  
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

