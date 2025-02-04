[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/ios-detect-game-controllers.html)
  * [中文](/cn/current/Manual/ios-detect-game-controllers.html)
  * [日本語](/ja/current/Manual/ios-detect-game-controllers.html)
  * [한국어](/kr/current/Manual/ios-detect-game-controllers.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/ios-detect-game-controllers.html)
  * [中文](/cn/current/Manual/ios-detect-game-controllers.html)
  * [日本語](/ja/current/Manual/ios-detect-game-controllers.html)
  * [한국어](/kr/current/Manual/ios-detect-game-controllers.html)

  * [Platform development ](PlatformSpecific.html)
  * [iOS](iphone.html)
  * [Developing for iOS](ios-developing.html)
  * [Input for iOS devices](ios-input.html)
  * [Game Controller support](ios-game-controller-support.html)
  * Detect Game Controllers

[](ios-game-controller-support.html)

Game Controller support

[](ios-handle-game-controller-input.html)

Handle Game Controller input

# Detect Game Controllers

Unity includes the **Game Controller** A device to control objects and
characters in a game.  
See in [Glossary](Glossary.html#gamecontroller) framework in the project only
if a script in the project references
[`Input.GetJoystickNames`](../ScriptReference/Input.GetJoystickNames.html). If
it’s available, Unity iOS Runtime loads the framework dynamically.

To get the list of all available controllers, call
[`Input.GetJoystickNames`](../ScriptReference/Input.GetJoystickNames.html).
You can re-check this list at any time to detect if controllers have been
attached or detached.

You can call this API to detect the type of controller that’s attached. Names
follow the pattern: `[$profile_type,$connection_type] joystick $number by
$model`. `$profile_type` can be either **basic** or **extended** , and
`$connection_type` is either **wired** or **wireless**. When Unity detects at
least one controller, you can either disable on-screen touch controls or amend
them to supplement controller input.

## Example: Detect attached Game Controllers

The following code sample checks to see if any controllers are connected to
the device.

    
    
    using System.Collections;
    using UnityEngine;
    
    public class GameControllers : MonoBehaviour
    {
        private bool connected = false;
    
        IEnumerator CheckForControllers() {
            while (true) {
                var controllers = Input.GetJoystickNames();
    
                if (!connected && controllers.Length > 0) {
                    connected = true;
                    Debug.Log("Connected");
                
                } else if (connected && controllers.Length == 0) {         
                    connected = false;
                    Debug.Log("Disconnected");
                }
    
                yield return new WaitForSeconds(1f);
            }
        }
    
        void Awake() {
            StartCoroutine(CheckForControllers());
        }
    }
    

## Additional resources:

  * [Input class](../ScriptReference/Input.html)

[](ios-game-controller-support.html)

Game Controller support

[](ios-handle-game-controller-input.html)

Handle Game Controller input

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

