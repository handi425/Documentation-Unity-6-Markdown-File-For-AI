[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UIE-Click-Events.html)
  * [中文](/cn/current/Manual/UIE-Click-Events.html)
  * [日本語](/ja/current/Manual/UIE-Click-Events.html)
  * [한국어](/kr/current/Manual/UIE-Click-Events.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UIE-Click-Events.html)
  * [中文](/cn/current/Manual/UIE-Click-Events.html)
  * [日本語](/ja/current/Manual/UIE-Click-Events.html)
  * [한국어](/kr/current/Manual/UIE-Click-Events.html)

  * [Working in Unity](working-in-unity.html)
  * [User interface (UI)](UIToolkits.html)
  * [UI Toolkit](UIElements.html)
  * [Control behavior with events](UIE-Events.html)
  * [Event reference](UIE-Events-Reference.html)
  * Click events

[](UIE-Change-Events.html)

Change events

[](UIE-Command-Events.html)

Command events

# Click events

A [ClickEvent](../ScriptReference/UIElements.ClickEvent.html) occurs when the
user clicks the left mouse button (or the first button on a pointing device)
over a VisualElement.

A click consists of a pointer down event followed by a pointer up event on the
same VisualElement. The pointer is allowed to move between the two events, as
long as the down and up events occur over the same VisualElement.

This event can be used to detect clicks on **visual elements** A node of a
visual tree that instantiates or derives from the C#
[`VisualElement`](../ScriptReference/UIElements.VisualElement.html) class. You
can style the look, define the behaviour, and display it on screen as part of
the UI. [More info](UIE-VisualTree.html)  
See in [Glossary](Glossary.html#Visualelement) that aren’t buttons. For
example, the implementation of the `Toggle` control uses the `ClickEvent` to
show or hide the check mark, and to change the control’s value.

The base class for `ClickEvent` is
[PointerEventBase](../ScriptReference/UIElements.PointerEventBase_1.html). For
more information please also see the documentation on [Pointer Events](UIE-
Pointer-Events.html).

**Event** | **Description** | **Trickles down** | **Bubbles up** | **Cancellable**  
---|---|---|---|---  
[ClickEvent](../ScriptReference/UIElements.ClickEvent.html) | Occurs when the left mouse button is clicked. | ✔ | ✔ | ✔  
  
## Unique properties

The `ClickEvent` has no unique properties, but inherits all properties from
its base class. You can find a list of properties on the [Pointer Events](UIE-
Pointer-Events.html) page.

## Event list

### ClickEvent

Unity sends this event when the left mouse button is clicked over a visual
element.

**`target`** : The element underneath the mouse or pointing device when the
click occurred.

The following example registers for a `ClickEvent` on a visual element:

    
    
    btnClose.RegisterCallback<ClickEvent, VisualElement>(Clicked, asset); // asset is the root visual element that will be closed
    
    private void Clicked(ClickEvent evt, VisualElement root)
    {
      root.ShowVisualElement(false); 
    }
    

## Examples

The following example shows how to react to the ClickEvent on a colored visual
element. When an element is clicked, its color will change to a new, random
color.

To see the example in action, do the following:

  1. Create a new C# script called ClickEventExampleWindow.
  2. Copy the example code into the C# script.
  3. Under **Window > UI Toolkit > Click Event Example**, open the newly created Editor window.

    
    
    using UnityEditor;
    using UnityEngine;
    using UnityEngine.UIElements;
    
    public class ClickEventExampleWindow : EditorWindow
    {
      [MenuItem("Window/UI Toolkit/ClickEventExample")]
      public static void ShowExample()
      {
        var wnd = GetWindow<ClickEventExampleWindow>();
        wnd.titleContent = new GUIContent("Click Event Example");
      }
    
      public void CreateGUI()
      {
        // Create a few different colored boxes
        for (int i = 0; i < 4; i++)
        {
          // Create VisualElement with random background color
          var newBox = new VisualElement() { style = { flexGrow = 1, backgroundColor = GetRandomColor() } };
          rootVisualElement.Add(newBox);
    
          // Register a click event to the visual element to change the background color to a new color
          newBox.RegisterCallback<ClickEvent>(OnBoxClicked);
        }
      }
    
      private void OnBoxClicked(ClickEvent evt)
      {
        // Only perform this action at the target, not in a parent
        if (evt.propagationPhase != PropagationPhase.AtTarget)
          return;
    
        // Assign a random new color
        var targetBox = evt.target as VisualElement;
        targetBox.style.backgroundColor = GetRandomColor();
      }
    
      private Color GetRandomColor()
      {
        return new Color(Random.Range(0, 1f), Random.Range(0, 1f), Random.Range(0, 1f));
      }
    }
    

[](UIE-Change-Events.html)

Change events

[](UIE-Command-Events.html)

Command events

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

