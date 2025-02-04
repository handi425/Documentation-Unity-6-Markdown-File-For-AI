[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/xr-sdk.html)
  * [中文](/cn/current/Manual/xr-sdk.html)
  * [日本語](/ja/current/Manual/xr-sdk.html)
  * [한국어](/kr/current/Manual/xr-sdk.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/xr-sdk.html)
  * [中文](/cn/current/Manual/xr-sdk.html)
  * [日本語](/ja/current/Manual/xr-sdk.html)
  * [한국어](/kr/current/Manual/xr-sdk.html)

  * [Platform development ](PlatformSpecific.html)
  * [XR](XR.html)
  * Unity XR SDK

[](VRAudioSpatializer.html)

Audio Spatializers

[](xrsdk-provider-setup.html)

Creating an XR provider

# Unity XR SDK

The Unity **XR** An umbrella term encompassing Virtual Reality (VR), Augmented
Reality (AR) and Mixed Reality (MR) applications. Devices supporting these
forms of interactive applications can be referred to as XR devices. [More
info](XR.html)  
See in [Glossary](Glossary.html#XR) SDK is aimed at specialist users who want
to develop their own XR providers that work with Unity. To download XR SDK,
you must sign up for access on [this page](https://create.unity3d.com/vsp-
signup-form).

The XR SDK package allows multiple backends (called “providers”) to implement
a single engine feature (called a “subsystem”) in Unity. User applications can
select and activate providers at runtime.

## Subsystems

A single subsystem consists of:

  * A developer-facing C# interface
  * A native interface that multiple backends (Providers) implement via dynamic libraries
  * Common engine code which handles communicating with the C# interface, the native interface, and the rest of the engine

![Subsystem diagram](../uploads/Main/subsystem.png)

### Subsystem descriptor

A subsystem descriptor is metadata about a subsystem which can be inspected
before loading or initializing a subsystem. This comes from a manifest file
and is accessed via a C# interface. A `Create` method activates the subsystem
and provides an instance of it to the user’s **scripts** A piece of code that
allows you to create your own Components, trigger game events, modify
Component properties over time and respond to user input in any way you like.
[More info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts).

For more information, see the [Runtime discovery and activation of
subsystems](xrsdk-runtime-discovery.html) page.

### Subsystem instance

When `Create` is called on a subsystem descriptor, this creates a subsystem
instance. Scripting code interacts with these instances in order to
communicate with the subsystem. The subsystem itself has its own lifecycle: it
can be started, stopped, and shut down.

## Provider

A provider is the native implementation of a subsystem. One subsystem can have
multiple providers. Some subsystems can allow multiple providers to be active
at a time, but others might be mutually exclusive.

![Provider diagram](../uploads/Main/provider.png) Provider diagram

Providers conform to the [Unity native plug-in interface](native-plugin-
interface.html), with some additional lifecycle support built on top. The
entry point is the `UnityPluginLoad` method. From there, the provider must
register with all subsystems it intends to implement.

    
    
    extern "C" void UNITY_INTERFACE_EXPORT UNITY_INTERFACE_API
    UnityPluginLoad(IUnityInterfaces* unityInterfaces)
    {
        s_XrDisplay = unityInterfaces->Get<IUnityXRDisplayInterface>();
        UnityLifecycleProvider displayLifecycleHandler =
        {
            NULL, // This can be any object you want to be passed as userData to the following functions
            &Lifecycle_Initialize,
            &Lifecycle_Start,
            &Lifecycle_Stop,
            &Lifecycle_Shutdown
        };
        s_XrDisplay->RegisterLifecycleProvider("Provider Plugin Name", "Display0", &displayLifecycleHandler);
    
        // Register with other subsystems...
    }
    

[](VRAudioSpatializer.html)

Audio Spatializers

[](xrsdk-provider-setup.html)

Creating an XR provider

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

