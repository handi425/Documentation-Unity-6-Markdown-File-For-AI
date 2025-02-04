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

#  [GUILayout](GUILayout.html).BeginScrollView

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

public static [Vector2](Vector2.html) BeginScrollView([Vector2](Vector2.html)
scrollPosition, params GUILayoutOption[] options);

## Declaration

public static [Vector2](Vector2.html) BeginScrollView([Vector2](Vector2.html)
scrollPosition, bool alwaysShowHorizontal, bool alwaysShowVertical, params
GUILayoutOption[] options);

## Declaration

public static [Vector2](Vector2.html) BeginScrollView([Vector2](Vector2.html)
scrollPosition, [GUIStyle](GUIStyle.html) horizontalScrollbar,
[GUIStyle](GUIStyle.html) verticalScrollbar, params GUILayoutOption[]
options);

## Declaration

public static [Vector2](Vector2.html) BeginScrollView([Vector2](Vector2.html)
scrollPosition, [GUIStyle](GUIStyle.html) style);

## Declaration

public static [Vector2](Vector2.html) BeginScrollView([Vector2](Vector2.html)
scrollPosition, [GUIStyle](GUIStyle.html) style, params GUILayoutOption[]
options);

## Declaration

public static [Vector2](Vector2.html) BeginScrollView([Vector2](Vector2.html)
scrollPosition, bool alwaysShowHorizontal, bool alwaysShowVertical,
[GUIStyle](GUIStyle.html) horizontalScrollbar, [GUIStyle](GUIStyle.html)
verticalScrollbar, params GUILayoutOption[] options);

## Declaration

public static [Vector2](Vector2.html) BeginScrollView([Vector2](Vector2.html)
scrollPosition, bool alwaysShowHorizontal, bool alwaysShowVertical,
[GUIStyle](GUIStyle.html) horizontalScrollbar, [GUIStyle](GUIStyle.html)
verticalScrollbar, [GUIStyle](GUIStyle.html) background, params
GUILayoutOption[] options);

### Parameters

scrollPosition | The position to use display.  
---|---  
alwaysShowHorizontal | Optional parameter to always show the horizontal scrollbar. If false or left out, it is only shown when the content inside the ScrollView is wider than the scrollview itself.  
alwaysShowVertical | Optional parameter to always show the vertical scrollbar. If false or left out, it is only shown when content inside the ScrollView is taller than the scrollview itself.  
horizontalScrollbar | Optional [GUIStyle](GUIStyle.html) to use for the horizontal scrollbar. If left out, the `horizontalScrollbar` style from the current [GUISkin](GUISkin.html) is used.  
verticalScrollbar | Optional [GUIStyle](GUIStyle.html) to use for the vertical scrollbar. If left out, the `verticalScrollbar` style from the current [GUISkin](GUISkin.html) is used.  
  
### Returns

**Vector2** The modified scrollPosition. Feed this back into the variable you
pass in, as shown in the example.

### Description

Begin an automatically laid out scrollview.

Automatically laid out scrollviews will take whatever content you have inside
them and display normally. If it doesn't fit, scrollbars will appear. A call
to BeginScrollView must always be matched with a call to EndScrollView.  
  
![](../StaticFiles/ScriptRefImages/GUILayoutScrollView.png)  
_Scroll View in the Game View.._

    
    
    using UnityEngine;  
      
    public class ExampleScript : [MonoBehaviour](MonoBehaviour.html)
    {
        // The variable to control where the scrollview 'looks' into its child elements.
        [Vector2](Vector2.html) scrollPosition;  
      
        // The string to display inside the scrollview. 2 buttons below add & clear this string.
        string longString = "This is a long-ish string";  
      
        void OnGUI()
        {
            // Begin a scroll view. All rects are calculated automatically -
            // it will use up any available screen space and make sure contents flow correctly.
            // This is kept small with the last two parameters to force scrollbars to appear.
            scrollPosition = [GUILayout.BeginScrollView](GUILayout.BeginScrollView.html)(
                scrollPosition, [GUILayout.Width](GUILayout.Width.html)(100), [GUILayout.Height](GUILayout.Height.html)(100));  
      
            // We just add a single label to go inside the scroll view. Note how the
            // scrollbars will work correctly with wordwrap.
            [GUILayout.Label](GUILayout.Label.html)(longString);  
      
            // Add a button to clear the string. This is inside the scroll area, so it
            // will be scrolled as well. Note how the button becomes narrower to make room
            // for the vertical scrollbar
            if ([GUILayout.Button](GUILayout.Button.html)("Clear"))
                longString = "";  
      
            // End the scrollview we began above.
            [GUILayout.EndScrollView](GUILayout.EndScrollView.html)();  
      
            // Now we add a button outside the scrollview - this will be shown below
            // the scrolling area.
            if ([GUILayout.Button](GUILayout.Button.html)("Add More Text"))
                longString += "\nHere is another line";
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

