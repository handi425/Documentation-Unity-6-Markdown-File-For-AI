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

#  [EditorWindow](EditorWindow.html).wantsMouseMove

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

public bool wantsMouseMove;

### Description

Checks whether MouseMove events are received in the GUI in this Editor window.

  
  
![](../StaticFiles/ScriptRefImages/WantsMouseMoveEx.png)  
_Editor Window that detects mouse moves when the toggle button is activated
and the mouse is over the window._

    
    
    // [Editor](Editor.html) Script that shows the mouse movement events captured.
    // "Mouse [Position](UIElements.Position.html)" shows where the mouse is outside of the window.
    
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;
    using System.Collections;
    using UnityEngine.UIElements;
    
    public class PointerMove : [EditorWindow](EditorWindow.html)
    {
        [[MenuItem](MenuItem.html)("Examples/Mouse Move Example")]
        static void InitWindow()
        {
            PointerMove window = (PointerMove)GetWindowWithRect(typeof(PointerMove), new [Rect](Rect.html)(0, 0, 300, 100));
            window.Show();
        }
    
        [Label](UIElements.Label.html) m_PointerPosition;
    
        void CreateGUI()
        {
            rootVisualElement.pickingMode = [PickingMode.Position](UIElements.PickingMode.Position.html);
    
            // Create a toggle button that toggles the value of wantsMouseMove
            var toggle = new [Toggle](UIElements.Toggle.html)
            {
                text = "Receive Movement"
            };
            wantsMouseMove = toggle.value;
            rootVisualElement.Add(toggle);
    
            m_PointerPosition = new [Label](UIElements.Label.html)();
            rootVisualElement.Add(m_PointerPosition);
            
            toggle.RegisterValueChangedCallback((evt) =>
            {
                if (evt.newValue)
                    rootVisualElement.RegisterCallback<[PointerMoveEvent](UIElements.PointerMoveEvent.html)>(LogPointerMoved);
                else
                    rootVisualElement.UnregisterCallback<[PointerMoveEvent](UIElements.PointerMoveEvent.html)>(LogPointerMoved);
            });
        }
    
        void LogPointerMoved([PointerMoveEvent](UIElements.PointerMoveEvent.html) evt)
        {
            m_PointerPosition.text = $"Pointer [Position](UIElements.Position.html): {evt.position}";
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

