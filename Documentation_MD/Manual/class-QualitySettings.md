[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/class-QualitySettings.html)
  * [中文](/cn/current/Manual/class-QualitySettings.html)
  * [日本語](/ja/current/Manual/class-QualitySettings.html)
  * [한국어](/kr/current/Manual/class-QualitySettings.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/class-QualitySettings.html)
  * [中文](/cn/current/Manual/class-QualitySettings.html)
  * [日本語](/ja/current/Manual/class-QualitySettings.html)
  * [한국어](/kr/current/Manual/class-QualitySettings.html)

  * [The Unity Editor](unity-editor.html)
  * [Editor Features](EditorFeatures.html)
  * [Project Settings](comp-ManagerGroup.html)
  * Quality

[](class-PresetManager.html)

Preset Manager

[](class-MonoManager.html)

Script Execution Order settings

# Quality

[Switch to Scripting](../ScriptReference/QualitySettings.html "Go to
QualitySettings page in the Scripting Reference")

Unity allows you to set the level of graphical quality it attempts to render.
Generally speaking, quality comes at the expense of frame rate and so it may
be best not to aim for the highest quality on mobile devices or older hardware
since it tends to have a detrimental effect on gameplay. Use the **Quality**
settings (menu: **Edit > Project Settings**, then select the **Quality**
category) to select the **Quality Level** in the Editor for the chosen device.
It is split into two main areas: the Quality matrix appears at the top; and
below it, the settings for the active **Quality Level** appear.

Unity lets you assign a name to a given combination of quality options for
easy reference. The rows of the matrix let you choose which of the different
platforms each **Quality Level** applies to. The **Default** row at the bottom
of the matrix is not a **Quality Level** in itself but rather sets the default
**Quality Level** used for each platform (a green checkbox in a column denotes
the level currently chosen for that platform). Unity comes with six **Quality
Levels** pre-enabled but you can add your own levels.

![Edit the settings for a specific Quality level](../uploads/Main/quality-
settings-panel.png)  
A: The **Quality Level** you have defined in this project.  
B: The currently active **Quality Level**.  
C: The configuration of the current **Quality Level**.  

To delete an unwanted **Quality Level** , use the trashcan icon (the rightmost
column).

To select a **Quality Level** for editing, click on its name in the matrix.

To define a new **Quality Level** , click the **Add Quality Level** button and
type the name for the new level in the **Name** property box.

Then you can choose which of the quality options documented in the following
sections you need to update or set:

  * Rendering
  * TexturesAn image used when rendering a GameObject, Sprite, or UI element. Textures are often applied to the surface of a mesh to give it visual detail. [More info](class-TextureImporter.html)  
See in [Glossary](Glossary.html#texture)

  * ParticlesA small, simple image or mesh that is emitted by a particle system. A particle system can display and move particles in great numbers to represent a fluid or amorphous entity. The effect of all the particles together creates the impression of the complete entity, such as smoke. [More info](class-ParticleSystem.html)  
See in [Glossary](Glossary.html#particle)

  * TerrainThe landscape in your scene. A Terrain GameObject adds a large flat plane to your scene and you can use the Terrain’s Inspector window to create a detailed landscape. [More info](terrain-UsingTerrains.html)  
See in [Glossary](Glossary.html#Terrain)

  * Shadows
  * Async Asset Upload
  * Level of DetailThe _Level Of Detail_ (LOD) technique is an optimization that reduces the number of triangles that Unity has to render for a GameObject when its distance from the Camera increases. [More info](LevelOfDetail.html)  
See in [Glossary](Glossary.html#levelofdetail)

  * Meshes

## Rendering

**Property** | **Description**  
---|---  
****Render Pipeline** A series of operations that take the contents of a
Scene, and displays them on a screen. Unity lets you choose from pre-built
render pipelines, or write your own. [More info](render-pipelines.html)  
See in [Glossary](Glossary.html#Renderpipeline)** | The Render Pipeline Asset to use for this **Quality Level**.  
**Pixel Light Count** | Set the maximum number of **pixel** The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](ShadowPerformance.html)  
See in [Glossary](Glossary.html#pixel) lights when Unity uses [Forward
Rendering](RenderTech-ForwardRendering.html)A rendering path that renders each
object in one or more passes, depending on lights that affect the object.
Lights themselves are also treated differently by Forward Rendering, depending
on their settings and intensity. [More info](RenderTech-ForwardRendering.html)  
See in [Glossary](Glossary.html#ForwardRendering).  
**AntiAliasing** A technique for decreasing artifacts, like jagged lines
(jaggies), in images to make them appear smoother.  
See in [Glossary](Glossary.html#Antialiasing) | Choose the level of Multi-Sample Anti-aliasing (MSAA) that the GPU performs. The options are _Disabled_ , _2x Multi Sampling_ , _4x Multi Sampling_ and _8x Multi Sampling_.  
  
Anti aliasing smooths the appearance of polygon edges. As the level of anti-
aliasing increases, so does the smoothness and the performance cost on the
GPU.  
  
MSAA is compatible only with Forward rendering. For more information on other
types of anti-aliasing and compatibility, see [Post
processing](PostProcessingOverview.html).  
**Realtime Reflection Probes** | Enable this option to update [reflection probes](class-ReflectionProbe.html)A rendering component that captures a spherical view of its surroundings in all directions, rather like a camera. The captured image is then stored as a Cubemap that can be used by objects with reflective materials. [More info](class-ReflectionProbe.html)  
See in [Glossary](Glossary.html#ReflectionProbe) during gameplay.  
**Resolution Scaling Fixed DPI Factor** | Downscales the device’s screen resolution below its native resolution. For more details, see [Android Player](class-PlayerSettingsAndroid.html#Scaling) settings and [iOS Player](class-PlayerSettingsiOS.html#Scaling) settings.  
**V Sync Count** | Choose to synchronize rendering with vertical blanks or not to synchronize at all. Unity can synchronize rendering with the refresh rate of the display device to avoid tearing artifacts. The available options are _Every V Blank_ , _Every Second V Blank_ , or _Don’t Sync_.  
**Realtime GI CPU Usage** | The CPU budget you allow Enlighten Realtime Global Illumination to use for lighting calculations at runtime. Increasing this makes the system react faster to changes in lighting at a cost of using more CPU time.  
**Note:** Some platforms allow all CPUs to be occupied by worker threads
whereas some enforce maximums. For example, some gaming consoles allow a
maximum of 4 CPU cores. For Android devices, if it is a bigLittle
architecture, only the little CPUs are used; otherwise the maximum is one less
than the total number of CPUs. Note that this is only shown for Scriptable
Render Pipelines.  
If you use the Built-in Render Pipeline, you can find this property in the
[graphics settings](class-GraphicsSettings.html).  
  
### Tearing

The picture on the display device is not continuously updated, but rather the
updates happen at regular intervals much like frame updates in Unity. However,
Unity’s updates are not necessarily synchronized with those of the display, so
it is possible for Unity to issue a new frame while the display is still
rendering the previous one. This results in a visual artifact called “tearing”
at the position onscreen where the frame change occurs.

![Simulated example of tearing. The shift in the picture is clearly visible in
the magnified portion.](../uploads/Main/Tearing.jpg) Simulated example of
tearing. The shift in the picture is clearly visible in the magnified portion.

It is possible to get Unity to switch frames only during the period where the
display device is not updating, the so-called “vertical blank”. The **V Sync
Count** option in **Quality** settings synchronizes frame switches with the
device’s vertical blank or optionally with every other vertical blank. The
latter may be useful if the game requires more than one device update to
complete the rendering of a frame.

## Textures

**Property** | **Description**  
---|---  
**Global Mipmap Limit** | Choose the highest resolution mipmap level that Unity uses when it renders textures. Higher mipmap levels have lower resolutions, which means that they require less GPU memory and GPU processing time.  
This property only affects textures with a [texture shape](class-
TextureImporter.html#textureshape) of 2D or 2D Array.  
  
The options are:

  * **0: Full Resolution**
  * **1: Half Resolution**
  * **2: Quarter Resolution**
  * **3: Eighth Resolution**

For more detailed information about what these resolutions mean, see [Mipmaps
introduction](texture-mipmaps-introduction.html).  
Textures that do not have mipmaps render at their full resolution, regardless
of the option you choose.  
**Mipmap Limit Groups** | Use these groups to designate specific textures that should disregard the [globalTextureMipmapLimit](../ScriptReference/QualitySettings-globalTextureMipmapLimit.html) or add a bias. This makes it possible to allocate more of your memory budget for important textures and less of it for less important textures.  
  
This property only affects textures with a [texture shape](class-
TextureImporter.html#textureshape) of 2D or 2D Array.  
  
The options are:

  * **Offset Global Mipmap Limit: –3**
  * **Offset Global Mipmap Limit: –2**
  * **Offset Global Mipmap Limit: –1**
  * **Use Global Mipmap Limit**
  * **Offset Global Mipmap Limit: +1**
  * **Offset Global Mipmap Limit: +2**
  * **Offset Global Mipmap Limit: +3**
  * **Override Global Mipmap Limit: Full Resolution**
  * **Override Global Mipmap Limit: Half Resolution**
  * **Override Global Mipmap Limit: Quarter Resolution**
  * **Override Global Mipmap Limit: Eighth Resolution**

The Offsets bias the Mipmap Limit value for the applicable group of textures.
For example, if the **Global Texture Mipmap Limit** is **Half Resolution** and
you select **Offset Global Mipmap Limit: –1** , then the new Mipmap Limit for
the applicable group of textures is **Full Resolution**.  
  
The Overrides replace the **Global Mipmap Limit** for the applicable group of
textures. For example, if the **Global Texture Mipmap Limit** is **Half
Resolution** and you select **Override Global Mipmap Limit: Full Resolution**
, then the new Mipmap Limit for the applicable group of textures is **Full
Resolution**.  
  
**Note:** If you delete or rename a Mipmap Limit Group, this triggers a dialog
box that provides you with the option to re-import the textures in that group.
Undo does not revert these import changes.  
  
**Anisotropic Textures** | Choose if and how Unity uses anisotropic Textures. The options are _Disabled_ , _Per Texture_ and _Forced On_ (that is, always enabled).  
**Mipmap Streaming**  
| Enable this checkbox to use [Mipmap Streaming](TextureStreaming.html). If
you are not planning to use the Mipmap Streaming system, disable this feature
to avoid any overhead.  
Add All Cameras | Enable this checkbox to make Unity calculate [Mipmap Streaming](TextureStreaming.html) for all active Cameras in the Project. This is enabled by default.   
  
For more information, see [Mipmap Streaming system: Configuring
Cameras](TextureStreaming-configure.html).  
Memory Budget | Set the total amount of memory you want to assign to all loaded textures (in MB) when using the [Mipmap Streaming system](TextureStreaming.html). This is set to 512 MB by default. For more information, see [Mipmap Streaming system: Setting the memory budget](TextureStreaming-configure.html#memory-budget).  
Renderers Per Frame | This controls the CPU processing overhead for the [Mipmap Streaming system](TextureStreaming.html) for the main thread and associated jobs. This is 512 by default (that is, processing 512 Mesh renderers per frame). Lower values reduce processing time, but increase delays to Unity loading the mipmaps.  
Max Level Reduction | Set the maximum number of mipmap levels that the [Mipmap Streaming system](TextureStreaming.html) can discard if the Mipmap Streaming system reaches the **Memory Budget**. This is set to 2 by default (which means that the system discards no more than two mipmap levels).   
  
This value is also the mipmap level that the Mipmap Streaming system initially
loads at startup. For example, when this is set to 2, Unity skips the two
highest mipmap levels on first load.  
  
For more information, see [Mipmap Streaming system: Setting the memory
budget](TextureStreaming-configure.html#memory-budget).  
Max IO Requests | Set the maximum number of texture file in/out (IO) requests from the [MipMap Streaming system](TextureStreaming.html) that are active at any one time. This is set to 1024 by default. This default is set high enough to prevent any IO cap beyond what is already active due to the [Async Upload pipeline](https://unity.com/blog/engine-platform/understanding-the-async-upload-pipeline) or file system itself.  
  
If the Scene Texture content changes significantly and rapidly, the system
might attempt to load more Texture mipmaps than the file IO can keep up with.
Lowering this value reduces the IO bandwidth that the Mipmap Streaming system
generates. The result is a more rapid response to changing mipmap
requirements.  
  
## Particles

**Property** | **Description**  
---|---  
**Soft Particles** Particles that create semi-transparent effects like smoke,
fog or fire. Soft particles fade out as they approach an opaque object, to
prevent intersections with the geometry. [More info](shader-
StandardParticleShaders.html)  
See in [Glossary](Glossary.html#SoftParticles) | Indicates whether to fade particles as they approach the edges of opaque **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject). For more information, see Soft
particles.  
**Particle Raycast Budget** | Set the maximum number of raycasts to use for approximate **particle system** A component that simulates fluid entities such as liquids, clouds and flames by generating and animating large numbers of small 2D images in the scene. [More info](class-ParticleSystem.html)  
See in [Glossary](Glossary.html#particlesystem) **collisions** A collision
occurs when the physics engine detects that the colliders of two GameObjects
make contact or overlap, when at least one has a Rigidbody component and is in
motion. [More info](CollidersOverview.html)  
See in [Glossary](Glossary.html#Collision) (those with _Medium_ or _Low_
quality). See [Particle System Collision Module](class-ParticleSystem.html).  
  
### Soft particles

Soft particles fade out near intersections with other **Scene** A Scene
contains the environments and menus of your game. Think of each unique Scene
file as a unique level. In each Scene, you place your environments, obstacles,
and decorations, essentially designing and building your game in pieces. [More
info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) geometry. This looks much nicer, but is
more resource intensive to process and only works on platforms that support
[depth textures](SL-CameraDepthTexture.html). Furthermore, you have to use the
[Deferred Shading](RenderTech-DeferredShading.html)A rendering path in the
Built-in Render Pipeline that places no limit on the number of Lights that can
affect a GameObject. All Lights are evaluated per-pixel, which means that they
all interact correctly with normal maps and so on. Additionally, all Lights
can have cookies and shadows. [More info](RenderTech-DeferredShading.html)  
See in [Glossary](Glossary.html#Deferredshading) **rendering path** The
technique that a render pipeline uses to render graphics. Choosing a different
rendering path affects how lighting and shading are calculated. Some rendering
paths are more suited to different platforms and hardware than others. [More
info](RenderingPaths.html)  
See in [Glossary](Glossary.html#RenderingPath), or make the **camera** A
component which creates an image of a particular viewpoint in your scene. The
output is either drawn to the screen or captured as a texture. [More
info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera) render [depth textures](SL-
CameraDepthTexture.html) from **scripts** A piece of code that allows you to
create your own Components, trigger game events, modify Component properties
over time and respond to user input in any way you like. [More info](creating-
scripts.html)  
See in [Glossary](Glossary.html#Scripts).

![Without Soft Particles - visible intersections with the
scene.](../uploads/Main/SoftParticlesOff.jpg) Without Soft Particles - visible
intersections with the scene. ![With Soft Particles - intersections fade out
smoothly.](../uploads/Main/SoftParticlesOn.jpg) With Soft Particles -
intersections fade out smoothly.

## Terrain

**Property** | **Description**  
---|---  
****Billboards** A textured 2D object that rotates so that it always faces the
Camera. [More info](class-BillboardRenderer.html)  
See in [Glossary](Glossary.html#Billboard) Face Camera Position** | Enable this option to force billboards to face the camera while rendering instead of the camera plane. This produces a better, more realistic image, but is more expensive to render.  
**Use Legacy Details Distribution** | Enable this option to use the previously supported scattering algorithm that often resulted in overlapping details. Included for backward compatibility with Terrains authored in Unity 2022.1 and earlier.  
**Terrain Setting Overrides** | Various override settings that, when enabled, override the value of all active terrains (except those with the “Ignore Quality Settings” setting enabled). For more information about these settings, see [Terrain Settings](terrain-OtherSettings.html).  
Pixel Error | Value set to Terrain Pixel Error. See [Terrain Settings](terrain-OtherSettings.html).  
Base Map Dist. | Value set to Terrain Basemap Distance. See [Terrain Settings](terrain-OtherSettings.html).  
Detail Density Scale | Value set to Terrain Density Scale. See [Terrain Settings](terrain-OtherSettings.html).  
Detail Distance | Value set to Terrain Detail Distance. See [Terrain Settings](terrain-OtherSettings.html).  
Tree Distance | Value set to Terrain Tree Distance. See [Terrain Settings](terrain-OtherSettings.html).  
Billboard Start | Value set to Terrain Billboard Start. See [Terrain Settings](terrain-OtherSettings.html).  
Fade Length | Value set to Terrain Fade Length. See [Terrain Settings](terrain-OtherSettings.html).  
Max **Mesh** The main graphics primitive of Unity. Meshes make up a large part
of your 3D worlds. Unity supports triangulated or Quadrangulated polygon
meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More
info](mesh.html)  
See in [Glossary](Glossary.html#Mesh) Trees | Value set to Terrain Max Mesh Trees. See [Terrain Settings](terrain-OtherSettings.html).  
  
## Shadows

**Property** | **Description**  
---|---  
**Shadowmask Mode** | Choose the shadowmask behavior when using the [Shadowmask](lighting-mode.html#shadowmask) Mixed lighting mode. Use the Lighting window (menu: **Window** > **Rendering** > **Lighting**) to set this up in your Scene.  
| **Distance Shadowmask** A version of the Shadowmask lighting mode that
includes high quality shadows cast from static GameObjects onto dynamic
GameObjects. [More info](lighting-mode.html#shadowmask)  
See in [Glossary](Glossary.html#DistanceShadowmask) | Unity uses real-time shadows up to the **Shadow Distance** , and baked shadows beyond it.  
| **Shadowmask** A Texture that shares the same UV layout and resolution with
its corresponding lightmap. [More info](lighting-mode.html#shadowmask)  
See in [Glossary](Glossary.html#Shadowmask) | Static GameObjects that cast shadows always cast baked shadows.  
**Shadows** A UI component that adds a simple outline effect to graphic
components such as Text or Image. It must be on the same GameObject as the
graphic component. [More
info](https://docs.unity3d.com/Packages/com.unity.ugui@latest/index.html?subfolder=/manual/script-
Shadow.html)  
See in [Glossary](Glossary.html#Shadow) | Choose which type of shadows to use. The available options are _Hard and Soft Shadows_ , _Hard Shadows Only_ and _Disable Shadows_.  
**Shadow Resolution** | Choose which resolution to render shadows at. The available options are _Low Resolution_ , _Medium Resolution_ , _High Resolution_ and _Very High Resolution_. The higher the resolution, the greater the processing overhead.  
**Shadow Projection** | Choose which method to use for projecting shadows from a directional light.  
| **Close Fit** | Renders higher resolution shadows but they can sometimes wobble slightly if the camera moves.  
| **Stable Fit** | Renders lower resolution shadows but they don’t wobble with camera movements.  
**Shadow Distance** | Enter the maximum distance from the Camera at which shadows are visible. Unity does not render shadows that fall beyond this distance.  
**Shadow Near Plane Offset** | Enter the offset shadow near plane to account for large triangles being distorted by shadow pancaking.  
**Shadow Cascades** | Choose the number of shadow cascades to use. The available options are _No Cascades_ , _Two Cascades_ , or _Four Cascades_. A higher number of cascades gives better quality but at the expense of processing overhead (see [Shadow Cascades](shadow-cascades.html) for further details).  
**Cascade splits** | Adjust the cascade shadow split(s) by moving the vertical line between each cascade left or right.  
Depending on what value you chose for the **Shadow Cascades** setting, you can
see two or four different colors. If **Shadow Cascades** is set to _No
Cascades_ , then this entire control is hidden.  
  
## Async Asset Upload

**Property** | **Description**  
---|---  
**Time Slice** | Set the amount of CPU time in milliseconds per frame Unity spends uploading buffered Texture and Mesh data to the GPU. See [LoadingTextureandMeshData](LoadingTextureandMeshData.html).  
**Buffer Size** | Set the size in megabytes of the Async Upload Buffer Unity uses to stream Texture and Mesh data for the to the GPU. See [LoadingTextureandMeshData](LoadingTextureandMeshData.html).  
**Persistent Buffer** | Indicates whether the upload buffer should persist even when there is nothing left to upload.  
  
## Level of Detail

**Property** | **Description**  
---|---  
**Lod Bias** | Set the level-of-detail (LOD) bias.   
LOD levels are chosen based on the onscreen size of an object. When the size
is between two LOD levels, the choice can be biased toward the less detailed
or more detailed of the two Models available. This is set as a fraction from 0
to +infinity. When it is set between 0 and 1 it favors less detail. A setting
of more than 1 favors greater detail. For example, setting LOD Bias to 2 and
having it change at 50% distance, LOD actually only changes on 25%.  
**Maximum LOD Level** | Set the highest LOD that the game uses. See Maximum LOD level for more information.  
  
### Maximum LOD level

Unity does not use Models which have a LOD below the MaximumLOD level and
omits them from the build (which saves storage and memory space). Unity uses
the smallest LOD value from all the MaximumLOD values linked with the
**Quality** settings for the target platform. If an LOD level is included,
then Models from that LODGroup are included in the build and always loaded at
runtime for that LODGroup, regardless of the Quality setting being used. As an
example, if LOD level 0 is used in any Quality setting then all the LOD levels
are included in the build and all the referenced Models load at runtime.

## Meshes

**Property** | **Description**  
---|---  
**Skin Weights** | Choose the number of bones that can affect a given vertex during an animation. The available options are _1 Bone_ , _2 Bones_ , _4 Bones_ , and _Unlimited_.  
  
  

* * *

  * Terrain Quality Setting Overrides added in 2022.2

QualitySettings

[](class-PresetManager.html)

Preset Manager

[](class-MonoManager.html)

Script Execution Order settings

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

