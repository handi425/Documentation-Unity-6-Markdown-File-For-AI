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

#  [Mesh](Mesh.html).triangles

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

public int[] triangles;

### Description

An array containing all triangles in the Mesh.

The array is a list of triangles that contains indices into the vertex array.
The size of the triangle array must always be a multiple of 3. Vertices can be
shared by simply indexing into the same vertex. If the Mesh contains multiple
sub-meshes (Materials), the triangle list will contain all the triangles
belonging to all its sub-meshes. When you assign a triangle array using this
function, the [subMeshCount](Mesh-subMeshCount.html) is set to 1. If you want
to have multiple sub-meshes, use [subMeshCount](Mesh-subMeshCount.html) and
[SetTriangles](Mesh.SetTriangles.html).  
  
It is recommended to assign a triangle array after assigning the vertex array,
in order to avoid out of bounds errors.

    
    
    // Builds a [Mesh](Mesh.html) containing a single triangle with uvs.
    // Create arrays of vertices, uvs and triangles, and copy them into the mesh.  
      
    using UnityEngine;  
      
    public class meshTriangles : [MonoBehaviour](MonoBehaviour.html)
    {
        // Use this for initialization
        void Start()
        {
            gameObject.AddComponent<[MeshFilter](MeshFilter.html)>();
            gameObject.AddComponent<[MeshRenderer](MeshRenderer.html)>();
            [Mesh](Mesh.html) mesh = GetComponent<[MeshFilter](MeshFilter.html)>().mesh;  
      
            mesh.Clear();  
      
            // make changes to the [Mesh](Mesh.html) by creating arrays which contain the new values
            mesh.vertices = new [Vector3](Vector3.html)[] {new [Vector3](Vector3.html)(0, 0, 0), new [Vector3](Vector3.html)(0, 1, 0), new [Vector3](Vector3.html)(1, 1, 0)};
            mesh.uv = new [Vector2](Vector2.html)[] {new [Vector2](Vector2.html)(0, 0), new [Vector2](Vector2.html)(0, 1), new [Vector2](Vector2.html)(1, 1)};
            mesh.triangles =  new int[] {0, 1, 2};
        }
    }
    

Additional resources: [SetTriangles](Mesh.SetTriangles.html),
[SetIndices](Mesh.SetIndices.html).

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

