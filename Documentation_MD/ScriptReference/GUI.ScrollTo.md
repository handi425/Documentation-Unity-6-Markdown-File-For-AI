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

#  [GUI](GUI.html).ScrollTo

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

public static void ScrollTo([Rect](Rect.html) position);

### Description

Scrolls all enclosing scrollviews so they try to make `position` visible.

    
    
    // Draws a Scroll view with 2 buttons inside.
    // When clicked each button it moves the scroll
    // where the other button is located  
      
    using UnityEngine;
    using System.Collections;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        public [Vector2](Vector2.html) scrollPos = [Vector2.zero](Vector2-zero.html);
        void OnGUI()
        {
            scrollPos = [GUI.BeginScrollView](GUI.BeginScrollView.html)(new [Rect](Rect.html)(10, 10, 100, 50), scrollPos, new [Rect](Rect.html)(0, 0, 220, 10));  
      
            if ([GUI.Button](GUI.Button.html)(new [Rect](Rect.html)(0, 0, 100, 20), "Go Right"))
                [GUI.ScrollTo](GUI.ScrollTo.html)(new [Rect](Rect.html)(120, 0, 100, 20));  
      
            if ([GUI.Button](GUI.Button.html)(new [Rect](Rect.html)(120, 0, 100, 20), "Go Left"))
                [GUI.ScrollTo](GUI.ScrollTo.html)(new [Rect](Rect.html)(0, 0, 100, 20));  
      
            [GUI.EndScrollView](GUI.EndScrollView.html)();
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

