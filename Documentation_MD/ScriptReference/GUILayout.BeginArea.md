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

#  [GUILayout](GUILayout.html).BeginArea

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

public static void BeginArea([Rect](Rect.html) screenRect);

## Declaration

public static void BeginArea([Rect](Rect.html) screenRect, string text);

## Declaration

public static void BeginArea([Rect](Rect.html) screenRect,
[Texture](Texture.html) image);

## Declaration

public static void BeginArea([Rect](Rect.html) screenRect,
[GUIContent](GUIContent.html) content);

## Declaration

public static void BeginArea([Rect](Rect.html) screenRect,
[GUIStyle](GUIStyle.html) style);

## Declaration

public static void BeginArea([Rect](Rect.html) screenRect, string text,
[GUIStyle](GUIStyle.html) style);

## Declaration

public static void BeginArea([Rect](Rect.html) screenRect,
[Texture](Texture.html) image, [GUIStyle](GUIStyle.html) style);

## Declaration

public static void BeginArea([Rect](Rect.html) screenRect,
[GUIContent](GUIContent.html) content, [GUIStyle](GUIStyle.html) style);

### Parameters

text | Optional text to display in the area.  
---|---  
image | Optional texture to display in the area.  
content | Optional text, image and tooltip top display for this area.  
style | The style to use. If left out, the empty [GUIStyle](GUIStyle.html) ([GUIStyle.none](GUIStyle-none.html)) is used, giving a transparent background.  
  
### Description

Begin a GUILayout block of GUI controls in a fixed screen area.

By default, any GUI controls made using GUILayout are placed in the top-left
corner of the screen. If you want to place a series of automatically laid out
controls in an arbitrary area, use GUILayout.BeginArea to define a new area
for the automatic layouting system to use.  
  
Additional resources: [EndArea](GUILayout.EndArea.html)  
  
![](../StaticFiles/ScriptRefImages/GUILayoutArea.png)  
_Explained Area of the example._

    
    
    using UnityEngine;  
      
    public class ExampleScript : [MonoBehaviour](MonoBehaviour.html)
    {
        void OnGUI()
        {
            // Starts an area to draw elements
            [GUILayout.BeginArea](GUILayout.BeginArea.html)(new [Rect](Rect.html)(10, 10, 100, 100));
            [GUILayout.Button](GUILayout.Button.html)("Click me");
            [GUILayout.Button](GUILayout.Button.html)("Or me");
            [GUILayout.EndArea](GUILayout.EndArea.html)();
        }
    }
    

This function is very useful when mixing GUILayout code. It must be matched
with a call to EndArea. BeginArea / EndArea cannot be nested.

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

