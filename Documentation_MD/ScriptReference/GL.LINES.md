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

#  [GL](GL.html).LINES

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

public static int LINES;

### Description

Mode for [Begin](GL.Begin.html): draw lines.

Draws lines between each pair of vertices passed. If you pass four vertices,
A, B, C and D, two lines are drawn: one between A and B, and one between C and
D.  
  
To set up the screen for drawing in 2D, use [GL.LoadOrtho](GL.LoadOrtho.html)
or [GL.LoadPixelMatrix](GL.LoadPixelMatrix.html). To set up the screen for
drawing in 3D, use [GL.LoadIdentity](GL.LoadIdentity.html) followed by
[GL.MultMatrix](GL.MultMatrix.html) with the desired transformation matrix.  
  
Additional resources: [GL.Begin](GL.Begin.html), [GL.End](GL.End.html).

    
    
    //Attach this script to a [GameObject](GameObject.html) with a [Camera](Camera.html) component  
      
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        // Draws a line from "startVertex" var to the curent mouse position.
        public [Material](Material.html) mat;
        [Vector3](Vector3.html) startVertex;
        [Vector3](Vector3.html) mousePos;  
      
        void Start()
        {
            startVertex = [Vector3.zero](Vector3-zero.html);
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            mousePos = [Input.mousePosition](Input-mousePosition.html);
            // Press space to update startVertex
            if ([Input.GetKeyDown](Input.GetKeyDown.html)([KeyCode.Space](KeyCode.Space.html)))
            {
                startVertex = new [Vector3](Vector3.html)(mousePos.x / [Screen.width](Screen-width.html), mousePos.y / [Screen.height](Screen-height.html), 0);
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
            [GL.LoadOrtho](GL.LoadOrtho.html)();  
      
            [GL.Begin](GL.Begin.html)([GL.LINES](GL.LINES.html));
            [GL.Color](GL.Color.html)([Color.red](Color-red.html));
            [GL.Vertex](GL.Vertex.html)(startVertex);
            [GL.Vertex](GL.Vertex.html)(new [Vector3](Vector3.html)(mousePos.x / [Screen.width](Screen-width.html), mousePos.y / [Screen.height](Screen-height.html), 0));
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

