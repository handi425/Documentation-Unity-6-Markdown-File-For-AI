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

#  [GUI](GUI.html).color

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

public static [Color](Color.html) color;

### Description

Applies a global tint to the GUI. The tint affects backgrounds and text
colors.

The tint is applied when Unity draws the content. It multiplies this property
by the current color, and uses the resulting color to draw the content.
**Note:** Because GUI.Color is a multiplier for the current text color, it has
no effect on UI labels when you use the light Unity theme. In the light theme,
the default color for label text is black, which has an RGB value of 0.
Multiplying any GUI.Color value by 0 yields 0, so the label text color does
not change. In the dark theme, the default label text color is white, which
has an RGB value of 1, so whatever color you specify in GUI.color becomes the
new label text color.

    
    
    // Tints all [GUI](GUI.html) drawn elements with yellow.  
      
    using UnityEngine;
    using System.Collections;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        void OnGUI()
        {
            [GUI.color](GUI-color.html) = [Color.yellow](Color-yellow.html);
            [GUI.Label](GUI.Label.html)(new [Rect](Rect.html)(10, 10, 100, 20), "Hello World!");
            [GUI.Box](GUI.Box.html)(new [Rect](Rect.html)(10, 50, 50, 50), "A BOX");
            [GUI.Button](GUI.Button.html)(new [Rect](Rect.html)(10, 110, 70, 30), "A button");
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

