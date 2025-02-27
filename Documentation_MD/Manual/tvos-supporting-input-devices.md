[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/tvos-supporting-input-devices.html)
  * [中文](/cn/current/Manual/tvos-supporting-input-devices.html)
  * [日本語](/ja/current/Manual/tvos-supporting-input-devices.html)
  * [한국어](/kr/current/Manual/tvos-supporting-input-devices.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/tvos-supporting-input-devices.html)
  * [中文](/cn/current/Manual/tvos-supporting-input-devices.html)
  * [日本語](/ja/current/Manual/tvos-supporting-input-devices.html)
  * [한국어](/kr/current/Manual/tvos-supporting-input-devices.html)

  * [Platform development ](PlatformSpecific.html)
  * [tvOS](tvOS-introducing.html)
  * [Developing for tvOS](tvOS-developing.html)
  * Supporting input devices on tvOS

[](tvOS-developing.html)

Developing for tvOS

[](tvos-setting-up-application-navigation.html)

Setting up app navigation from the Unity UI

# Supporting input devices on tvOS

While tvOS builds on the foundation of iOS, it does create new challenges such
as adapting content to function with tvOS inputs, and for display on a bigger
screen.

There are two main inputs for tvOS:

  * The Apple TV Remote
  * Made For iOS (MFi) controllers

## Apple TV Remote

The Apple TV Remote (Siri Remote) is a multi-purpose input device that works
as a traditional menu navigation controller, app controller, gyroscope,
acceleration sensor, and as a touch gesture device. Unity routes Apple TV
Remote input to corresponding Unity APIs, but performs no other processing on
that input. Your application might need some adjustments to its input scheme
to leverage the Apple TV Remote’s specific input features. For instance, your
application can treat it as a traditional application controller, with one
analog axis and an extra action button, or your application can use the
accelerometer for interactions such as steering. You can experiment with
various schemes when porting an app to tvOS.

## Made for iOS (MFi)

Unity provides Made For iOS (MFi), which is a standardized controller support
for iOS and tvOS. MFi controllers offer out of the box input mappings, and you
can set up custom action mappings from **Edit** > **Project Settings** >
**Input Manager**. For more information, refer to [Handle Game Controller
input](ios-handle-game-controller-input.html) and [Game
Controllers](https://developer.apple.com/design/human-interface-
guidelines/tvos/remote-and-controllers/game-controllers/)A device to control
objects and characters in a game.  
See in [Glossary](Glossary.html#gamecontroller).

Two further wireless MFi controllers can be connected to an Apple TV device,
which effectively turns it into a console. Your application can use the
controllers in the same way as iOS MFi controllers, but you must ensure its
usability with the Apple TV Remote alone. The tvOS system limits the number of
additional controllers to two.

Here are some technical details on accessing specific TV Remote features:

**Feature** | **Description**  
---|---  
**Touch area** | Maps to both [Input.touches](../ScriptReference/Input-touches.html) ([Touch.type](../ScriptReference/Touch-type.html) is set to [Indirect](../ScriptReference/TouchType.Indirect.html) and is ignored by the Unity GUI), and the Joystick Input API (for example, [Input.GetAxis(“Horizontal”)](../ScriptReference/Input.GetAxis.html)).  
**Touch area click** | Maps to button A, which then maps to [joystick button 14](ios-handle-game-controller-input.html#InputMapping)  
**Gyroscope** | Maps to [Input.gyro](../ScriptReference/Input-gyro.html). [Input.gyro.attitude](../ScriptReference/Gyroscope-attitude.html) derives from the gravity vector, and as such it doesn’t rotate around the axis parallel to the gravity vector. The same applies for [Input.gyro.rotationRate](../ScriptReference/Gyroscope-rotationRate.html).  
**Acceleration** | Maps to [Input.acceleration](../ScriptReference/Input-acceleration.html).   
**Note** : [Input.acceleration](../ScriptReference/Input-acceleration.html)
derives from the gyroscope API and might have some instabilities. The tvOS SDK
doesn’t have a dedicated accelerometer API.  
**Pause/Play button** | Maps to button X, which then maps to [joystick button 15](ios-handle-game-controller-input.html#InputMapping)  
**Menu button** | A long press calls the tvOS task switcher. You can’t override this behavior.  
Your app can process short taps one of two ways:  
**a)** Return to the tvOS system home screen, if
[UnityEngine.tvOS.Remote.allowExitToHome](../ScriptReference/tvOS.Remote-
allowExitToHome.html) is true.  
**b)** Let your app respond to taps (which maps to the Pause button/[joystick
button 0](ios-handle-game-controller-input.html#InputMapping) when
[UnityEngine.tvOS.Remote.allowExitToHome](../ScriptReference/tvOS.Remote-
allowExitToHome.html) is false. This is the default behavior.  
Your app should switch between **a)** and **b)** based on its current state:  
\- If the user is currently interacting with the top menu, enable behavior
**a)**.  
\- If the user is interacting with the app in real time, enable behavior
**b)** and call the in-app pause menu when they press this button.  
**Swipe to the edge of the remote** | Generates directional pad (D-pad) up/down/left/right button presses.  
For a list of mappings, refer to [Game Controller input mapping](ios-handle-
game-controller-input.html#InputMapping).  
  
You can control the Apple TV Remote operational modes via a dedicated API as
follows:

  * [UnityEngine.tvOS.Remote.allowExitToHome](../ScriptReference/tvOS.Remote-allowExitToHome.html)
  * [UnityEngine.tvOS.Remote.allowRemoteRotation](../ScriptReference/tvOS.Remote-allowRemoteRotation.html)
  * [UnityEngine.tvOS.Remote.reportAbsoluteDpadValues](../ScriptReference/tvOS.Remote-reportAbsoluteDpadValues.html)
  * [UnityEngine.tvOS.Remote.touchesEnabled](../ScriptReference/tvOS.Remote-touchesEnabled.html)

**Note** : When
[UnityEngine.tvOS.Remote.allowExitToHome](../ScriptReference/tvOS.Remote-
allowExitToHome.html) is false, the Menu button maps to [joystick button
0](ios-handle-game-controller-input.html#InputMapping). This causes a conflict
with the default [Input](class-InputManager.html) window, because it also uses
[joystick button 0](ios-handle-game-controller-input.html#InputMapping) to map
the Submit virtual button. This results in the Menu button triggering actions
on UI elements. To fix this issue, remove or modify the Submit virtual button
bindings in the [Input](class-InputManager.html) window (menu: **Edit** >
**Project Settings** , then select the **Input** category).

[](tvOS-developing.html)

Developing for tvOS

[](tvos-setting-up-application-navigation.html)

Setting up app navigation from the Unity UI

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

