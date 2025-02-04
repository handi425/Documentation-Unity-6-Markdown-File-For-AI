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

#  [Graphics](Graphics.html).DrawTexture

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

public static void DrawTexture([Rect](Rect.html) screenRect,
[Texture](Texture.html) texture, [Material](Material.html) mat = null, int
pass = -1);

## Declaration

public static void DrawTexture([Rect](Rect.html) screenRect,
[Texture](Texture.html) texture, int leftBorder, int rightBorder, int
topBorder, int bottomBorder, [Material](Material.html) mat = null, int pass =
-1);

## Declaration

public static void DrawTexture([Rect](Rect.html) screenRect,
[Texture](Texture.html) texture, [Rect](Rect.html) sourceRect, int leftBorder,
int rightBorder, int topBorder, int bottomBorder, [Material](Material.html)
mat = null, int pass = -1);

## Declaration

public static void DrawTexture([Rect](Rect.html) screenRect,
[Texture](Texture.html) texture, [Rect](Rect.html) sourceRect, int leftBorder,
int rightBorder, int topBorder, int bottomBorder, [Color](Color.html) color,
[Material](Material.html) mat = null, int pass = -1);

### Parameters

screenRect | Rectangle on the screen to use for the texture. In pixel coordinates with (0,0) in the upper-left corner.  
---|---  
texture |  [Texture](Texture.html) to draw.  
sourceRect | Region of the texture to use. In normalized coordinates with (0,0) in the bottom-left corner.  
leftBorder | Number of pixels from the left that are not affected by scale.  
rightBorder | Number of pixels from the right that are not affected by scale.  
topBorder | Number of pixels from the top that are not affected by scale.  
bottomBorder | Number of pixels from the bottom that are not affected by scale.  
color |  [Color](Color.html) that modulates the output. The neutral value is (0.5, 0.5, 0.5, 0.5). Set as vertex color for the shader.  
mat | Custom [Material](Material.html) that can be used to draw the texture. Unity passes the texture into the shader as `_MainTex`. If null is passed, a default material with the Internal-GUITexture.shader is used.  
pass | If -1 (default), draws all passes in the material. Otherwise, draws given pass only.  
  
### Description

Draw a texture in screen coordinates.

If you want to draw a texture from inside of OnGUI code, you should only do
that from [EventType.Repaint](EventType.Repaint.html) events. It's probably
better to use [GUI.DrawTexture](GUI.DrawTexture.html) for GUI code.

    
    
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        // Draws a texture on the screen at 10, 10 with 100 width, 100 height.  
      
        [Texture](Texture.html) aTexture;  
      
        void OnGUI()
        {
            if (Event.current.type.Equals([EventType.Repaint](EventType.Repaint.html)))
            {
                [Graphics.DrawTexture](Graphics.DrawTexture.html)(new [Rect](Rect.html)(10, 10, 100, 100), aTexture);
            }
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

