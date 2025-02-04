[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/xrsdk-unity-subsystems-manifest-json.html)
  * [中文](/cn/current/Manual/xrsdk-unity-subsystems-manifest-json.html)
  * [日本語](/ja/current/Manual/xrsdk-unity-subsystems-manifest-json.html)
  * [한국어](/kr/current/Manual/xrsdk-unity-subsystems-manifest-json.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/xrsdk-unity-subsystems-manifest-json.html)
  * [中文](/cn/current/Manual/xrsdk-unity-subsystems-manifest-json.html)
  * [日本語](/ja/current/Manual/xrsdk-unity-subsystems-manifest-json.html)
  * [한국어](/kr/current/Manual/xrsdk-unity-subsystems-manifest-json.html)

  * [Platform development ](PlatformSpecific.html)
  * [XR](XR.html)
  * [Unity XR SDK](xr-sdk.html)
  * Provider setup
  * UnitySubsystemsManifest.json

[](xrsdk-provider-setup.html)

Creating an XR provider

[](xrsdk-runtime-discovery.html)

Runtime discovery and activation of subsystems

# UnitySubsystemsManifest.json

`UnitySubsystemsManifest.json` contains metadata about your provider that can
be queried before your **plug-in** A set of code created outside of Unity that
creates functionality in Unity. There are two kinds of plug-ins you can use in
Unity: Managed plug-ins (managed .NET assemblies created with tools like
Visual Studio) and Native plug-ins (platform-specific native code libraries).
[More info](./plug-ins.html)  
See in [Glossary](Glossary.html#Plug-in) is loaded. The values in this
dictionary are used to populate specific instances of SubsystemDescriptors in
C#. For example, information within the `displays` list is used to populate
[XRDisplaySubsystemDescriptors](../ScriptReference/XR.XRDisplaySubsystemDescriptor.html).

For Unity to find the a native library referenced by the
`UnitySubsystemsManifest.json` file, the library must be no more than two
subfolders deeper than the `UnitySubsystemsManifest.json` file.

Example .json file:

    
    
    {
        "name": "PluginName",
        "version": "1.0.0",
        "libraryName": "UnityXRDisplayExample",
    
        "displays": [
            {
                "id": "Display0",
                "supportedMirrorBlitReservedModes" : ["leftEye","rightEye", "sideBySide"]
            }
        ],
        "inputs:": [
            {
                "id": "MockHMD Head Tracking Stationary"
            },
            {
                "id": "MockHMD Head Tracking Simulated"
            }
        ]
    }
    

**Metadata** | **Description**  
---|---  
`name` | The name of your provider. Must match the first parameter of your **native plug-in** A platform-specific native code library that is created outside of Unity for use in Unity. Allows you can access features like OS calls and third-party code libraries that would otherwise not be available to Unity. [More info](./plug-ins.html)  
See in [Glossary](Glossary.html#Nativeplug-in)’s `RegisterLifecycleHandler`
call.  
`version` | Unused currently.  
`libraryName` | Must match the name of your provider’s native plug-in binary without the extension.  
`displays` | Collection of Display subsystem providers.  
`id` | Identifier for this display plug-in configuration. The `id` must match the string you pass into your native plug-in’s `RegisterLifecycleHandler` call for that subsystem. You can have more than one `display`, as long as your native plug-in calls `RegisterLifecycleHandler` for each.  
`inputs` | Collection of Input subsystem providers.  
  
Your manifest file can include additional fields for a display record after
`id` \- subsystems specify which parameters are valid.

[](xrsdk-provider-setup.html)

Creating an XR provider

[](xrsdk-runtime-discovery.html)

Runtime discovery and activation of subsystems

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

