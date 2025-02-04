[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UIToolkits.html)
  * [中文](/cn/current/Manual/UIToolkits.html)
  * [日本語](/ja/current/Manual/UIToolkits.html)
  * [한국어](/kr/current/Manual/UIToolkits.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UIToolkits.html)
  * [中文](/cn/current/Manual/UIToolkits.html)
  * [日本語](/ja/current/Manual/UIToolkits.html)
  * [한국어](/kr/current/Manual/UIToolkits.html)

  * [Working in Unity](working-in-unity.html)
  * User interface (UI)

[](MobileInput.html)

Mobile device input

[](UI-system-compare.html)

Comparison of UI systems in Unity

# User interface (UI)

Unity provides three **UI**(User Interface) Allows a user to interact with
your application. Unity currently supports three UI systems. [More info](UI-
system-compare.html)  
See in [Glossary](Glossary.html#UI) systems that you can use to create user
interfaces (UI) for the Unity Editor and applications made in the Unity
Editor:

  * UI Toolkit
  * The Unity UI package (uGUI)
  * IMGUI

This page provides an overview of each.

## UI Toolkit

[UI Toolkit](UIElements.html) is the newest UI system in Unity. It’s designed
to optimize performance across platforms, and is based on standard web
technologies. You can use UI Toolkit to create extensions for the Unity
Editor, and to create runtime UI for games and applications.

UI Toolkit includes:

  * A retained-mode UI system that contains the core features and functionality required to create user interfaces.
  * UI Asset types inspired by standard web formats such as HTML, XML, and CSS. Use them to structure and style UI.
  * Tools and resources for learning to use UI Toolkit, and for creating and debugging your interfaces.

Unity intends for UI Toolkit to become the recommended UI system for new UI
development projects, but it is still missing some features found in Unity UI
(uGUI) and IMGUI.

## The Unity UI (uGUI) package

The [Unity User Interface (Unity UI)](com.unity.ugui.html) package (also
called uGUI) is an older, GameObject-based UI system that you can use to
develop runtime UI for games and applications. In Unity UI, you use components
and the Game view to arrange, position, and style the user interface. It
supports advanced rendering and text features.

See the Unity UI package documentation for the
[manual](https://docs.unity3d.com/Packages/com.unity.ugui@latest) and [API
reference](https://docs.unity3d.com/Packages/com.unity.ugui@latest/index.html?subfolder=/api/index.html).

## IMGUI

[Immediate Mode Graphical User Interface](GUIScriptingGuide.html) (IMGUI) is a
code-driven UI Toolkit that uses the `OnGUI` function, and **scripts** A piece
of code that allows you to create your own Components, trigger game events,
modify Component properties over time and respond to user input in any way you
like. [More info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts) that implement it, to draw and manage
user interfaces. You can use IMGUI to create custom **Inspectors** A Unity
window that displays information about the currently selected GameObject,
asset or project settings, allowing you to inspect and edit the values. [More
info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector) for script components, extensions
for the Unity Editor, and in-game debugging displays. It is not recommended
for building runtime UI.

## Choosing a UI system for your project

Unity intends for UI Toolkit to become the recommended UI system for new UI
development projects, but it is still missing some features found in Unity UI
(uGUI) and IMGUI. These older systems are better in certain use cases, and are
required to support legacy projects.

Your choice of UI system for a given project depends on the kind of UI you
plan to develop, and the features you need support for.

For a comparison of the available UI systems, see the [Comparison of UI
systems in Unity](UI-system-compare.html).

[](MobileInput.html)

Mobile device input

[](UI-system-compare.html)

Comparison of UI systems in Unity

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

