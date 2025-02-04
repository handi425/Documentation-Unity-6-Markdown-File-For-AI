[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UIE-create-a-conditional-ui.html)
  * [中文](/cn/current/Manual/UIE-create-a-conditional-ui.html)
  * [日本語](/ja/current/Manual/UIE-create-a-conditional-ui.html)
  * [한국어](/kr/current/Manual/UIE-create-a-conditional-ui.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UIE-create-a-conditional-ui.html)
  * [中文](/cn/current/Manual/UIE-create-a-conditional-ui.html)
  * [日本語](/ja/current/Manual/UIE-create-a-conditional-ui.html)
  * [한국어](/kr/current/Manual/UIE-create-a-conditional-ui.html)

  * [Working in Unity](working-in-unity.html)
  * [User interface (UI)](UIToolkits.html)
  * [UI Toolkit](UIElements.html)
  * [Structure UI](UIE-structure-ui.html)
  * [Structure UI examples](UIE-uxml-examples.html)
  * Use Toggle to create a conditional UI

[](UIE-create-a-popup-window.html)

Create a pop-up window

[](UIB-structuring-ui-custom-elements.html)

Create a custom control with two attributes

# Use Toggle to create a conditional UI

This example uses a Toggle to create a conditional **UI**(User Interface)
Allows a user to interact with your application. Unity currently supports
three UI systems. [More info](UI-system-compare.html)  
See in [Glossary](Glossary.html#UI).

## Example overview

The example creates a custom Editor window with two toggles. You can use the
toggles to do the following:

  * Show or hide a label
  * Activate or deactivate a button

You can find the completed files that this example creates in this [GitHub
repository](https://github.com/Unity-Technologies/ui-toolkit-manual-code-
examples/tree/master/ToggleExample).

## Create the example

To create the example:

  1. Create a Unity project with any template.

  2. In the **Project window** A window that shows the contents of your `Assets` folder (Project tab) [More info](ProjectView.html)  
See in [Glossary](Glossary.html#Projectwindow), create a folder named
`Editor`.

  3. In the `Editor` folder, create a C# script file named `ToggleExample` with the following content:
    
        using UnityEngine;
    using UnityEditor;
    using UnityEngine.UIElements;
    namespace Samples.Editor.Controls
    {
        public class ToggleExample : EditorWindow
        {
            private Toggle showToggle;
            private Toggle activateToggle;
            private Label labelToShow;
            private Button buttonToActivate;
            [MenuItem("Window/ToggleExample")]
            public static void OpenWindow()
            {
                var window = GetWindow<ToggleExample>("Controls: Toggle Sample");
                window.minSize = new Vector2(200, 170);
                EditorGUIUtility.PingObject(MonoScript.FromScriptableObject(window));
            }
            public void CreateGUI()
            {
                showToggle = new Toggle("Show label")
                {
                    value = true
                };
                activateToggle = new Toggle("Active button")
                {
                    value = true
                };
                labelToShow = new Label("This label is shown when the above toggle is set to On");
                buttonToActivate = new Button(() => Debug.Log("Button pressed!"))
                {
                    text = "Active if above toggle is On"
                };
                rootVisualElement.Add(showToggle);
                rootVisualElement.Add(labelToShow);
                rootVisualElement.Add(activateToggle);
                rootVisualElement.Add(buttonToActivate);
                showToggle.RegisterValueChangedCallback(evt => labelToShow.visible = evt.newValue);
                activateToggle.RegisterValueChangedCallback(evt => buttonToActivate.SetEnabled(evt.newValue));
            }
        }
    }
    

  4. To try the example, from the menu, select **Window** > **ToggleExample**.

## Additional resources

  * [Toggle](UIE-uxml-element-Toggle.html)A checkbox that allows the user to switch an option on or off. [More info](UIE-uxml-element-Toggle.html)  
See in [Glossary](Glossary.html#Toggle)

[](UIE-create-a-popup-window.html)

Create a pop-up window

[](UIB-structuring-ui-custom-elements.html)

Create a custom control with two attributes

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

