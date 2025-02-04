[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/class-TextureImporter.html)
  * [中文](/cn/current/Manual/class-TextureImporter.html)
  * [日本語](/ja/current/Manual/class-TextureImporter.html)
  * [한국어](/kr/current/Manual/class-TextureImporter.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/class-TextureImporter.html)
  * [中文](/cn/current/Manual/class-TextureImporter.html)
  * [日本語](/ja/current/Manual/class-TextureImporter.html)
  * [한국어](/kr/current/Manual/class-TextureImporter.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Textures](Textures-landing.html)
  * [Textures reference](textures-reference.html)
  * Texture Import Settings window reference

[](textures-reference.html)

Textures reference

[](texture-type-default.html)

Default texture Import Settings window reference

# Texture Import Settings window reference

[Switch to Scripting](../ScriptReference/TextureImporter.html "Go to
TextureImporter page in the Scripting Reference")

The **Texture Import Settings** window defines how Unity imports images from
your project’s `Assets` folder into the Unity Editor.

To access this window, select the image file in the **Project window** A
window that shows the contents of your `Assets` folder (Project tab) [More
info](ProjectView.html)  
See in [Glossary](Glossary.html#Projectwindow). The **Texture Import
Settings** window appears in the **Inspector** A Unity window that displays
information about the currently selected GameObject, asset or project
settings, allowing you to inspect and edit the values. [More
info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector).

**Note:** Some of the less commonly used properties are hidden by default.
Expand the Advanced section in the Inspector window to view these properties.

![The Texture Import Settings window](../uploads/Main/class-
TextureImporter.png) The Texture Import Settings window

There are several sections on the Texture Import Settings window:

**(A)** Texture Type. Select the type of Texture you want to create.

**(B)** Texture Shape. Select the shape and set properties specific to that
shape in this area.

**(C)** Type-specific and advanced properties. Depending on what **Texture
Type** value you select, extra properties might appear in this area.

**(D)** Platform-specific overrides. Use the **Platform-specific overrides**
panel to set default options and their overrides for a specific platforms.

**(E)** **Texture preview**. You can preview the Texture and adjust its values
here.

## Texture Type

Use the **Texture Type** property to select the type of Texture you want to
create from the source image file. The other properties in the Texture Import
settings window change depending on the value you set.

The following table lists the available texture types and explains their
purpose.

**Property** | **Function**  
---|---  
**Default** | This is the most common setting used for all Textures. It provides access to most of the properties for Texture importing. For more information, see the [Default](texture-type-default.html) Texture type.  
**Normal map** A type of Bump Map texture that allows you to add surface
detail such as bumps, grooves, and scratches to a model which catch the light
as if they are represented by real geometry.  
See in [Glossary](Glossary.html#Normalmap) | The **Normal map** texture type formats the texture asset so it’s suitable for real-time normal mapping. For more information, see the [Normal map](texture-type-normal-map.html) texture type documentation.   
  
For more information on normal mapping in general, see [Importing
Textures](texture-type-normal-map.html).  
**Editor GUI and Legacy GUI** | The **Editor GUI and Legacy GUI** texture type formats the texture asset so it’s suitable for HUD and GUI controls. For more information, see the [Editor GUI and Legacy GUI](texture-type-editor-gui-and-legacy-gui.html) texture type documentation.  
**Sprite (2D and UI)** | The **Sprite (2D and UI)** texture type formats the texture asset so it’s suitable to use in 2D applications as a [Sprite](sprite/sprite-landing.html)A 2D graphic objects. If you are used to working in 3D, Sprites are essentially just standard textures but there are special techniques for combining and managing sprite textures for efficiency and convenience during development. [More info](sprite/sprite-landing.html)  
See in [Glossary](Glossary.html#Sprite). For more information, see the [Sprite
(2D and UI)](texture-type-sprite.html) texture type documentation.  
**Cursor** | The **Cursor** texture type formats the texture asset so it’s suitable to use as a custom mouse cursor. For more information, see the [Cursor](texture-type-cursor.html) texture type documentation.  
**Cookie** | The **Cookie** texture type formats the texture asset so it’s suitable to use as a [light cookie](Cookies.html) in the Built-in **Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](render-pipelines.html)  
See in [Glossary](Glossary.html#Renderpipeline). For more information, see the
[Cookie](texture-type-cookie.html) texture type documentation.  
**Lightmap** A pre-rendered texture that contains the effects of light sources
on static objects in the scene. Lightmaps are overlaid on top of scene
geometry to create the effect of lighting. [More info](Lightmapping.html)  
See in [Glossary](Glossary.html#Lightmap) | The **Lightmap** texture type formats the texture asset so it’s suitable to use as a [Lightmap](class-LightmapParameters.html). This option enables encoding into a specific format (RGBM or dLDR depending on the platform) and a **post-processing** A process that improves product visuals by applying filters and effects before the image appears on screen. You can use post-processing effects to simulate physical camera and film properties, for example Bloom and Depth of Field. [More info](PostProcessingOverview.html) post processing, postprocessing, postprocess  
See in [Glossary](Glossary.html#post-processing) step on texture data (a push-
pull dilation pass). For more information, see the [Lightmap](texture-type-
lightmap.html) texture type documentation.  
**Directional Lightmap** | The **Directional Lightmap** texture type formats the texture asset so it’s suitable to use as a directional [Lightmap](class-LightmapParameters.html). For more information, see the [Directional Lightmap](texture-type-directional-lightmap.html) texture type documentation.  
**Shadowmask** | The **Shadowmask** texture type formats the texture asset so it’s suitable to use as a [shadowmask](lighting-mode.html#shadowmask)A Texture that shares the same UV layout and resolution with its corresponding lightmap. [More info](lighting-mode.html#shadowmask)  
See in [Glossary](Glossary.html#Shadowmask). For more information, see the
[Shadowmask](texture-type-shadowmask.html) texture type documentation.  
**Single Channel** | The **Single Channel** texture type formats the texture asset so it only has one channel. For information on the properties available only for the this type, see the [Single Channel](texture-type-singlechannel.html) texture type documentation.  
  
## Texture Shape

Use the **Texture Shape** property to select and define the shape and
structure of the Texture. There are four shape types:

  * **2D** is the most common setting for all Textures; it defines the image file as a 2D Texture. These are used to map Textures to 3D Meshes and GUI elements, among other Project elements.
  * **Cube** defines the Texture as a [cubemap](class-Cubemap-landing.html)A collection of six square textures that can represent the reflections in an environment or the skybox drawn behind your geometry. The six squares form the faces of an imaginary cube that surrounds an object; each face represents the view along the directions of the world axes (up, down, left, right, forward and back). [More info](class-Cubemap-landing.html)  
See in [Glossary](Glossary.html#Cubemap). You could use this for Skyboxes or
**Reflection Probes** A rendering component that captures a spherical view of
its surroundings in all directions, rather like a camera. The captured image
is then stored as a Cubemap that can be used by objects with reflective
materials. [More info](class-ReflectionProbe.html)  
See in [Glossary](Glossary.html#ReflectionProbe), for example. This type is
only available with the [Default](texture-type-default.html), [Normal
Map](texture-type-normal-map.html), and [Single Channel](texture-type-
singlechannel.html) Texture types.

  * **2D Array** defines the Texture as a [2D array texture](class-Texture2DArray.html). This is commonly used as an optimization for some rendering techniques, where many textures of the same size & format are used.
  * **3D** defines the Texture as a [3D texture](class-Texture3D.html). 3D textures are used by some rendering techniques to represent volumetric data.

### 2D Array and 3D columns and rows

When you set the **Texture Shape** property to **2D Array** or **3D** , Unity
displays the **Columns** and **Rows** properties. Use these to tell Unity how
to divide the flipbook texture into cells.

**Property:** | **Function:**  
---|---  
**Columns** | The number of columns that the source flipbook texture is divided into.  
**Rows** | The number of rows that the source flipbook texture is divided into.  
  
## Type-specific and advanced properties

Depending on which **Texture Type** you select, different properties can
appear in the Texture Import Settings window. Some of these properties are
specific to the Texture Type itself, such as **Sprite Mode** available with
the [Sprite (2D and UI)](texture-type-sprite.html) type.

Use Advanced settings to make finer adjustments to the way Unity handles the
Texture. The order and availability of these settings can vary depending on
the **Texture Type** you choose.

For information on the properties for each texture type, see the documentation
for that texture type:

  * [Default](texture-type-default.html)
  * [Normal map](texture-type-normal-map.html)
  * [Editor GUI and Legacy GUI](texture-type-editor-gui-and-legacy-gui.html)
  * [Sprite (2D and UI)](texture-type-sprite.html)
  * [Cursor](texture-type-cursor.html)
  * [Cookie](texture-type-cookie.html)
  * [Lightmap](texture-type-lightmap.html)
  * [Directional Lightmap](texture-type-directional-lightmap.html)
  * [Shadowmask](texture-type-shadowmask.html)
  * [Single Channel](texture-type-singlechannel.html)

## Platform-specific overrides

The following table describes which properties are available:

**Property:** | **Function:**  
---|---  
**Max Size** | Set the maximum imported Texture dimensions in **pixels** The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](ShadowPerformance.html)  
See in [Glossary](Glossary.html#pixel). Artists often prefer to work with huge
dimension-size Textures, but you can scale down the Texture to a suitable
dimension-size.  
**Resize Algorithm** | Choose an algorithm for downscaling the Texture when the Texture dimensions are larger than the specified **Max Size**.  
| **Mitchell** | Resize the Texture using the Mitchell algorithm. This is the default resize algorithm.  
| **Bilinear** | Resize the Texture using bilinear interpolation. For images where small, sharp details are important, this can preserve more of these details than Mitchell.  
**Format** | Bypass the automatic system to specify what internal representation to use for the Texture. The list of available formats depends on the platform and Texture type. For more information, see [Texture formats for platform-specific overrides](class-TextureImporterOverride).   
  
**Note:** Even when you don’t override a platform, this option shows the
format chosen by the automatic system. This property is only available when
overriding for a specific platform, and not as a default setting.  
**Compression** A method of storing data that reduces the amount of storage
space it requires. See [Texture Compression](class-TextureImporterOverride),
[Animation Compression](class-AnimationClip.html#AssetProperties), [Audio
Compression](class-AudioClip.html), [Build
Compression](ReducingFilesize.html).  
See in [Glossary](Glossary.html#compression) | Choose the compression type for the Texture. This helps Unity choose the right compression format for a Texture. Depending on the platform and the availability of compression formats, different settings might end up with the same internal format. For example, **Low Quality Compression** affects mobile platforms, but not desktop platforms.  
| **None** | Do not compress the Texture.  
| **Low Quality** | Compress the Texture in a low-quality format. This might use less memory than **Normal Quality**.  
| **Normal Quality** | Compress the Texture using a standard format.  
| **High Quality** | Compress the Texture in a high-quality format. This might use more memory than **Normal Quality**.  
**Use Crunch Compression** | Use crunch compression, if applicable. Crunch is a lossy compression format on top of DXT or ETC **Texture compression** 3D Graphics hardware requires Textures to be compressed in specialized formats which are optimized for fast Texture sampling. [More info](class-TextureImporterOverride)  
See in [Glossary](Glossary.html#TextureCompression). Unity decompresses
Textures to DXT or ETC on the CPU and then uploads them to the GPU at runtime.
Crunch compression helps the Texture use the lowest possible amount of space
on disk and for downloads. Crunch Textures can take a long time to compress,
but decompression at runtime is very fast.  
**Compressor Quality** | When using Crunch Texture compression, use the slider to adjust the quality. A higher compression quality means larger Textures and longer compression times.  
  
**Note:** For Android platforms, the Compressor Quality values provide
slightly different options. For more information, see [Texture formats for
platform-specific overrides](class-TextureImporterOverride).  
**Split Alpha Channel** | Allows alpha splitting for this Texture on these platforms: **tvOS** , **iOS** , and **Android**. For more information, see the [Notes on Android for Texture compression formats](class-TextureImporterOverride#android).  
**Override ETC2 fallback** | ETC2 texture decompression fallback override on Android devices that don’t support ETC2.  
  
Allows to choose which texture format to decompress the texture to on Android
devices that have no ETC2 texture format support. For more information, see
the [Notes on Android for Texture compression formats](class-
TextureImporterOverride#android).  
  
[](textures-reference.html)

Textures reference

[](texture-type-default.html)

Default texture Import Settings window reference

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

