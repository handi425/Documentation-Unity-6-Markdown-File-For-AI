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

#  [Mesh](Mesh.html).SetVertexBufferData

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

public void SetVertexBufferData(NativeArray<T> data, int dataStart, int
meshBufferStart, int count, int stream,
[Rendering.MeshUpdateFlags](Rendering.MeshUpdateFlags.html) flags);

## Declaration

public void SetVertexBufferData(T[] data, int dataStart, int meshBufferStart,
int count, int stream,
[Rendering.MeshUpdateFlags](Rendering.MeshUpdateFlags.html) flags);

## Declaration

public void SetVertexBufferData(List<T> data, int dataStart, int
meshBufferStart, int count, int stream,
[Rendering.MeshUpdateFlags](Rendering.MeshUpdateFlags.html) flags);

### Parameters

data | Vertex data array.  
---|---  
dataStart | The first element in the data to copy from.  
meshBufferStart | The first element in mesh vertex buffer to receive the data.  
count | Number of vertices to copy.  
stream | Vertex buffer stream to set data for (default 0). Value must be within range 0 to 3.  
flags | Flags controlling the function behavior, see [MeshUpdateFlags](Rendering.MeshUpdateFlags.html).  
  
### Description

Sets the data of the vertex buffer of the Mesh.

Simple usage of [Mesh](Mesh.html) scripting API involves using functions like
[vertices](Mesh-vertices.html), [normals](Mesh-normals.html) to setup vertex
data.  
  
For advanced use cases that require maximum performance, you can use the
advanced API, which has functions like [SetSubMesh](Mesh.SetSubMesh.html),
[SetIndexBufferParams](Mesh.SetIndexBufferParams.html),
[SetIndexBufferData](Mesh.SetIndexBufferData.html), and
[SetVertexBufferParams](Mesh.SetVertexBufferParams.html). This advanced API
gives access to the underlying mesh data structures that primarily work on raw
index buffers, vertex buffers and mesh subset data.  
  
You can use `SetVertexBufferData` to set vertex data directly, without using
format conversions for each vertex attribute. The supplied data layout has to
match the vertex data layout of the mesh (see
[SetVertexBufferParams](Mesh.SetVertexBufferParams.html),
[GetVertexAttributes](Mesh.GetVertexAttributes.html)). Partial updates of the
data are also possible, via `dataStart`, `meshBufferStart`, `count`
parameters.

    
    
    using UnityEngine;
    using UnityEngine.Rendering;
    using Unity.Collections;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        // [Vertex](UIElements.Vertex.html) with FP32 position, FP16 2D normal and a 4-byte tangent.
        // In some cases StructLayout attribute needs
        // to be used, to get the data layout match exactly what it needs to be.
        [System.Runtime.InteropServices.StructLayout(System.Runtime.InteropServices.LayoutKind.Sequential)]
        struct ExampleVertex
        {
            public [Vector3](Vector3.html) pos;
            public ushort normalX, normalY;
            public [Color32](Color32.html) tangent;
        }  
      
        void Start()
        {
            var mesh = new [Mesh](Mesh.html)();
            // specify vertex count and layout
            var layout = new[]
            {
                new [VertexAttributeDescriptor](Rendering.VertexAttributeDescriptor.html)([VertexAttribute.Position](Rendering.VertexAttribute.Position.html), [VertexAttributeFormat.Float32](Rendering.VertexAttributeFormat.Float32.html), 3),
                new [VertexAttributeDescriptor](Rendering.VertexAttributeDescriptor.html)([VertexAttribute.Normal](Rendering.VertexAttribute.Normal.html), [VertexAttributeFormat.Float16](Rendering.VertexAttributeFormat.Float16.html), 2),
                new [VertexAttributeDescriptor](Rendering.VertexAttributeDescriptor.html)([VertexAttribute.Tangent](Rendering.VertexAttribute.Tangent.html), [VertexAttributeFormat.UNorm8](Rendering.VertexAttributeFormat.UNorm8.html), 4),
            };
            var vertexCount = 10;
            mesh.SetVertexBufferParams(vertexCount, layout);  
      
            // set vertex data
            var verts = new NativeArray<ExampleVertex>(vertexCount, [Allocator.Temp](Unity.Collections.Allocator.Temp.html));  
      
            // ... fill in vertex array data here...  
      
            mesh.SetVertexBufferData(verts, 0, 0, vertexCount);
        }
    }
    

Additional resources:
[SetVertexBufferParams](Mesh.SetVertexBufferParams.html),
[SetIndexBufferParams](Mesh.SetIndexBufferParams.html),
[SetIndexBufferData](Mesh.SetIndexBufferData.html),
[SetSubMesh](Mesh.SetSubMesh.html),
[MeshUpdateFlags](Rendering.MeshUpdateFlags.html),
[AcquireReadOnlyMeshData](Mesh.AcquireReadOnlyMeshData.html).

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

