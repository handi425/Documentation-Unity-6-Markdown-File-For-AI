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

#  [EditorWindow](EditorWindow.html).ShowPopup

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

public void ShowPopup();

### Description

Shows an Editor window using popup-style framing.

This means the window has no frame, and is not draggable. It is intended for
showing something like a popup menu within an existing window.  
  
![](../StaticFiles/ScriptRefImages/ShowPopupEx.png)  
  
Opening a window using this method will not give it the functionality of a
popup window, only the styling. For full popup functionality (eg, auto closing
when the window loses focus), use [PopupWindow](PopupWindow.html).

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);
    using UnityEngine.UIElements;
    
    public class ShowPopupExample : [EditorWindow](EditorWindow.html)
    {
        [[MenuItem](MenuItem.html)("Examples/ShowPopup Example")]
        static void Init()
        {
            ShowPopupExample window = [ScriptableObject.CreateInstance](ScriptableObject.CreateInstance.html)<ShowPopupExample>();
            window.position = new [Rect](Rect.html)([Screen.width](Screen-width.html) / 2, [Screen.height](Screen-height.html) / 2, 250, 150);
            window.ShowPopup();
        }
    
        void CreateGUI()
        {
            var label = new [Label](UIElements.Label.html)("This is an example of [EditorWindow.ShowPopup](EditorWindow.ShowPopup.html)");
            rootVisualElement.Add(label);
    
            var button = new [Button](UIElements.Button.html)();
            button.text = "Agree!";
            button.clicked += () => this.Close();
            rootVisualElement.Add(button);
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

