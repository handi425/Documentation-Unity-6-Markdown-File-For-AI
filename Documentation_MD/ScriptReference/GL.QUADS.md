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

#  [GL](GL.html).QUADS

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

public static int QUADS;

### Description

Mode for [Begin](GL.Begin.html): draw quads.

Draws quads using each set of 4 vertices passed. If you pass 4 vertices, one
quad is drawn, where each vertex becomes one corner of the quad. If you pass 8
vertices, 2 quads will be drawn.  
  
To set up the screen for drawing in 2D, use [GL.LoadOrtho](GL.LoadOrtho.html)
or [GL.LoadPixelMatrix](GL.LoadPixelMatrix.html). To set up the screen for
drawing in 3D, use [GL.LoadIdentity](GL.LoadIdentity.html) followed by
[GL.MultMatrix](GL.MultMatrix.html) with the desired transformation matrix.  
  
Additional resources: [GL.Begin](GL.Begin.html), [GL.End](GL.End.html).

    
    
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        // Draw red a rombus on the screen
        // and also draw a small cyan Quad in the left corner
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
            [GL.Begin](GL.Begin.html)([GL.QUADS](GL.QUADS.html));
            [GL.Color](GL.Color.html)([Color.red](Color-red.html));
            [GL.Vertex3](GL.Vertex3.html)(0, 0.5f, 0);
            [GL.Vertex3](GL.Vertex3.html)(0.5f, 1, 0);
            [GL.Vertex3](GL.Vertex3.html)(1, 0.5f, 0);
            [GL.Vertex3](GL.Vertex3.html)(0.5f, 0, 0);  
      
            [GL.Color](GL.Color.html)([Color.cyan](Color-cyan.html));
            [GL.Vertex3](GL.Vertex3.html)(0, 0, 0);
            [GL.Vertex3](GL.Vertex3.html)(0, 0.25f, 0);
            [GL.Vertex3](GL.Vertex3.html)(0.25f, 0.25f, 0);
            [GL.Vertex3](GL.Vertex3.html)(0.25f, 0, 0);
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

