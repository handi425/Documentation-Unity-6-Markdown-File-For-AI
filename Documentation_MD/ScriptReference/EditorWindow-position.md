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

#  [EditorWindow](EditorWindow.html).position

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

public [Rect](Rect.html) position;

### Description

The desired position of the window in screen space.

Setting this value will undock the window if it is docked.  
  
![](../StaticFiles/ScriptRefImages/EditorWindowPosition.png)  
_Create an undocked editor window with position._

    
    
    // The position of the window is displayed when it is
    // external from Unity.
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);
    using UnityEngine.UIElements;
    
    public class PositionExample : [EditorWindow](EditorWindow.html)
    {
        [Vector2Int](Vector2Int.html) p1;
        bool showButton = true;
    
        [[MenuItem](MenuItem.html)("Examples/Window [Position](UIElements.Position.html)")]
        static void Init()
        {
            GetWindow<PositionExample>("position");
        }
    
        void CreateGUI()
        {
            [Rect](Rect.html) r = position;
            var label = new [Label](UIElements.Label.html)("[Position](UIElements.Position.html): " + r.x + "x" + r.y);
            rootVisualElement.Add(label);
            
            var field = new [Vector2IntField](UIElements.Vector2IntField.html)("Set the position:");
            rootVisualElement.Add(field);
            if (showButton)
            {
                var button = new [Button](UIElements.Button.html)(() => {
                    r.x = field.value.x;
                    r.y = field.value.y;
    
                    position = r;
                });
                button.text = "Accept new position";
                rootVisualElement.Add(button);
            }
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

