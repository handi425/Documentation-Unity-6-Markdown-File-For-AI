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

#  [Graphics](Graphics.html).DrawMeshNow

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

[ ]()

## Declaration

public static void DrawMeshNow([Mesh](Mesh.html) mesh, [Vector3](Vector3.html)
position, [Quaternion](Quaternion.html) rotation);

## Declaration

public static void DrawMeshNow([Mesh](Mesh.html) mesh, [Vector3](Vector3.html)
position, [Quaternion](Quaternion.html) rotation, int materialIndex);

## Declaration

public static void DrawMeshNow([Mesh](Mesh.html) mesh,
[Matrix4x4](Matrix4x4.html) matrix);

## Declaration

public static void DrawMeshNow([Mesh](Mesh.html) mesh,
[Matrix4x4](Matrix4x4.html) matrix, int materialIndex);

### Parameters

mesh | The [Mesh](Mesh.html) to draw.  
---|---  
position | Position of the mesh.  
rotation | Rotation of the mesh.  
matrix | The transformation matrix of the mesh (combines position, rotation and other transformations).  
materialIndex | Subset of the mesh to draw.  
  
### Description

Draw a mesh immediately.

This function will draw a given mesh immediately. Currently set shader and
material (see [Material.SetPass](Material.SetPass.html)) will be used.  
  
The mesh will be just drawn once, it won't be per-pixel lit and will not cast
or receive real-time shadows. If you want full integration with lighting and
shadowing, use [Graphics.DrawMesh](Graphics.DrawMesh.html) instead.

    
    
    using UnityEngine;
    using System.Collections;  
      
    // Attach this script to a [Camera](Camera.html)
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html) {
        public [Mesh](Mesh.html) mesh;
        public [Material](Material.html) mat;
        public void OnPostRender() {
            // set first shader pass of the material
            mat.SetPass(0);
            // draw mesh at the origin
            [Graphics.DrawMeshNow](Graphics.DrawMeshNow.html)(mesh, [Vector3.zero](Vector3-zero.html), [Quaternion.identity](Quaternion-identity.html));
        }
    }

Additional resources: [Graphics.DrawMesh](Graphics.DrawMesh.html),
[Material.SetPass](Material.SetPass.html).

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

