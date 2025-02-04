[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UIE-Transitioning-From-UGUI.html)
  * [中文](/cn/current/Manual/UIE-Transitioning-From-UGUI.html)
  * [日本語](/ja/current/Manual/UIE-Transitioning-From-UGUI.html)
  * [한국어](/kr/current/Manual/UIE-Transitioning-From-UGUI.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UIE-Transitioning-From-UGUI.html)
  * [中文](/cn/current/Manual/UIE-Transitioning-From-UGUI.html)
  * [日本語](/ja/current/Manual/UIE-Transitioning-From-UGUI.html)
  * [한국어](/kr/current/Manual/UIE-Transitioning-From-UGUI.html)

  * [Working in Unity](working-in-unity.html)
  * [User interface (UI)](UIToolkits.html)
  * [UI Toolkit](UIElements.html)
  * [Migration guides](UIE-migration-guides.html)
  * Migrate from Unity UI (uGUI) to UI Toolkit

[](UIE-migration-guides.html)

Migration guides

[](UIE-IMGUI-migration.html)

Migrate from Immediate Mode GUI (IMGUI) to UI Toolkit

# Migrate from Unity UI (uGUI) to UI Toolkit

This page guides developers with experience in Unity **UI**(User Interface)
Allows a user to interact with your application. Unity currently supports
three UI systems. [More info](UI-system-compare.html)  
See in [Glossary](Glossary.html#UI) (uGUI) to transition to the new UI Toolkit
system. It explores the similarities and differences between uGUI and the UI
Toolkit.

As uGUI is a runtime-only UI system, this page focuses on runtime UI. UI
Toolkit can create both runtime and Editor UI. This guide applies to both use
cases for UI Toolkit.

## UI hierarchy

Both uGUI and UI Toolkit build and maintain the UI inside a hierarchy tree
structure. In uGUI, all elements in this hierarchy are visible as individual
**GameObjects** The fundamental object in Unity scenes, which can represent
characters, props, scenery, cameras, waypoints, and more. A GameObject’s
functionality is defined by the Components attached to it. [More info](class-
GameObject.html)  
See in [Glossary](Glossary.html#GameObject) in the hierarchy view panel. In UI
Toolkit, **visual elements** A node of a visual tree that instantiates or
derives from the C#
[`VisualElement`](../ScriptReference/UIElements.VisualElement.html) class. You
can style the look, define the behaviour, and display it on screen as part of
the UI. [More info](UIE-VisualTree.html)  
See in [Glossary](Glossary.html#Visualelement) are organized into a [visual
tree](UIE-VisualTree.html)An object graph, made of lightweight nodes, that
holds all the elements in a window or panel. It defines every UI you build
with the UI Toolkit.  
See in [Glossary](Glossary.html#Visualtree). The [visual tree](UIE-
VisualTree.html) isn’t visible in the panel.

To view and debug the UI hierarchy in UI Toolkit, you can use the UI Debugger.
You can find UI Debugger in the Editor toolbar, under **Window > UI Toolkit >
Debugger**.

![UI Debugger](../uploads/Main/UIEDebugger.png) UI Debugger

## Key differences

### Canvas versus UIDocument

The `Canvas` component in uGUI is similar to the `UIDocument` component in UI
Toolkit. Both are MonoBehaviours that attach to GameObjects.

In uGUI, a `Canvas` component sits at the root of the UI tree. It works with
the `Canvas Scaler` component to determine the sort order, rendering, and
scaling mode of the UI underneath.

In UI Toolkit, the `UIDocument` component contains a reference to a
`PanelSettings` object. The `PanelSettings` contains the rendering settings
for the UI, including the scale mode and the sort order. Multiple `UIDocument`
components can point to the same `PanelSettings` object, which optimizes
performance when using multiple UI screens in the same **scene** A Scene
contains the environments and menus of your game. Think of each unique Scene
file as a unique level. In each Scene, you place your environments, obstacles,
and decorations, essentially designing and building your game in pieces. [More
info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene).

![Panel Settings](../uploads/Main/UIEPanelSettings.png) Panel Settings

In uGUI, the UI tree hierarchy sits underneath the GameObject holding the
`Canvas` component. In UI Toolkit, the `UIDocument` component holds a
reference to the root element of the Visual Tree.

The `UIDocument` component also contains a reference to the UXML file that
defines the UI layout from which the Visual Tree is built at runtime. Refer to
Creating UI section for more information.

**Note:** For Editor UI, no `UIDocument` component is needed. You can derive
your custom class from `EditorWindow`, then implement `CreateGUI()`. For a
practical example, refer to the guide on [Creating custom Editor windows](UIE-
HowTo-CreateEditorWindow.html).

## GameObject components vs visual elements

UI Toolkit refers to UI elements as controls or visual elements. Examples of
UI elements are:

  * Controls
  * Buttons
  * Text labels

uGUI builds the UI hierarchy from GameObjects. Adding new UI elements requires
adding new GameObjects to the hierarchy. The individual controls are
implemented as `MonoBehaviour` components.

In UI Toolkit, the [visual tree](UIE-VisualTree.html) is virtual and doesn’t
use GameObjects. You can no longer build or view the UI hierarchy in the
hierarchy view, but it removes the overhead of using a GameObject for each UI
element.

In uGUI, UI elements derive (directly or indirectly) from the `UIBehavior`
base class. Similarly, in UI Toolkit all UI elements derive from a base class
called `VisualElement`. The key difference is the `VisualElement` class
doesn’t derive from `MonoBehaviour`. You can not attach visual elements to
GameObjects.

Working with UI Toolkit controls in the script is similar to working with uGUI
controls.

The following table shows common script interactions with UI controls in uGUI,
and their UI Toolkit counterparts.

**Action** | **uGUI** | **UI Toolkit**  
---|---|---  
Write text into a label | `m_Label.text = "My Text";` | `m_Label.text = "My Text";`  
Read the state of a toggle | `bool isToggleChecked = m_Toggle.isOn;` | `bool isToggleChecked = m_Toggle.value;`  
Assign a callback to a button | `m_Button.onClick.AddListener(MyCallbackFunc);` |  `m_Button.clicked += MyCallbackFunc_1;`  
or  
`m_Button.RegisterCallback<ClickEvent>(MyCallbackFunc_2);`  
  
To learn more about controls and their properties and events, please see the
**[Controls Overview](UIE-Controls.html)** page.

### Access UI elements

In uGUI, there are two ways **scripts** A piece of code that allows you to
create your own Components, trigger game events, modify Component properties
over time and respond to user input in any way you like. [More info](creating-
scripts.html)  
See in [Glossary](Glossary.html#Scripts) can access UI elements:

  * Assigning a reference to the UI components in the Editor.
  * Finding the components in the hierarchy using helper functions such as `GetComponentInChildren<T>()`.

Since there are no GameObject or components in UI Toolkit, you can’t directly
assign references to a control in the Editor. They must be resolved at runtime
using a query function. Instead, access the Visual Tree via the `UIDocument`
component.

`UIDocument` is a `MonoBehaviour`, so you can assign it as a reference and
make it part of a **Prefab** An asset type that allows you to store a
GameObject complete with components and properties. The prefab acts as a
template from which you can create new object instances in the scene. [More
info](Prefabs.html)  
See in [Glossary](Glossary.html#Prefab). The `UIDocument` component holds a
reference to the root visual element. From the root, scripts can find child
elements by type or by name, similar to uGUI.

The table below shows a direct comparison of accessing UI controls in Unity UI
and UI Toolkit

**Action** | **uGUI** | **UI Toolkit**  
---|---|---  
Find UI element by name | `transform.FindChild("childName");` | `rootVisualElement.Query("childName");`  
Find UI element by type | `transform.GetComponentInChildren<Button>();` | `rootVisualElement.Query<Button>();`  
Direct assignment of a reference in Editor | Possible | Not possible  
  
## Create UI

One of the biggest differences between uGUI and UI Toolkit is the creation of
user interfaces.

Both uGUI and UI Toolkit allow you to visually build the UI and preview it in
the Editor. In uGUI, the UI is then saved inside a Prefab, along with any
logic scripts attached to individual UI controls.

In UI Toolkit, The UI layout is created in UI Builder, then saved as one or
multiple UXML files. At runtime, `UIDocument` components load the UXML files
that the Visual Tree assembles in memory.

For a method similar to uGUI, you can create UI controls directly from a
script, then add them to a Visual Tree at runtime.

### Prefabs

uGUI uses GameObjects for individual UI controls and Prefabs that both contain
visuals and logic. UI Toolkit takes a different approach to re-usability, as
it separates logic and layout. You can create reusable UI components through
UXML and custom controls.

To create a similar template to a Prefab in UI Toolkit:

  1. Create a UXML file for the partial UI element.
  2. Create a GameObject with a `UIDocument` component.
  3. Reference the UXML file in the GameObject.
  4. Add a script to handle the UI component logic to the same GameObject.
  5. Save the GameObject as a Prefab.

### UI layout

Arranging individual UI elements on screen in uGUI is a manual process. By
default, UI controls are free floating and are only affected by their direct
parent. Other UI controls under the same parent don’t affect their siblings
positions or sizes. Pivots and anchors control the position and size of an
element.

The UI Toolkit layout system is influenced by web design, and based on
automatic layout generation. The automatic layout system affects all elements
by default, and an element’s size and position will affect other elements
under the same parent.

The default behavior in UI Toolkit is comparable to placing all elements
inside a `VerticalLayoutGroup` in uGUI, and adding a `LayoutElement` component
to each.

You can disable automatic layout generation by changing the
[IStyle](../ScriptReference/UIElements.IStyle.html) `position` property of the
visual element. All visual elements have this property. See [Visual Tree](UIE-
VisualTree.html) for a code sample.

UI Toolkit has no direct equivalents for anchoring and pivots of UI elements,
due to the fundamental layout differences compared to uGUI.

The size and position of an element is controlled by the layout engine. For
more information, see [Layout Engine](UIE-LayoutEngine.html) and [Coordinate
and position systems](UIE-coordinate-and-position-system.html).

### Rendering order

In uGUI, the order of the GameObjects in the hierarchy determines the
rendering order. Objects further down in the hierarchy render last and appear
on top. In a scene with multiple Canvases, the `Sort Order` on the root
`Canvas` component determines the render order of the individual UI trees.

The render order in a [visual tree](UIE-VisualTree.html) in UI Toolkit
operates the same way. Parent elements render before their children, and
children render from the first to the last, so that the last appears on top.
In a scene with multiple UI Documents, the render order is determined by the
`Sort Order` setting on the root `UIDocument` component.

To change the rendering order of an element in uGUI, such as making an element
appear on top, you can call the sibling functions on the `Transform` component
of the GameObject. The `VisualElement` class offers comparable functions to
control the rendering order. As all UI Toolkit controls derive from this
class, all controls have access to this function.

The table below shows the uGUI functions to control render order and the
equivalent functions in UI Toolkit:

**Action** | **uGUI** | **UI Toolkit**  
---|---|---  
Make element render underneath all other siblings | `transform.SetAsFirstSibling();` | `myVisualElement.SendToBack();`  
Make element render on top of all other siblings | `transform.SetAsLastSibling();` | `myVisualElement.BringToFront();`  
Manually control the element’s render order relative to its siblings | `transform.SetSiblingIndex(newIndex);` |  `myVisualElement.PlaceBehind(sibling);`  
`myVisualElement.PlaceInFront(sibling);`  
  
## Events

Just like in uGUI, user interactions in UI Toolkit trigger events. The code
can subscribe to receive a callback on events, such as pressing a button or
moving a slider.

In uGUI, all UI elements are based on MonoBehaviour, and can expose their
events in the Editor. This allows to set up logic with other GameObjects, for
example to hide or show other UI elements, or to assign callback functions.

![uGUI Button OnClick Inspector](../uploads/Main/uie-uGUI-button-callback.png)
uGUI Button OnClick Inspector

In UI Toolkit, logic and UI layout are stored separately. Callbacks can no
longer be set up directly on GameObjects or stored in Prefabs. You must set up
all callbacks at runtime, and handle them via scripting.

    
    
    Button playButton = new Button("Play");
    playButton.RegisterCallback<ClickEvent>(OnPlayButtonPressed);
    ...
    private void OnPlayButtonPressed(ClickEvent evt)
    {
      // Handle button press
    }
    

The event dispatching system in UI Toolkit differs from events in uGUI.
Depending on the event type, events aren’t just sent to the target UI control,
but also to all the parent controls.

To learn more about this, see [Dispatch events](UIE-Events-Dispatching.html).

## Use uGUI and UI Toolkit in the same project

It’s possible that you use uGUI and UI Toolkit in the same project.

In its current version, UI Toolkit doesn’t support 3D world space picking and
rendering. You should make your entire game menu with UI Toolkit, and make
your [3D world
space](https://docs.unity3d.com/Packages/com.unity.ugui@1.0/manual/HOWTO-
UIWorldSpace.html) with uGUI.

You can also make your entire project with uGUI and only make some menu items
with UI Toolkit.

You can use either UI Toolkit or uGUI for any item that doesn’t interact
outside of its own boundaries. For example, for a runtime UI, you can use uGUI
to create on-screen buttons, such as the joystick for mobile, and use UI
Toolkit to create a modal window.

However, advanced interactions between mixed UI don’t work:

  * You can’t only use a keyboard to navigate freely between focused element in UI Toolkit and a uGUI selected object. To navigate, you must use C# scripts to register events on the boundary elements, and manually select or focus the next element from the other domain.
  * You can’t embed uGUI inside a UI Toolkit hierarchy or UI Toolkit in a uGUI hierarchy. You can use a `RenderTexture` to draw, but the events won’t catch up.
  * Styling and event conventions in UI Toolkit are different from uGUI. It is difficult to make a project that has a UI that feels unified if you use a scattered mixture of uGUI and UI Tookit.

## Additional resources

  * [Get started with UI Toolkit](UIE-simple-ui-toolkit-workflow.html)
  * [UXML](UIE-UXML.html)
  * [Unity style sheets (USS)](UIE-USS.html)
  * [Examples](UIE-examples.html)

[](UIE-migration-guides.html)

Migration guides

[](UIE-IMGUI-migration.html)

Migrate from Immediate Mode GUI (IMGUI) to UI Toolkit

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

