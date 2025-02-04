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

#  [EditorWindow](EditorWindow.html).Focus

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

public void Focus();

### Description

Moves keyboard focus to another EditorWindow.

The [Focus](EditorWindow.Focus.html) public method controls which window is
active for use of the keyboard. In the examples below the active EditorWindow
keyboard is changed to a different EditorWindow keyboard. Additional
resources: [focusedWindow](EditorWindow-focusedWindow.html).  
  
  
![](../StaticFiles/ScriptRefImages/Window1.png)  
_Focus one window by pressing the button on other window._

    
    
    // A window that changes state to the second window when
    // the button is pressed.
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);
    using UnityEngine.UIElements;
    
    public class FocusExample1 : [EditorWindow](EditorWindow.html)
    {
        public static FocusExample1 Instance = null;
    
        [[MenuItem](MenuItem.html)("Examples/Focus Example 1")]
        static void Init()
        {
            Instance = GetWindow<FocusExample1>("Focus1");
        }
    
        void CreateGUI()
        {
            var button = new [Button](UIElements.Button.html)(() => {
                if (FocusExample2.Instance)
                    FocusExample2.Instance.Focus();
            });
            button.text = "Focus Window2";
            rootVisualElement.Add(button);    
        }
    }
    
    
    
    // Second window.
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);
    using UnityEngine.UIElements;
    
    public class FocusExample2 : [EditorWindow](EditorWindow.html)
    {
        public static FocusExample2 Instance = null;
    
        [[MenuItem](MenuItem.html)("Examples/Focus Example 2")]
        static void Init()
        {
            Instance = GetWindow<FocusExample2>("Focus2");
        }
        void CreateGUI()
        {
            var button = new [Button](UIElements.Button.html)(() => {
                if (FocusExample1.Instance)
                    FocusExample1.Instance.Focus();
            });
            button.text = "Focus Window1";
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

