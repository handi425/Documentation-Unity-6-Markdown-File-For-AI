[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/android-API.html)
  * [中文](/cn/current/Manual/android-API.html)
  * [日本語](/ja/current/Manual/android-API.html)
  * [한국어](/kr/current/Manual/android-API.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/android-API.html)
  * [中文](/cn/current/Manual/android-API.html)
  * [日本語](/ja/current/Manual/android-API.html)
  * [한국어](/kr/current/Manual/android-API.html)

  * [Platform development ](PlatformSpecific.html)
  * [Android](android.html)
  * [Developing for Android](android-developing.html)
  * Android mobile scripting

[](android-developing.html)

Developing for Android

[](android-input.html)

Input for Android devices

# Android mobile scripting

For cross-platform Projects, use the `UNITY_ANDROID` define directive to
conditionally compile Android-specific C# code. For more information, refer to
[Platform dependent compilation](platform-dependent-compilation.html).

## Access device-specific features and properties

Applications can access most features of an Android device through the
[Input](../ScriptReference/Input.html) and
[Handheld](../ScriptReference/Handheld.html) classes. For more information,
see:

  * [Mobile device input](MobileInput.html)
  * [Mobile keyboard](MobileKeyboard.html)

### Vibration support

To trigger a vibration, call
[Handheld.Vibrate](../ScriptReference/Handheld.Vibrate.html). Devices without
vibration hardware ignore this call.

### Activity indicator

Mobile operating systems have built-in activity indicators your application
can use during slow operations. For more information, refer to
[Handheld.StartActivityIndicator](../ScriptReference/Handheld.StartActivityIndicator.html).

To access device-specific properties, use these APIs:

**Script** | **Device property**  
---|---  
[SystemInfo.deviceUniqueIdentifier](../ScriptReference/SystemInfo-deviceUniqueIdentifier.html) | Always returns the md5 of `ANDROID_ID`. For more information, see Android developer documentation on [ANDROID_ID](https://developer.android.com/reference/android/provider/Settings.Secure.html#ANDROID_ID).  
[SystemInfo.deviceName](../ScriptReference/SystemInfo-deviceName.html) | Returns the device name. For Android devices, Unity tries to read `device_name` and `bluetooth_name` from secure system settings. If these strings have no values, Unity returns `<unknown>`.  
[SystemInfo.deviceModel](../ScriptReference/SystemInfo-deviceModel.html) | Returns the device model. This often includes the manufacturer name and model number (for example, “LGE Nexus 5 or ”SAMSUNG-SM-G900A").  
[SystemInfo.operatingSystem](../ScriptReference/SystemInfo-operatingSystem.html) | Returns the operating system name and version.  
  
[](android-developing.html)

Developing for Android

[](android-input.html)

Input for Android devices

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

