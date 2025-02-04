[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/lighting/reflection-probes-introduction.html)
  * [中文](/cn/current/Manual/urp/lighting/reflection-probes-introduction.html)
  * [日本語](/ja/current/Manual/urp/lighting/reflection-probes-introduction.html)
  * [한국어](/kr/current/Manual/urp/lighting/reflection-probes-introduction.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/lighting/reflection-probes-introduction.html)
  * [中文](/cn/current/Manual/urp/lighting/reflection-probes-introduction.html)
  * [日本語](/ja/current/Manual/urp/lighting/reflection-probes-introduction.html)
  * [한국어](/kr/current/Manual/urp/lighting/reflection-probes-introduction.html)

  * [Lighting](../../LightingOverview.html)
  * [Lighting in URP](../../urp/lighting-landing.html)
  * [Reflections in URP](../../urp/lighting/reflection-probes.html)
  * Reflection Probes in URP

[](../../urp/lighting/reflection-probes.html)

Reflections in URP

[](../../urp/lighting/reflection-probes-troubleshooting.html)

Troubleshooting reflections

# Reflection Probes in URP

URP uses the following properties to determine the contribution of
**Reflection Probes** A rendering component that captures a spherical view of
its surroundings in all directions, rather like a camera. The captured image
is then stored as a Cubemap that can be used by objects with reflective
materials. [More info](../../class-ReflectionProbe.html)  
See in [Glossary](../../Glossary.html#ReflectionProbe) to a **GameObject** The
fundamental object in Unity scenes, which can represent characters, props,
scenery, cameras, waypoints, and more. A GameObject’s functionality is defined
by the Components attached to it. [More info](../../class-GameObject.html)  
See in [Glossary](../../Glossary.html#GameObject):

  * **Reflection Probe Volume**
  * **Blend Distance**

**Note:** When performing indirect draw calls, Unity does not support
reflection probes in the **Deferred** and the **Forward** rendering paths.
Unity supports them in the **Forward+** **rendering path** The technique that
a render pipeline uses to render graphics. Choosing a different rendering path
affects how lighting and shading are calculated. Some rendering paths are more
suited to different platforms and hardware than others. [More
info](../../RenderingPaths.html)  
See in [Glossary](../../Glossary.html#RenderingPath).

## Reflection probe volumes

Each reflection probe has a box volume. A reflection probe only affects parts
of a GameObject that are inside the box volume. When a **pixel** The smallest
unit in a computer image. Pixel size depends on your screen resolution. Pixel
lighting is calculated at every screen pixel. [More
info](../../ShadowPerformance.html)  
See in [Glossary](../../Glossary.html#pixel) of an object is outside of any
reflection probe volume, Unity uses the **skybox** A special type of Material
used to represent skies. Usually six-sided. [More info](../../sky-
landing.html)  
See in [Glossary](../../Glossary.html#Skybox) reflection.

In URP, Unity evaluates the contribution of each probe for each individual
pixel, depending on the position of the pixel relative to the boundary of the
probe volume.

This behavior is different from the Built-in **Render Pipeline** A series of
operations that take the contents of a Scene, and displays them on a screen.
Unity lets you choose from pre-built render pipelines, or write your own.
[More info](../../render-pipelines.html)  
See in [Glossary](../../Glossary.html#Renderpipeline), where Unity evaluates
the contribution of a probe for the whole object.

## Blend Distance

Each reflection probe has the **Blend Distance** property. This property is
the distance from the face of a reflection box volume towards the center of
the box volume.

Unity uses the Blend Distance property to determine the contribution of a
reflection probe. When a pixel of an object is on the face of a reflection
probe volume, that pixel gets 0% of reflections from the probe. When a pixel
is inside the reflection probe volume and its distance from each face exceeds
the Blend Distance value, the pixel gets 100% of reflections.

If the Blend Distance value is more than half of the distance between faces of
the reflection probe volume, the reflection probe cannot provide 100%
contribution to any pixel within the volume.

## Which Reflection Probes affect a GameObject

When a GameObject is within multiple reflection probe volumes, maximum two of
the probes can affect the GameObject. Unity selects which probes affect the
GameObject using the following criteria:

  * The **Importance** property of a reflection probe. Unity selects two probes with higher Importance values and ignores the others.

  * If the Importance values are the same, Unity selects probes which have the smallest box volumes.

  * If the Importance values and the box volumes are the same, Unity determines which two reflection probe volumes contain larger surface areas of a GameObject, and picks the probes of those volumes.

When two reflection probes affect a GameObject, for each pixel, Unity
calculates the weight of each probe depending on the distance of this pixel
from the faces of the probe box volumes and the values of the **Blend
Distance** properties.

If the pixel is relatively close to faces of both box volumes and the sum of
weights of both probes is less than 1, Unity assigns the remaining weight to
the `_GlossyEnvironmentCubeMap`. This cube map contains the reflection from
the lighting source set in the Lighting window under **Environment Lighting**
> **Source**. In most cases this source is the skybox.

If the pixel is within both box volumes and farther than the Blend Distance
values from faces of both volumes:

  * If the **Importance** properties of the reflection probes are the same, Unity blends reflections from the probes with equal weights.

  * If the **Importance** property of one of the probes is higher, Unity applies the reflections only from that probe.

[](../../urp/lighting/reflection-probes.html)

Reflections in URP

[](../../urp/lighting/reflection-probes-troubleshooting.html)

Troubleshooting reflections

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

