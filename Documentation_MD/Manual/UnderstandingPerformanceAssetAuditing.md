[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UnderstandingPerformanceAssetAuditing.html)
  * [中文](/cn/current/Manual/UnderstandingPerformanceAssetAuditing.html)
  * [日本語](/ja/current/Manual/UnderstandingPerformanceAssetAuditing.html)
  * [한국어](/kr/current/Manual/UnderstandingPerformanceAssetAuditing.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UnderstandingPerformanceAssetAuditing.html)
  * [中文](/cn/current/Manual/UnderstandingPerformanceAssetAuditing.html)
  * [日本語](/ja/current/Manual/UnderstandingPerformanceAssetAuditing.html)
  * [한국어](/kr/current/Manual/UnderstandingPerformanceAssetAuditing.html)

  * [Optimization](analysis.html)
  * [Understanding optimization in Unity](UnderstandingPerformance.html)
  * Asset auditing

[](UnderstandingPerformance.html)

Understanding optimization in Unity

[](UnderstandingPerformanceStringsAndText.html)

Strings and text

# Asset auditing

Many of the problems found in real projects occur because of honest mistakes –
temporary “test” changes and misclicks by a tired developer can silently add
poorly-performing Assets, or change the import settings of existing Assets.

For any project of significant scale, it is best to have a first line of
defense against human errors. It is relatively simple to write a small piece
of code that ensures that no one can add a 4K uncompressed Texture to a
project.

And yet, this is a surprisingly common problem. A 4K uncompressed Texture
occupies 60 megabytes of memory. On a low-end mobile device, such as an iPhone
4S, it is dangerous to consume more than about 180–200 megabytes of memory. If
added by mistake, this Texture inadvertently occupies between a third and a
quarter of the application’s memory budget, and causes difficult-to-diagnose
out-of-memory errors.

While it is now possible to track these issues down with the 5.3 Memory
**Profiler** A window that helps you to optimize your game. It shows how much
time is spent in the various areas of your game. For example, it can report
the percentage of time spent rendering, animating, or in your game logic.
[More info](Profiler.html)  
See in [Glossary](Glossary.html#Profiler), it is arguably better to make sure
such mistakes are impossible in the first place.

## Using AssetPostprocessor

The `AssetPostprocessor` class in the Unity Editor can be used to enforce
certain minimum standards on a Unity project. This class receives callbacks
when Assets are imported. To use it, inherit from `AssetPostprocessor` and
implement one or more `OnPreprocess` methods. Significant ones include:

  * `OnPreprocessTexture`

  * `OnPreprocessModel`

  * `OnPreprocessAnimation`

  * `OnPreprocessAudio`

See the Scripting Reference on
[AssetPostprocessor](../ScriptReference/AssetPostprocessor.html) for more
possible `OnPreprocess` methods.

    
    
    public class ReadOnlyModelPostprocessor : AssetPostprocessor {
    
       public void OnPreprocessModel() {
    
            ModelImporter modelImporter =
    
     (ModelImporter)assetImporter;
    
            if(modelImporter.isReadable) {
    
                modelImporter.isReadable = false;
    
                modelImporter.SaveAndReimport();
    
            }
    
        }
    
    }
    
    

This is a simple example of an `AssetPostprocessor` enforcing rules on a
project:

This class is called any time a model is imported into the project, or
whenever a model has its import settings changed. The code simply checks to
see if the `Read/Write enabled` flag (represented by the `isReadable`
property) is set to `true`. If it is, it forces the flag to be `false` and
then saves and reimports the Asset.

Note that calling `SaveAndReimport` causes this snippet of code to be called
again! However, because it is now assured that `isReadable` is false, this
code does not produce an infinite reimport loop.

The reason for this change is discussed in the “Models” section, below.

## Common Asset rules

#### Textures

**Disable the read/write enabled flag**

The `Read/Write enabled` flag causes a Texture to be kept twice in memory:
once on the GPU and once in CPU-addressable memory(1) (NOTE: This is because,
on most platforms, readback from GPU memory is extremely slow. Reading a
Texture from GPU memory into a temporary buffer for use by CPU code (e.g.
Texture.GetPixel) would be very nonperformant.). In Unity, this setting is
disabled by default, but it can be accidentally switched on.

`Read/Write Enabled` is only necessary when manipulating Texture data outside
of **Shaders** A program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) (such as with the `Texture.GetPixel`
and `Texture.SetPixel` APIs) and should be avoided whenever possible.

