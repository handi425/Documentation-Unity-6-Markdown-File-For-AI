[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/probevolumes-bakedifferentlightingsetups.html)
  * [中文](/cn/current/Manual/urp/probevolumes-bakedifferentlightingsetups.html)
  * [日本語](/ja/current/Manual/urp/probevolumes-bakedifferentlightingsetups.html)
  * [한국어](/kr/current/Manual/urp/probevolumes-bakedifferentlightingsetups.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/probevolumes-bakedifferentlightingsetups.html)
  * [中文](/cn/current/Manual/urp/probevolumes-bakedifferentlightingsetups.html)
  * [日本語](/ja/current/Manual/urp/probevolumes-bakedifferentlightingsetups.html)
  * [한국어](/kr/current/Manual/urp/probevolumes-bakedifferentlightingsetups.html)

  * [Lighting](../LightingOverview.html)
  * [Lighting in URP](../urp/lighting-landing.html)
  * [Adaptive Probe Volumes (APV) in URP](../urp/probevolumes.html)
  * [Changing lighting at runtime](../urp/probe-volumes-change-lighting-at-runtime.html)
  * Bake different lighting setups with Lighting Scenarios

[](../urp/probevolumes-understand-changing-lighting-at-runtime.html)

Choose how to change lighting at runtime

[](../urp/probevolumes-skyocclusion.html)

Update light from the sky at runtime with sky occlusion

# Bake different lighting setups with Lighting Scenarios

A Lighting Scenario contains the baked lighting data for a **scene** A Scene
contains the environments and menus of your game. Think of each unique Scene
file as a unique level. In each Scene, you place your environments, obstacles,
and decorations, essentially designing and building your game in pieces. [More
info](../CreatingScenes.html)  
See in [Glossary](../Glossary.html#Scene) or Baking Set. You can bake
different lighting setups into different Lighting Scenario assets, and change
which one the Universal **Render Pipeline** A series of operations that take
the contents of a Scene, and displays them on a screen. Unity lets you choose
from pre-built render pipelines, or write your own. [More info](../render-
pipelines.html)  
See in [Glossary](../Glossary.html#Renderpipeline) (URP) uses at runtime.

For example, you can create one Lighting Scenario with the lights on, and
another Lighting Scenario with the lights off. At runtime, you can enable the
second Lighting Scenario when the player turns the lights off.

## Enable Lighting Scenarios

To use Lighting Scenarios, go to the active [URP Asset](universalrp-
asset.html) and enable **Lighting** > **Light Probe Lighting** > **Lighting
Scenarios**.

## Add a Lighting Scenario

To create a new Lighting Scenario so you can store baking results inside, do
the following:

  1. Open the [Adaptive Probe Volumes panel](probevolumes-lighting-panel-reference.html) in the Lighting window.
  2. In the **Lighting Scenarios** section, select the **Add** (**+**) button to add a Lighting Scenario.

## Bake into a Lighting Scenario

To bake into a Lighting Scenario, follow these steps:

  1. In the **Lighting Scenarios** section, select a Lighting Scenario to make it active.
  2. Select **Generate Lighting**. URP stores the baking results in the active Lighting Scenario.

You can set which Lighting Scenario URP uses at runtime using the
[ProbeReferenceVolume API](https://docs.unity3d.com/Packages/com.unity.render-
pipelines.core@17.0/api/UnityEngine.Rendering.ProbeReferenceVolume.html).

If you change the active Lighting Scenarios at runtime, URP changes only the
indirect lighting data in the **Light Probes** Light probes store information
about how light passes through space in your scene. A collection of light
probes arranged within a given space can improve lighting on moving objects
and static LOD scenery within that space. [More info](../LightProbes.html)  
See in [Glossary](../Glossary.html#LightProbe). You might still need to use
**scripts** A piece of code that allows you to create your own Components,
trigger game events, modify Component properties over time and respond to user
input in any way you like. [More info](../creating-scripts.html)  
See in [Glossary](../Glossary.html#Scripts) to move geometry, modify lights or
change direct lighting.

## Blend between Lighting Scenarios

To enable blending between Lighting Scenarios, go to the active [URP
Asset](universalrp-asset.html) and enable **Light Probe Lighting** >
**Scenario Blending**.

You can blend between Lighting Scenarios at runtime using the
[BlendLightingScenario
API](https://docs.unity3d.com/Packages/com.unity.render-
pipelines.core@17.0/api/UnityEngine.Rendering.ProbeReferenceVolume.html#UnityEngine_Rendering_ProbeReferenceVolume_BlendLightingScenario_System_String_System_Single_).

For example, the following script does the following:

  1. Sets `scenario01` as the active Lighting Scenario.
  2. Sets up the number of cells to blend per frame, which can be useful for optimization purposes.
  3. Updates the Adaptive Probe Volume blending factor every frame to blend between `scenario01` and `scenario02`.

    
    
    using System.Collections;
    using System.Collections.Generic;
    using UnityEngine;
    
    public class BlendLightingScenarios : MonoBehaviour
    {
        UnityEngine.Rendering.ProbeReferenceVolume probeRefVolume;
        public string scenario01 = "Scenario01Name";
        public string scenario02 = "Scenario02Name";
        [Range(0, 1)] public float blendingFactor = 0.5f;
        [Min(1)] public int numberOfCellsBlendedPerFrame = 10;
    
        void Start()
        {
            probeRefVolume = UnityEngine.Rendering.ProbeReferenceVolume.instance;
            probeRefVolume.lightingScenario = scenario01;
            probeRefVolume.numberOfCellsBlendedPerFrame = numberOfCellsBlendedPerFrame;
        }
    
        void Update()
        {
            probeRefVolume.BlendLightingScenario(scenario02, blendingFactor);
        }
    }
    

### Preview blending between Lighting Scenarios

You can use the [Rendering Debugger](features/rendering-debugger-
reference.html#probe-volume-panel) to preview transitions between Lighting
Scenarios. Follow these steps:

  1. Go to **Window** > **Analysis** > **Rendering Debugger** to open the Rendering Debugger.
  2. Set **Scenario Blend Target** to a Lighting Scenario.
  3. Use **Scenario Blending Factor** to check the effect of blending between the Lighting Scenarios in the **Scene view** An interactive view into the world you are creating. You use the Scene View to select and position scenery, characters, cameras, lights, and all other types of Game Object. [More info](../UsingTheSceneView.html)  
See in [Glossary](../Glossary.html#SceneView).

### Keep Light Probes the same in different Lighting Scenarios

If you move static geometry between bakes, Light Probe positions might be
different. This means you can’t blend between Lighting Scenarios, because the
number of Light Probes and their positions must be the same in each Lighting
Scenario you blend between.

To avoid this, you can prevent URP recomputing probe positions when you bake.
Follow these steps:

  1. Bake one Lighting Scenario.
  2. Set another Lighting Scenario as the active Lighting Scenario.
  3. Change your scene lighting or geometry.
  4. In the **Probe Placement** section, set **Probe Positions** to **Don’t Recalculate**.
  5. Select **Generate Lighting** to recompute only the indirect lighting, and skip the probe placement computations.

## Additional resources

  * [ProbeReferenceVolume API](https://docs.unity3d.com/Packages/com.unity.render-pipelines.core@17.0/api/UnityEngine.Rendering.ProbeReferenceVolume.html)
  * [Bake multiple scenes together with Baking Sets](probevolumes-usebakingsets.html)

[](../urp/probevolumes-understand-changing-lighting-at-runtime.html)

Choose how to change lighting at runtime

[](../urp/probevolumes-skyocclusion.html)

Update light from the sky at runtime with sky occlusion

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

