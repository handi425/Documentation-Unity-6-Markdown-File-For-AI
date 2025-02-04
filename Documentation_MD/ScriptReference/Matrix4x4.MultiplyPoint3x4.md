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

#  [Matrix4x4](Matrix4x4.html).MultiplyPoint3x4

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

public [Vector3](Vector3.html) MultiplyPoint3x4([Vector3](Vector3.html)
point);

### Description

Transforms a position by this matrix (fast).

Returns a position `v` transformed by the current transformation matrix. This
function is a faster version of [MultiplyPoint](Matrix4x4.MultiplyPoint.html);
but it can only handle regular 3D transformations. `MultiplyPoint` is slower,
but can handle projective transformations as well.  
  
Additional resources: [MultiplyPoint](Matrix4x4.MultiplyPoint.html),
[MultiplyVector](Matrix4x4.MultiplyVector.html).

    
    
    using UnityEngine;  
      
    public class ExampleScript : [MonoBehaviour](MonoBehaviour.html)
    {
        // Stretch a mesh at an arbitrary angle around the X axis.  
      
        // [Angle](UIElements.Angle.html) and amount of stretching.
        float rotAngle;
        float stretch;  
      
    
        [MeshFilter](MeshFilter.html) mf;
        [Vector3](Vector3.html)[] origVerts;
        [Vector3](Vector3.html)[] newVerts;  
      
    
        void Start()
        {
            // Get the [Mesh](Mesh.html) Filter component, save its original vertices
            // and make a new vertex array for processing.
            mf = GetComponent< [MeshFilter](MeshFilter.html) > ();
            origVerts = mf.mesh.vertices;
            newVerts = new [Vector3](Vector3.html)[origVerts.Length];
        }  
      
    
        void [Update](PlayerLoop.Update.html)()
        {
            // Create a rotation matrix from a [Quaternion](Quaternion.html).
            [Quaternion](Quaternion.html) rot = [Quaternion.Euler](Quaternion.Euler.html)(rotAngle, 0, 0);
            [Matrix4x4](Matrix4x4.html) m = [Matrix4x4.TRS](Matrix4x4.TRS.html)([Vector3.zero](Vector3-zero.html), rot, [Vector3.one](Vector3-one.html));  
      
            // Get the inverse of the matrix (ie, to undo the rotation).
            [Matrix4x4](Matrix4x4.html) inv = m.inverse;  
      
            // For each vertex...
            for (var i = 0; i < origVerts.Length; i++)
            {
                // [Rotate](UIElements.Rotate.html) the vertex and scale it along its new Y axis.
                var pt = m.MultiplyPoint3x4(origVerts[i]);
                pt.y *= stretch;  
      
                // Return the vertex to its original rotation (but with the
                // scaling still applied).
                newVerts[i] = inv.MultiplyPoint3x4(pt);
            }  
      
            // Copy the transformed vertices back to the mesh.
            mf.mesh.vertices = newVerts;
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

