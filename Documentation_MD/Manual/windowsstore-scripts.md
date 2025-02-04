[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/windowsstore-scripts.html)
  * [中文](/cn/current/Manual/windowsstore-scripts.html)
  * [日本語](/ja/current/Manual/windowsstore-scripts.html)
  * [한국어](/kr/current/Manual/windowsstore-scripts.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/windowsstore-scripts.html)
  * [中文](/cn/current/Manual/windowsstore-scripts.html)
  * [日本語](/ja/current/Manual/windowsstore-scripts.html)
  * [한국어](/kr/current/Manual/windowsstore-scripts.html)

  * [Platform development ](PlatformSpecific.html)
  * [Universal Windows Platform](WindowsStore.html)
  * [Develop for Universal Windows Platform](uwp-developing.html)
  * WinRT API in C# scripts for UWP

[](uwp-debug-generated-cpp.html)

Debug generated C++ code

[](windowsstore-appcallbacks.html)

AppCallbacks class reference

# WinRT API in C# scripts for UWP

You can use the WinRT API directly in Unity **scripts** A piece of code that
allows you to create your own Components, trigger game events, modify
Component properties over time and respond to user input in any way you like.
[More info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts) when you have Windows Runtime support
enabled. For information on how to use the WinRT API and enable Windows
Runtime support, refer to [Windows Runtime support](il2cpp-windows-runtime-
support.html).

You need to meet the following requirements to use WinRT API in your Unity
scripts:

  * Your scripts must be written in C#.
  * Your API compatibility level must be set to .NET 4.6 or .NET Standard 2.0 in the [Player settings](class-PlayerSettings.html)Settings that let you set various player-specific options for the final game built by Unity. [More info](class-PlayerSettings.html)  
See in [Glossary](Glossary.html#PlayerSettings).

  * All the code that uses WinRT API must be under the `ENABLE_WINMD_SUPPORT` directive. This is necessary because the Editor uses Mono, which doesn’t support WinRT APIs.

This code example demonstrates how to get advertising using WinRT API
directly:

    
    
    using UnityEngine;
    public class WinRTAPI : MonoBehaviour
    {
        void Update()
        {
            auto adId = GetAdvertisingId();
            // ...
        }
    
        string GetAdvertisingId()
        {
            #if ENABLE_WINMD_SUPPORT
                return Windows.System.UserProfile.AdvertisingManager.AdvertisingId;
            #else
                return "";
            #endif
        }
    }
    

## Additional resources

  * [Windows Runtime support](il2cpp-windows-runtime-support.html)
  * [Microsoft documentation on WinRT APIs with Unity for HoloLens](https://learn.microsoft.com/en-us/windows/mixed-reality/develop/unity/using-the-windows-namespace-with-unity-apps-for-hololens)

[](uwp-debug-generated-cpp.html)

Debug generated C++ code

[](windowsstore-appcallbacks.html)

AppCallbacks class reference

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

