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

# MeshDataArray

struct in UnityEngine

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

[Switch to Manual](../Manual/class-Mesh.html "Go to Mesh Component in the
Manual")

### Description

An array of Mesh data snapshots for C# Job System access.

Access to most Unity objects is not thread-safe, so in order to efficiently
process or create meshes from the C# Job System, use the `MeshDataArray` and
`MeshData` structs.  
  
You can use [Mesh.AcquireReadOnlyMeshData](Mesh.AcquireReadOnlyMeshData.html)
for read-only access to mesh data of multiple meshes, and
[Mesh.AllocateWritableMeshData](Mesh.AllocateWritableMeshData.html) together
with
[Mesh.ApplyAndDisposeWritableMeshData](Mesh.ApplyAndDisposeWritableMeshData.html)
for creating new meshes.  
  
A single `MeshDataArray` struct represents snapshot of mesh data of multiple
meshes. Use [Length](Mesh.MeshDataArray.Length.html) and [index
operator](Mesh.MeshDataArray.Index_operator.html) to access data of an
individual Mesh. Memory allocation and C# Job System safety tracking is built
into `MeshDataArray` struct, so that the tracking overhead is minimal when
working with multiple meshes at the same time. It is thus much more efficient
to use a single `MeshDataArray/` struct for multiple meshes, than to operate
on several individual structs.  
  
It is important to dispose of a `MeshDataArray` struct once you have finished
working with it. Use [Dispose](Mesh.MeshDataArray.Dispose.html) to dispose of
the struct when you have finished using it, or use the C# `using` pattern to
do this automatically:

    
    
    using Unity.Collections;
    using UnityEngine;
    public class ExampleScript : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            var mesh = new [Mesh](Mesh.html)();
            mesh.vertices = new[] {[Vector3.one](Vector3-one.html), [Vector3.zero](Vector3-zero.html)};
            using (var dataArray = [Mesh.AcquireReadOnlyMeshData](Mesh.AcquireReadOnlyMeshData.html)(mesh))
            {
                var data = dataArray[0];
                // prints "2"
                [Debug.Log](Debug.Log.html)(data.vertexCount);
                var gotVertices = new NativeArray<[Vector3](Vector3.html)>(mesh.vertexCount, [Allocator.TempJob](Unity.Collections.Allocator.TempJob.html));
                data.GetVertices(gotVertices);
                // prints "(1.0, 1.0, 1.0)" and "(0.0, 0.0, 0.0)"
                foreach (var v in gotVertices)
                    [Debug.Log](Debug.Log.html)(v);
                gotVertices.Dispose();
            }
        }
    }
    

Additional resources:
[Mesh.AcquireReadOnlyMeshData](Mesh.AcquireReadOnlyMeshData.html),
[Mesh.AllocateWritableMeshData](Mesh.AllocateWritableMeshData.html),
[Mesh.ApplyAndDisposeWritableMeshData](Mesh.ApplyAndDisposeWritableMeshData.html),
[MeshData](Mesh.MeshData.html).

### Properties

[Length](Mesh.MeshDataArray.Length.html)| Number of Mesh data elements in the
MeshDataArray.  
---|---  
[this[int]](Mesh.MeshDataArray.Index_operator.html)| Access MeshDataArray
element by an index.  
  
### Public Methods

[Dispose](Mesh.MeshDataArray.Dispose.html)| Use this method to dispose of the
MeshDataArray struct.  
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