**Disable Mipmaps if possible**

For objects that have a relatively invariant Z-depth relative to the
**Camera** A component which creates an image of a particular viewpoint in
your scene. The output is either drawn to the screen or captured as a texture.
[More info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera), it is possible to disable mipmaps to
save about a third of the memory required to load the Texture. If an object
changes Z-depth, disabling mipmaps can lead to worse Texture sampling
performance on the GPU.

In general, this is useful for **UI**(User Interface) Allows a user to
interact with your application. Unity currently supports three UI systems.
[More info](UI-system-compare.html)  
See in [Glossary](Glossary.html#UI) Textures and other Textures that are
displayed at a constant size on screen.

**Compress all Textures**

Using a texture **compression** A method of storing data that reduces the
amount of storage space it requires. See [Texture Compression](class-
TextureImporterOverride), [Animation Compression](class-
AnimationClip.html#AssetProperties), [Audio Compression](class-
AudioClip.html), [Build Compression](ReducingFilesize.html).  
See in [Glossary](Glossary.html#compression) format suitable for the project’s
target platform is crucial for saving memory.

If the selected **texture compression** 3D Graphics hardware requires Textures
to be compressed in specialized formats which are optimized for fast Texture
sampling. [More info](class-TextureImporterOverride)  
See in [Glossary](Glossary.html#TextureCompression) format is unsuited to the
target platform, Unity decompresses the Texture when the Texture is loaded,
consuming both CPU time and an excessive amount of memory. This is most
commonly a problem on Android devices, which often support vastly different
texture compression formats depending on the chipset.

**Enforce sensible Texture size limits**

While this is simple, it is also very easy to forget to resize a Texture or to
inadvertently alter the Texture size import setting. Determine a sensible
maximum size for different types of Textures and enforce these via code.

For many mobile applications, 2048x2048 or 1024x1024 is sufficient for Texture
atlases, and 512x512 is sufficient for Textures applied to 3D models.

#### Models

**Disable the Read/Write enabled flag**

The`Read/Write enabled` flag for models operates identically to the one
described for Textures. However, it is enabled by default for models.

Unity requires this flag to be enabled if a project is modifying a **Mesh**
The main graphics primitive of Unity. Meshes make up a large part of your 3D
worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs,
Nurms, Subdiv surfaces must be converted to polygons. [More info](mesh.html)  
See in [Glossary](Glossary.html#Mesh) at runtime via script, or if the Mesh is
used as the basis for a MeshCollider component. If the model is not used in a
MeshCollider and is not manipulated by **scripts** A piece of code that allows
you to create your own Components, trigger game events, modify Component
properties over time and respond to user input in any way you like. [More
info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts), disable this flag to save half of
the model’s memory.

**Disable rigs on non-character models**

By default, Unity imports a generic rig for non-character models. This causes
an `Animator` component be to added if the model is instantiated at runtime.
If the model is not animated via the Animation system, this adds unnecessary
overhead to the animation system, because all active Animators must be ticked
once per frame.

Disable the rig on non-animated models to avoid this automatic addition of an
**Animator component** A component on a model that animates that model using
the Animation system. The component has a reference to an Animator Controller
asset that controls the animation. [More info](class-AnimatorController.html)  
See in [Glossary](Glossary.html#AnimatorComponent) and possible inadvertent
addition of unwanted Animators to a **Scene** A Scene contains the
environments and menus of your game. Think of each unique Scene file as a
unique level. In each Scene, you place your environments, obstacles, and
decorations, essentially designing and building your game in pieces. [More
info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene).

**Enable the Optimize Game Objects option on animated models**

The **Optimize Game Objects** option has a significant performance impact on
animated models. When the option is disabled, Unity creates a large transform
hierarchy mirroring the model’s bone structure whenever the model is
instantiated. This transform hierarchy is expensive to update, especially if
other components (such as Particle Systems or Colliders) are attached to it.
It also limits Unity’s ability to multithread Mesh **skinning** The process of
binding bone joints to the vertices of a character’s mesh or ‘skin’. Performed
with an external tool, such as Blender or Autodesk Maya. [More
info](UsingHumanoidChars.html)  
See in [Glossary](Glossary.html#Skinning) and bone animation calculations.

If specific locations on a model’s bone structure need to be exposed (such as
exposing a model’s hands in order to dynamically attach weapon models) then
these locations can be specifically allowed in the `Extra Transforms` list.

Some additional details can be found in the Unity Manual page on the [Model
Importer](https://docs.unity3d.com/Manual/FBXImporter-Rig.html).

**Use Mesh compression when possible**

Enabling Mesh compression reduces the number of bits used to represent the
floating-point numbers for different channels of a model’s data. This can lead
to a minor loss of precision, and the effects of this imprecision should be
checked by artists before use in a final project.

The specific numbers of bits that a given compression level uses are detailed
in the
[ModelImporterMeshCompression](https://docs.unity3d.com/ScriptReference/ModelImporterMeshCompression.html)
Scripting Reference.

Note that it is possible to use different levels of compression for different
channels, so a project may choose to compress only tangents and normals while
leaving UVs and vertex positions uncompressed.

**Note:**Mesh Renderer** A mesh component that takes the geometry from the
Mesh Filter and renders it at the position defined by the object’s Transform
component. [More info](class-MeshRenderer.html)  
See in [Glossary](Glossary.html#MeshRenderer) Settings**

When adding Mesh Renderers to **Prefabs** An asset type that allows you to
store a GameObject complete with components and properties. The prefab acts as
a template from which you can create new object instances in the scene. [More
info](Prefabs.html)  
See in [Glossary](Glossary.html#Prefab) or **GameObjects** The fundamental
object in Unity scenes, which can represent characters, props, scenery,
cameras, waypoints, and more. A GameObject’s functionality is defined by the
Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject), take note of the settings on the
component. By default, Unity enables Shadow casting and receiving, **Light
Probe** Light probes store information about how light passes through space in
your scene. A collection of light probes arranged within a given space can
improve lighting on moving objects and static LOD scenery within that space.
[More info](LightProbes.html)  
See in [Glossary](Glossary.html#LightProbe) sampling, **Reflection Probe** A
rendering component that captures a spherical view of its surroundings in all
directions, rather like a camera. The captured image is then stored as a
Cubemap that can be used by objects with reflective materials. [More
info](class-ReflectionProbe.html)  
See in [Glossary](Glossary.html#ReflectionProbe) sampling, and Motion Vector
calculation.

If a project does not require one or more of these features, ensure that
they’re turned off by an automated script. Any runtime code that adds
MeshRenderers needs to toggle these settings as well.

For 2D games, accidentally adding a MeshRenderer to the Scene with the shadow
options turned on adds a full shadow pass to the rendering loop. This is
generally a waste of performance.

#### Audio

**Platform-appropriate compression settings**

Enable a compression format for audio that matches the available hardware. All
iOS devices include hardware MP3 decompressors, and many Android devices
support Vorbis natively.

Further, import uncompressed audio files into Unity. Unity always recompresses
audio when building a project. There is no need to import compressed audio and
then recompress it; this only serves to degrade the quality of the final
**audio clips** A container for audio data in Unity. Unity supports mono,
stereo and multichannel audio assets (up to eight channels). Unity can import
.aif, .wav, .mp3, and .ogg audio file format, and .xm, .mod, .it, and .s3m
tracker module formats. [More info](class-AudioClip.html)  
See in [Glossary](Glossary.html#AudioClip).

**Force audio clips to mono**

Few mobile devices actually have stereo speakers. On a mobile project, forcing
the imported audio clips to be mono-channel halves their memory consumption.
This setting is also applicable to any audio without stereo effects, such as
most UI sound effects.

**Reduce audio bitrate**

While this requires consultation with an audio designer, attempt to minimize
the bitrate of audio files in order to further save on memory consumption and
built project size.

[](UnderstandingPerformance.html)

Understanding optimization in Unity

[](UnderstandingPerformanceStringsAndText.html)

Strings and text

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

