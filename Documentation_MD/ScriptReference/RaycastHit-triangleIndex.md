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

#  [RaycastHit](RaycastHit.html).triangleIndex

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

public int triangleIndex;

### Description

The index of the triangle that was hit.

Triangle index is only valid if the collider that was hit is a
[MeshCollider](MeshCollider.html).

    
    
    // This script draws a debug line around mesh triangles
    // as you move the mouse over them.
    using UnityEngine;
    using System.Collections;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        [Camera](Camera.html) cam;  
      
        void Start()
        {
            cam = GetComponent<[Camera](Camera.html)>();
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            [RaycastHit](RaycastHit.html) hit;
            if (![Physics.Raycast](Physics.Raycast.html)(cam.ScreenPointToRay([Input.mousePosition](Input-mousePosition.html)), out hit))
                return;  
      
            [MeshCollider](MeshCollider.html) meshCollider = hit.collider as [MeshCollider](MeshCollider.html);
            if (meshCollider == null || meshCollider.sharedMesh == null)
                return;  
      
            [Mesh](Mesh.html) mesh = meshCollider.sharedMesh;
            [Vector3](Vector3.html)[] vertices = mesh.vertices;
            int[] triangles = mesh.triangles;
            [Vector3](Vector3.html) p0 = vertices[triangles[hit.triangleIndex * 3 + 0]];
            [Vector3](Vector3.html) p1 = vertices[triangles[hit.triangleIndex * 3 + 1]];
            [Vector3](Vector3.html) p2 = vertices[triangles[hit.triangleIndex * 3 + 2]];
            [Transform](Transform.html) hitTransform = hit.collider.transform;
            p0 = hitTransform.TransformPoint(p0);
            p1 = hitTransform.TransformPoint(p1);
            p2 = hitTransform.TransformPoint(p2);
            [Debug.DrawLine](Debug.DrawLine.html)(p0, p1);
            [Debug.DrawLine](Debug.DrawLine.html)(p1, p2);
            [Debug.DrawLine](Debug.DrawLine.html)(p2, p0);
        }
    }
    

Additional resources: [Physics.Raycast](Physics.Raycast.html),
[Physics.Linecast](Physics.Linecast.html),
[Physics.RaycastAll](Physics.RaycastAll.html).

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

