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

#  [GUI](GUI.html).Label

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

public static void Label([Rect](Rect.html) position, string text);

## Declaration

public static void Label([Rect](Rect.html) position, [Texture](Texture.html)
image);

## Declaration

public static void Label([Rect](Rect.html) position,
[GUIContent](GUIContent.html) content);

## Declaration

public static void Label([Rect](Rect.html) position, string text,
[GUIStyle](GUIStyle.html) style);

## Declaration

public static void Label([Rect](Rect.html) position, [Texture](Texture.html)
image, [GUIStyle](GUIStyle.html) style);

## Declaration

public static void Label([Rect](Rect.html) position,
[GUIContent](GUIContent.html) content, [GUIStyle](GUIStyle.html) style);

### Parameters

position | Rectangle on the screen to use for the label.  
---|---  
text | Text to display on the label.  
image |  [Texture](Texture.html) to display on the label.  
content | Text, image and tooltip for this label.  
style | The style to use. If left out, the `label` style from the current [GUISkin](GUISkin.html) is used.  
  
### Description

Make a text or texture label on screen.

Labels have no user interaction, do not catch mouse clicks and are always
rendered in normal style. If you want to make a control that responds visually
to user input, use a [Box](GUI.Box.html) control.  
  
Example: Draw the classic Hello World! string:  
  
![](../StaticFiles/ScriptRefImages/GUILabel.png)  
_Text label on the Game View._

    
    
    using UnityEngine;
    using System.Collections;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        void OnGUI()
        {
            [GUI.Label](GUI.Label.html)(new [Rect](Rect.html)(10, 10, 100, 20), "Hello World!");
        }
    }
    

Example: Draw a texture on-screen. Labels are also used to display textures,
instead of a string, simply pass in a texture:  
  
![](../StaticFiles/ScriptRefImages/GUILabelTexture.png)  
_Texture Label._

    
    
    using UnityEngine;
    using System.Collections;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        public [Texture2D](Texture2D.html) textureToDisplay;  
      
        void OnGUI()
        {
            [GUI.Label](GUI.Label.html)(new [Rect](Rect.html)(10, 40, textureToDisplay.width, textureToDisplay.height), textureToDisplay);
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

