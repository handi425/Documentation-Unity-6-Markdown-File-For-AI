[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/class-LightProbeProxyVolume-configure.html)
  * [中文](/cn/current/Manual/class-LightProbeProxyVolume-configure.html)
  * [日本語](/ja/current/Manual/class-LightProbeProxyVolume-configure.html)
  * [한국어](/kr/current/Manual/class-LightProbeProxyVolume-configure.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/class-LightProbeProxyVolume-configure.html)
  * [中文](/cn/current/Manual/class-LightProbeProxyVolume-configure.html)
  * [日本語](/ja/current/Manual/class-LightProbeProxyVolume-configure.html)
  * [한국어](/kr/current/Manual/class-LightProbeProxyVolume-configure.html)

  * [Lighting](LightingOverview.html)
  * [Lighting in the Built-In Render Pipeline](lighting-birp.html)
  * [Configure a GameObject to sample more Light Probes in the Built-In Render Pipeline](LightProbeProxyVolume-landing.html)
  * Configure a Light Probe Proxy Volume in the Built-In Render Pipeline

[](class-LightProbeProxyVolume-add.html)

Set a GameObject to use a Light Probe Proxy Volume in the Built-In Render
Pipeline

[](class-LightProbeProxyVolume-reference.html)

Light Probe Proxy Volume component reference for the Built-In Render Pipeline

# Configure a Light Probe Proxy Volume in the Built-In Render Pipeline

The area in which the 3D grid of interpolated **Light Probes** Light probes
store information about how light passes through space in your scene. A
collection of light probes arranged within a given space can improve lighting
on moving objects and static LOD scenery within that space. [More
info](LightProbes.html)  
See in [Glossary](Glossary.html#LightProbe) are generated is affected by the
**Bounding Box Mode** property.

The main difference between **Automatic Local** and **Automatic World** is
that in **Automatic Local** , the bounding box is more resource-intensive to
compute when a large hierarchy of GameObjects uses the same LPPV component
from a parent **GameObject** The fundamental object in Unity scenes, which can
represent characters, props, scenery, cameras, waypoints, and more. A
GameObject’s functionality is defined by the Components attached to it. [More
info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject). However, the resulting bounding
box may be smaller in size, meaning the lighting data is more compact.

The number of interpolated Light Probes from within the **bounding volume** A
closed shape representing the edges and faces of a collider or trigger.  
See in [Glossary](Glossary.html#Boundingvolume) is affected by the **Proxy
Volume Resolution** property. There are two options:

  * **Automatic** (default value) - The resolution on each axis is computed using the number of interpolated Light Probes per unit area that you specify, and the size of the bounding box.

  * **Custom** \- Allows you to specify a different resolution on each axis (see below).

**Note:** The final resolution on each axis must be a power of two, and the
maximum value of the resolution is 32.

**Probe Position Mode** specifies the relative position of an interpolated
Light Probe to a cell center. This option may be useful in situations when
some of the interpolated Light Probes pass through walls or other geometries
and cause light leaking. The example below shows the difference between **Cell
Corner** and **Cell Center** in a 2D view, using a 4x4 grid resolution:

![](../uploads/Main/LightProbeProxyVolumeWindow4.png)

**Data Format** specifies which format the associated 3D texture uses. There
are two options:

  * **Float** (default value) - The texture uses the 32-bit floating-point channel format to store the spherical harmonics coefficients.

  * **Half Float** \- The texture uses the half-float (16-bit float) channel format to store the spherical harmonics coefficients. The advantage of this format is that half-float linear texture sampling is supported by the majority of devices and the precision difference between this format and the 32-bit floating point channel format is not noticeable. Also, the texture sampling performance on the GPU is better with this data format.

## Additional resources

  * [Light Probe Proxy Volume component reference](class-LightProbeProxyVolume-reference.html)

[](class-LightProbeProxyVolume-add.html)

Set a GameObject to use a Light Probe Proxy Volume in the Built-In Render
Pipeline

[](class-LightProbeProxyVolume-reference.html)

Light Probe Proxy Volume component reference for the Built-In Render Pipeline

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

