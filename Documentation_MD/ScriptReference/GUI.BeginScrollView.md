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

#  [GUI](GUI.html).BeginScrollView

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

public static [Vector2](Vector2.html) BeginScrollView([Rect](Rect.html)
position, [Vector2](Vector2.html) scrollPosition, [Rect](Rect.html) viewRect);

## Declaration

public static [Vector2](Vector2.html) BeginScrollView([Rect](Rect.html)
position, [Vector2](Vector2.html) scrollPosition, [Rect](Rect.html) viewRect,
bool alwaysShowHorizontal, bool alwaysShowVertical);

## Declaration

public static [Vector2](Vector2.html) BeginScrollView([Rect](Rect.html)
position, [Vector2](Vector2.html) scrollPosition, [Rect](Rect.html) viewRect,
[GUIStyle](GUIStyle.html) horizontalScrollbar, [GUIStyle](GUIStyle.html)
verticalScrollbar);

## Declaration

public static [Vector2](Vector2.html) BeginScrollView([Rect](Rect.html)
position, [Vector2](Vector2.html) scrollPosition, [Rect](Rect.html) viewRect,
bool alwaysShowHorizontal, bool alwaysShowVertical, [GUIStyle](GUIStyle.html)
horizontalScrollbar, [GUIStyle](GUIStyle.html) verticalScrollbar);

### Parameters

position | Rectangle on the screen to use for the ScrollView.  
---|---  
scrollPosition | The pixel distance that the view is scrolled in the X and Y directions.  
viewRect | The rectangle used inside the scrollview.  
horizontalScrollbar | Optional [GUIStyle](GUIStyle.html) to use for the horizontal scrollbar. If left out, the `horizontalScrollbar` style from the current [GUISkin](GUISkin.html) is used.  
verticalScrollbar | Optional [GUIStyle](GUIStyle.html) to use for the vertical scrollbar. If left out, the `verticalScrollbar` style from the current [GUISkin](GUISkin.html) is used.  
alwaysShowHorizontal | Optional parameter to always show the horizontal scrollbar. If false or left out, it is only shown when `viewRect` is wider than `position`.  
alwaysShowVertical | Optional parameter to always show the vertical scrollbar. If false or left out, it is only shown when `viewRect` is taller than `position`.  
  
### Returns

**Vector2** The modified scrollPosition. Feed this back into the variable you
pass in, as shown in the example.

### Description

Begin a scrolling view inside your GUI.

ScrollViews let you make a smaller area on-screen look 'into' a much larger
area, using scrollbars placed on the sides of the ScrollView.

    
    
    using UnityEngine;
    using System.Collections;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        // The position on of the scrolling viewport
        public [Vector2](Vector2.html) scrollPosition = [Vector2.zero](Vector2-zero.html);  
      
        void OnGUI()
        {
            // An absolute-positioned example: We make a scrollview that has a really large client
            // rect and put it in a small rect on the screen.
            scrollPosition = [GUI.BeginScrollView](GUI.BeginScrollView.html)(new [Rect](Rect.html)(10, 300, 100, 100), scrollPosition, new [Rect](Rect.html)(0, 0, 220, 200));  
      
            // Make four buttons - one in each corner. The coordinate system is defined
            // by the last parameter to BeginScrollView.
            [GUI.Button](GUI.Button.html)(new [Rect](Rect.html)(0, 0, 100, 20), "Top-left");
            [GUI.Button](GUI.Button.html)(new [Rect](Rect.html)(120, 0, 100, 20), "Top-right");
            [GUI.Button](GUI.Button.html)(new [Rect](Rect.html)(0, 180, 100, 20), "Bottom-left");
            [GUI.Button](GUI.Button.html)(new [Rect](Rect.html)(120, 180, 100, 20), "Bottom-right");  
      
            // End the scroll view that we began above.
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

