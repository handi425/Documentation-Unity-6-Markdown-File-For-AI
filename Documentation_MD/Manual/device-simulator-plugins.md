[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/device-simulator-plugins.html)
  * [中文](/cn/current/Manual/device-simulator-plugins.html)
  * [日本語](/ja/current/Manual/device-simulator-plugins.html)
  * [한국어](/kr/current/Manual/device-simulator-plugins.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/device-simulator-plugins.html)
  * [中文](/cn/current/Manual/device-simulator-plugins.html)
  * [日本語](/ja/current/Manual/device-simulator-plugins.html)
  * [한국어](/kr/current/Manual/device-simulator-plugins.html)

  * [The Unity Editor](unity-editor.html)
  * [Unity's interface](UsingTheEditor.html)
  * [Device Simulator](device-simulator.html)
  * Extending the device simulator

[](device-simulator-adding-a-device.html)

Adding a device

[](Hierarchy.html)

The Hierarchy window

# Extending the device simulator

The Device Simulator supports plugins to extend its functionality and change
the **UI**(User Interface) Allows a user to interact with your application.
Unity currently supports three UI systems. [More info](UI-system-compare.html)  
See in [Glossary](Glossary.html#UI) of the Control Panel in the Simulator
view.

## Creating a plugin

To create a Device Simulator plugin, extend the
[DeviceSimulatorPlugin](../ScriptReference/DeviceSimulation.DeviceSimulatorPlugin.html)
class.

To insert UI into the Device Simulator view, your plugin must:

  * Override the `title` property to return a non-empty string.
  * Override the `OnCreateUI` method to return a [VisualElement](../ScriptReference/UIElements.VisualElement.html) that contains the UI.

If your plugin doesn’t meet these conditions, the Device Simulator
instantiates the plugin but doesn’t display its UI in the Simulator view.

The following example demonstrates how to create a plugin that overrides the
title property and adds UI to the Simulator view.

    
    
    public class TouchInfoPlugin : DeviceSimulatorPlugin
    {
        public override string title => "Touch Info";
        private Label m_TouchCountLabel;
        private Label m_LastTouchEvent;
        private Button m_ResetCountButton;
    
        [SerializeField]
        private int m_TouchCount = 0;
    
        public override void OnCreate()
        {
            deviceSimulator.touchScreenInput += touchEvent =>
            {
                m_TouchCount += 1;
                UpdateTouchCounterText();
                m_LastTouchEvent.text = $"Last touch event: {touchEvent.phase.ToString()}";
            };
        }
    
        public override VisualElement OnCreateUI()
        {
            VisualElement root = new VisualElement();
            
            m_LastTouchEvent = new Label("Last touch event: None");
            
            m_TouchCountLabel = new Label();
            UpdateTouchCounterText();
    
            m_ResetCountButton = new Button {text = "Reset Count" };
            m_ResetCountButton.clicked += () =>
            {
                m_TouchCount = 0;
                UpdateTouchCounterText();
            };
    
            root.Add(m_LastTouchEvent);
            root.Add(m_TouchCountLabel);
            root.Add(m_ResetCountButton);
                
            return root;
        }
    
        private void UpdateTouchCounterText()
        {
            if (m_TouchCount > 0)
                m_TouchCountLabel.text = $"Touches recorded: {m_TouchCount}";
            else
                m_TouchCountLabel.text = "No taps recorded";
        }
    }
    

[](device-simulator-adding-a-device.html)

Adding a device

[](Hierarchy.html)

The Hierarchy window

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

