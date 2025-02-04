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

#
[RayTracingGeometryInstanceConfig](Rendering.RayTracingGeometryInstanceConfig.html).vertexAttributes

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

public VertexAttributeDescriptor[] vertexAttributes;

### Description

An array of vertex attributes that define the vertex format of
[vertexBuffer](Rendering.RayTracingGeometryInstanceConfig-vertexBuffer.html).

The Position attribute is mandatory for building an acceleration structure.
You can access other vertex attributes in shader code using helper functions
from **UnityRayTracingMeshUtils.cginc** header.

    
    
    // Defining a vertex format that contains the position, the normal and texture coordinates attributes.
    [VertexAttributeDescriptor](Rendering.VertexAttributeDescriptor.html)[] vertexDescs = new [VertexAttributeDescriptor](Rendering.VertexAttributeDescriptor.html)[3];
    vertexDescs[0] = new [VertexAttributeDescriptor](Rendering.VertexAttributeDescriptor.html)([VertexAttribute.Position](Rendering.VertexAttribute.Position.html), [VertexAttributeFormat.Float32](Rendering.VertexAttributeFormat.Float32.html), 3, 0);
    vertexDescs[1] = new [VertexAttributeDescriptor](Rendering.VertexAttributeDescriptor.html)([VertexAttribute.Normal](Rendering.VertexAttribute.Normal.html), [VertexAttributeFormat.Float32](Rendering.VertexAttributeFormat.Float32.html), 3, 0);
    vertexDescs[2] = new [VertexAttributeDescriptor](Rendering.VertexAttributeDescriptor.html)([VertexAttribute.TexCoord0](Rendering.VertexAttribute.TexCoord0.html), [VertexAttributeFormat.Float32](Rendering.VertexAttributeFormat.Float32.html), 2, 0);

Unity supports the following Position attribute data formats for building
acceleration structures:

  * [VertexAttributeFormat.Float32](Rendering.VertexAttributeFormat.Float32.html)
  * [VertexAttributeFormat.Float16](Rendering.VertexAttributeFormat.Float16.html)
  * [VertexAttributeFormat.SNorm16](Rendering.VertexAttributeFormat.SNorm16.html)

The Position attribute must be part of vertex buffer stream 0.  
  
Additional resources:
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

