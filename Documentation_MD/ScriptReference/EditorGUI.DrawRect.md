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

#  [EditorGUI](EditorGUI.html).DrawRect

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

public static void DrawRect([Rect](Rect.html) rect, [Color](Color.html)
color);

### Parameters

rect | The position and size of the rectangle to draw.  
---|---  
color | The color of the rectange.  
  
### Description

Draws a filled rectangle of color at the specified position and size within
the current editor window.

Use this to give blocks of Color to areas you want to highlight in the
Inspector window of a GameObject in the Editor. You can also use them to
simulate statistics in the Editor, for example, an in-Editor health bar.

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    public class EditorGUIDrawRectExample : [EditorWindow](EditorWindow.html)
    {
        //This is the value of the [Slider](UIElements.Slider.html)
        float m_Value = 50;  
      
        [[MenuItem](MenuItem.html)("Example/Draw [Rect](Rect.html)")]
        static void Init()
        {
            var window = (EditorGUIDrawRectExample)GetWindow(typeof(EditorGUIDrawRectExample));
            window.position = new [Rect](Rect.html)(0, 0, 350, 300);
        }  
      
        void OnGUI()
        {
            //This is the [Label](UIElements.Label.html) for the [Slider](UIElements.Slider.html)
            [GUI.Label](GUI.Label.html)(new [Rect](Rect.html)(0, 0, 100, 30), "Rectangle Width");
            //This is the [Slider](UIElements.Slider.html) that changes the size of the Rectangle drawn
            m_Value = [GUI.HorizontalSlider](GUI.HorizontalSlider.html)(new [Rect](Rect.html)(100, 0, 100, 30), m_Value, 1.0f, 250.0f);  
      
            //The rectangle is drawn in the [Editor](Editor.html) (when MyScript is attached) with the width depending on the value of the [Slider](UIElements.Slider.html)
            [EditorGUI.DrawRect](EditorGUI.DrawRect.html)(new [Rect](Rect.html)(50, 50, m_Value, 70), [Color.green](Color-green.html));
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

