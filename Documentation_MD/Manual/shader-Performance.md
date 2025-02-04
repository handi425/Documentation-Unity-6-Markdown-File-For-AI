[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/shader-Performance.html)
  * [中文](/cn/current/Manual/shader-Performance.html)
  * [日本語](/ja/current/Manual/shader-Performance.html)
  * [한국어](/kr/current/Manual/shader-Performance.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/shader-Performance.html)
  * [中文](/cn/current/Manual/shader-Performance.html)
  * [日本語](/ja/current/Manual/shader-Performance.html)
  * [한국어](/kr/current/Manual/shader-Performance.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Prebuilt shaders](shader-built-in-landing.html)
  * [Legacy prebuilt shaders](Built-inShaderGuide.html)
  * Usage and Performance of Built-in Shaders

[](Built-inShaderGuide.html)

Legacy prebuilt shaders

[](shader-NormalFamily.html)

Normal Shader Family

# Usage and Performance of Built-in Shaders

Shaders in Unity are used through **Materials** An asset that defines how a
surface should be rendered. [More info](class-Material.html)  
See in [Glossary](Glossary.html#Material), which essentially combine
**shader** A program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) code with parameters like textures. An
in-depth explanation of the Shader/Material relationship can be read
[here](Materials.html).

Material properties will appear in the **Inspector** A Unity window that
displays information about the currently selected GameObject, asset or project
settings, allowing you to inspect and edit the values. [More
info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector) when either the Material itself or
a **GameObject** The fundamental object in Unity scenes, which can represent
characters, props, scenery, cameras, waypoints, and more. A GameObject’s
functionality is defined by the Components attached to it. [More info](class-
GameObject.html)  
See in [Glossary](Glossary.html#GameObject) that uses the Material is
selected. The Material Inspector looks like this:

![](../uploads/Main/MatInspector.png)

Each Material will look a little different in the Inspector, depending on the
specific shader it is using. The shader iself determines what kind of
properties will be available to adjust in the Inspector. Material inspector is
described in detail in [Material reference page](class-Material.html).
Remember that a shader is implemented through a Material. So while the shader
defines the properties that will be shown in the Inspector, each Material
actually contains the adjusted data from sliders, colors, and textures. The
most important thing to remember about this is that a single shader can be
used in multiple Materials, but a single Material cannot use multiple shaders.

## Shader names

Changing the name of a Legacy Shader can affect its functionality. This is
because prior to Unity 5.0, some of the functionality of a shader was
determined by its path and name. This is still how the Legacy Shaders work.
For more information, see [Legacy shader names](class-
Shader.html#legacyShaderNames)

## Performance Considerations

There are a number of factors that can affect the overall performance of your
game. This page will talk specifically about the performance considerations
for [Built-in Shaders](Built-inShaderGuide.html). Performance of a shader
mostly depends on two things: shader itself and which [Rendering
Path](RenderingPaths.html)The technique that a render pipeline uses to render
graphics. Choosing a different rendering path affects how lighting and shading
are calculated. Some rendering paths are more suited to different platforms
and hardware than others. [More info](RenderingPaths.html)  
See in [Glossary](Glossary.html#RenderingPath) is used by the project or
specific **camera** A component which creates an image of a particular
viewpoint in your scene. The output is either drawn to the screen or captured
as a texture. [More info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera). For performance tips when writing
your own shaders, see [ShaderLab Shader Performance](SL-
ShaderPerformance.html) page.

### Rendering Paths and shader performance

From the rendering paths Unity supports, [Deferred Shading](RenderTech-
DeferredShading.html)A rendering path in the Built-in Render Pipeline that
places no limit on the number of Lights that can affect a GameObject. All
Lights are evaluated per-pixel, which means that they all interact correctly
with normal maps and so on. Additionally, all Lights can have cookies and
shadows. [More info](RenderTech-DeferredShading.html)  
See in [Glossary](Glossary.html#Deferredshading) and [Vertex Lit](RenderTech-
VertexLit.html) paths have the most predictable performance. In Deferred
shading, each object is generally drawn once, no matter what lights are
affecting it. Similarly, in Vertex Lit each object is generally drawn once. So
then, the performance differences in shaders mostly depend on how many
textures they use and what calculations they do.

### Shader Performance in Forward rendering path

In [Forward](RenderTech-ForwardRendering.html) rendering path, performance of
a shader depends on **both** the shader itself and the lights in the **scene**
A Scene contains the environments and menus of your game. Think of each unique
Scene file as a unique level. In each Scene, you place your environments,
obstacles, and decorations, essentially designing and building your game in
pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene). The following section explains the
details. There are two basic categories of shaders from a performance
perspective, **Vertex-Lit** , and **Pixel-Lit**.

**Vertex-Lit** shaders in **Forward rendering** A rendering path that renders
each object in one or more passes, depending on lights that affect the object.
Lights themselves are also treated differently by Forward Rendering, depending
on their settings and intensity. [More info](RenderTech-ForwardRendering.html)  
See in [Glossary](Glossary.html#ForwardRendering) path are always cheaper than
Pixel-Lit shaders. These shaders work by calculating lighting based on the
**mesh** The main graphics primitive of Unity. Meshes make up a large part of
your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes.
Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More
info](mesh.html)  
See in [Glossary](Glossary.html#Mesh) vertices, using all lights at once.
Because of this, no matter how many lights are shining on the object, it will
only have to be drawn once.

**Pixel-Lit** shaders calculate final lighting at each **pixel** The smallest
unit in a computer image. Pixel size depends on your screen resolution. Pixel
lighting is calculated at every screen pixel. [More
info](ShadowPerformance.html)  
See in [Glossary](Glossary.html#pixel) that is drawn. Because of this, the
object has to be drawn once to get the ambient & main directional light, and
once for each additional light that is shining on it. Thus the formula is N
rendering passes, where N is the final number of pixel lights shining on the
object. This increases the load on the CPU to process and send off commands to
the graphics card, and on the graphics card to process the vertices and draw
the pixels. The size of the Pixel-lit object on the screen will also affect
the speed at which it is drawn. The larger the object, the slower it will be
drawn.

So pixel lit shaders come at performance cost, but that cost allows for some
spectacular effects: shadows, normal-mapping, good looking specular highlights
and light cookies, just to name a few.

Remember that lights can be forced into a pixel (“important”) or vertex/SH
(“not important”) mode. Any vertex lights shining on a Pixel-Lit shader will
be calculated based on the object’s vertices or whole object, and will not add
to the rendering cost or visual effects that are associated with pixel lights.

## General shader performance

Out of [Built-in Shaders](Built-inShaderGuide.html), they come roughly in this
order of increasing complexity:

  * **Unlit**. This is just a texture, not affected by any lighting.
  * **VertexLit**.
  * **Diffuse**.
  * **Normal mapped**. This is a bit more expensive than Diffuse: it adds one more texture (normal map), and a couple of shader instructions.
  * **Specular**. This adds specular highlight calculation.
  * **Normal Mapped Specular**. Again, this is a bit more expensive than Specular.
  * **Parallax Normal mapped**. This adds parallax normal-mapping calculation.
  * **Parallax Normal Mapped Specular**. This adds both parallax normal-mapping and specular highlight calculation.

## Mobile simplified shaders

Additionally, Unity has several simplified shaders targeted at mobile
platforms, under “Mobile” category. These shaders work on other platforms as
well, so if you can live with their simplifications (e.g. approximate
specular, no per-material color support etc.), try using them!

To see the specific simplifications that have been made for each shader, look
at the `.shader` files from the “built-in shaders” package and the information
is listed at the top of the file in some comments.

Some examples of changes that are common across the Mobile shaders are:

  * There is no material color or main color for tinting the shader.
  * For the shaders taking a **normal map** A type of Bump Map texture that allows you to add surface detail such as bumps, grooves, and scratches to a model which catch the light as if they are represented by real geometry.  
See in [Glossary](Glossary.html#Normalmap), the tiling and offset from the
base texture is used.

  * The particle shaders do not support `AlphaTest` or `ColorMask`.
  * Limited feature and lighting support - e.g. some shaders only support one directional light.

[](Built-inShaderGuide.html)

Legacy prebuilt shaders

[](shader-NormalFamily.html)

Normal Shader Family

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

