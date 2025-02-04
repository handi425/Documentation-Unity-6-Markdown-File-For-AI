[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UIE-Command-Events.html)
  * [中文](/cn/current/Manual/UIE-Command-Events.html)
  * [日本語](/ja/current/Manual/UIE-Command-Events.html)
  * [한국어](/kr/current/Manual/UIE-Command-Events.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UIE-Command-Events.html)
  * [中文](/cn/current/Manual/UIE-Command-Events.html)
  * [日本語](/ja/current/Manual/UIE-Command-Events.html)
  * [한국어](/kr/current/Manual/UIE-Command-Events.html)

  * [Working in Unity](working-in-unity.html)
  * [User interface (UI)](UIToolkits.html)
  * [UI Toolkit](UIElements.html)
  * [Control behavior with events](UIE-Events.html)
  * [Event reference](UIE-Events-Reference.html)
  * Command events

[](UIE-Click-Events.html)

Click events

[](UIE-Drag-Events.html)

Drag-and-drop events

# Command events

Command events are sent to allow the Unity Editor to forward top-level menu
actions to the Editor **UI**(User Interface) Allows a user to interact with
your application. Unity currently supports three UI systems. [More info](UI-
system-compare.html)  
See in [Glossary](Glossary.html#UI), as well as their equivalent keyboard
shortcuts.

The following are the available commands:

  * `Copy`
  * `Cut`
  * `Paste`
  * `Delete`
  * `SoftDelete`
  * `Duplicate`
  * `FrameSelected`
  * `FrameSelectedWithLock`
  * `SelectAll`
  * `Find`
  * `FocusProjectWindow`

**Event** | **Description** | **Trickles down** | **Bubbles up** | **Cancellable**  
---|---|---|---|---  
[ValidateCommandEvent](../ScriptReference/UIElements.ValidateCommandEvent.html) | The Editor sends this event when determining whether an element in the panel handles the command. | ✔ | ✔ | ✔  
[ExecuteCommandEvent](../ScriptReference/UIElements.ExecuteCommandEvent.html) | The Editor sends this event when an element in the panel executes a command. | ✔ | ✔ | ✔  
  
## Unique properties

**`target`** : The element with keyboard focus. This value is `null` if no
element has focus.

**`commandName`** : The command to validate or execute.

## Event List

### ValidateCommandEvent

The `ValidateCommandEvent` event asks an EditorWindow if it can execute a
command. For example, the Editor can enable or disable a menu item based on
the results from the validation command event.

To verify if the Editor can execute a command:

  1. Register a callback for `ValidateCommandEvent`.
  2. Test the `commandName` property of the event.
  3. Call the `Event.StopPropogation()` method on the event if the command can be executed.

### ExecuteCommandEvent

The `ExecuteCommandEvent` event asks an Editor Window to execute a command.

Even if this event follows a validation event, it’s best practice to ensure
the action is possible first, independently of any previous validation.

To respond to the command:

  1. Register a callback for `ExecuteCommandEvent`.
  2. Test the `commandName` property of the event.
  3. Call the `Event.StopPropogation()` method on the event before executing the actual logic of the command, so the Editor knows that the comment has been executed.

## Example

The following example uses command events to support copy and paste in a
custom Editor Window. The example displays a list of fruits in a custom Editor
window. Users can use keyboard shortcuts to copy and paste any fruits.

    
    
    using System;
    using System.Collections.Generic;
    using System.Linq;
    using UnityEditor;
    using UnityEngine;
    using UnityEngine.UIElements;
    
    public class CopyPasteExample : EditorWindow
    {
        [MenuItem("Window/UI Toolkit Examples/CopyPasteExample")]
        public static void Show()
        {
            GetWindow<CopyPasteExample>();
        }
    
        readonly List<string> fruits = new ()
        {
            "Banana",
            "Apple",
            "Lime",
            "Orange"
        };
        
        ListView m_ListView;
    
        public void CreateGUI()
        {
            Func<VisualElement> makeItem = () => new Label();
    
            Action<VisualElement, int> bindItem = (e, i) => (e as Label).text = fruits[i];
    
            m_ListView = new ListView();
            m_ListView.makeItem = makeItem;
            m_ListView.bindItem = bindItem;
            m_ListView.itemsSource = fruits;
            m_ListView.selectionType = SelectionType.Single;
            
            m_ListView.RegisterCallback<ValidateCommandEvent>(OnValidateCommand);
            m_ListView.RegisterCallback<ExecuteCommandEvent>(OnExecuteCommand);
            
            rootVisualElement.Add(m_ListView);
        }
    
        void OnExecuteCommand(ExecuteCommandEvent evt)
        {
            if (evt.commandName == "Copy" && m_ListView.selectedIndices.Count() > 0)
            {
                EditorGUIUtility.systemCopyBuffer = fruits[m_ListView.selectedIndex];
                evt.StopPropagation();
            }
            else if (evt.commandName == "Paste" && !string.IsNullOrEmpty(EditorGUIUtility.systemCopyBuffer))
            {
                fruits.Add(EditorGUIUtility.systemCopyBuffer);
                m_ListView.RefreshItems();
                evt.StopPropagation();
            }
        }
    
        void OnValidateCommand(ValidateCommandEvent evt)
        {
            if (evt.commandName == "Copy" && m_ListView.selectedIndices.Count() > 0)
            {
                evt.StopPropagation();
            }
            else if (evt.commandName == "Paste" && !string.IsNullOrEmpty(EditorGUIUtility.systemCopyBuffer))
            {
                evt.StopPropagation();
            }
        }
    }
    

[](UIE-Click-Events.html)

Click events

[](UIE-Drag-Events.html)

Drag-and-drop events

Copyright ©2005-2025 Unity Technologies. All rights reserved. Built from
6000.0.36f1 (02b661dc617c). Built on: 2025-01-14.

[Tutorials](https://learn.unity.com/)[Community
Answers](https://answers.unity3d.com)[Knowledge
Base](https://support.unity3d.com/hc/en-
us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-
store)[Terms of
use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy
Policy](https://unity.com/legal/privacy-
policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share
My Personal Information](https://unity.com/legal/do-not-sell-my-personal-
information)

[Your Privacy Choices (Cookie Settings)](javascript:void\(0\);)

