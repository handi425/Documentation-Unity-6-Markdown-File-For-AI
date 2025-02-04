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

#  [GL](GL.html).Color

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

public static void Color([Color](Color.html) c);

### Description

Sets current vertex color.

In OpenGL this matches `glColor4f(c.r,c.g,c.b,c.a)`; on other graphics APIs
the same functionality is emulated.  
  
In order for per-vertex colors to work reliably across different hardware, you
have to use a shader that binds in the color channel. See
[BindChannels](../Manual/SL-BindChannels.html) documentation.  
  
This function can only be called between [GL.Begin](GL.Begin.html) and
[GL.End](GL.End.html) functions.

    
    
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        // Draws a red line from the bottom right
        // to the top left of the [Screen](Screen.html)
        // And a yellow line from the bottom left
        // to the top right of the [Screen](Screen.html)
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
      
            [GL.Begin](GL.Begin.html)([GL.LINES](GL.LINES.html));
            [GL.Color](GL.Color.html)([Color.red](Color-red.html));
            [GL.Vertex3](GL.Vertex3.html)(1, 0, 0);
            [GL.Vertex3](GL.Vertex3.html)(0, 1, 0);
            [GL.Color](GL.Color.html)([Color.yellow](Color-yellow.html));
            [GL.Vertex3](GL.Vertex3.html)(0, 0, 0);
            [GL.Vertex3](GL.Vertex3.html)(1, 1, 0);
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

