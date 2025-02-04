[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/ShadowPerformance.html)
  * [中文](/cn/current/Manual/ShadowPerformance.html)
  * [日本語](/ja/current/Manual/ShadowPerformance.html)
  * [한국어](/kr/current/Manual/ShadowPerformance.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/ShadowPerformance.html)
  * [中文](/cn/current/Manual/ShadowPerformance.html)
  * [日本語](/ja/current/Manual/ShadowPerformance.html)
  * [한국어](/kr/current/Manual/ShadowPerformance.html)

  * [Lighting](LightingOverview.html)
  * [Shadows](Shadows.html)
  * Troubleshooting shadows

[](shadow-cascades-implementation-details.html)

Implementation details of shadow cascades

[](reflections-landing.html)

Reflections

# Troubleshooting shadows

## Reduce shadow flickering

Shadows might flicker if they’re far away from the **camera** A component
which creates an image of a particular viewpoint in your scene. The output is
either drawn to the screen or captured as a texture. [More
info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera). Refer to [Understanding the View
Frustum](UnderstandingFrustum.html) for more information.

If shadows are closer to the camera than the world space origin, enable
camera-relative culling. Unity uses the camera as the relative position for
shadow calculations instead of the world space origin, which reduces
flickering.

To enable camera-relative culling, follow these steps:

  1. Go to **Project Settings** > **Graphics** > **Culling Settings** > **Camera-Relative Culling**.
  2. Enable **Shadows**.

## Shadow performance

Rendering real-time shadows has a high performance impact. Any **GameObjects**
The fundamental object in Unity scenes, which can represent characters, props,
scenery, cameras, waypoints, and more. A GameObject’s functionality is defined
by the Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) that might cast shadows must first
be rendered into the shadow map and then that map is used to render objects
that might receive shadows.

Soft shadows have a greater rendering overhead than hard shadows, but this
only affects the GPU and does not cause much extra CPU work.

