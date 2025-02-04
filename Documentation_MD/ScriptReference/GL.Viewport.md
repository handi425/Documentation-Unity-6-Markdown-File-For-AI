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

#  [GL](GL.html).Viewport

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

public static void Viewport([Rect](Rect.html) pixelRect);

### Description

Set the rendering viewport.

All rendering is constrained to be inside the passed `pixelRect`. If the
Viewport is modified, all the rendered content inside of it gets stretched.

    
    
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        // Draw a red Quad that covers all the view port, and the when space is pressed
        // the viewport gets expanded to the whole screen and stretch the contents inside
        [Material](Material.html) mat;
        bool stretch = false;  
      
        void [Update](PlayerLoop.Update.html)()
        {
            if ([Input.GetKeyDown](Input.GetKeyDown.html)([KeyCode.Space](KeyCode.Space.html)))
            {
                if (stretch)
                {
                    stretch = false;
                }
                else
                {
                    stretch = true;
                }
            }
        }  
      
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
            if (stretch)
            {
                [GL.Viewport](GL.Viewport.html)(new [Rect](Rect.html)(0, 0, [Screen.width](Screen-width.html), [Screen.height](Screen-height.html)));
            }
            else
            {
                [GL.Viewport](GL.Viewport.html)(new [Rect](Rect.html)(0, 0, [Screen.width](Screen-width.html) / 2, [Screen.height](Screen-height.html)));
            }
            [GL.Color](GL.Color.html)([Color.red](Color-red.html));
            [GL.Begin](GL.Begin.html)([GL.QUADS](GL.QUADS.html));
            [GL.Vertex3](GL.Vertex3.html)(0, 0, 0);
            [GL.Vertex3](GL.Vertex3.html)(0, [Screen.height](Screen-height.html), 0);
            [GL.Vertex3](GL.Vertex3.html)([Screen.width](Screen-width.html), [Screen.height](Screen-height.html), 0);
            [GL.Vertex3](GL.Vertex3.html)([Screen.width](Screen-width.html), 0, 0);
            [GL.Color](GL.Color.html)([Color.yellow](Color-yellow.html));
            [GL.End](GL.End.html)();
            [GL.Begin](GL.Begin.html)([GL.TRIANGLES](GL.TRIANGLES.html));
            [GL.Vertex3](GL.Vertex3.html)([Screen.width](Screen-width.html) / 2, [Screen.height](Screen-height.html) / 4, 1);
            [GL.Vertex3](GL.Vertex3.html)([Screen.width](Screen-width.html) / 4, [Screen.height](Screen-height.html) / 2, 1);
            [GL.Vertex3](GL.Vertex3.html)([Screen.width](Screen-width.html) - [Screen.width](Screen-width.html) / 4, [Screen.height](Screen-height.html) / 2, 1);
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

