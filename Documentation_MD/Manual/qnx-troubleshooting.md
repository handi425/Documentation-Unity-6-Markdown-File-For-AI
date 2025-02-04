[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/qnx-troubleshooting.html)
  * [中文](/cn/current/Manual/qnx-troubleshooting.html)
  * [日本語](/ja/current/Manual/qnx-troubleshooting.html)
  * [한국어](/kr/current/Manual/qnx-troubleshooting.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/qnx-troubleshooting.html)
  * [中文](/cn/current/Manual/qnx-troubleshooting.html)
  * [日本語](/ja/current/Manual/qnx-troubleshooting.html)
  * [한국어](/kr/current/Manual/qnx-troubleshooting.html)

  * [Platform development ](PlatformSpecific.html)
  * [Embedded systems](embedded-systems.html)
  * [QNX](qnx.html)
  * [Develop for QNX](qnx-develop.html)
  * Troubleshooting the QNX Player

[](qnx-optional-features.html)

Enable optional features for QNX

[](qnx-build-and-deliver.html)

Build and deliver for QNX

# Troubleshooting the QNX Player

This page lists the common problems and limitations that might occur when
using the QNX Player.

## The QNX Player fails to enumerate all display resolutions

Due to an ABI breakage in the QNX 7.1 screen system headers, the Player might
not be able to query all available display modes. For more information, refer
to the [QNX Article - Ref#
J2941150](https://www.qnx.com/developers/articles/rel_6934_0.html).

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

[](qnx-optional-features.html)

Enable optional features for QNX

[](qnx-build-and-deliver.html)

Build and deliver for QNX

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