If rendering real-time shadows for complex geometry is prohibitively
expensive, consider using low **LOD** The _Level Of Detail_ (LOD) technique is
an optimization that reduces the number of triangles that Unity has to render
for a GameObject when its distance from the Camera increases. [More
info](LevelOfDetail.html)  
See in [Glossary](Glossary.html#LOD) meshes or even primitives to cast
shadows.

If this is too resource-intensive, you can fake shadows using a blurred
texture applied to a simple **mesh** The main graphics primitive of Unity.
Meshes make up a large part of your 3D worlds. Unity supports triangulated or
Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted
to polygons. [More info](mesh.html)  
See in [Glossary](Glossary.html#Mesh) or **quad** A primitive object that
resembles a plane but its edges are only one unit long, it uses only 4
vertices, and the surface is oriented in the XY plane of the local coordinate
space. [More info](PrimitiveObjects.html)  
See in [Glossary](Glossary.html#Quad) underneath your characters, or can
create blob shadows with custom shaders.

## Shadow acne

A surface directly illuminated by a light sometimes appears to be partly in
shadow. This is because **pixels** that should be exactly at the distance
specified in the shadow map are sometimes calculated as being further away
(this is a consequence of using shadow filtering, or a low-resolution image
for the shadow map). The result is arbitrary patterns of pixels in shadow when
they should be lit, giving a visual effect known as “shadow acne”.

![Shadow acne in the form of false self-shadowing
artifacts](../uploads/Main/ShadowBiasAcne.jpg) Shadow acne in the form of
false self-shadowing artifacts

### Adjust the shadow bias settings

By adjusting the shadow bias values you can reduce or eliminate such shadow
artifacts as shadow acne, shadow detachment (also known as peter-panning),
light leaking, and self-shadowing.

In the Built-in **Render Pipeline** A series of operations that take the
contents of a Scene, and displays them on a screen. Unity lets you choose from
pre-built render pipelines, or write your own. [More info](render-
pipelines.html)  
See in [Glossary](Glossary.html#Renderpipeline), you can set these values with
the **Bias** and **Normal Bias** properties in the [**Light
Inspector**](class-Light.html) window when shadows are enabled.

Do not set the **Bias** value too high, because areas around a shadow near the
GameObject casting it are sometimes falsely illuminated. This results in a
disconnected shadow, making the GameObject look as if it is flying above the
ground.

![A high Bias value makes the shadow appear disconnected from the
GameObject](../uploads/Main/ShadowBiasPeterPanning.jpg) A high **Bias** value
makes the shadow appear “disconnected” from the GameObject

Likewise, setting the **Normal Bias** value too high makes the shadow appear
too narrow for the GameObject:

![A high Normal Bias value makes the shadow shape too
narrow](../uploads/Main/ShadowBiasTooThin.jpg) A high **Normal Bias** value
makes the shadow shape too narrow

In some situations, **Normal Bias** can cause an unwanted effect called light
bleeding, where light bleeds through from nearby geometry into areas that
should be shadowed. A potential solution is to open the GameObject’s [Mesh
Renderer](class-MeshRenderer.html)A mesh component that takes the geometry
from the Mesh Filter and renders it at the position defined by the object’s
Transform component. [More info](class-MeshRenderer.html)  
See in [Glossary](Glossary.html#MeshRenderer) and change the **Cast Shadows**
property to **Two Sided**. This can sometimes help, although it can be more
resource-intensive and increase performance overhead when rendering the
**Scene** A Scene contains the environments and menus of your game. Think of
each unique Scene file as a unique level. In each Scene, you place your
environments, obstacles, and decorations, essentially designing and building
your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene).

The bias values for a light may need tweaking to make sure that unwanted
effects don’t occur. It is generally easier to gauge the right value by eye
rather than attempting to calculate it.

![A low Shadow near plane offset value create the appearance of holes in
shadows](../uploads/Main/ShadowNearOffsetTooLow.jpeg) A low Shadow near plane
offset value create the appearance of holes in shadows ![Correct
shadowing](../uploads/Main/ShadowNearOffsetOk.jpg) Correct shadowing

### Shadow pancaking

To further prevent shadow acne we are using a technique known as **Shadow
pancaking**. The idea is to reduce the range of the light space used when
rendering the shadow map along the light direction. This leads to an increased
precision in the shadow map, reducing shadow acne.

![A diagram showing the shadow pancaking
principle](../uploads/Main/PancakingIdea.png) A diagram showing the shadow
pancaking principle

In the above diagram:

  * The **light blue circles** represent the shadow casters
  * The **dark blue rectangle** represents the original light space
  * The **green line** represents the optimized near plane (excluding any shadow casters not visible in the view frustum)

Clamp these shadow casters to the near clip plane of the optimized space (in
the Vertex Shader). Note that while this works well in general, it can create
artifacts for very large triangles crossing the near clip plane:

![Large triangle problem](../uploads/Main/PancakingProblem.png) Large triangle
problem

In this case, only one vertex of the blue triangle is behind the near clip
plane and gets clamped to it. However, this alters the triangle shape, and can
create incorrect shadowing.

You can tweak the **Shadow Near Plane Offset** property from the
[Quality](class-QualitySettings.html) window to avoid this problem. This pulls
back the near clip plane. However, setting this value very high eventually
introduces shadow acne, because it raises the range that the shadow map needs
to cover in the light direction. Alternatively, you can also tesselate the
problematic shadow casting triangles.

## Shadows not appearing

If you find that one or more objects are not casting shadows then you should
check the following points:

  * Real-time shadows can be disabled completely in the [Quality](class-QualitySettings.html) window. Make sure that you have the correct quality level enabled and that shadows are switched on for that setting.

  * All [Mesh Renderers](class-MeshRenderer.html) in the scene must be set up with their _Receive Shadows_ and _Cast Shadows_ correctly set. Both are enabled by default, but check that they haven’t been disabled unintentionally.

  * Only opaque objects cast and receive shadows, so objects using the built-in [Transparent](shader-TransparentFamily.html) or Particle shaders will neither cast nor receive. Generally, you can use the [Transparent Cutout](shader-TransparentCutoutFamily.html) shaders instead for objects with “gaps” such as fences, vegetation, etc. Custom [Shaders](Shaders.html)A program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) must be pixel-lit and use the
[Geometry render queue](SL-SubShaderTags.html).

  * Objects using **VertexLit** shaders can’t receive shadows, but they can cast them.

  * Unity can’t calculate shadows for GameObjects that have materials with “Unlit” type shaders. Unity can only calculate shadows for materials with shaders that support lighting.

  * In the Built-in Render Pipeline, using the [Forward rendering path](RenderTech-ForwardRendering.html), some shaders allow only the brightest directional light to cast shadows (in particular, this happens with Unity’s built-in shaders from 4.x versions). If you want to have more than one shadow-casting light then you should use the [Deferred Shading](RenderTech-DeferredShading.html)A rendering path in the Built-in Render Pipeline that places no limit on the number of Lights that can affect a GameObject. All Lights are evaluated per-pixel, which means that they all interact correctly with normal maps and so on. Additionally, all Lights can have cookies and shadows. [More info](RenderTech-DeferredShading.html)  
See in [Glossary](Glossary.html#Deferredshading) **rendering path** The
technique that a render pipeline uses to render graphics. Choosing a different
rendering path affects how lighting and shading are calculated. Some rendering
paths are more suited to different platforms and hardware than others. [More
info](RenderingPaths.html)  
See in [Glossary](Glossary.html#RenderingPath) instead. You can enable your
own shaders to support “full shadows” by using the `fullforwardshadows`
[surface shader](SL-SurfaceShaders.html)A streamlined way of writing shaders
for the Built-in Render Pipeline. [More info](SL-SurfaceShaders.html)  
See in [Glossary](Glossary.html#SurfaceShader) directive.

## Additional resources

  * [Optimize shadow rendering](shadows-optimization.html)

  * [Troubleshooting shadows in URP](urp/shadows-troubleshooting-urp.html)

[](shadow-cascades-implementation-details.html)

Implementation details of shadow cascades

[](reflections-landing.html)

Reflections

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

