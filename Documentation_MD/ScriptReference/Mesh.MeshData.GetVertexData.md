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

#  [Mesh.MeshData](Mesh.MeshData.html).GetVertexData

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

public NativeArray<T> GetVertexData(int stream = 0);

### Parameters

stream | The vertex buffer stream to get data for. The default value is 0.  
---|---  
  
### Returns

**NativeArray <T>** Returns a `NativeArray` containing the vertex buffer data.

### Description

Gets raw data for a given vertex buffer stream format in the `MeshData`.

`GetVertexData` returns a direct "pointer" into the raw vertex buffer data
without any memory allocations, data copies or conversions. You do not need to
dispose of the returned `NativeArray`, because it does not represent a new
memory allocation.  
  
You need to know the exact Mesh data layout to do this: for instance, the
presence and formats of all the mesh vertex attributes. The data layout
matches the one from
[Mesh.SetVertexBufferData](Mesh.SetVertexBufferData.html).  
  
If the `MeshData` is writeable, and you have set the vertex buffer size and
layout using
[Mesh.MeshData.SetVertexBufferParams](Mesh.MeshData.SetVertexBufferParams.html),
you can write vertex data directly to the array. If the `MeshData` is read-
only, the array is read-only.  
  
Additional resources:
[Mesh.AllocateWritableMeshData](Mesh.AllocateWritableMeshData.html),
[Mesh.AcquireReadOnlyMeshData](Mesh.AcquireReadOnlyMeshData.html),
[Mesh.MeshData.SetVertexBufferParams](Mesh.MeshData.SetVertexBufferParams.html).

    
    
    using UnityEngine;
    public class ExampleScript : [MonoBehaviour](MonoBehaviour.html)
    {
        struct [Vertex](UIElements.Vertex.html)
        {
            public [Vector3](Vector3.html) pos;
            public [Vector2](Vector2.html) uv;
        }
        void Start()
        {
            var mesh = new [Mesh](Mesh.html)();
            mesh.vertices = new[] {[Vector3.one](Vector3-one.html), [Vector3.up](Vector3-up.html)};
            mesh.uv = new[] {[Vector2.right](Vector2-right.html), [Vector2.up](Vector2-up.html)};
            using (var data = [Mesh.AcquireReadOnlyMeshData](Mesh.AcquireReadOnlyMeshData.html)(mesh))
            {
                var verts = data[0].GetVertexData<[Vertex](UIElements.Vertex.html)>();
                // prints "pos (1.0, 1.0, 1.0) uv (1.0, 0.0)" and "pos (0.0, 1.0, 0.0) uv (0.0, 1.0)"
                foreach (var v in verts)
                    [Debug.Log](Debug.Log.html)($"pos {v.pos} uv {v.uv}");
            }
        }
    }
    

Additional resources:
[Mesh.SetVertexBufferParams](Mesh.SetVertexBufferParams.html),
[Mesh.SetVertexBufferData](Mesh.SetVertexBufferData.html),
[GetIndexData](Mesh.MeshData.GetIndexData.html),
[Mesh.AcquireReadOnlyMeshData](Mesh.AcquireReadOnlyMeshData.html).

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

