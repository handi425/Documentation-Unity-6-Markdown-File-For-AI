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

#  [GUILayoutUtility](GUILayoutUtility.html).GetRect

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

public static [Rect](Rect.html) GetRect([GUIContent](GUIContent.html) content,
[GUIStyle](GUIStyle.html) style);

## Declaration

public static [Rect](Rect.html) GetRect([GUIContent](GUIContent.html) content,
[GUIStyle](GUIStyle.html) style, params GUILayoutOption[] options);

### Parameters

content | The content to make room for displaying.  
---|---  
style | The [GUIStyle](GUIStyle.html) to layout for.  
options | An optional list of layout options that specify extra layouting properties. Any values passed in here will override settings defined by the `style`.  
Additional resources: [GUILayout.Width](GUILayout.Width.html),
[GUILayout.Height](GUILayout.Height.html),
[GUILayout.MinWidth](GUILayout.MinWidth.html),
[GUILayout.MaxWidth](GUILayout.MaxWidth.html),
[GUILayout.MinHeight](GUILayout.MinHeight.html),
[GUILayout.MaxHeight](GUILayout.MaxHeight.html),
[GUILayout.ExpandWidth](GUILayout.ExpandWidth.html),
[GUILayout.ExpandHeight](GUILayout.ExpandHeight.html).  
  
### Returns

**Rect** A rectangle that is large enough to contain content when rendered in
style.

### Description

Reserve layout space for a rectangle for displaying some contents with a
specific style.

    
    
    using UnityEngine;  
      
    public class ExampleScript : [MonoBehaviour](MonoBehaviour.html)
    {
        // Shows the button rect properties in a label when the mouse is over it
        [GUIContent](GUIContent.html) buttonText = new [GUIContent](GUIContent.html)("some button");
        [GUIStyle](GUIStyle.html) buttonStyle = [GUIStyle.none](GUIStyle-none.html);  
      
        void OnGUI()
        {
            [Rect](Rect.html) rt = [GUILayoutUtility.GetRect](GUILayoutUtility.GetRect.html)(buttonText, buttonStyle);
            if (rt.Contains(Event.current.mousePosition))
            {
                [GUI.Label](GUI.Label.html)(new [Rect](Rect.html)(0, 20, 200, 70), "PosX: " + rt.x + "\nPosY: " + rt.y +
                    "\nWidth: " + rt.width + "\nHeight: " + rt.height);
            }
            [GUI.Button](GUI.Button.html)(rt, buttonText, buttonStyle);
        }
    }
    

* * *

## Declaration

public static [Rect](Rect.html) GetRect(float width, float height);

## Declaration

public static [Rect](Rect.html) GetRect(float width, float height,
[GUIStyle](GUIStyle.html) style);

## Declaration

public static [Rect](Rect.html) GetRect(float width, float height, params
GUILayoutOption[] options);

## Declaration

public static [Rect](Rect.html) GetRect(float width, float height,
[GUIStyle](GUIStyle.html) style, params GUILayoutOption[] options);

### Parameters

width | The width of the area you want.  
---|---  
height | The height of the area you want.  
style | An optional [GUIStyle](GUIStyle.html) to layout for. If specified, the style's `padding` value will be added to your sizes & its `margin` value will be used for spacing.  
options | An optional list of layout options that specify extra layouting properties. Any values passed in here will override settings defined by the `style`.  
Additional resources: [GUILayout.Width](GUILayout.Width.html),
[GUILayout.Height](GUILayout.Height.html),
[GUILayout.MinWidth](GUILayout.MinWidth.html),
[GUILayout.MaxWidth](GUILayout.MaxWidth.html),
[GUILayout.MinHeight](GUILayout.MinHeight.html),
[GUILayout.MaxHeight](GUILayout.MaxHeight.html),
[GUILayout.ExpandWidth](GUILayout.ExpandWidth.html),
[GUILayout.ExpandHeight](GUILayout.ExpandHeight.html).  
  
### Returns

**Rect** The rectangle to put your control in.

### Description

Reserve layout space for a rectangle with a fixed content area.

* * *

## Declaration

public static [Rect](Rect.html) GetRect(float minWidth, float maxWidth, float
minHeight, float maxHeight);

## Declaration

public static [Rect](Rect.html) GetRect(float minWidth, float maxWidth, float
minHeight, float maxHeight, [GUIStyle](GUIStyle.html) style);

## Declaration

public static [Rect](Rect.html) GetRect(float minWidth, float maxWidth, float
minHeight, float maxHeight, params GUILayoutOption[] options);

## Declaration

public static [Rect](Rect.html) GetRect(float minWidth, float maxWidth, float
minHeight, float maxHeight, [GUIStyle](GUIStyle.html) style, params
GUILayoutOption[] options);

### Parameters

minWidth | The minimum width of the area passed back.  
---|---  
maxWidth | The maximum width of the area passed back.  
minHeight | The minimum width of the area passed back.  
maxHeight | The maximum width of the area passed back.  
style | An optional style. If specified, the style's `padding` value will be added to the sizes requested & the style's `margin` values will be used for spacing.  
options | An optional list of layout options that specify extra layouting properties. Any values passed in here will override settings defined by the `style`.  
Additional resources: [GUILayout.Width](GUILayout.Width.html),
[GUILayout.Height](GUILayout.Height.html),
[GUILayout.MinWidth](GUILayout.MinWidth.html),
[GUILayout.MaxWidth](GUILayout.MaxWidth.html),
[GUILayout.MinHeight](GUILayout.MinHeight.html),
[GUILayout.MaxHeight](GUILayout.MaxHeight.html),
[GUILayout.ExpandWidth](GUILayout.ExpandWidth.html),
[GUILayout.ExpandHeight](GUILayout.ExpandHeight.html).  
  
### Returns

**Rect** A rectangle with size between minWidth & maxWidth on both axes.

### Description

Reserve layout space for a flexible rect.

The rectangle's size will be between the min & max values.

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

