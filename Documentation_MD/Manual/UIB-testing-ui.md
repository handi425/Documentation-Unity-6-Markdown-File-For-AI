[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UIB-testing-ui.html)
  * [中文](/cn/current/Manual/UIB-testing-ui.html)
  * [日本語](/ja/current/Manual/UIB-testing-ui.html)
  * [한국어](/kr/current/Manual/UIB-testing-ui.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UIB-testing-ui.html)
  * [中文](/cn/current/Manual/UIB-testing-ui.html)
  * [日本語](/ja/current/Manual/UIB-testing-ui.html)
  * [한국어](/kr/current/Manual/UIB-testing-ui.html)

  * [Working in Unity](working-in-unity.html)
  * [User interface (UI)](UIToolkits.html)
  * [UI Toolkit](UIElements.html)
  * [UI Builder](UIBuilder.html)
  * Test UI

[](UIB-styling-ui-using-uss-variables.html)

Assign USS variables in UI Builder

[](UIE-structure-ui.html)

Structure UI

# Test UI

You can test your **UI**(User Interface) Allows a user to interact with your
application. Unity currently supports three UI systems. [More info](UI-system-
compare.html)  
See in [Glossary](Glossary.html#UI) inside the UI Builder, and use debugging
tools to investigate styles.

## Test UI in Preview mode

To test your UI inside the UI Builder, directly inside the **Canvas** , you
can enable **Preview** mode, found in the ****Viewport** The user’s visible
area of an app on their screen.  
See in [Glossary](Glossary.html#Viewport)**’s **toolbar** A row of buttons and
basic controls at the top of the Unity Editor that allows you to interact with
the Editor in various ways (e.g. scaling, translation). [More
info](Toolbar.html)  
See in [Glossary](Glossary.html#Toolbar). **Preview** mode removes the UI
Builder-specific picking overlay and handles from the **Canvas**. You can tell
if you have **Preview** mode enabled by looking for an orange border around
the entire **Viewport** :

![PreviewMode](../uploads/Main/UIBuilder/PreviewMode.png) PreviewMode

With **Preview** mode enabled, you can test the following:

  * State-based controls like `Foldout`, which you can click on to expand and see how the rest of the UI reacts.
  * Input fields like `IntegerField`, where you can test input validation.
  * Large containers like `ScrollView`, where you can test scrolling up and down.
  * `:hover` pseudo states to check hover-only styles.

In **Preview** mode, you can still work on your UI. However, **Canvas**
picking and manipulators are turned off in **Preview** mode.

## Debug styles

If you don’t know where a style comes from, you can find the styles for an
element in the **Matching Selectors** section in the UI Builder’s
**Inspector** A Unity window that displays information about the currently
selected GameObject, asset or project settings, allowing you to inspect and
edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector).

  1. In the **Canvas** of the UI Builder, select the element.
  2. In the Inspector window, expand **StyleSheet** > **Matching Selectors**.

![An example of Matching
Selectors](../uploads/Main/UIBuilder/MatchingSelectorsFoldout.png)

The **Matching Selectors** section displays the following:

  * USS selectors from your own style sheets
  * USS selectors from the default Unity theme

**Note** : USS selectors that appear lower in the list always override the
same style properties in higher USS selectors.

If the **Matching Selectors** section doesn’t provide enough information, you
can use the [UI Toolkit Debugger](UIE-ui-debugger.html). The UI Toolkit
Debugger is a tool that you can use to inspect and debug your UI elements in
real-time. It provides a visual representation of your UI hierarchy. You use
it to examine the state and properties of each UI element.

## Additional resources

  * [Style UI with USS](UIE-USS.html)
  * [USS selectors](UIE-USS-Selectors.html)
  * [UI Toolkit Debugger](UIE-ui-debugger.html)

[](UIB-styling-ui-using-uss-variables.html)

Assign USS variables in UI Builder

[](UIE-structure-ui.html)

Structure UI

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

