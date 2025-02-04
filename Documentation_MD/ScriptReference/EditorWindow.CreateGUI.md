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

#  [EditorWindow](EditorWindow.html).CreateGUI()

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

### Description

`CreateGUI` is called when the EditorWindow's rootVisualElement is ready to be
populated.

Use `CreateGUI` to add UI Toolkit UI elements to your window.  
  
When creating a custom Editor window, follow these guidelines:

  * Put code dependent on UXML/USS loading in the [CreateGUI](EditorWindow.CreateGUI.html) method to ensure that all necessary assets are available.
  * Keep the event registration code inside [CreateGUI](EditorWindow.CreateGUI.html) or after [CreateGUI](EditorWindow.CreateGUI.html) is called.

It's important to note that `CreateGUI` might not be called before the first
call to [Update](EditorWindow.Update.html). For more information, refer to
[the order of execution of the Editor window](EditorWindow.html).  
  
For an example on how to create an Editor window to react to user input, refer
to [Create a custom Editor window with C# script](../Manual/UIE-HowTo-
CreateEditorWindow.html).

    
    
    // The window appears in front of the [Editor](Editor.html).
    // The window shows the type of a Unity object the cursor is over.
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);
    using UnityEngine.UIElements;
    
    public class MouseOverWindowExample : [EditorWindow](EditorWindow.html)
    {
        string mouseOver = "Nothing...";
        [Label](UIElements.Label.html) label;
    
        [[MenuItem](MenuItem.html)("Examples/Mouse Over Example")]
        static void Init()
        {
            GetWindow<MouseOverWindowExample>("mouseOver");
        }
    
        void CreateGUI()
        {
            label = new [Label](UIElements.Label.html)($"Mouse over: {mouseOver}");
            rootVisualElement.Add(label);
        }
    
        void [Update](PlayerLoop.Update.html)()
        {
            label.schedule.Execute(() =>
            {
                mouseOver = [EditorWindow.mouseOverWindow](EditorWindow-mouseOverWindow.html) ?
                            EditorWindow.mouseOverWindow.ToString() : "Nothing...";
                label.text = $"Mouse over: {mouseOver}";
            }).Every(10);
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

