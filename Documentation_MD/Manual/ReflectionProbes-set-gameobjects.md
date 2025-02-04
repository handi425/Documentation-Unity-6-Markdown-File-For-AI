[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/ReflectionProbes-set-gameobjects.html)
  * [中文](/cn/current/Manual/ReflectionProbes-set-gameobjects.html)
  * [日本語](/ja/current/Manual/ReflectionProbes-set-gameobjects.html)
  * [한국어](/kr/current/Manual/ReflectionProbes-set-gameobjects.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/ReflectionProbes-set-gameobjects.html)
  * [中文](/cn/current/Manual/ReflectionProbes-set-gameobjects.html)
  * [日本語](/ja/current/Manual/ReflectionProbes-set-gameobjects.html)
  * [한국어](/kr/current/Manual/ReflectionProbes-set-gameobjects.html)

  * [Lighting](LightingOverview.html)
  * [Reflections](reflections-landing.html)
  * Add GameObjects to reflections

[](UsingReflectionProbes.html)

Place a Reflection Probe

[](ReflectionProbes-set-gameobjects-use.html)

Set GameObjects to use Reflection Probes

# Add GameObjects to reflections

## Add GameObjects to baked Reflection Probes

The reflections captured by baked probes can only include **scene** A Scene
contains the environments and menus of your game. Think of each unique Scene
file as a unique level. In each Scene, you place your environments, obstacles,
and decorations, essentially designing and building your game in pieces. [More
info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) objects marked as ****Reflection
Probe** A rendering component that captures a spherical view of its
surroundings in all directions, rather like a camera. The captured image is
then stored as a Cubemap that can be used by objects with reflective
materials. [More info](class-ReflectionProbe.html)  
See in [Glossary](Glossary.html#ReflectionProbe) Static** (using the
**Static** menu at the top left of the inspector panel for all objects). You
can further refine the objects that get included in the reflection **cubemap**
A collection of six square textures that can represent the reflections in an
environment or the skybox drawn behind your geometry. The six squares form the
faces of an imaginary cube that surrounds an object; each face represents the
view along the directions of the world axes (up, down, left, right, forward
and back). [More info](class-Cubemap-landing.html)  
See in [Glossary](Glossary.html#Cubemap) using the ****Culling Mask** Allows
you to include or omit objects to be rendered by a Camera, by Layer.  
See in [Glossary](Glossary.html#CullingMask)** and ****Clipping Planes** A
plane that limits how far or close a camera can see from its current position.
A camera’s viewable range is between the far and near clipping planes. See far
clipping plane and near clipping plane. [More info](class-Camera.html)  
See in [Glossary](Glossary.html#clippingplane)** properties, which work the
same way as for a [Camera](class-Camera.html)A component which creates an
image of a particular viewpoint in your scene. The output is either drawn to
the screen or captured as a texture. [More info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera) (the probe is essentially like a
camera that is rotated to view each of the six cubemap faces).

## Add GameObjects to realtime Reflection Probes

You don’t need to mark objects as **Reflection Probe Static** to capture their
reflections (as you would with a baked probe). However, you can selectively
exclude objects from the reflection cubemap using the **Culling Mask** and
**Clipping Planes** properties, which work the same way as for a
[Camera](class-Camera.html) (the probe is essentially like a camera that is
rotated to view each of the six cubemap faces).

## Update Reflection Probes

To update probes, do one of the following:

  * In a probe’s ****Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector)** window, select **Bake**.

  * In the Lighting window, select **Generate Lighting**. This updates all probes.

The bake process will take place asynchronously while you continue to work in
the editor. If you move any static objects, change their materials or
otherwise alter their visual appearance during the baking process, you must
rebake to see the updated results.

**Note** : Currently, real-time probes will only update their reflections in
the **Scene view** An interactive view into the world you are creating. You
use the Scene View to select and position scenery, characters, cameras,
lights, and all other types of Game Object. [More
info](UsingTheSceneView.html)  
See in [Glossary](Glossary.html#SceneView) when **Reflection Probe Static**
objects are moved or change their appearance. This means that moving dynamic
objects won’t cause an update even though those objects appear in the
reflection. You should choose the **Bake Reflection Probes** option from the
**Generate Lighting** button dropdown in the [Lighting window](lighting-
window.html) to update reflections when a dynamic object is changed.

[](UsingReflectionProbes.html)

Place a Reflection Probe

[](ReflectionProbes-set-gameobjects-use.html)

Set GameObjects to use Reflection Probes

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

