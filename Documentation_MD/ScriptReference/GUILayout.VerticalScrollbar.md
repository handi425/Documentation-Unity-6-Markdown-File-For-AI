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

#  [GUILayout](GUILayout.html).VerticalScrollbar

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

public static float VerticalScrollbar(float value, float size, float topValue,
float bottomValue, params GUILayoutOption[] options);

## Declaration

public static float VerticalScrollbar(float value, float size, float topValue,
float bottomValue, [GUIStyle](GUIStyle.html) style, params GUILayoutOption[]
options);

### Parameters

value | The position between min and max.  
---|---  
size | How much can we see?  
topValue | The value at the top end of the scrollbar.  
bottomValue | The value at the bottom end of the scrollbar.  
style | The style to use for the scrollbar background. If left out, the `horizontalScrollbar` style from the current [GUISkin](GUISkin.html) is used.  
options | An optional list of layout options that specify extra layouting properties. Any values passed in here will override settings defined by the `style`.  
  
### Returns

**float** The modified value. This can be changed by the user by dragging the
scrollbar, or clicking the arrows at the end.

### Description

Make a vertical scrollbar.

A scrollbar control returns a float value that represents the position of the
draggable "thumb" withtin the bar. You can use the value to adjust another GUI
element to reflect the scroll position. However, most scrollable views can be
handled more easily using a _scroll view_ control.  
  
![](../StaticFiles/ScriptRefImages/GUILayoutVerticalScrollBar.png)  
_Vertical Scrollbar in the Game View._

    
    
    using UnityEngine;  
      
    public class ExampleScript : [MonoBehaviour](MonoBehaviour.html)
    {
        float vSbarValue;  
      
        void OnGUI()
        {
            vSbarValue = [GUILayout.VerticalScrollbar](GUILayout.VerticalScrollbar.html)(vSbarValue, 1.0f, 10.0f, 0.0f);
        }
    }
    

The styles of the scroll buttons at the end of the bar can be located in the
current skin by adding "upbutton" and "downbutton" to the style name. The name
of the scrollbar thumb (the thing you drag) is found by appending "thumb" to
the style name.

    
    
    using UnityEngine;  
      
    public class ExampleScript : [MonoBehaviour](MonoBehaviour.html)
    {
        float scrollPos = 0.5f;  
      
        // This will use the following style names to determine the size / placement of the buttons
        // MyVerticalScrollbarupbutton    - Name of style used for the up button.
        // MyVerticalScrollbardownbutton - Name of style used for the down button.
        // MyVerticalScrollbarthumb         - Name of style used for the draggable thumb.
        void OnGUI()
        {
            scrollPos = [GUILayout.HorizontalScrollbar](GUILayout.HorizontalScrollbar.html)(scrollPos, 1, 0, 100, "MyVerticalScrollbar");
        }
    }
    

Additional resources: [BeginScrollView](GUILayout.BeginScrollView.html),
[HorizontalScrollbar](GUILayout.HorizontalScrollbar.html).

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

