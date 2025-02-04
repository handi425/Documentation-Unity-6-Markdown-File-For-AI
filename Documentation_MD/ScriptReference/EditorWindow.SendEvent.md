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

#  [EditorWindow](EditorWindow.html).SendEvent

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

public bool SendEvent([Event](Event.html) e);

### Description

Sends an Event to a window.

The [SendEvent](EditorWindow.SendEvent.html) public function passes a selected
[Event](Event.html) to a chosen visible window. The [Event](Event.html) can be
found in the [EventType](EventType.html) list.  
  
In the following scripts `SendEventExample` looks up the `ReceiveEventExample`
window. A `Paste` event is then sent over when the button is pressed.

    
    
    // Send an event to another editor window. The second
    // window needs to be visible to receive the event.
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);
    using UnityEngine.UIElements;
    
    public class SendEventExample : [EditorWindow](EditorWindow.html)
    {
        [[MenuItem](MenuItem.html)("Examples/Send [Event](Event.html)")]
        static void Init()
        {
            SendEventExample window =
                [EditorWindow.GetWindow](EditorWindow.GetWindow.html)<SendEventExample>(true, "Send [Event](Event.html) Window");
            window.Show();
        }
    
        void CreateGUI()
        {
            var buttonSendEvent = new [Button](UIElements.Button.html)();
            buttonSendEvent.text = "Send [Event](Event.html)";
            buttonSendEvent.clicked += () =>
            {
                [EditorWindow](EditorWindow.html) win = GetWindow<ReceiveEventExample>();
                if (win)
                    using (var commandEvent = ExecuteCommandEvent.GetPooled([EditorGUIUtility.CommandEvent](EditorGUIUtility.CommandEvent.html)("Paste")))
                    {
                        win.rootVisualElement.SendEvent(commandEvent);
                    }
            };
            rootVisualElement.Add(buttonSendEvent);
        }
    }
    
    
    
    // An [Editor](Editor.html) window that receives sent events.
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);
    using UnityEngine.UIElements;
    
    public class ReceiveEventExample : [EditorWindow](EditorWindow.html)
    {
        [[MenuItem](MenuItem.html)("Examples/Receive [Events](PackageManager.Events.html)")]
        static void Init()
        {
            ReceiveEventExample window =
                [EditorWindow.GetWindow](EditorWindow.GetWindow.html)<ReceiveEventExample>(true, "Receive [Events](PackageManager.Events.html) Window");
            window.Show();
        }
    
        void CreateGUI()
        {
            var button = new [Button](UIElements.Button.html)();
            button.text = "[Button](UIElements.Button.html)";
            rootVisualElement.Add(button);
    
            rootVisualElement.RegisterCallback<[ExecuteCommandEvent](UIElements.ExecuteCommandEvent.html)>(evt =>
            {
                if (evt.commandName == "Paste")
                    button.text = "Paste received";
            }, [TrickleDown.TrickleDown](UIElements.TrickleDown.TrickleDown.html));
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

