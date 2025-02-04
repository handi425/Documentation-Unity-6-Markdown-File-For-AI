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

#  [GUI](GUI.html).DrawTextureWithTexCoords

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

public static void DrawTextureWithTexCoords([Rect](Rect.html) position,
[Texture](Texture.html) image, [Rect](Rect.html) texCoords);

## Declaration

public static void DrawTextureWithTexCoords([Rect](Rect.html) position,
[Texture](Texture.html) image, [Rect](Rect.html) texCoords, bool alphaBlend);

### Parameters

position | Rectangle on the screen to draw the texture within.  
---|---  
image |  [Texture](Texture.html) to display.  
texCoords | How to scale the image when the aspect ratio of it doesn't fit the aspect ratio to be drawn within.  
alphaBlend | Whether to alpha blend the image on to the display (the default). If false, the picture is drawn on to the display.  
  
### Description

Draw a texture within a rectangle with the given texture coordinates.

Use this function for clipping or tiling the image within the given rectangle.
The second [Rect](Rect.html) `texCoords` describes how the texture is adjusted
to fit the position [Rect](Rect.html). The first rectangle has its size in
pixels provided; the second rectangle is given in a 0.0 to 1.0 range.  
  
Additional resources: [GUI.color](GUI-color.html), [GUI.contentColor](GUI-
contentColor.html).

    
    
    using UnityEngine;  
      
    // Use DrawTextureWithTexCoords() to draw a texture.  The texture is draw on the window
    // inside a given pixel rectangle.  The size of the drawn texture is based on the value
    // of hor.  This ranges from 0.5 to 1.25 so the bottom left half of the texture to a
    // greater than normal value.  
      
    public class ExampleScript : [MonoBehaviour](MonoBehaviour.html)
    {
        public [Texture2D](Texture2D.html) tex;
        private [Rect](Rect.html) rect;
        private float hor;
        private [Rect](Rect.html) hs;
        private [Rect](Rect.html) label;  
      
        void Start()
        {
            float center = [Screen.width](Screen-width.html) / 2.0f;
            rect = new [Rect](Rect.html)(center - 200, 200, 400, 250);
            hs = new [Rect](Rect.html)(center - 200, 125, 400, 30);
            label = new [Rect](Rect.html)(center - 20, 155, 50, 30);
            hor = 0.5f;
        }  
      
        void OnGUI()
        {
            hor = [GUI.HorizontalSlider](GUI.HorizontalSlider.html)(hs, hor, 0.5f, 1.25f);
            [GUI.Label](GUI.Label.html)(label, hor.ToString("F3"));
            [GUI.DrawTextureWithTexCoords](GUI.DrawTextureWithTexCoords.html)(rect, tex, new [Rect](Rect.html)(0.0f, 0.0f, hor, hor));
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

