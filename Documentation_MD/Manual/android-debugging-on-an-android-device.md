[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/android-debugging-on-an-android-device.html)
  * [中文](/cn/current/Manual/android-debugging-on-an-android-device.html)
  * [日本語](/ja/current/Manual/android-debugging-on-an-android-device.html)
  * [한국어](/kr/current/Manual/android-debugging-on-an-android-device.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/android-debugging-on-an-android-device.html)
  * [中文](/cn/current/Manual/android-debugging-on-an-android-device.html)
  * [日本語](/ja/current/Manual/android-debugging-on-an-android-device.html)
  * [한국어](/kr/current/Manual/android-debugging-on-an-android-device.html)

  * [Platform development ](PlatformSpecific.html)
  * [Android](android.html)
  * [Developing for Android](android-developing.html)
  * [Testing and debugging](android-testing-and-debugging.html)
  * Debug on Android devices

[](android-testing-and-debugging.html)

Testing and debugging

[](android-symbols.html)

Android symbols

# Debug on Android devices

Unity supports the following ways to debug an application on an Android
device:

  * USB debugging.
  * Both wired and wireless connection through Android Debug Bridge.

## USB debugging

Unity supports USB debugging for Android devices. To use USB debugging, enable
developer options on your device. To do this, refer to Android’s [Configure
developer options](https://developer.android.com/studio/debug/dev-options)
documentation.

Use a USB cable to connect the device to your computer. If you are developing
on a Windows computer, you might need to install a device-specific USB driver.
Refer to the manufacturer’s website for your device for additional
information.

The setup process differs for Windows and macOS. For more information on
connecting your Android device to the SDK, refer to the [Run Your
App](https://developer.android.com/studio/run/device) section of the Android
Developer documentation.

## Android Debug Bridge

Unity supports Android Debug Bridge (ADB) over USB and wireless connection for
Android devices. Wireless connection is useful when you can’t perform USB
debugging, when a controller is plugged into the Android device, or when
debugging **VR** Virtual Reality [More info](VROverview.html)  
See in [Glossary](Glossary.html#VR) applications and you insert the Android
device into the VR Kit.

### Connect via USB

To connect an Android device to Unity through **ADB** An Android Debug Bridge
(ADB). You can use an ADB to deploy an Android package (APK) manually after
building. [More info](https://developer.android.com/studio/command-
line/adb.html)  
See in [Glossary](Glossary.html#ADB) using a USB:

  1. Enable ADB on the device. For information on how to do this, refer to [Set up a device for development](https://developer.android.com/studio/run/device#setting-up).
  2. Use a USB cable to connect your Android device to the machine running Unity.
  3. Navigate to **File** > **Build Profiles**.
  4. Select or add an Android **build profile** A set of customizable configuration settings to use when creating a build for your target platform. [More info](build-profiles.html)  
See in [Glossary](Glossary.html#Buildprofile).

  5. From the **Run Device** build setting, select your device from the available options. If your device doesn’t appear, click **Refresh**.
  6. Select **Build And Run** to build the application and run it on the device.

### Connect wirelessly

To wirelessly connect an Android device to Unity through ADB:

  1. Enable wireless ADB on the device. For information on how to do this, refer to [Connect to your device using Wi-Fi](https://developer.android.com/studio/run/device#wireless).
  2. Find the IP address of your device. The process to do this depends on your device manufacturer.
  3. Navigate to **File** > **Build Profiles**.
  4. Select or create an Android build profile.
  5. From the **Run Device** build setting, select the **< Enter IP>** option.
  6. In the window that opens, enter the IP address and port number of the device. If the device’s port number is `5555`, you don’t need to enter it.
  7. Select **Add**. Once Unity connects to the device, the device name appears in the **Run Device** list and is selected.
  8. Select **Build And Run** to build the application and run it on the device.

## View Android logs

When you run a build of your application on an Android device, Android
collects messages such as stack traces and
[logs](../ScriptReference/Debug.Log.html) from **scripts** A piece of code
that allows you to create your own Components, trigger game events, modify
Component properties over time and respond to user input in any way you like.
[More info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts). To see these messages, Android
provides the [logcat command-line
tool](https://developer.android.com/studio/command-line/logcat). To use this
tool with your Unity application, either:

  * Launch ADB with the `logcat` parameter:  
`$ adb logcat`

  * Use the [Android Logcat](https://docs.unity3d.com/Packages/com.unity.mobile.android-logcat@latest/index.html) package which implements the logcat command-line tool and displays messages from the application in a dedicated window in Unity.

For more information, refer to [Android
Logcat](https://docs.unity3d.com/Packages/com.unity.mobile.android-
logcat@latest/index.html).

[](android-testing-and-debugging.html)

Testing and debugging

[](android-symbols.html)

Android symbols

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

