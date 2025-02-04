[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/shadows-troubleshooting-urp.html)
  * [中文](/cn/current/Manual/urp/shadows-troubleshooting-urp.html)
  * [日本語](/ja/current/Manual/urp/shadows-troubleshooting-urp.html)
  * [한국어](/kr/current/Manual/urp/shadows-troubleshooting-urp.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/shadows-troubleshooting-urp.html)
  * [中文](/cn/current/Manual/urp/shadows-troubleshooting-urp.html)
  * [日本語](/ja/current/Manual/urp/shadows-troubleshooting-urp.html)
  * [한국어](/kr/current/Manual/urp/shadows-troubleshooting-urp.html)

  * [Lighting](../LightingOverview.html)
  * [Lighting in URP](../urp/lighting-landing.html)
  * [Shadows in URP](../urp/Shadows-in-URP.html)
  * Troubleshooting shadows in URP

[](../shadows-optimization.html)

Optimize shadow rendering in URP

[](../urp/lighting/reflection-probes.html)

Reflections in URP

# Troubleshooting shadows in URP

Techniques for troubleshooting shadow rendering in the Universal **Render
Pipeline** A series of operations that take the contents of a Scene, and
displays them on a screen. Unity lets you choose from pre-built render
pipelines, or write your own. [More info](../render-pipelines.html)  
See in [Glossary](../Glossary.html#Renderpipeline) (URP).

## Adjust the shadow bias settings in URP

By adjusting the shadow bias values you can reduce or eliminate such shadow
artifacts as shadow acne, shadow detachment (also known as peter-panning),
light leaking, and self-shadowing.

In URP, you can set the shadow bias in the **URP Asset** and on individual
lights.

In the **URP Asset** , the shadow bias settings are in the **Shadows**
section. The values you set here are the default values for all lights in the
**scene** A Scene contains the environments and menus of your game. Think of
each unique Scene file as a unique level. In each Scene, you place your
environments, obstacles, and decorations, essentially designing and building
your game in pieces. [More info](../CreatingScenes.html)  
See in [Glossary](../Glossary.html#Scene).

To set the shadow bias values for a specific light:

  1. In the **Shadows** section of the **Light** component, ensure that **Shadows Type** is set to **Soft Shadows** or **Hard Shadows**.

  2. Set the **Bias** property to **Custom**. Unity shows the properties **Depth** and **Normal**. Use those properties to set the shadow bias values for the current light.

Using high shadow bias values might result in light leaking through meshes.
This is where there is a visible gap between the shadow and its caster, and
leads to shadow shapes that do not accurately represent their casters.

## Avoid shadow flickering caused by maximum light limit in URP

URP has the [per-camera limit](urp-universal-renderer.html#real-time-lights-
limitations) on the number of visible lights in the **camera** A component
which creates an image of a particular viewpoint in your scene. The output is
either drawn to the screen or captured as a texture. [More
info](../CamerasOverview.html)  
See in [Glossary](../Glossary.html#Camera) frustum. For example, on mobile
platforms, this limit is 1 Main Light and 32 Additional Lights.

In the Forward **Rendering Path** The technique that a render pipeline uses to
render graphics. Choosing a different rendering path affects how lighting and
shading are calculated. Some rendering paths are more suited to different
platforms and hardware than others. [More info](../RenderingPaths.html)  
See in [Glossary](../Glossary.html#RenderingPath), there is also the [per-
object light limit](urp-universal-renderer.html#rendering-path-comparison).

If the number of visible lights exceeds the limit, Unity disables some lights.
It might disable a real-time shadow-casting light, which causes shadow
flickering.

To avoid this issue, ensure that the number of visible lights in the camera
frustum does not exceed the limit. You can get the number of visible lights
using the `cullResults.visibleLights` array of the
[RenderingData.cullResults](https://docs.unity3d.com/Packages/com.unity.render-
pipelines.universal@17.0/api/UnityEngine.Rendering.Universal.RenderingData.html#UnityEngine_Rendering_Universal_RenderingData_cullResults)
API.

The following example shows how to use the `cullresults.visibleLights` array:

    
    
    public override void AddRenderPasses(ScriptableRenderer renderer, ref RenderingData renderingData)
    {
        int visibleLightCount = renderingData.cullResults.visibleLights.Length;
    }
    

[](../shadows-optimization.html)

Optimize shadow rendering in URP

[](../urp/lighting/reflection-probes.html)

Reflections in URP

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

