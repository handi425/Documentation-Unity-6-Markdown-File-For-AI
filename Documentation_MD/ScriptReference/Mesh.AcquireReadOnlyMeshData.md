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

#  [Mesh](Mesh.html).AcquireReadOnlyMeshData

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
AcquireReadOnlyMeshData([Mesh](Mesh.html) mesh);

## Declaration

public static [Mesh.MeshDataArray](Mesh.MeshDataArray.html)
AcquireReadOnlyMeshData(Mesh[] meshes);

## Declaration

public static [Mesh.MeshDataArray](Mesh.MeshDataArray.html)
AcquireReadOnlyMeshData(List<Mesh> meshes);

### Parameters

mesh | The input mesh.  
---|---  
meshes | The input meshes.  
  
### Returns

**MeshDataArray** Returns a `MeshDataArray` containing read-only `MeshData`
structs. See [MeshDataArray](Mesh.MeshDataArray.html) and
[MeshData](Mesh.MeshData.html).

### Description

Gets a snapshot of Mesh data for read-only access.

When you pass one or more Meshes to
[Mesh.AcquireReadOnlyMeshData](Mesh.AcquireReadOnlyMeshData.html), Unity
returns a [MeshDataArray](Mesh.MeshDataArray.html) of read-only `MeshData`
structs. You can access the resulting `MeshDataArray` and `MeshData` structs
from any thread. Creating a `MeshDataArray` has some overhead for memory
tracking and safety reasons, so it is more efficient to make a single call to
[Mesh.AcquireReadOnlyMeshData](Mesh.AcquireReadOnlyMeshData.html) and request
multiple `MeshData` structs in the same `MeshDataArray` than it is to make
multiple calls to
[Mesh.AcquireReadOnlyMeshData](Mesh.AcquireReadOnlyMeshData.html).  
  
Each `MeshData` struct contains a read-only snapshot of data for a given Mesh.  
  
You must dispose of the `MeshDataArray` once you have finished working with
it. Calling [Mesh.AcquireReadOnlyMeshData](Mesh.AcquireReadOnlyMeshData.html)
does not cause any memory allocations or data copies by default, as long as
you dispose of the `MeshDataArray` before modifying the Mesh. However, if you
call [Mesh.AcquireReadOnlyMeshData](Mesh.AcquireReadOnlyMeshData.html) and
then modify the Mesh while the `MeshDataArray` exists, Unity must copy the
`MeshDataArray` into a new memory allocation. In addition to this, if you call
[Mesh.AcquireReadOnlyMeshData](Mesh.AcquireReadOnlyMeshData.html) and then
modify the Mesh, your modifications are not reflected in the `MeshData`
structs.  
  
This method will throw an `InvalidOperationException` if [isReadable](Mesh-
isReadable.html) is `false` for one or more input meshes. When working in the
Unity Editor, use
[MeshUtility.AcquireReadOnlyMeshData](MeshUtility.AcquireReadOnlyMeshData.html)
to skip this check.  
  
Use [Dispose](Mesh.MeshDataArray.Dispose.html) to dispose of the
`MeshDataArray`, or use the C# `using` pattern to do this automatically:

    
    
    using Unity.Collections;
    using UnityEngine;  
      
    public class ExampleScript : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            [Mesh](Mesh.html) mesh = new [Mesh](Mesh.html)();
            mesh.vertices = new[] {[Vector3.one](Vector3-one.html), [Vector3.zero](Vector3-zero.html)};
            using ([Mesh.MeshDataArray](Mesh.MeshDataArray.html) dataArray = [Mesh.AcquireReadOnlyMeshData](Mesh.AcquireReadOnlyMeshData.html)(mesh))
            {
                [Mesh.MeshData](Mesh.MeshData.html) data = dataArray[0];
                // prints "2"
                [Debug.Log](Debug.Log.html)(data.vertexCount);
                NativeArray<[Vector3](Vector3.html)> gotVertices = new NativeArray<[Vector3](Vector3.html)>(mesh.vertexCount, [Allocator.TempJob](Unity.Collections.Allocator.TempJob.html));
                data.GetVertices(gotVertices);
                // prints "(1.0, 1.0, 1.0)" and "(0.0, 0.0, 0.0)"
                foreach ([Vector3](Vector3.html) v in gotVertices)
                    [Debug.Log](Debug.Log.html)(v);
                gotVertices.Dispose();
            }
        }
    }
    

Additional resources: [MeshDataArray](Mesh.MeshDataArray.html),
[MeshData](Mesh.MeshData.html),
[AllocateWritableMeshData](Mesh.AllocateWritableMeshData.html),
[ApplyAndDisposeWritableMeshData](Mesh.ApplyAndDisposeWritableMeshData.html).

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

