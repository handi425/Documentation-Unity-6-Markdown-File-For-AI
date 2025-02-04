[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/RefProbePerformance.html)
  * [中文](/cn/current/Manual/RefProbePerformance.html)
  * [日本語](/ja/current/Manual/RefProbePerformance.html)
  * [한국어](/kr/current/Manual/RefProbePerformance.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/RefProbePerformance.html)
  * [中文](/cn/current/Manual/RefProbePerformance.html)
  * [日本語](/ja/current/Manual/RefProbePerformance.html)
  * [한국어](/kr/current/Manual/RefProbePerformance.html)

  * [Lighting](LightingOverview.html)
  * [Reflections](reflections-landing.html)
  * Optimize reflections

[](ReflectionProbes-EnableReflectionsOfReflections.html)

Enable reflections of reflections

[](AdvancedRefProbe.html)

Troubleshooting reflections

# Optimize reflections

Rendering a **reflection probe** A rendering component that captures a
spherical view of its surroundings in all directions, rather like a camera.
The captured image is then stored as a Cubemap that can be used by objects
with reflective materials. [More info](class-ReflectionProbe.html)  
See in [Glossary](Glossary.html#ReflectionProbe)’s **cubemap** A collection of
six square textures that can represent the reflections in an environment or
the skybox drawn behind your geometry. The six squares form the faces of an
imaginary cube that surrounds an object; each face represents the view along
the directions of the world axes (up, down, left, right, forward and back).
[More info](class-Cubemap-landing.html)  
See in [Glossary](Glossary.html#Cubemap) takes a significant amount of
processor time for a number of reasons:

  1. Each of the six cubemap faces must be rendered separately using a “**camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera)” at the probe’s origin.

  2. The probes will need to be rendered a separate time for each reflection bounce level (see documentation on [Advanced Reflection Probes](AdvancedRefProbe.html) for further details).

  3. The various mipmap levels of the cubemap must undergo a blurring process to allow for glossy reflections.

The time taken to render the probes affects the baking workflow in the editor
and, more importantly, runtime performance of the player. Below are some tips
for keeping the performance impact of reflection probes to a minimum.

## General tips

The following issues affect both offline baking _and_ runtime performance.

### Resolution

The higher the resolution of a cubemap, the greater its rendering time will
be. You can optimise probes by setting lower resolutions in places where the
reflection detail is less important (for example, if a reflective object is
small and/or distant then it will naturally show less detail). Higher
resolutions should still be used wherever the detail will be noticeable.

### Culling Mask

A standard technique to improve a normal camera’s performance is to use the
**Culling Mask** Allows you to include or omit objects to be rendered by a
Camera, by Layer.  
See in [Glossary](Glossary.html#CullingMask) property to avoid rendering
insignificant objects; the technique works equally well for reflection probes.
For example, if your **Scene** A Scene contains the environments and menus of
your game. Think of each unique Scene file as a unique level. In each Scene,
you place your environments, obstacles, and decorations, essentially designing
and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) contains many small objects (eg, rocks
and plants) you might consider putting them all on the same layer and then
using the culling mask to avoid rendering them in the reflection.

### Texture compression

To optimize the rendering time and lower the GPU memory consumption, use
texture compression. To control texture compression for baked Reflection
Probes, open the Lighting window (menu: **Window** > **Rendering** >
**Lighting**), navigate to **Environmental Lighting** > **Reflections** and
use the **Compression** A method of storing data that reduces the amount of
storage space it requires. See [Texture Compression](class-
TextureImporterOverride), [Animation Compression](class-
AnimationClip.html#AssetProperties), [Audio Compression](class-
AudioClip.html), [Build Compression](ReducingFilesize.html).  
See in [Glossary](Glossary.html#compression) drop-down menu. Note that real-
time Reflection Probes are not compressed in memory, and their size in memory
depends on Resolution and HDR settings. Because of this, sampling real-time
Reflection Probes is usually more resource-intensive than sampling baked
Reflection Probes.

## Real-time probe optimization

The rendering overhead is generally more significant for real-time probes than
for those baked in the editor. Updates are potentially quite frequent and this
can have an impact on frame rate if not managed correctly. With this in mind,
real-time probes provide the following properties to let you handle probe
rendering as efficiently as possible:

### Refresh Mode

The **Refresh Mode** lets you choose when the probe will update. The most
resource-intensive option in terms of processor time is **Every Frame**. This
gives the most frequent updates with minimal programming effort but you may
encounter performance problems if you use this mode for all probes.

If the mode is set to **On Awake** , the probe will be updated at runtime but
only once at the start of the scene. This is useful if the scene (or part of
it) is set up at run-time but does not change during its lifetime.

The final mode, **Via Scripting** , lets you control probe updates from a
script. Although some effort is involved in coding the script, this approach
does allow for useful optimisations. For example, you might update a probe
according to the apparent size of passing objects (ie, small objects or large
objects at a distance are not worth an update).

### Time Slicing

When the **Refresh Mode** described above is set to **Every Frame** the
processing load can be considerable. **Time Slicing** allows you to spread the
cost of updates over several frames and thereby reduce the load at any given
time. This property has three different options:

  1. **All Faces at Once** will cause the six cubemap faces to be rendered immediately (on the same frame) but then the blurring operation for each of the six first level mipmaps will take place on separate frames. The remaining mipmaps will then be blurred on a single frame and the results copied to the cubemap on another frame. The full update therefore takes nine frames to complete.

  2. **Individual Faces** works the same way as **All Faces at Once** except that the initial rendering of each cubemap face takes place on its own frame (instead of all six on the first frame). The full update takes fourteen frames to complete; this option has the lowest impact on frame rate but the relative long update time might be noticeable when, say, lighting conditions change abruptly, for example, a lamp is suddenly switched on.

  3. **No Time Slicing** disables the time slicing operation completely and so each probe update takes place within a single frame. This ensures that the reflections are synchronised exactly with the appearance of surrounding objects but the processing cost can be prohibitive.

As with the other optimisations, you should consider using the lower-quality
options in places where reflections are less important and save the **No Time
Slicing** option for places where the detail will be noticed.

  

##  

  * Updated in 5.6

  * 2017–06–06 Page published 

[](ReflectionProbes-EnableReflectionsOfReflections.html)

Enable reflections of reflections

[](AdvancedRefProbe.html)

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

