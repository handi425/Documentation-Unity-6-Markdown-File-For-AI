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

#  [Mesh](Mesh.html).Clear

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

public void Clear(bool keepVertexLayout = true);

### Parameters

keepVertexLayout | True if the existing Mesh data layout should be preserved.  
---|---  
  
### Description

Clears all vertex data and all triangle indices.

You should call this function before rebuilding [triangles](Mesh-
triangles.html) array.

    
    
    // Convert any [GameObject](GameObject.html) into a single triangle  
      
    using UnityEngine;  
      
    public class meshClear : [MonoBehaviour](MonoBehaviour.html)
    {
        private bool once = false;  
      
        void [Update](PlayerLoop.Update.html)()
        {
            if ([Time.time](Time-time.html) > 2.0f)
            {
                convertMesh();
            }
        }  
      
        void convertMesh()
        {
            if (once)
                return;  
      
            [Mesh](Mesh.html) mesh = GetComponent<[MeshFilter](MeshFilter.html)>().mesh;  
      
            // Clears all the data that the mesh currently has
            mesh.Clear();  
      
            // create 3 vertices for the triangle
            mesh.vertices = new [Vector3](Vector3.html)[] {new [Vector3](Vector3.html)(0, 0, 0), new [Vector3](Vector3.html)(0, 1, 0), new [Vector3](Vector3.html)(1, 1, 0)};
            mesh.uv = new [Vector2](Vector2.html)[] {new [Vector2](Vector2.html)(0, 0), new [Vector2](Vector2.html)(0, 1), new [Vector2](Vector2.html)(1, 1)};
            mesh.triangles = new int[] {0, 1, 2};  
      
            once = true;
        }
    }
    

Default behaviour of this function keeps the existing vertex layout: if the
mesh had tangent vectors and vertex colors, for example, then the tangents and
colors will be part of mesh data once you fill in new vertex data. If you want
to completely clear the mesh and start with an empty vertex layout, pass false
for `keepVertexLayout` parameter. Alternatively, assigning an empty array to
any mesh component will also remove it from the vertex layout.

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

