[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/xrsdk-provider-setup.html)
  * [中文](/cn/current/Manual/xrsdk-provider-setup.html)
  * [日本語](/ja/current/Manual/xrsdk-provider-setup.html)
  * [한국어](/kr/current/Manual/xrsdk-provider-setup.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/xrsdk-provider-setup.html)
  * [中文](/cn/current/Manual/xrsdk-provider-setup.html)
  * [日本語](/ja/current/Manual/xrsdk-provider-setup.html)
  * [한국어](/kr/current/Manual/xrsdk-provider-setup.html)

  * [Platform development ](PlatformSpecific.html)
  * [XR](XR.html)
  * [Unity XR SDK](xr-sdk.html)
  * Provider setup
  * Creating an XR provider

[](xr-sdk.html)

Unity XR SDK

[](xrsdk-unity-subsystems-manifest-json.html)

UnitySubsystemsManifest.json

# Creating an XR provider

An **XR** An umbrella term encompassing Virtual Reality (VR), Augmented
Reality (AR) and Mixed Reality (MR) applications. Devices supporting these
forms of interactive applications can be referred to as XR devices. [More
info](XR.html)  
See in [Glossary](Glossary.html#XR) provider is part of a Unity project and
minimally consists of a manifest file and one or more native **plug-ins** A
set of code created outside of Unity that creates functionality in Unity.
There are two kinds of plug-ins you can use in Unity: Managed plug-ins
(managed .NET assemblies created with tools like Visual Studio) and Native
plug-ins (platform-specific native code libraries). [More info](./plug-
ins.html)  
See in [Glossary](Glossary.html#Plug-in). It can also include other assets
such as **scripts** A piece of code that allows you to create your own
Components, trigger game events, modify Component properties over time and
respond to user input in any way you like. [More info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts) and images. As long as these are in
your project when you launch the Editor, Unity discovers them.

**Note:** You must relaunch Unity whenever you change a provider’s manifest or
Editor **native plug-in** A platform-specific native code library that is
created outside of Unity for use in Unity. Allows you can access features like
OS calls and third-party code libraries that would otherwise not be available
to Unity. [More info](./plug-ins.html)  
See in [Glossary](Glossary.html#Nativeplug-in).

## File layout

Native plug-ins must be in a subfolder relative to the manifest file,
`UnitySubsystemsManifest.json`, and no more than two folders below the
manifest itself.

## UnitySubsystemsManifest.json

This manifest contains information about your provider, including the
subsystems it offers and the plug-in name. It’s important to note that the
`xreditorsubsystem` keyword should be included in the `package.json` file of
any package that defines subsystems in `UnitySubsystemsManifest.json` and
requires these subsystems to function within the Unity Editor. The presence of
this keyword is essential for ensuring that the Unity Editor recognizes and
properly discovers these subsystems. Without this keyword, subsystems intended
for editor usage may not perform as expected, though this does not impact the
player build process.

For more information, refer to the [UnitySubsystemsManifest.json](xrsdk-unity-
subsystems-manifest-json.html) page.

## Building a provider plug-in

To learn how to build a native plug-in for your targeted platform, refer to
documentation on the [Unity native plug-in interface](native-plugin-
interface.html). After you get your dynamic library into Unity, ensure that
all the options (such as the target platform in the [Plug-in Settings](plug-
in-inspector.html)) are correct.

You need to register a lifecycle handler for the subsystems that you intend to
implement. For example:

    
    
    extern "C" void UNITY_INTERFACE_EXPORT UNITY_INTERFACE_API
    UnityPluginLoad(IUnityInterfaces* unityInterfaces)
    {
      s_XrDisplay = unityInterfaces->Get<IUnityXRDisplayInterface>();
      UnityLifecycleProvider displayLifecycleHandler =
      {
        NULL, // This can be any object you want to pass as userData to the following functions
        &Lifecycle_Initialize,
        &Lifecycle_Start,
        &Lifecycle_Stop,
        &Lifecycle_Shutdown
      };
      s_XrDisplay->RegisterLifecycleProvider("Provider Plugin Name", "Display0", &displayLifecycleHandler);
    
      // Register with other subsystems
    }
    

**Note:** The parameters passed to `RegisterLifecycleProvider` must match the
`name` and `id` fields in your [manifest file](xrsdk-unity-subsystems-
manifest-json.html).

When you call your `Initialize` method at a later point, you get an instance
handle you can use to call methods that take a `UnitySubsystemHandle`.
Example:

    
    
    /// Callback executed when a subsystem should initialize in preparation for becoming active.
    static UnitySubsystemErrorCode UNITY_INTERFACE_API Lifecycle_Initialize(UnitySubsystemHandle handle, void* data)
    {
      // Register for callbacks on the graphics thread.
      UnityXRDisplayGraphicsThreadProvider gfxThreadProvider = { NULL, NULL, &GfxThread_WaitForNextFrameDesc, NULL };
      s_XrDisplay->RegisterProviderForGraphicsThread(handle, &gfxThreadProvider);
    
      return kUnitySubsystemErrorCodeSuccess;
    }
    

The SDK package includes an example project that builds sample plug-ins.

## Loading in Unity

For more information about loading your provider in Unity, refer to the
[Runtime discovery and activation of subsystems](xrsdk-runtime-discovery.html)
page.

[](xr-sdk.html)

Unity XR SDK

[](xrsdk-unity-subsystems-manifest-json.html)

UnitySubsystemsManifest.json

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

