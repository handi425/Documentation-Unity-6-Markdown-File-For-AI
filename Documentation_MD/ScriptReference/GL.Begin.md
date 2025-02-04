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

#  [GL](GL.html).Begin

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

public static void Begin(int mode);

### Parameters

mode | Primitives to draw: can be [TRIANGLES](GL.TRIANGLES.html), [TRIANGLE_STRIP](GL.TRIANGLE_STRIP.html), [QUADS](GL.QUADS.html) or [LINES](GL.LINES.html).  
---|---  
  
### Description

Begin drawing 3D primitives.

In OpenGL this matches `glBegin`; on other graphics APIs the same
functionality is emulated. Between GL.Begin and [GL.End](GL.End.html) it is
valid to call [GL.Vertex](GL.Vertex.html), [GL.Color](GL.Color.html),
[GL.TexCoord](GL.TexCoord.html) and other immediate mode drawing functions.  
  
You should be careful about culling when drawing primitives yourself. The
culling rules may be different depending on which graphics API the game is
running. In most cases the safest way is to use `Cull Off` command in the
shader.  
  
Additional resources: [GL.End](GL.End.html).

    
    
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        // Draws a Triangle, a Quad and a line
        // with different colors  
      
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
      
            [GL.Begin](GL.Begin.html)([GL.TRIANGLES](GL.TRIANGLES.html)); // Triangle
            [GL.Color](GL.Color.html)(new [Color](Color.html)(1, 1, 1, 1));
            [GL.Vertex3](GL.Vertex3.html)(0.50f, 0.25f, 0);
            [GL.Vertex3](GL.Vertex3.html)(0.25f, 0.25f, 0);
            [GL.Vertex3](GL.Vertex3.html)(0.375f, 0.5f, 0);
            [GL.End](GL.End.html)();  
      
            [GL.Begin](GL.Begin.html)([GL.QUADS](GL.QUADS.html)); // Quad
            [GL.Color](GL.Color.html)(new [Color](Color.html)(0.5f, 0.5f, 0.5f, 1));
            [GL.Vertex3](GL.Vertex3.html)(0.5f, 0.5f, 0);
            [GL.Vertex3](GL.Vertex3.html)(0.5f, 0.75f, 0);
            [GL.Vertex3](GL.Vertex3.html)(0.75f, 0.75f, 0);
            [GL.Vertex3](GL.Vertex3.html)(0.75f, 0.5f, 0);
            [GL.End](GL.End.html)();  
      
            [GL.Begin](GL.Begin.html)([GL.LINES](GL.LINES.html)); // Line
            [GL.Color](GL.Color.html)(new [Color](Color.html)(0, 0, 0, 1));
            [GL.Vertex3](GL.Vertex3.html)(0, 0, 0);
            [GL.Vertex3](GL.Vertex3.html)(0.75f, 0.75f, 0);
            [GL.End](GL.End.html)();
            [GL.PopMatrix](GL.PopMatrix.html)();
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

