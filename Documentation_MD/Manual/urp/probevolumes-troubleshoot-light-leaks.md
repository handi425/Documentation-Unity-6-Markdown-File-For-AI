[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/probevolumes-troubleshoot-light-leaks.html)
  * [中文](/cn/current/Manual/urp/probevolumes-troubleshoot-light-leaks.html)
  * [日本語](/ja/current/Manual/urp/probevolumes-troubleshoot-light-leaks.html)
  * [한국어](/kr/current/Manual/urp/probevolumes-troubleshoot-light-leaks.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/probevolumes-troubleshoot-light-leaks.html)
  * [中文](/cn/current/Manual/urp/probevolumes-troubleshoot-light-leaks.html)
  * [日本語](/ja/current/Manual/urp/probevolumes-troubleshoot-light-leaks.html)
  * [한국어](/kr/current/Manual/urp/probevolumes-troubleshoot-light-leaks.html)

  * [Lighting](../LightingOverview.html)
  * [Lighting in URP](../urp/lighting-landing.html)
  * [Adaptive Probe Volumes (APV) in URP](../urp/probevolumes.html)
  * [Troubleshooting Adaptive Probe Volumes](../urp/probevolumes-fixissues.html)
  * Troubleshooting light leaks in Adaptive Probe Volumes in URP

[](../urp/probevolumes-troubleshoot-artefacts.html)

Troubleshooting dark blotches or streaks in Adaptive Probe Volumes in URP

[](../urp/probevolumes-inspector-reference.html)

Adaptive Probe Volume Inspector reference

# Troubleshooting light leaks in Adaptive Probe Volumes in URP

Light leaks are areas that are too light or dark, often in the corners of a
wall or ceiling.

![A light leak.](../../uploads/urp/probe-volumes/probevolumes-lightleak.JPG)  
  

