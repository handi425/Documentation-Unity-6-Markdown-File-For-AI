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

#  [GUI](GUI.html).RepeatButton

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

public static bool RepeatButton([Rect](Rect.html) position, string text);

## Declaration

public static bool RepeatButton([Rect](Rect.html) position,
[Texture](Texture.html) image);

## Declaration

public static bool RepeatButton([Rect](Rect.html) position,
[GUIContent](GUIContent.html) content);

## Declaration

public static bool RepeatButton([Rect](Rect.html) position, string text,
[GUIStyle](GUIStyle.html) style);

## Declaration

public static bool RepeatButton([Rect](Rect.html) position,
[Texture](Texture.html) image, [GUIStyle](GUIStyle.html) style);

## Declaration

public static bool RepeatButton([Rect](Rect.html) position,
[GUIContent](GUIContent.html) content, [GUIStyle](GUIStyle.html) style);

### Parameters

position | Rectangle on the screen to use for the button.  
---|---  
text | Text to display on the button.  
image |  [Texture](Texture.html) to display on the button.  
content | Text, image and tooltip for this button.  
style | The style to use. If left out, the `button` style from the current [GUISkin](GUISkin.html) is used.  
  
### Returns

**bool** True when the users clicks the button.

### Description

Make a button that is active as long as the user holds it down.

    
    
    // Draws 2 buttons, one with an image, and other with a text
    // Prints a message when they get clicked.  
      
    // Prints a message when they get clicked.  
      
    using UnityEngine;
    using System.Collections;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        public [Texture](Texture.html) btnTexture;  
      
        void OnGUI()
        {
            if (!btnTexture)
            {
                [Debug.LogError](Debug.LogError.html)("Please assign a texture on the inspector");
                return;
            }  
      
            if ([GUI.RepeatButton](GUI.RepeatButton.html)(new [Rect](Rect.html)(10, 10, 50, 50), btnTexture))
                [Debug.Log](Debug.Log.html)("Clicked the button with an image");  
      
            if ([GUI.RepeatButton](GUI.RepeatButton.html)(new [Rect](Rect.html)(10, 70, 50, 30), "Click"))
                [Debug.Log](Debug.Log.html)("Clicked the button with text");
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

