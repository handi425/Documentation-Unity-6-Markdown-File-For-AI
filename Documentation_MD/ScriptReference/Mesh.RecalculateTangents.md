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

#  [Mesh](Mesh.html).RecalculateTangents

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

public void
RecalculateTangents([Rendering.MeshUpdateFlags](Rendering.MeshUpdateFlags.html)
flags = MeshUpdateFlags.Default);

### Parameters

flags | Flags controlling the function behavior, see [MeshUpdateFlags](Rendering.MeshUpdateFlags.html).  
---|---  
  
### Description

Recalculates the tangents of the Mesh from the normals and texture
coordinates.

After modifying the vertices and the normals of the Mesh, tangents need to be
updated if the Mesh is rendered using Shaders that reference normal maps.
Unity calculates tangents using the vertex positions, normals and texture
coordinates of the Mesh.  
  
`RecalculateTangents` adds a tangent attribute to the vertex, or changes the
tangent attribute to the correct format. The attribute has a dimension of 4
and uses the
[VertexAttributeFormat.Float32](Rendering.VertexAttributeFormat.Float32.html)
format. `RecalculateTangents` adds the attribute even if the Mesh doesn't have
any vertices.

    
    
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            [Mesh](Mesh.html) mesh = GetComponent<[MeshFilter](MeshFilter.html)>().mesh;
            mesh.RecalculateTangents();
        }
    }
    

`RecalculateTangents` converts Mesh vertex position, normal and UV0 data to
[VertexAttributeFormat.Float32](Rendering.VertexAttributeFormat.Float32.html)
format, if the format is different.  
  
If the Mesh does not have normals, texture coordinates or triangles, then the
tangents are all set to a (1,0,0,1) vector.  
  
Additional resources: [RecalculateNormals](Mesh.RecalculateNormals.html).

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

