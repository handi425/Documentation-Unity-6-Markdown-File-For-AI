[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UIB-styling-ui-using-uss-variables.html)
  * [中文](/cn/current/Manual/UIB-styling-ui-using-uss-variables.html)
  * [日本語](/ja/current/Manual/UIB-styling-ui-using-uss-variables.html)
  * [한국어](/kr/current/Manual/UIB-styling-ui-using-uss-variables.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UIB-styling-ui-using-uss-variables.html)
  * [中文](/cn/current/Manual/UIB-styling-ui-using-uss-variables.html)
  * [日本語](/ja/current/Manual/UIB-styling-ui-using-uss-variables.html)
  * [한국어](/kr/current/Manual/UIB-styling-ui-using-uss-variables.html)

  * [Working in Unity](working-in-unity.html)
  * [User interface (UI)](UIToolkits.html)
  * [UI Toolkit](UIElements.html)
  * [UI Builder](UIBuilder.html)
  * Assign USS variables in UI Builder

[](UIB-styling-ui-using-uss-selectors.html)

Style UI with UI Builder

[](UIB-testing-ui.html)

Test UI

# Assign USS variables in UI Builder

[USS variables](UIE-USS-variables.html) define values that you can reuse in
other USS rules. USS variables are primarily used for themes, with the default
Unity themes exposing a long list of standard variables to make your
**UI**(User Interface) Allows a user to interact with your application. Unity
currently supports three UI systems. [More info](UI-system-compare.html)  
See in [Glossary](Glossary.html#UI) more consistent with standard controls.

You can’t create USS variables with UI Builder. You must use a text editor to
create a new USS variable in the USS file.

You can assign a USS variable that’s in the current theme or any assigned
StyleSheets to the current UI Document (UXML) to a style property in UI
Builder. When you work on an Editor UI, make sure to [enable **Editor
Extension Authoring**](UIB-interface-overview.html#enable-editor-extension-
authoring-for-ui-documents-uxml) to see all available Editor variables.

To assign a variable:

  1. In the StyleSheet window, select the selector.

  2. In the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector) window, right-click a style field.

  3. Select **Set Variable**. This converts the style field into a text field.

  4. Enter the name of the USS variable. As you type the name of the variable, a dropdown list displays the available variables.

![USSVariablesSearch](../uploads/Main/UIBuilder/USSVariablesSearch.png)
USSVariablesSearch

You can also select a variable from the dropdown list, and see its current
value and the StyleSheet asset it’s coming from. Pressing **Enter** sets the
variable and reverts the style field back to its original type.

**Tip** : For style fields that are already text fields, you can also assign a
variable by starting to type `--` instead of a number.

You can identify which style fields have a variable assigned by checking if
the field’s label has a chain icon on the left.

![USSVariablesSet](../uploads/Main/UIBuilder/USSVariablesSet.png)
USSVariablesSet

To remove a variable assignment, right-click a style field and select **Remove
Variable**.

**Note** : Any inline styles set on a style property will override the USS
variables.

## Additional resources

  * [UI Builder](UIBuilder.html)

[](UIB-styling-ui-using-uss-selectors.html)

Style UI with UI Builder

[](UIB-testing-ui.html)

Test UI

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

