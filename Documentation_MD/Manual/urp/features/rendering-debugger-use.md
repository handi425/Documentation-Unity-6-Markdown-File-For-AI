[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/features/rendering-debugger-use.html)
  * [中文](/cn/current/Manual/urp/features/rendering-debugger-use.html)
  * [日本語](/ja/current/Manual/urp/features/rendering-debugger-use.html)
  * [한국어](/kr/current/Manual/urp/features/rendering-debugger-use.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/features/rendering-debugger-use.html)
  * [中文](/cn/current/Manual/urp/features/rendering-debugger-use.html)
  * [日本語](/ja/current/Manual/urp/features/rendering-debugger-use.html)
  * [한국어](/kr/current/Manual/urp/features/rendering-debugger-use.html)

  * [Rendering](../../rendering-and-post-processing.html)
  * [Graphics performance and profiling](../../graphics-performance-profiling.html)
  * [Graphics performance and profiling in URP](../../graphics-performance-and-profiling-in-urp.html)
  * [Rendering Debugger in URP](../../urp/features/rendering-debugger.html)
  * Enable the Rendering Debugger in URP

[](../../urp/features/rendering-debugger.html)

Rendering Debugger in URP

[](../../urp/features/rendering-debugger-add-controls.html)

Add controls to the Rendering Debugger in URP

# Enable the Rendering Debugger in URP

The Rendering Debugger window is available in the following modes:

Mode | Platform | Availability | How to Open the Rendering Debugger  
---|---|---|---  
Editor | All | Yes (window in the Editor) | Select **Window > Analysis > Rendering Debugger**  
Play mode | All | Yes (overlay in the Game view) | On a desktop or laptop computer, press **LeftCtrl+Backspace** (**LeftCtrl+Delete** on macOS)  
On a console controller, press L3 and R3 (Left Stick and Right Stick)  
Runtime | Desktop/Laptop | Yes (only in Development builds) | Press **LeftCtrl+Backspace** (**LeftCtrl+Delete** on macOS)  
Runtime | Console | Yes (only in Development builds) | Press L3 and R3 (Left Stick and Right Stick)  
Runtime | Mobile | Yes (only in Development builds) | Use a three-finger double tap  
![The Rendering Debugger overlay in Play
mode.](../../../uploads/urp/rendering-debugger-play-mode.jpg) The Rendering
Debugger overlay in Play mode.

To enable all the sections of the **Rendering Debugger** in your built
application, disable **Strip Debug Variants** in **Project Settings > Graphics
> URP Global Settings**. Otherwise, you can only use the [Display
Stats](rendering-debugger-reference.html#display-stats) section.

To disable the runtime **UI**(User Interface) Allows a user to interact with
your application. Unity currently supports three UI systems. [More
info](../../UI-system-compare.html)  
See in [Glossary](../../Glossary.html#UI), use the
[enableRuntimeUI](https://docs.unity3d.com/Packages/com.unity.render-
pipelines.core@17.0/api/UnityEngine.Rendering.DebugManager.html#UnityEngine_Rendering_DebugManager_enableRuntimeUI)
property.

**Note:** When using the **Rendering Debugger** window in the Development
build, clear the **Strip Debug Variants** check box in **Project Settings >
Graphics > URP Global Settings**.

##  Navigation at runtime

### Keyboard

Action | Control  
---|---  
**Change the current active item** | Use the arrow keys  
**Change the current tab** | Use the Page up and Page down keys (Fn + Up and Fn + Down keys respectively for MacOS)  
**Display the current active item independently of the debug window** | Press the right Shift key  
  
### Xbox Controller

Action | Control  
---|---  
**Change the current active item** | Use the Directional pad (D-Pad)  
**Change the current tab** | Use the Left Bumper and Right Bumper  
**Display the current active item independently of the debug window** | Press the X button  
  
### PlayStation Controller

Action | Control  
---|---  
**Change the current active item** | Use the Directional buttons  
**Change the current tab** | Use the L1 button and R1 button  
**Display the current active item independently of the debug window** | Press the Square button  
  
[](../../urp/features/rendering-debugger.html)

Rendering Debugger in URP

[](../../urp/features/rendering-debugger-add-controls.html)

Add controls to the Rendering Debugger in URP

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

