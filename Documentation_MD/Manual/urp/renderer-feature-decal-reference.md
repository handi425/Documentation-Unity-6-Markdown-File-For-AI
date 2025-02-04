[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/renderer-feature-decal-reference.html)
  * [中文](/cn/current/Manual/urp/renderer-feature-decal-reference.html)
  * [日本語](/ja/current/Manual/urp/renderer-feature-decal-reference.html)
  * [한국어](/kr/current/Manual/urp/renderer-feature-decal-reference.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/renderer-feature-decal-reference.html)
  * [中文](/cn/current/Manual/urp/renderer-feature-decal-reference.html)
  * [日本語](/ja/current/Manual/urp/renderer-feature-decal-reference.html)
  * [한국어](/kr/current/Manual/urp/renderer-feature-decal-reference.html)

  * [Visual effects](../visual-effects.html)
  * [Decals and projectors](../visual-effects-decals.html)
  * [Decals in URP](../urp/renderer-feature-decal-landing.html)
  * Decal Renderer Feature reference

[](../urp/decal-shader.html)

Create a decal via a Decal Projector in URP

[](../urp/renderer-feature-decal-projector-reference.html)

Decal Projector component reference for URP

# Decal Renderer Feature reference

This section describes the properties of the Decal Renderer Feature.

![Decal Renderer Feature, Inspector view.](../../uploads/urp/decal/decal-rf-
inspector.png)  
_Decal Renderer Feature, Inspector view._

### Technique

Select the rendering technique for the Renderer Feature.

This section describes the options in this property.

#### Automatic

Unity selects the rendering technique automatically based on the build
platform. The [Accurate G-buffer normals](rendering/accurate-g-buffer-
normals.html) option is also taken into account, as it prevents normal
blending from working correctly without the D-Buffer technique.

#### DBuffer

Unity renders decals into the Decal buffer (DBuffer). Unity overlays the
content of the DBuffer on top of the opaque objects during the opaque
rendering.

Selecting this technique reveals the **Surface Data** property. The Surface
Data property lets you specify which surface properties of decals Unity blends
with the underlying meshes. The Surface Data property has the following
options:

  * **Albedo** : decals affect the base color and the emission color.
  * **Albedo Normal** : decals affect the base color, the emission color, and the normals.
  * **Albedo Normal MAOS** : decals affect the base color, the emission color, the normals, the metallic values, the smoothness values, and the **ambient occlusion** A method to approximate how much ambient light (light not coming from a specific direction) can hit a point on a surface.  
See in [Glossary](../Glossary.html#Ambientocclusion) values.

**Limitations:**

  * This technique does not support the OpenGL and OpenGL ES API.

  * This technique requires the DepthNormal prepass, which makes the technique less efficient on GPUs that implement tile-based rendering.

  * This technique does not work on particles and **terrain** The landscape in your scene. A Terrain GameObject adds a large flat plane to your scene and you can use the Terrain’s Inspector window to create a detailed landscape. [More info](../terrain-UsingTerrains.html)  
See in [Glossary](../Glossary.html#Terrain) details.

####  Screen Space

Unity renders decals after the opaque objects using normals that Unity
reconstructs from the depth texture, or from the G-Buffer when using the
Deferred **rendering path** The technique that a render pipeline uses to
render graphics. Choosing a different rendering path affects how lighting and
shading are calculated. Some rendering paths are more suited to different
platforms and hardware than others. [More info](../RenderingPaths.html)  
See in [Glossary](../Glossary.html#RenderingPath). Unity renders decals as
meshes on top of the opaque meshes. This technique supports only the normal
blending. When using the Deferred rendering path with [Accurate G-buffer
normals](rendering/accurate-g-buffer-normals.html), blending of normals is not
supported, and will yield incorrect results.

Screen space decals are recommended for mobile platforms that use tile-based
rendering, because URP doesn’t create a DepthNormal prepass unless you enable
**Use Rendering Layers**.

Selecting this technique reveals the following properties.

**Property** | **Description**  
---|---  
**Normal Blend** | The options in this property (Low, Medium, and High) determine the number of samples of the depth texture that Unity takes when reconstructing the normal vector from the depth texture. The higher the quality, the more accurate the reconstructed normals are, and the higher the performance impact is.  
**Low** | Unity takes one depth sample when reconstructing normals.  
**Medium** | Unity takes three depth samples when reconstructing normals.  
**High** | Unity takes five depth samples when reconstructing normals.  
  
### Max Draw Distance

The maximum distance from the **Camera** A component which creates an image of
a particular viewpoint in your scene. The output is either drawn to the screen
or captured as a texture. [More info](../CamerasOverview.html)  
See in [Glossary](../Glossary.html#Camera) at which Unity renders decals.

### Use Rendering Layers

Select this check box to enable the [Rendering Layers](features/rendering-
layers.html) functionality.

If you enable **Use Rendering Layers** , URP creates a DepthNormal prepass.
This makes decals less efficient on GPUs that implement tile-based rendering.

[](../urp/decal-shader.html)

Create a decal via a Decal Projector in URP

[](../urp/renderer-feature-decal-projector-reference.html)

Decal Projector component reference for URP

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

