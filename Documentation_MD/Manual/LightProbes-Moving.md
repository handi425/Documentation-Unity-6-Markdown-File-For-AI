[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/LightProbes-Moving.html)
  * [中文](/cn/current/Manual/LightProbes-Moving.html)
  * [日本語](/ja/current/Manual/LightProbes-Moving.html)
  * [한국어](/kr/current/Manual/LightProbes-Moving.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/LightProbes-Moving.html)
  * [中文](/cn/current/Manual/LightProbes-Moving.html)
  * [日本語](/ja/current/Manual/LightProbes-Moving.html)
  * [한국어](/kr/current/Manual/LightProbes-Moving.html)

  * [Lighting](LightingOverview.html)
  * [Direct and indirect lighting](direct-and-indirect-lighting.html)
  * [Precalculating indirect light with Light Probes](LightProbes-landing.html)
  * Move Light Probes at runtime

[](light-probes-and-scene-loading.html)

Load Light Probes in multiple scenes

[](light-probes-troubleshooting.html)

Troubleshooting Light Probes

# Move Light Probes at runtime

You might need to move **Light Probes** Light probes store information about
how light passes through space in your scene. A collection of light probes
arranged within a given space can improve lighting on moving objects and
static LOD scenery within that space. [More info](LightProbes.html)  
See in [Glossary](Glossary.html#LightProbe) at runtime. For example, if you
create a world by [loading multiple scenes
additively](setupmultiplescenes.html) and then move each **scene** A Scene
contains the environments and menus of your game. Think of each unique Scene
file as a unique level. In each Scene, you place your environments, obstacles,
and decorations, essentially designing and building your game in pieces. [More
info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) to a different position, you need to
move the Light Probes with their related scene objects.

You can use the [LightProbes API](../ScriptReference/LightProbes.html) to move
Light Probes at runtime. You can’t move Light Probes by updating the
**Transform component** A Transform component determines the Position,
Rotation, and Scale of each object in the scene. Every GameObject has a
Transform. [More info](class-Transform.html)  
See in [Glossary](Glossary.html#TransformComponent) of the **Light Probe
Group** A component that enables you to add Light Probes to GameObjects in
your scene. [More info](class-LightProbeGroup.html)  
See in [Glossary](Glossary.html#LightProbeGroup) object, because the Transform
only affects baking.

When you move Light Probes using the API, only the positions change. The baked
data stored in the Light Probes stays the same.

Follow these steps:

  1. Clone the Light Probes data that a loaded scene uses, using the [LightProbes.GetInstantiatedLightProbesForScene](../ScriptReference/LightProbes.GetInstantiatedLightProbesForScene.html) API. The loaded scene (the `Scene` object) will use this cloned data from now on.
  2. Set new positions using the [GetPositionsSelf](../ScriptReference/LightProbes.GetPositionsSelf.html) and [SetPositionsSelf](../ScriptReference/LightProbes.SetPositionsSelf.html) APIs.
  3. Update the internal structure of the Light Probe data in the scene using the [LightProbes.Tetrahedralize](../ScriptReference/LightProbes.Tetrahedralize.html) or [LightProbes.TetrahedralizeAsync](../ScriptReference/LightProbes.TetrahedralizeAsync.html) API, so objects use the correct light data.

If you baked the scene together with other scenes that contain Light Probes,
the returned data contains Light Probes from all the baked scenes. Refer to
[Light Probes and Scene loading](light-probes-and-scene-loading.html) for more
information about using Light Probes in multiple scenes.

The `Tetrahedralize` APIs can take a long time. If you move multiple Light
Probes, it’s best to tetrahedralize once at the end.

You can use the
[LightProbes.GetSharedLightProbesForScene](../ScriptReference/LightProbes.GetSharedLightProbesForScene.html)
API instead if you need to read the positions of the Light Probes in a scene,
but not move them.

## Example

The following code moves the Light Probes in the current scene to a new
position each frame.

Attach the script to any object in a scene. When you run the project, select
any object that uses Light Probes so you can see the probes move. The Light
Probe Group object doesn’t move.

    
    
    using UnityEngine;
    using UnityEngine.SceneManagement;
    
    public class LoadSingleSceneAndMoveProbes : MonoBehaviour
    {
        void Update()
        {
            // Get a copy of the Light Probes in the current scene
            LightProbes lightProbes = LightProbes.GetInstantiatedLightProbesForScene(SceneManager.GetActiveScene());
    
            // Get the Light Probe positions
            Vector3[] positions = lightProbes.GetPositionsSelf();
    
            // Update the positions
            for (int i = 0; i < positions.Length; i++)
            {
                positions[i].x = positions[i].x + 0.01f;
            }
    
            // Copy the new positions back to the Light Probes
            lightProbes.SetPositionsSelf(positions, true);
    
            // Tetrahedralize to update the data in the LightProbes object of the scene.
            LightProbes.Tetrahedralize();
        }
    }
    

[](light-probes-and-scene-loading.html)

Load Light Probes in multiple scenes

[](light-probes-troubleshooting.html)

Troubleshooting Light Probes

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

