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

#  [GL](GL.html).LoadOrtho

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

public static void LoadOrtho();

### Description

Helper function to set up an orthograhic projection.

Loads an orthographic projection into the projection matrix and loads an
identity into the model and view matrices.  
  
The resulting projection performs the following mappings:  
**1.** x = 0..1 to x = -1..1 (left..right)  
**2.** y = 0..1 to y = -1..1 (bottom..top)  
**3.** z = 1..-100 to z = -1..1 (near..far)  
  
This is equivalent to the following operations:

    
    
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        void OnPostRender()
        {
            // ...  
      
            [GL.LoadOrtho](GL.LoadOrtho.html)();  
      
            // is equivalent to:  
      
            [GL.LoadIdentity](GL.LoadIdentity.html)();
            var proj = [Matrix4x4.Ortho](Matrix4x4.Ortho.html)(0, 1, 0, 1, -1, 100);
            [GL.LoadProjectionMatrix](GL.LoadProjectionMatrix.html)(proj);  
      
            // ...
        }
    }
    

Changing the model, view or projection matrices overrides the current
rendering matrices. It is good practice to save and restore these matrices
using [GL.PushMatrix](GL.PushMatrix.html) and
[GL.PopMatrix](GL.PopMatrix.html).

    
    
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        // Draws a triangle under an already drawn triangle
        [Material](Material.html) mat;  
      
        void OnPostRender()
        {
            if (!mat)
            {
                [Debug.LogError](Debug.LogError.html)("Please Assign a material on the inspector");
                return;
            }
            [GL.PushMatrix](GL.PushMatrix.html)();
            mat.SetPass(0);
            [GL.LoadOrtho](GL.LoadOrtho.html)();
            [GL.Color](GL.Color.html)([Color.red](Color-red.html));
            [GL.Begin](GL.Begin.html)([GL.TRIANGLES](GL.TRIANGLES.html));
            [GL.Vertex3](GL.Vertex3.html)(0.25f, 0.1351f, 0);
            [GL.Vertex3](GL.Vertex3.html)(0.25f, 0.3f, 0);
            [GL.Vertex3](GL.Vertex3.html)(0.5f, 0.3f, 0);
            [GL.End](GL.End.html)();  
      
            [GL.Color](GL.Color.html)([Color.yellow](Color-yellow.html));
            [GL.Begin](GL.Begin.html)([GL.TRIANGLES](GL.TRIANGLES.html));
            [GL.Vertex3](GL.Vertex3.html)(0.5f, 0.25f, -1);
            [GL.Vertex3](GL.Vertex3.html)(0.5f, 0.1351f, -1);
            [GL.Vertex3](GL.Vertex3.html)(0.1f, 0.25f, -1);
            [GL.End](GL.End.html)();  
      
            [GL.PopMatrix](GL.PopMatrix.html)();
        }
    }
    

Additional resources: [GL.LoadProjectionMatrix](GL.LoadProjectionMatrix.html),
[Matrix4x4.Ortho](Matrix4x4.Ortho.html).

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

