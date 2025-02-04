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

#  [Mesh](Mesh.html).uv

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

public Vector2[] uv;

### Description

The texture coordinates (UVs) in the first channel.

This channel is also commonly called "UV0". It maps to the shader semantic
`TEXCOORD0`. When you call
[Mesh.HasVertexAttribute](Mesh.HasVertexAttribute.html), this channel
corresponds to
[VertexAttribute.TexCoord0](Rendering.VertexAttribute.TexCoord0.html).  
  
By default, Unity uses this channel to store UVs for commonly used textures:
diffuse maps, specular maps, and so on.  
  
Unity stores UVs in 0-1 space. [0,0] represents the bottom-left corner of the
texture, and [1,1] represents the top-right. Values are not clamped; you can
use values below 0 and above 1 if needed.  
  
This property is supported for backwards compatibility, but the newer
[GetUVs](Mesh.GetUVs.html) and [SetUVs](Mesh.SetUVs.html) functions allow you
to access the same data in a more user-friendly way, and use a Vector3 or
Vector4 value if you need to.  
  
This property returns a copy of the data. This means that it causes a heap
memory allocation. It also means that to make changes to the original data,
you must update the copy and then reassign the updated copy to the mesh.  
  
The following example demonstrates how to create an array to hold UV data,
assign texture coordinates to it, and then assign it to the mesh.

    
    
    using UnityEngine;
    using System.Collections;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            [Mesh](Mesh.html) mesh = GetComponent<[MeshFilter](MeshFilter.html)>().mesh;
            [Vector3](Vector3.html)[] vertices = mesh.vertices;
            [Vector2](Vector2.html)[] uvs = new [Vector2](Vector2.html)[vertices.Length];  
      
            for (int i = 0; i < uvs.Length; i++)
            {
                uvs[i] = new [Vector2](Vector2.html)(vertices[i].x, vertices[i].z);
            }
            mesh.uv = uvs;
        }
    }
    

Additional resources: [GetUVs](Mesh.GetUVs.html), [SetUVs](Mesh.SetUVs.html),
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