Light leaks often occur when geometry receives light from a **Light Probe**
Light probes store information about how light passes through space in your
scene. A collection of light probes arranged within a given space can improve
lighting on moving objects and static LOD scenery within that space. [More
info](../LightProbes.html)  
See in [Glossary](../Glossary.html#LightProbe) that isn’t visible to the
geometry, for example because the Light Probe is on the other side of a wall.
Adaptive Probe Volumes use regular grids of Light Probes, so Light Probes
might not follow walls or be at the boundary between different lighting areas.

To fix light leaks, you can do the following:

  * Create thicker walls.
  * Add an Adaptive Probe Volumes Options override to your scene.
  * Enable Rendering Layers.
  * Adjust Baking Set properties.
  * Use a Probe Adjustment Volume.

### Create thicker walls

Adjust walls so their width is closer to the distance between probes in the
local [brick](probevolumes-concept.html#how-probe-volumes-work)

### Add an Adaptive Probe Volumes Options override to your scene

You can add a [Volume](volumes-landing-page.html), then add an **Adaptive
Probe Volumes Options** override to the Volume. This adjusts the position that
**GameObjects** The fundamental object in Unity scenes, which can represent
characters, props, scenery, cameras, waypoints, and more. A GameObject’s
functionality is defined by the Components attached to it. [More
info](../class-GameObject.html)  
See in [Glossary](../Glossary.html#GameObject) use to sample the Light Probes.

  1. Add a [Volume](set-up-a-volume.html) to your **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](../CreatingScenes.html)  
See in [Glossary](../Glossary.html#Scene) and make sure its area overlaps the
**camera** A component which creates an image of a particular viewpoint in
your scene. The output is either drawn to the screen or captured as a texture.
[More info](../CamerasOverview.html)  
See in [Glossary](../Glossary.html#Camera) position.

  2. Select **Add Override** , then select **Lighting** > **Adaptive Probe Volumes Options**.
  3. Enable **Normal Bias** , then adjust the value to move the position that GameObject pixels use to sample the Light Probes, along the **pixel** The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](../ShadowPerformance.html)  
See in [Glossary](../Glossary.html#pixel)’s surface normal.

  4. Enable **View Bias** , then adjust the value to move the position that GameObject pixels use to sample the Light Probes, towards the camera.
  5. Disable and enable **Leak Reduction Mode** to check if it improves light leaks.

Volumes only affect the scene if the camera is near or inside the volume.
Refer to [Understand volumes](Volumes.html) for more information.

Refer to [Probe Volumes Options Override reference](probevolumes-options-
override-reference.html) for more information on **Adaptive Probe Volumes
Options** settings.

### Use Rendering Layer Masks

You can configure the **Rendering**Layer Masks** A value defining which layers
to include or exclude from an operation, such as rendering, collision or your
own code. [More info](../Layers.html)  
See in [Glossary](../Glossary.html#LayerMask)** in the [Adaptive Probe Volumes
panel](probevolumes-lighting-panel-reference.html) in the Lighting window.
This allow APV to assign a Rendering Layer Mask to each Light Probe.

For performance reasons, Adaptive Probe Volumes only supports up to 4
Rendering Layers Masks. You can use the list to create a new mask and use the
dropdown to assign it any Rendering Layer. When lighting is generated, Unity
will try to automatically assign a mask to each probe by looking at the
Rendering Layer Masks of objects surrounding the probe. Additionally, you can
use a **Probe Adjustment Volume** to override the Rendering Layer Mask
assigned to Light Probes.

At runtime, renderers will only sample lighting data from probes that have a
matching Rendering Layer Mask. If the object doesn’t match any of the Masks
defined in the Lighting window, it will sample lighting from all the valid
surrounding probes. Note that this feature requires **Use Rendering Layers**
to be enabled in the URP Asset.

For example, in order to fix light leaking issues, you can create an Interior
and an Exterior Rendering Layer Mask to ensure interior objects will never
sample lighting data from exterior probes and fix light leaking through the
walls. A renderer can have several Rendering Layers enabled in it’s Rendering
Layer Masks. This is useful when dealing with dynamic objects that may want to
sample lighting from both the exterior and interior probes.

You can visualize which layers are assigned to a probe: \- Go to the Probe
Volumes tab \- Enable **Display Probes** \- Set the **Probe Shading Mode**
field to **Rendering Layer Masks** \- Use the toggles in the **Scene View** An
interactive view into the world you are creating. You use the Scene View to
select and position scenery, characters, cameras, lights, and all other types
of Game Object. [More info](../UsingTheSceneView.html)  
See in [Glossary](../Glossary.html#SceneView) Overlay to hide Probes matching
a Rendering Layer Mask

### Adjust Baking Set properties

If adding a Volume doesn’t work, use the [Adaptive Probe Volumes
panel](probevolumes-lighting-panel-reference.html) in the Lighting window to
adjust Virtual Offset and Dilation settings.

  1. In **Probe Dilation Settings** , reduce **Search Radius**. This can help in situations where invalid Light Probes are receiving lighting data from more distant Light Probes. However, a lower **Search Radius** might cause light leaks.
  2. In **Virtual Offset Settings** , reduce **Search Distance Multiplier** and **Ray Origin Bias**.
  3. If there are light leaks in multiple locations, adjust **Min Probe Spacing** and **Max Probe Spacing** to increase the density of Light Probes.
  4. Select **Generate Lighting** to rebake the scene using the new settings.

Note: Don’t use very low values for the settings, or Dilation and Virtual
Offset might not work.

### Add a Probe Adjustment Volume component

Use a Probe Adjustment Volume component to make Light Probes invalid in a
small area. This triggers Dilation during baking, and improves the results of
**Leak Reduction Mode** at runtime.

  1. In the Adaptive Probe Volume Inspector, select **Add Component** , then select **Light** > **Probe Adjustment Volume**.
  2. Set the **Size** so the **Probe Adjustment Volume** area overlaps the Light Probes causing light leaks.
  3. Set **Probe Volume Overrides** > **Mode** to **Invalidate Probes** , to invalidate the Light Probes in the Volume.
  4. If you have a Volume with a Probe Volumes Options override, enable **Leak Reduction Mode**.
  5. In **Probe Volume Settings** , select **Generate Lighting** to rebake the scene using the new settings.

Using a Probe Adjustment Volume component solves most light leak issues, but
often not all.

If you use many Probe Adjustment Volumes in a scene, your bake will be slower,
and your scene might be harder to understand and maintain.

Refer to [Probe Adjustment Volume component reference](probevolumes-
adjustment-volume-component-reference.html) for more information.

## Fix seams

Seams are artefacts that appear when one lighting condition transitions
immediately into another. Seams are caused when two adjacent bricks have
different Light Probe densities. Refer to [bricks](probevolumes-
concept.html#how-probe-volumes-work) for more information.

![Two seams.](../../uploads/urp/probe-volumes/probevolumes-seams.JPG)  
  

To fix seams, do the following:

  1. Add a [Volume](set-up-a-volume.html) to your scene and make sure its area overlaps the position of the camera.
  2. Select **Add Override** , then select **Lighting** > **Probe Volumes Options**.
  3. Enable **Sampling Noise** , then try adjusting the value to add noise and make the transition more diffuse. Noise can help break up noticeable edges in indirect lighting at brick boundaries.

## Additional resources

  * [Configure the size and density of Adaptive Probe Volumes](probevolumes-changedensity.html)
  * [Adaptive Probe Volumes panel reference](probevolumes-lighting-panel-reference.html)
  * [Probe Volumes Options Override reference](probevolumes-options-override-reference.html)
  * [Probe Adjustment Volume component reference](probevolumes-adjustment-volume-component-reference.html)

[](../urp/probevolumes-troubleshoot-artefacts.html)

Troubleshooting dark blotches or streaks in Adaptive Probe Volumes in URP

[](../urp/probevolumes-inspector-reference.html)

Adaptive Probe Volume Inspector reference

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

