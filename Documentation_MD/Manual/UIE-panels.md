[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UIE-panels.html)
  * [中文](/cn/current/Manual/UIE-panels.html)
  * [日本語](/ja/current/Manual/UIE-panels.html)
  * [한국어](/kr/current/Manual/UIE-panels.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UIE-panels.html)
  * [中文](/cn/current/Manual/UIE-panels.html)
  * [日本語](/ja/current/Manual/UIE-panels.html)
  * [한국어](/kr/current/Manual/UIE-panels.html)

  * [Working in Unity](working-in-unity.html)
  * [User interface (UI)](UIToolkits.html)
  * [UI Toolkit](UIElements.html)
  * [Structure UI](UIE-structure-ui.html)
  * [The visual tree](UIE-VisualTree-landing.html)
  * Panels

[](UIE-VisualTree.html)

Introduction to visual elements and the visual tree

[](UIE-draw-order.html)

Draw order

# Panels

The panel is the parent object of a [visual tree](UIE-VisualTree.html)An
object graph, made of lightweight nodes, that holds all the elements in a
window or panel. It defines every UI you build with the UI Toolkit.  
See in [Glossary](Glossary.html#Visualtree). It owns the `rootVisualElement`
but itself isn’t a **visual element** A node of a visual tree that
instantiates or derives from the C#
[`VisualElement`](../ScriptReference/UIElements.VisualElement.html) class. You
can style the look, define the behaviour, and display it on screen as part of
the UI. [More info](UIE-VisualTree.html)  
See in [Glossary](Glossary.html#Visualelement). A visual tree must connect to
a panel for the visual elements inside a tree to render. All panels belong to
either an [Editor Window](../ScriptReference/EditorWindow.html) or a runtime
[UIDocument](../ScriptReference/UIElements.UIDocument.html). The panel also
handles focus control and event dispatching for the visual tree.

Every element in a visual tree holds a direct reference to the panel that
holds the visual tree. To verify the connection of a
[`VisualElement`](../ScriptReference/UIElements.VisualElement.html) to a
panel, you can test the [`panel`](../ScriptReference/UIElements.VisualElement-
panel.html) property of this element. When the visual element isn’t connected,
the test returns `null`.

## Additional resources

  * [Dispatch events](UIE-Events-Dispatching.html)
  * [The visual tree](UIE-VisualTree.html)
  * [The Panel Settings asset](UIE-Runtime-Panel-Settings.html)
  * [Relative and absolute positioning C# example](UIE-relative-absolute-positioning-example.html)

[](UIE-VisualTree.html)

Introduction to visual elements and the visual tree

[](UIE-draw-order.html)

Draw order

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

