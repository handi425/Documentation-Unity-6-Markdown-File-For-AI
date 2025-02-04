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

#  [Mesh](Mesh.html).vertices

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

public Vector3[] vertices;

### Description

Returns a copy of the vertex positions or assigns a new vertex positions
array.

The number of vertices in the Mesh is changed by assigning a vertex array with
a different number of vertices.  
  
If you resize the vertex array then all other vertex attributes (normals,
colors, tangents, UVs) are automatically resized too.
[RecalculateBounds](Mesh.RecalculateBounds.html) is automatically invoked if
no vertices have been assigned to the Mesh when setting the vertices.  
  
Note that this method returns the vertices in local space, not in world space.

    
    
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        [Mesh](Mesh.html) mesh;
        [Vector3](Vector3.html)[] vertices;
        void Start()
        {
            mesh = GetComponent<[MeshFilter](MeshFilter.html)>().mesh;
            vertices = mesh.vertices;
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            for (var i = 0; i < vertices.Length; i++)
            {
                vertices[i] += [Vector3.up](Vector3-up.html) * [Time.deltaTime](Time-deltaTime.html);
            }  
      
            // assign the local vertices array into the vertices array of the [Mesh](Mesh.html).
            mesh.vertices = vertices;
            mesh.RecalculateBounds();
        }
    }
    

**Note:** To make changes to the [vertices](Mesh-vertices.html) it is
important to copy the vertices from the [Mesh](Mesh.html). Once the
[vertices](Mesh-vertices.html) have been copied and changed the
[vertices](Mesh-vertices.html) can be reassigned back to the
[Mesh](Mesh.html).

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

