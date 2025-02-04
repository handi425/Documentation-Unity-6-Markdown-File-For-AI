[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/xrsdk-pre-init-interface.html)
  * [中文](/cn/current/Manual/xrsdk-pre-init-interface.html)
  * [日本語](/ja/current/Manual/xrsdk-pre-init-interface.html)
  * [한국어](/kr/current/Manual/xrsdk-pre-init-interface.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/xrsdk-pre-init-interface.html)
  * [中文](/cn/current/Manual/xrsdk-pre-init-interface.html)
  * [日本語](/ja/current/Manual/xrsdk-pre-init-interface.html)
  * [한국어](/kr/current/Manual/xrsdk-pre-init-interface.html)

  * [Platform development ](PlatformSpecific.html)
  * [XR](XR.html)
  * [Unity XR SDK](xr-sdk.html)
  * Interfaces
  * XR SDK PreInit interface

[](xrsdk-meshing.html)

XR SDK Meshing subsystem

[](xrsdk-stats.html)

XR SDK Stats interface

# XR SDK PreInit interface

This interface allows you to configure the graphics device before it’s
created. Common use cases include choosing a specific GPU in multi-GPU
scenarios, enabling graphics extensions, and modifying buffer creation.

## Overview

Your provider can export the native symbol `XRSDKPreInit`, which is called
early in runtime initialization, before graphics device creation. It should
fill out a `UnityXRPreInitProvider` structure with the relevant entry points
for providing the engine with information it might need during early
initialization. Some providers need this because the graphics device is
created before providers are able to initialize.

## Discovery

The Unity project build process requires the name of your provider library
before it can call `XRSDKPreInit()` at engine startup. To do this, implement
the `IXRLoaderPreInit.GetPreInitLibraryName` interface on your `XRLoader`:

    
    
    public string GetPreInitLibraryName(BuildTarget buildTarget, BuildTargetGroup buildTargetGroup)
    {
        return "XRSDKMyProviderLibraryName";
    }
    

When Unity starts up, it runs the code above to load the library. Then, Unity
opens that library, looks for the `XRSDKPreInit` export, and calls it. At that
point, `XRSDKPreInit` should register a `UnityXRPreInitProvider`.

## Registration in XRSDKPreInit

Here’s a simple example that registers all of the callbacks that you can use
for early engine initialization:

    
    
    XRSDKPreInit(IUnityInterfaces * interfaces)
    {
        IUnityXRPreInit* preInit = (IUnityXRPreInit*)interfaces->GetInterface(GetUnityInterfaceGUID<IUnityXRPreInit>());
    
        UnityXRPreInitProvider provider = { 0 };
    
        provider.userData = nullptr;
        provider.GetPreInitFlags = GetPreInitFlags;
        provider.GetGraphicsAdapterId = GetGraphicsAdapterId;
        provider.GetVulkanInstanceExtensions = GetVulkanInstanceExtensions;
        provider.GetVulkanDeviceExtensions = GetVulkanDeviceExtensions;
    
        preInit->RegisterPreInitProvider(&provider);
    }
    

Set any callbacks that you don’t need to `nullptr`.

* * *

## Callbacks

### GetPreInitFlags

`GetPreInitFlags` returns a 64-bit bitfield of flags. The following flags are
currently exposed:

  * `kUnityXRPreInitFlagsEGLUsePBuffer` \- On EGL platforms (Android, standalone Meta/Oculus devices, etc.), EGL should be initialized using PBuffers.
  * `kUnityXRPreInitFlagsEGLUseNoErrorContext` \- On EGL platforms, EGL should be initialized with a NO_ERROR context.

Providers shouldn’t set any undefined bits, as they might be used for future
expansion.

### GetGraphicsAdapterId

`GetGraphicsAdapterId` sets the graphics adapter that the Unity runtime
graphics device uses for graphics API initialization. For example, if a user
plugs a headset into a different GPU than the user’s primary display device,
Unity might need to initialize the graphics API that explicitly targets the
secondary GPU.

### GetVulkanDeviceExtensions and GetVulkanInstanceExtensions

`GetVulkanDeviceExtensions` and `GetVulkanInstanceExtensions` are used if the
provider needs Unity to initialize Vulkan with specific extensions for the
device and instance. This is often used for compositor surface sharing. Both
of these return a space-separated string of extensions.

* * *

## Known issues

  * Currently, `GetPreInitLibraryName` is only called on the first XRLoader in the XRManager **prefab** An asset type that allows you to store a GameObject complete with components and properties. The prefab acts as a template from which you can create new object instances in the scene. [More info](Prefabs.html)  
See in [Glossary](Glossary.html#Prefab), so only the first Provider in the
list can provide PreInit entry points at runtime.

  * PreInit requires a native library to expose the entry point during early engine initialization.
  * PreInit doesn’t apply to the Editor at this time.

[](xrsdk-meshing.html)

XR SDK Meshing subsystem

[](xrsdk-stats.html)

XR SDK Stats interface

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

