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

#  [GL](GL.html).LoadPixelMatrix

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

public static void LoadPixelMatrix();

### Description

Setup a matrix for pixel-correct rendering.

Loads an orthographic projection into the projection matrix and loads an
identity into the model and view matrices. The projection matrix is such that
the X and Y coordinates map directly to pixels. The coordinate (0,0) is at the
bottom left corner of current camera's viewport. The Z coordinates go from 1
at the near plane to -100 at the far plane.  
  
Changing the model, view or projection matrices overrides the current
rendering matrices. It is good practice to save and restore these matrices
using [GL.PushMatrix](GL.PushMatrix.html) and
[GL.PopMatrix](GL.PopMatrix.html).

    
    
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        // Draws a red triangle using pixels as coordinates to paint on.
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
            [GL.LoadPixelMatrix](GL.LoadPixelMatrix.html)();  
      
            [GL.Begin](GL.Begin.html)([GL.TRIANGLES](GL.TRIANGLES.html));
            [GL.Color](GL.Color.html)([Color.red](Color-red.html));
            [GL.Vertex3](GL.Vertex3.html)(0, 0, 0);
            [GL.Vertex3](GL.Vertex3.html)(0, [Screen.height](Screen-height.html) / 2, 0);
            [GL.Vertex3](GL.Vertex3.html)([Screen.width](Screen-width.html) / 2, [Screen.height](Screen-height.html) / 2, 0);
            [GL.End](GL.End.html)();  
      
            [GL.PopMatrix](GL.PopMatrix.html)();
        }
    }
    

* * *

## Declaration

public static void LoadPixelMatrix(float left, float right, float bottom,
float top);

### Description

Setup a matrix for pixel-correct rendering.

Loads an orthographic projection into the projection matrix and loads an
identity into the model and view matrices. The projection matrix is such that
the X and Y coordinates map directly to pixels. The (left,bottom) is at the
bottom left corner of current camera's viewport; and (top,right) is at the top
right corner of current camera's viewport. The Z coordinates go from 1 at the
near plane to -1 at the far plane.  
  
Changing the model, view or projection matrices overrides the current
rendering matrices. It is good practice to save and restore these matrices
using [GL.PushMatrix](GL.PushMatrix.html) and
[GL.PopMatrix](GL.PopMatrix.html).  
  

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

