[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/VRAudioSpatializer.html)
  * [中文](/cn/current/Manual/VRAudioSpatializer.html)
  * [日本語](/ja/current/Manual/VRAudioSpatializer.html)
  * [한국어](/kr/current/Manual/VRAudioSpatializer.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/VRAudioSpatializer.html)
  * [中文](/cn/current/Manual/VRAudioSpatializer.html)
  * [日本語](/ja/current/Manual/VRAudioSpatializer.html)
  * [한국어](/kr/current/Manual/VRAudioSpatializer.html)

  * [Platform development ](PlatformSpecific.html)
  * [XR](XR.html)
  * [XR audio](xr-audio.html)
  * Audio Spatializers

[](xr-audio.html)

XR audio

[](xr-sdk.html)

Unity XR SDK

# Audio Spatializers

Audio spatializers use “physical” characteristics of a **scene** A Scene
contains the environments and menus of your game. Think of each unique Scene
file as a unique level. In each Scene, you place your environments, obstacles,
and decorations, essentially designing and building your game in pieces. [More
info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene), such as the distance and angle between
an [AudioListener](class-AudioListener.html) and an [AudioSource](class-
AudioSource.html), to modify the properties of sound transmitted to the user.
Spatialization can improve the perception that a sound originates from a
specific location in a scene.

The Unity audio engine supports spatialization through **plug-ins** A set of
code created outside of Unity that creates functionality in Unity. There are
two kinds of plug-ins you can use in Unity: Managed plug-ins (managed .NET
assemblies created with tools like Visual Studio) and Native plug-ins
(platform-specific native code libraries). [More info](./plug-ins.html)  
See in [Glossary](Glossary.html#Plug-in) built with the Unity [Audio
Spatializer SDK](AudioSpatializerSDK.html). Unity does not provide any built-
in spatializer plug-ins itself, but several plug-in implementations are
available in third-party 3D audio SDKs. These audio SDKs typically provide
additional Unity components and tools for 3D audio.

The following is a non-comprehensive list of third-party audio SDKs that
provide Unity audio spatialization plug-ins:

Maker | Name | Platforms | Documentation  
---|---|---|---  
Microsoft | [Microsoft Spatializer](https://github.com/microsoft/spatialaudio-unity) | Windows, Android | https://learn.microsoft.com/en-us/windows/mixed-reality/develop/unity/spatial-sound-in-unity  
Oculus | [Oculus Spatializer Unity](https://developer.oculus.com/downloads/package/oculus-spatializer-unity/) | Windows, Android | https://developer.oculus.com/documentation/unity/unity-audio/  
Qualcomm | [Qualcomm 3D Audio Plugin for Unity](https://assetstore.unity.com/packages/tools/audio/3d-audio-plugin-for-unity-148379) | Windows, Android | https://developer.qualcomm.com/software/3d-audio-plugin-unity  
Steam | [Steam Audio](https://valvesoftware.github.io/steam-audio/downloads.html) | Windows, macOS, Linux, Android | https://valvesoftware.github.io/steam-audio/doc/unity/index.html  
Vive | [3DSP Audio SDK](https://developer.vive.com/resources/vive-sense/3dsp-audio-sdk/download/latest/) | Windows, Android | https://hub.vive.com/storage/3dsp/  
Google (now open source) | [Resonance Audio](https://resonance-audio.github.io/resonance-audio/) | Android, iOS, Web | https://resonance-audio.github.io/resonance-audio/develop/unity/developer-guide  
Apple | [PHASE](https://github.com/apple/unityplugins/tree/main/plug-ins/Apple.PHASE/) | iOS, macOS | https://developer.apple.com/documentation/phase  
  
In some cases, spatializer plug-ins are included with the [XR provider plug-
in](xr-support-packages.html) for an associated **XR** An umbrella term
encompassing Virtual Reality (VR), Augmented Reality (AR) and Mixed Reality
(MR) applications. Devices supporting these forms of interactive applications
can be referred to as XR devices. [More info](XR.html)  
See in [Glossary](Glossary.html#XR) device. For example, the Oculus provider
plug-in includes the OculusSpatializer plug-in and the Windows **Mixed
Reality** Mixed Reality (MR) combines its own virtual environment with the
user’s real-world environment and allows them to interact with each other.  
See in [Glossary](Glossary.html#MixedReality) feature group for OpenXR
includes the MS HRTF Spatializer plug-in. Note that these provider plug-ins
don’t include any additional components that might be available in the full
SDK packages from their maker.

**Note:** Although many spatializer plug-ins were developed for use with
**VR** Virtual Reality [More info](VROverview.html)  
See in [Glossary](Glossary.html#VR) devices, their use isn’t limited to VR
games or applications.

## Enable an audio spatializer plug-in

After you have added the package containing an **audio spatializer** A plug-in
that changes the way audio is transmitted from an audio source into the
surrounding space. It takes the source and regulates the gains of the left and
right ear contributions based on the distance and angle between the
AudioListener and the AudioSource. [More info](AudioSpatializerSDK.html)  
See in [Glossary](Glossary.html#AudioSpatializer) plug-in to your project, you
can enable the plug-in in the project audio settings.

To enable a plug-in:

  1. Open the Project Settings window (menu: **Edit > Project Settings**).
  2. Select the **Audio** category.
  3. Choose the plug-in from the **Spatializer Plugin** dropdown menu.

![](../uploads/Main/AudioManagerInspector.png)

[](xr-audio.html)

XR audio

[](xr-sdk.html)

Unity XR SDK

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

