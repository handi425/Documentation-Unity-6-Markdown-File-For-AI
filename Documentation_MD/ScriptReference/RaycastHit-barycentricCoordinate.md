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

#  [RaycastHit](RaycastHit.html).barycentricCoordinate

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

public [Vector3](Vector3.html) barycentricCoordinate;

### Description

The barycentric coordinate of the triangle we hit.

This lets you interpolate any of the vertex data along the 3 axes.

    
    
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        // Attach this script to a camera and it will
        // draw a debug line pointing outward from the normal
        void [Update](PlayerLoop.Update.html)()
        {
            // Only if we hit something, do we continue
            [RaycastHit](RaycastHit.html) hit;  
      
    
            if (![Physics.Raycast](Physics.Raycast.html)(Camera.main.ScreenPointToRay([Input.mousePosition](Input-mousePosition.html)), out hit))
            {
                return;
            }  
      
            // Just in case, also make sure the collider also has a renderer
            // material and texture
            [MeshCollider](MeshCollider.html) meshCollider = hit.collider as [MeshCollider](MeshCollider.html);
            if (meshCollider == null || meshCollider.sharedMesh == null)
            {
                return;
            }  
      
            [Mesh](Mesh.html) mesh = meshCollider.sharedMesh;
            [Vector3](Vector3.html)[] normals = mesh.normals;
            int[] triangles = mesh.triangles;  
      
            // Extract local space normals of the triangle we hit
            [Vector3](Vector3.html) n0 = normals[triangles[hit.triangleIndex * 3 + 0]];
            [Vector3](Vector3.html) n1 = normals[triangles[hit.triangleIndex * 3 + 1]];
            [Vector3](Vector3.html) n2 = normals[triangles[hit.triangleIndex * 3 + 2]];  
      
            // interpolate using the barycentric coordinate of the hitpoint
            [Vector3](Vector3.html) baryCenter = hit.barycentricCoordinate;  
      
            // Use barycentric coordinate to interpolate normal
            [Vector3](Vector3.html) interpolatedNormal = n0 * baryCenter.x + n1 * baryCenter.y + n2 * baryCenter.z;
            // normalize the interpolated normal
            interpolatedNormal = interpolatedNormal.normalized;  
      
            // [Transform](Transform.html) local space normals to world space
            [Transform](Transform.html) hitTransform = hit.collider.transform;
            interpolatedNormal = hitTransform.TransformDirection(interpolatedNormal);  
      
            // [Display](Display.html) with [Debug.DrawLine](Debug.DrawLine.html)
            [Debug.DrawRay](Debug.DrawRay.html)(hit.point, interpolatedNormal);
        }
    }
    

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

