[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UIE-create-ui-document-component.html)
  * [中文](/cn/current/Manual/UIE-create-ui-document-component.html)
  * [日本語](/ja/current/Manual/UIE-create-ui-document-component.html)
  * [한국어](/kr/current/Manual/UIE-create-ui-document-component.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UIE-create-ui-document-component.html)
  * [中文](/cn/current/Manual/UIE-create-ui-document-component.html)
  * [日本語](/ja/current/Manual/UIE-create-ui-document-component.html)
  * [한국어](/kr/current/Manual/UIE-create-ui-document-component.html)

  * [Working in Unity](working-in-unity.html)
  * [User interface (UI)](UIToolkits.html)
  * [UI Toolkit](UIElements.html)
  * [Support for runtime UI](UIE-support-for-runtime-ui.html)
  * [Configure runtime UI](UIE-render-runtime-ui.html)
  * UI Document component

[](UIE-Runtime-Panel-Settings.html)

Panel Settings properties reference

[](UIE-Runtime-Event-System.html)

Runtime UI event system and input handling

# UI Document component

A **UI**(User Interface) Allows a user to interact with your application.
Unity currently supports three UI systems. [More info](UI-system-compare.html)  
See in [Glossary](Glossary.html#UI) Document component references a UXML
document and a Panel Settings asset. It serves as a bridge between the
**Scene** A Scene contains the environments and menus of your game. Think of
each unique Scene file as a unique level. In each Scene, you place your
environments, obstacles, and decorations, essentially designing and building
your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) and a UXML document. The UXML document
specifies the UI structure, while the Panel Settings asset handles rendering.

## Create a UI Document component

To create a UI Document component, do one of the following:

  * To add a UI Document component to an existing GameObject in your scene, select **Component** > **UI Toolkit** > **UI Document**.
  * To create a new GameObject with a preconfigured UI Document component, select **GameObject** > **UI Toolkit** > **UI Document**.

## Connect the UI to a panel

To Connect the UI to a panel, in the ****Inspector** A Unity window that
displays information about the currently selected GameObject, asset or project
settings, allowing you to inspect and edit the values. [More
info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector)** window of the UI Document
component, configure UI Document component.

![UI Document component](../uploads/Main/uitk/ui-document.png) UI Document
component

  * **Panel Settings** : The Panel Settings asset that renders the UI.
  * **Source Asset** : The UXML document that contains the UI to display.
  * **Sort Order** : The rendering order of the UI Document component. The lower the value, the earlier the UI Document component renders.

## Render multiple UXML Documents on the same panel

A panel can display UI from more than one UXML Document component. This allows
you to break complex UIs into smaller, more manageable parts. Each UXML
Document component references a different UXML document and the same Panel
Settings asset.

Each UI Document component has a **Sort Order** property that controls
rendering order. Child UI Document components render on top of their parent UI
Document components. Sibling UI Document components (at the same hierarchy
level) render in ascending order based on their **Sort Order** value. The
lower the **Sort Order** value, the earlier the UI Document component renders.

**Note** : If there are multiple UI document components attached to the same
Panel Settings, all these documents have a common focus navigation context. If
they have distinct Panel Settings, navigation won’t jump automatically from
one to the other even if you arrange them side by side. To make navigation
jump from one to the other, you must set the `focusController` of the Panel
Settings to the `FocusController` of the UI Document component you want to
jump to.

## Lifecycle of UI Document components

Unity loads a UI Document component’s source UXML documents when it calls the
`OnEnable()` method on the component. To ensure the **visual tree** An object
graph, made of lightweight nodes, that holds all the elements in a window or
panel. It defines every UI you build with the UI Toolkit.  
See in [Glossary](Glossary.html#Visualtree) loads correctly, add logic to
interact with the controls inside the `OnEnable()` method. This means your
script must respond to `OnEnable()` and `OnDisable()` to safely reference
**visual elements** A node of a visual tree that instantiates or derives from
the C# [`VisualElement`](../ScriptReference/UIElements.VisualElement.html)
class. You can style the look, define the behaviour, and display it on screen
as part of the UI. [More info](UIE-VisualTree.html)  
See in [Glossary](Glossary.html#Visualelement) from your UXML documents.

A UI Document component clears its contents when it responds to the
`OnEnable()` and `OnDisable()` methods. This approach removes UI elements that
the UI Document won’t reuse soon and effectively clears the associated
resources. Additionally, if a UI Document component isn’t assigned with a
[Panel Settings](UIE-Runtime-Panel-Settings.html) asset, it automatically
clears its contents.

To hide a UI element that’s likely to be reused soon or needs to appear
quickly to avoid an initialization penalty, [set the `display` of the
`UIDocument.rootVisualElement` to `none`](UIE-USS-
SupportedProperties.html#display). You can also use this to hide a UI element
component that’s part of a larger UI hierarchy.

## Additional resources

  * [Create a panel](UIE-create-panel.html)

[](UIE-Runtime-Panel-Settings.html)

Panel Settings properties reference

[](UIE-Runtime-Event-System.html)

Runtime UI event system and input handling

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

