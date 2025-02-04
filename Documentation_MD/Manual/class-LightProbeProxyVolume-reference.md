[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/class-LightProbeProxyVolume-reference.html)
  * [中文](/cn/current/Manual/class-LightProbeProxyVolume-reference.html)
  * [日本語](/ja/current/Manual/class-LightProbeProxyVolume-reference.html)
  * [한국어](/kr/current/Manual/class-LightProbeProxyVolume-reference.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/class-LightProbeProxyVolume-reference.html)
  * [中文](/cn/current/Manual/class-LightProbeProxyVolume-reference.html)
  * [日本語](/ja/current/Manual/class-LightProbeProxyVolume-reference.html)
  * [한국어](/kr/current/Manual/class-LightProbeProxyVolume-reference.html)

  * [Lighting](LightingOverview.html)
  * [Lighting in the Built-In Render Pipeline](lighting-birp.html)
  * [Configure a GameObject to sample more Light Probes in the Built-In Render Pipeline](LightProbeProxyVolume-landing.html)
  * Light Probe Proxy Volume component reference for the Built-In Render Pipeline

[](class-LightProbeProxyVolume-configure.html)

Configure a Light Probe Proxy Volume in the Built-In Render Pipeline

[](class-LightProbeProxyVolume-Shader.html)

Add Light Probe Proxy Volume support to a custom shader in the Built-In Render
Pipeline

# Light Probe Proxy Volume component reference for the Built-In Render
Pipeline

There are three options available:

**Bounding Box Mode:** | **Function:**  
---|---  
**Automatic Local** (default value) | A local-space bounding box is computed. The interpolated Light Probe positions are generated inside this bounding box. If a Renderer component isn’t attached to the **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject), then a default bounding box is
generated. The bounding box computation encloses the current Renderer, and
sets all the Renderers down the hierarchy that have the **Light Probes** Light
probes store information about how light passes through space in your scene. A
collection of light probes arranged within a given space can improve lighting
on moving objects and static LOD scenery within that space. [More
info](LightProbes.html)  
See in [Glossary](Glossary.html#LightProbe) property to **Use Proxy Volume**.  
**Automatic World** | A bounding box is computed which encloses the current Renderer and all the Renderers down the hierarchy that have the **Light Probes** property set to **Use Proxy Volume**. The bounding box is world-aligned.  
**Custom** | A custom bounding box is used. The bounding box is specified in the local-space of the GameObject. The bounding box editing tools are available. You can edit the **bounding volume** A closed shape representing the edges and faces of a collider or trigger.  
See in [Glossary](Glossary.html#Boundingvolume) manually by modifying the
**Size** and **Origin** values in the **UI**(User Interface) Allows a user to
interact with your application. Unity currently supports three UI systems.
[More info](UI-system-compare.html)  
See in [Glossary](Glossary.html#UI) (see below).  
  
[](class-LightProbeProxyVolume-configure.html)

Configure a Light Probe Proxy Volume in the Built-In Render Pipeline

[](class-LightProbeProxyVolume-Shader.html)

Add Light Probe Proxy Volume support to a custom shader in the Built-In Render
Pipeline

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

