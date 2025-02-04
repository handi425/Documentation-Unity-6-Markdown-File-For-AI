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

#  [Matrix4x4](Matrix4x4.html).TRS

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

public static [Matrix4x4](Matrix4x4.html) TRS([Vector3](Vector3.html) pos,
[Quaternion](Quaternion.html) q, [Vector3](Vector3.html) s);

### Description

Creates a translation, rotation and scaling matrix.

The returned matrix is such that it places objects at position `pos`, oriented
in rotation `q` and scaled by `s`.

    
    
    using UnityEngine;  
      
    public class ExampleScript : [MonoBehaviour](MonoBehaviour.html)
    {
        // [Translate](UIElements.Translate.html), rotate and scale a mesh. Try altering
        // the parameters in the inspector while running
        // to see the effect they have.  
      
        public [Vector3](Vector3.html) translation;
        public [Vector3](Vector3.html) eulerAngles;
        public [Vector3](Vector3.html) scale = new [Vector3](Vector3.html)(1, 1, 1);  
      
    
        [MeshFilter](MeshFilter.html) mf;
        [Vector3](Vector3.html)[] origVerts;
        [Vector3](Vector3.html)[] newVerts;  
      
    
        void Start()
        {
            // Get the [Mesh](Mesh.html) Filter component, save its original vertices
            // and make a new vertex array for processing.
            mf = GetComponent<[MeshFilter](MeshFilter.html)> ();
            origVerts = mf.mesh.vertices;
            newVerts = new [Vector3](Vector3.html)[origVerts.Length];
        }  
      
    
        void [Update](PlayerLoop.Update.html)()
        {
            // Set a [Quaternion](Quaternion.html) from the specified Euler angles.
            [Quaternion](Quaternion.html) rotation = [Quaternion.Euler](Quaternion.Euler.html)(eulerAngles.x, eulerAngles.y, eulerAngles.z);  
      
            // Set the translation, rotation and scale parameters.
            [Matrix4x4](Matrix4x4.html) m = [Matrix4x4.TRS](Matrix4x4.TRS.html)(translation, rotation, scale);  
      
            // For each vertex...
            for (int i = 0; i < origVerts.Length; i++)
            {
                // Apply the matrix to the vertex.
                newVerts[i] = m.MultiplyPoint3x4(origVerts[i]);
            }  
      
            // Copy the transformed vertices back to the mesh.
            mf.mesh.vertices = newVerts;
        }
    }
    

Additional resources: [TRS](Matrix4x4.TRS.html),
[Rotate](Matrix4x4.Rotate.html), [Scale](Matrix4x4.Scale.html),
[Translate](Matrix4x4.Translate.html), [SetTRS](Matrix4x4.SetTRS.html)
functions.

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

