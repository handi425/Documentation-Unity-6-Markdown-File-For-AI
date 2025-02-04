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

#  [GUI](GUI.html).VerticalScrollbar

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

public static float VerticalScrollbar([Rect](Rect.html) position, float value,
float size, float topValue, float bottomValue);

## Declaration

public static float VerticalScrollbar([Rect](Rect.html) position, float value,
float size, float topValue, float bottomValue, [GUIStyle](GUIStyle.html)
style);

### Parameters

position | Rectangle on the screen to use for the scrollbar.  
---|---  
value | The position between min and max.  
size | How much can we see?  
topValue | The value at the top of the scrollbar.  
bottomValue | The value at the bottom of the scrollbar.  
style | The style to use for the scrollbar background. If left out, the `horizontalScrollbar` style from the current [GUISkin](GUISkin.html) is used.  
  
### Returns

**float** The modified value. This can be changed by the user by dragging the
scrollbar, or clicking the arrows at the end.

### Description

Make a vertical scrollbar. Scrollbars are what you use to scroll through a
document. Most likely, you want to use scrollViews instead.

    
    
    using UnityEngine;
    using System.Collections;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        public float vSbarValue;  
      
        void OnGUI()
        {
            vSbarValue = [GUI.VerticalScrollbar](GUI.VerticalScrollbar.html)(new [Rect](Rect.html)(25, 25, 100, 30), vSbarValue, 1.0F, 10.0F, 0.0F);
        }
    }
    

**Finding extra elements:**  
  
The styles of the buttons at the end of the scrollbar are searched for in the
current skin by adding "upbutton" and "downbutton" to the style name. The name
of the scrollbar thumb (the thing you drag) is found by appending "thumb" to
the style name.

    
    
    // This will use the following style names to determine the size / placement of the buttons
    // MyVertScrollbarupbutton   - Name of style used for the up button.
    // MyVertScrollbardownbutton - Name of style used for the down button.
    // MyVertScrollbarthumb      - Name of style used for the draggable thumb.  
      
    using UnityEngine;
    using System.Collections;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        public float scrollPos = 0.5f;  
      
        void OnGUI()
        {
            scrollPos = [GUI.VerticalScrollbar](GUI.VerticalScrollbar.html)(new [Rect](Rect.html)(0, 0, 100, 20), scrollPos, 1, 0, 100, "Scroll");
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

