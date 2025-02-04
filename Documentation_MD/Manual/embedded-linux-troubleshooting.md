[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/embedded-linux-troubleshooting.html)
  * [中文](/cn/current/Manual/embedded-linux-troubleshooting.html)
  * [日本語](/ja/current/Manual/embedded-linux-troubleshooting.html)
  * [한국어](/kr/current/Manual/embedded-linux-troubleshooting.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/embedded-linux-troubleshooting.html)
  * [中文](/cn/current/Manual/embedded-linux-troubleshooting.html)
  * [日本語](/ja/current/Manual/embedded-linux-troubleshooting.html)
  * [한국어](/kr/current/Manual/embedded-linux-troubleshooting.html)

  * [Platform development ](PlatformSpecific.html)
  * [Embedded systems](embedded-systems.html)
  * [Embedded Linux](embedded-linux.html)
  * [Develop for Embedded Linux](embedded-linux-develop.html)
  * Troubleshooting the Embedded Linux Unity Editor

[](embedded-linux-optional-features.html)

Enable optional features for Embedded Linux

[](embedded-linux-build-and-deliver.html)

Build and deliver for Embedded Linux

# Troubleshooting the Embedded Linux Unity Editor

This page lists the common problems that might occur when using the Embedded
Linux Unity Editor.

## The Player build fails with an error

When exporting the Unity project, the following error appears: `No
EmbeddedLinux Burst Support on X86/Arm32 architecture`. Disabling Burst in
Settings and removing it from the project doesn’t fix the issue because
another package has a dependency on it.

### Solution

Burst isn’t supported on 32-bit Embedded Linux platforms. To prevent facing
the error, you can disable Burst by starting the Unity Editor with the
`--burst-disable-compilation` argument.

## Wayand is not available error

Starting the player on the target device fails with: SDL `Error: wayland,x11
not available` although Wayland is available.

### Solution

This error might occur due to one of the following reasons:

  * The Wayland library isn’t located by SDL2. Make sure that the Wayland library is locatable by `dlopen` from the player application.
  * Unity requires at least Wayland version 1.18. Because some systems have only version 1.16 or lower available, ensure to check that at least Wayland version 1.18 is supported on the target device.
  * The connection to the Wayland display fails. Make sure the Wayland environment is properly set up.

### Solution

The `-nographics commandline` argument in the Player build of the Unity Editor
is the root cause of this problem, because it generates sky ambient probe and
**reflection probe** A rendering component that captures a spherical view of
its surroundings in all directions, rather like a camera. The captured image
is then stored as a Cubemap that can be used by objects with reflective
materials. [More info](class-ReflectionProbe.html)  
See in [Glossary](Glossary.html#ReflectionProbe) that require loading a gfx
device, otherwise these probes include uninitialized data. To prevent this
from happening, run the Player build without `-nographics`, or generate
lighting in the Editor for each **scene** A Scene contains the environments
and menus of your game. Think of each unique Scene file as a unique level. In
each Scene, you place your environments, obstacles, and decorations,
essentially designing and building your game in pieces. [More
info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) included in the build. That is, don’t
add lights or generate **lightmaps** A pre-rendered texture that contains the
effects of light sources on static objects in the scene. Lightmaps are
overlaid on top of scene geometry to create the effect of lighting. [More
info](Lightmapping.html)  
See in [Glossary](Glossary.html#Lightmap), and instead generate lighting that
will automatically bake the sky probes. When `-nographics` is set, no probes
will be rendered.

## Additional resources

  * [Troubleshooting the Linux Editor issues](https://docs.unity3d.com/2022.3/Documentation/Manual/linux-editor-troubleshooting.html)

[](embedded-linux-optional-features.html)

Enable optional features for Embedded Linux

[](embedded-linux-build-and-deliver.html)

Build and deliver for Embedded Linux

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

