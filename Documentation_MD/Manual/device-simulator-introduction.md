[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/device-simulator-introduction.html)
  * [中文](/cn/current/Manual/device-simulator-introduction.html)
  * [日本語](/ja/current/Manual/device-simulator-introduction.html)
  * [한국어](/kr/current/Manual/device-simulator-introduction.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/device-simulator-introduction.html)
  * [中文](/cn/current/Manual/device-simulator-introduction.html)
  * [日本語](/ja/current/Manual/device-simulator-introduction.html)
  * [한국어](/kr/current/Manual/device-simulator-introduction.html)

  * [The Unity Editor](unity-editor.html)
  * [Unity's interface](UsingTheEditor.html)
  * [Device Simulator](device-simulator.html)
  * Device Simulator introduction

[](device-simulator.html)

Device Simulator

[](device-simulator-view.html)

The Simulator view

# Device Simulator introduction

The Device Simulator is a Unity Editor feature that simulates how your
application appears and behaves on a mobile device.

The Device Simulator consists of:

  * The Simulator view: Views your application on a simulated mobile device.
  * Simulated classes: Tests code that responds to device-specific behaviors.
  * Device definitions: Describes the device to simulate.
  * Device Simulator plugins: Configures the **UI**(User Interface) Allows a user to interact with your application. Unity currently supports three UI systems. [More info](UI-system-compare.html)  
See in [Glossary](Glossary.html#UI) of the Simulator view.

## Controls in the Simulator view

The Simulator view simulates many common features of mobile devices,
including:

  * Auto-rotation
  * Screen safe area
  * Touch input

## Player Settings

The Device Simulator reacts to the following **Player Settings** Settings that
let you set various player-specific options for the final game built by Unity.
[More info](class-PlayerSettings.html)  
See in [Glossary](Glossary.html#PlayerSettings) in the same way that a real
device does:

  * **Fullscreen Mode**
  * **Resolution Scaling**
  * **Default Orientation**
  * **Graphics API**
  * **Render outside safe area**

## Simulated touch input

If you click on the simulated device screen with the mouse cursor, the device
simulator creates touch events in the active input solution (either the [Input
Manager](class-InputManager.html)Settings where you can define all the
different input axes, buttons and controls for your project. [More
info](class-InputManager.html)  
See in [Glossary](Glossary.html#InputManager), the [Input
System](https://docs.unity3d.com/Packages/com.unity.inputsystem@latest), or
both, depending on your project settings).

**Note** : The Device Simulator only simulates input when the Editor is in
Play mode. The Device Simulator doesn’t support multitouch; it can only
simulate one finger touch.

## Limitations

The main purpose of the Device Simulator is to view the layout of your
application on a target device and test basic interactions. It doesn’t provide
an accurate representation of how your application runs on the device.

The Simulator view does not simulate the following:

  * The performance characteristics of a device, such as a device’s processor speed or available memory.
  * The rendering capabilities of a device.
  * Native plugins that don’t work in the Editor.
  * Platform #define directives for the simulated device, like UNITY_IOS.
  * Gyroscope rotation.

Only one Simulator view can simulate at one time. This is the active Simulator
view.

  * If you have only one Simulator view open and no Game views open, the one Simulator view is active regardless of whether it’s visible or not.
  * If you have multiple Simulator views open and no Game views open, the last Simulator view that had focus is active.
  * If you have a mix of Simulator views and Game views open, if you focus a Game view, Unity disables all simulators and if you focus a Simulator view, the Simulator view remains active while it has focus.

The Device Simulator doesn’t simulate all APIs in the simulated classes. For
more information, see [Simulated classes](device-simulator-simulated-
classes.html).

[](device-simulator.html)

Device Simulator

[](device-simulator-view.html)

The Simulator view

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

