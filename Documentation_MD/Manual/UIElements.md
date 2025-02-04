[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UIElements.html)
  * [中文](/cn/current/Manual/UIElements.html)
  * [日本語](/ja/current/Manual/UIElements.html)
  * [한국어](/kr/current/Manual/UIElements.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UIElements.html)
  * [中文](/cn/current/Manual/UIElements.html)
  * [日本語](/ja/current/Manual/UIElements.html)
  * [한국어](/kr/current/Manual/UIElements.html)

  * [Working in Unity](working-in-unity.html)
  * [User interface (UI)](UIToolkits.html)
  * UI Toolkit

[](UI-system-compare.html)

Comparison of UI systems in Unity

[](UIE-simple-ui-toolkit-workflow.html)

Get started with UI Toolkit

# UI Toolkit

UI Toolkit is a collection of features, resources, and tools for developing
user interface (UI). You can use **UI**(User Interface) Allows a user to
interact with your application. Unity currently supports three UI systems.
[More info](UI-system-compare.html)  
See in [Glossary](Glossary.html#UI) Toolkit to develop custom UI and
extensions for the Unity Editor, runtime debugging tools, and runtime UI for
games and applications.

UI Toolkit is inspired by standard web technologies. If you have experience
developing web pages or applications, your knowledge is transferable and the
core concepts are familiar.

**Note** : Unity recommends you to use UI Toolkit for your new UI development
projects. However, Unity UI (uGUI) and IMGUI are appropriate for certain use
cases, and are required to support deprecated projects. For more information,
see the [Comparison of UI systems in Unity](UI-system-compare.html).

## UI system

The core of UI Toolkit is a retained-mode UI system based on recognized web
technologies. It supports stylesheets, and dynamic and contextual event
handling.

The UI system includes the following features:

  * **[Visual tree](UIE-VisualTree.html) An object graph, made of lightweight nodes, that holds all the elements in a window or panel. It defines every UI you build with the UI Toolkit.  
See in [Glossary](Glossary.html#Visualtree):** An object graph, made of
lightweight nodes, that holds all the elements in a window or panel. It
defines every UI you build with the UI Toolkit.

  * **[Controls](UIE-ElementRef.html):** A library of standard UI controls such as buttons, popups, list views, and color pickers. You can use them as is, customize them, or create your own controls.
  * **[Data binding system](UIE-data-binding.html):** A system links properties to the controls that modify their values.
  * **[Layout Engine](UIE-LayoutEngine.html):** A layout system based on the CSS Flexbox model. It positions elements based on layout and styling properties.
  * **[Event System](UIE-Events.html) A way of sending events to objects in the application based on input, be it keyboard, mouse, touch, or custom input. The Event System consists of a few components that work together to send events. [More info](UIE-Runtime-Event-System.html)  
See in [Glossary](Glossary.html#EventSystem):** A system communicates user
interactions to elements, such as input, touch and pointer interactions, drag-
and-drop operations, and other event types. The system includes a dispatcher,
a handler, a synthesizer, and a library of event types.

  * **[UI Renderer](UIE-ui-renderer.html):** A rendering system built directly on top of Unity’s graphics device layer.
  * **[Editor UI support](UIE-support-for-editor-ui.html):** A set of components to create Editor UI.
  * **[Runtime UI Support](UIE-support-for-runtime-ui.html):** A set of components to create runtime UI.

## UI assets

Use the following asset types to build UI similar to how you develop web
applications:

  * **[UXML documents](UIE-UXML.html):** HTML and XML inspired markup language defines the structure of UI and reusable UI templates. Although you can build interfaces directly in C# files, Unity recommends using UXML documents if possible.
  * **[Unity Style Sheets (USS)](UIE-USS.html):** Style sheets apply visual styles and behaviors to UI. They’re similar to Cascading Style Sheets (CSS) used on the web, and support a subset of standard CSS properties. Although you can apply styles directly in C# files, Unity recommends using USS files if possible.

## UI tools and resources

Use the following tools to create and debug your interfaces, and learn how to
use the UI Toolkit:

  * **[UI Debugger](UIE-ui-debugger.html):** A diagnostic tool that resembles a web browser’s debugging view. Use it to explore a hierarchy of elements and get information about its underlying UXML structure and USS styles. You can find it in the Editor under **Window** > **UI Toolkit** > **Debugger**.
  * **[UI Builder](UIBuilder.html):** A UI tool lets you visually create and edit UI Toolkit assets such as UXML and USS files.
  * **UI Samples:** A library of code samples for UI controls that you can view in the Editor under **Window** > **UI Toolkit** > **Samples**.

[](UI-system-compare.html)

Comparison of UI systems in Unity

[](UIE-simple-ui-toolkit-workflow.html)

Get started with UI Toolkit

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

