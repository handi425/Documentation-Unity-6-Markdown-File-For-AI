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

#  [Mesh](Mesh.html).AllocateWritableMeshData

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

public static [Mesh.MeshDataArray](Mesh.MeshDataArray.html)
AllocateWritableMeshData(int meshCount);

### Parameters

meshCount | The amount of meshes that will be created.  
---|---  
  
### Returns

**MeshDataArray** Returns a `MeshDataArray` containing writeable `MeshData`
structs. See [MeshDataArray](Mesh.MeshDataArray.html) and
[MeshData](Mesh.MeshData.html).

### Description

Allocates data structures for Mesh creation using C# Jobs.

Use [Mesh.AllocateWritableMeshData](Mesh.AllocateWritableMeshData.html) to
obtain a [MeshDataArray](Mesh.MeshDataArray.html) of writeable `MeshData`
structs. You can access the resulting `MeshDataArray` and `MeshData` structs
from any thread. Creating a `MeshDataArray` has some overhead for memory
tracking and safety reasons, so it is more efficient to make a single call to
[Mesh.AllocateWritableMeshData](Mesh.AllocateWritableMeshData.html) and
request multiple `MeshData` structs in the same `MeshDataArray` than it is to
make multiple calls to
[Mesh.AllocateWritableMeshData](Mesh.AllocateWritableMeshData.html). If you
use the override that takes a Mesh or Mesh Array as argument you will be
returned a copy of an existing Mesh that can be used on a thread.  
  
You can populate writeable `MeshData` structs with data to create new Meshes.
Use
[Mesh.MeshData.SetVertexBufferParams](Mesh.MeshData.SetVertexBufferParams.html)
to set the vertex buffer size and layout, and then write to the array returned
by [Mesh.MeshData.GetVertexData](Mesh.MeshData.GetVertexData.html) to set the
vertices. Use
[Mesh.MeshData.SetIndexBufferParams](Mesh.MeshData.SetIndexBufferParams.html)
to set the index buffer size and format, and then write to the array returned
by [Mesh.MeshData.GetIndexData](Mesh.MeshData.GetIndexData.html) to set the
indices. Write to [Mesh.MeshData.subMeshCount](Mesh.MeshData-
subMeshCount.html) to set the number of sub meshes, and then use
[Mesh.MeshData.SetSubMesh](Mesh.MeshData.SetSubMesh.html) to set sub mesh
data.  
  
When you have populated the writeable `MeshData` struct with your data, use
[Mesh.ApplyAndDisposeWritableMeshData](Mesh.ApplyAndDisposeWritableMeshData.html)
to apply the data to [Mesh](Mesh.html) objects and automatically dispose of
the `MeshDataArray`.

    
    
    using UnityEngine;
    using UnityEngine.Rendering;  
      
    [[RequireComponent](RequireComponent.html)(typeof([MeshFilter](MeshFilter.html)))]
    public class ExampleScript : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            // Allocate mesh data for one mesh.
            var dataArray = [Mesh.AllocateWritableMeshData](Mesh.AllocateWritableMeshData.html)(1);
            var data = dataArray[0];  
      
            // Tetrahedron vertices with positions and normals.
            // 4 faces with 3 unique vertices in each -- the faces
            // don't share the vertices since normals have to be
            // different for each face.
            data.SetVertexBufferParams(12,
                new [VertexAttributeDescriptor](Rendering.VertexAttributeDescriptor.html)([VertexAttribute.Position](Rendering.VertexAttribute.Position.html)),
                new [VertexAttributeDescriptor](Rendering.VertexAttributeDescriptor.html)([VertexAttribute.Normal](Rendering.VertexAttribute.Normal.html), stream:1));
            // Four tetrahedron vertex positions:
            var sqrt075 = [Mathf.Sqrt](Mathf.Sqrt.html)(0.75f);
            var p0 = new [Vector3](Vector3.html)(0,0,0);
            var p1 = new [Vector3](Vector3.html)(1,0,0);
            var p2 = new [Vector3](Vector3.html)(0.5f,0,sqrt075);
            var p3 = new [Vector3](Vector3.html)(0.5f,sqrt075,sqrt075/3);
            // The first vertex buffer data stream is just positions;
            // fill them in.
            var pos = data.GetVertexData<[Vector3](Vector3.html)>();
            pos[0] = p0; pos[1] = p1; pos[2] = p2;
            pos[3] = p0; pos[4] = p2; pos[5] = p3;
            pos[6] = p2; pos[7] = p1; pos[8] = p3;
            pos[9] = p0; pos[10] = p3; pos[11] = p1;
            // Note: normals will be calculated later in RecalculateNormals.  
      
            // Tetrahedron index buffer: 4 triangles, 3 indices per triangle.
            // All vertices are unique so the index buffer is just a
            // 0,1,2,...,11 sequence.
            data.SetIndexBufferParams(12, [IndexFormat.UInt16](Rendering.IndexFormat.UInt16.html));
            var ib = data.GetIndexData<ushort>();
            for (ushort i = 0; i < ib.Length; ++i)
                ib[i] = i;  
      
            // One sub-mesh with all the indices.
            data.subMeshCount = 1;
            data.SetSubMesh(0, new [SubMeshDescriptor](Rendering.SubMeshDescriptor.html)(0, ib.Length));  
      
            // Create the mesh and apply data to it:
            var mesh = new [Mesh](Mesh.html)();
            mesh.name = "Tetrahedron";
            [Mesh.ApplyAndDisposeWritableMeshData](Mesh.ApplyAndDisposeWritableMeshData.html)(dataArray, mesh);
            mesh.RecalculateNormals();
            mesh.RecalculateBounds();  
      
            GetComponent<[MeshFilter](MeshFilter.html)>().mesh = mesh;
        }
    }
    

Additional resources:
[ApplyAndDisposeWritableMeshData](Mesh.ApplyAndDisposeWritableMeshData.html),
[MeshDataArray](Mesh.MeshDataArray.html), [MeshData](Mesh.MeshData.html).

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

