[ ]()

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

LanguageEnglish

  * [English]()

  * C#

[ ](https://docs.unity3d.com)

## Scripting API

Version: Unity 6 Select a different version

LanguageEnglish

  * [English]()

# SupportedRenderingFeatures

class in UnityEngine.Rendering

/

Implemented in:[UnityEngine.CoreModule](UnityEngine.CoreModule.html)

Leave feedback

Suggest a change

## Success!

Thank you for helping us improve the quality of Unity Documentation. Although
we cannot accept all submissions, we do read each suggested change from our
users and will make updates where applicable.

Close

## Submission failed

For some reason your suggested change could not be submitted. Please <a>try
again</a> in a few minutes. And thank you for taking the time to help us
improve the quality of Unity Documentation.

Close

Your name Your email Suggestion* Submit suggestion

Cancel

[ ]()

### Description

Describes the rendering features supported by a given render pipeline.

Set the active supported rendering features when enabling a render pipeline.
This will change the state of the editor UI to reflect the changes.

### Static Properties

[active](Rendering.SupportedRenderingFeatures-active.html)| Get / Set a
SupportedRenderingFeatures.  
---|---  
  
### Properties

[ambientProbeBaking](Rendering.SupportedRenderingFeatures-
ambientProbeBaking.html)| Determines if this renderer supports ambient probe
baking.  
---|---  
[defaultMixedLightingModes](Rendering.SupportedRenderingFeatures-
defaultMixedLightingModes.html)| This is the fallback mode if the mode the
user had previously selected is no longer available. See
SupportedRenderingFeatures.mixedLightingModes.  
[defaultReflectionProbeBaking](Rendering.SupportedRenderingFeatures-
defaultReflectionProbeBaking.html)| Specifies whether this renderer bakes a
default Reflection Probe.  
[editableMaterialRenderQueue](Rendering.SupportedRenderingFeatures-
editableMaterialRenderQueue.html)| Determines whether the Scriptable Render
Pipeline will override the default Material’s Render Queue settings and, if
true, hides the Render Queue property in the Inspector.  
[enlighten](Rendering.SupportedRenderingFeatures-enlighten.html)| Determines
if Enlighten Realtime Global Illumination lightmapper is supported by the
currently selected pipeline. If it is not supported, Enlighten-specific
settings do not appear in the Editor, which then defaults to the CPU
Lightmapper.  
[lightmapBakeTypes](Rendering.SupportedRenderingFeatures-
lightmapBakeTypes.html)| What baking types are supported. The unsupported ones
will be hidden from the UI. See LightmapBakeType.  
[lightmapsModes](Rendering.SupportedRenderingFeatures-lightmapsModes.html)|
Specifies what modes are supported. Has to be at least one. See LightmapsMode.  
[lightProbeProxyVolumes](Rendering.SupportedRenderingFeatures-
lightProbeProxyVolumes.html)| Are light probe proxy volumes supported?  
[mixedLightingModes](Rendering.SupportedRenderingFeatures-
mixedLightingModes.html)| Specifies what LightmapMixedBakeModes that are
supported. Please define a
SupportedRenderingFeatures.defaultMixedLightingModes in case multiple modes
are supported.  
[motionVectors](Rendering.SupportedRenderingFeatures-motionVectors.html)| Are
motion vectors supported?  
[overridesEnableLODCrossFade](Rendering.SupportedRenderingFeatures-
overridesEnableLODCrossFade.html)| Specifies whether the renderer overrides
the Enable LOD Cross Fade settings in the Quality Settings Panel. If It does,
the renderer does not need the built-in UI for Enable LOD Cross Fade settings.  
[overridesEnvironmentLighting](Rendering.SupportedRenderingFeatures-
overridesEnvironmentLighting.html)| Determines if the renderer will override
the Environment Lighting and will no longer need the built-in UI for it.  
[overridesFog](Rendering.SupportedRenderingFeatures-overridesFog.html)|
Determines if the renderer will override the fog settings in the Lighting
Panel and will no longer need the built-in UI for it.  
[overridesLightProbeSystem](Rendering.SupportedRenderingFeatures-
overridesLightProbeSystem.html)| Determines if the renderer will override the
light probe system with a different one.  
[overridesLightProbeSystemWarningMessage](Rendering.SupportedRenderingFeatures-
overridesLightProbeSystemWarningMessage.html)| The message to display in the
LightProbeGroup editor if the light probe system is overridden by the
renderer.  
[overridesLODBias](Rendering.SupportedRenderingFeatures-
overridesLODBias.html)| Specifies whether the renderer overrides the LOD bias
settings in the Quality Settings Panel. If It does, the renderer does not need
the built-in UI for LOD bias settings.  
[overridesMaximumLODLevel](Rendering.SupportedRenderingFeatures-
overridesMaximumLODLevel.html)| Specifies whether the renderer overrides the
maximum LOD level settings in the Quality Settings Panel. If It does, the
renderer does not need the built-in UI for maximum LOD level settings.  
[overridesOtherLightingSettings](Rendering.SupportedRenderingFeatures-
overridesOtherLightingSettings.html)| Determines if the renderer will override
halo and flare settings in the Lighting Panel and will no longer need the
built-in UI for it.  
[overridesRealtimeReflectionProbes](Rendering.SupportedRenderingFeatures-
overridesRealtimeReflectionProbes.html)| Specifies whether the render pipeline
overrides the real-time Reflection Probes settings in the Quality settings. If
It does, the render pipeline does not need the built-in UI for real-time
Reflection Probes settings.  
[overridesShadowmask](Rendering.SupportedRenderingFeatures-
overridesShadowmask.html)| Specifies whether the render pipeline overrides the
Shadowmask settings in the Quality settings.  
[particleSystemInstancing](Rendering.SupportedRenderingFeatures-
particleSystemInstancing.html)| Determines if the renderer supports Particle
System GPU instancing.  
[receiveShadows](Rendering.SupportedRenderingFeatures-receiveShadows.html)|
Can renderers support receiving shadows?  
[reflectionProbeModes](Rendering.SupportedRenderingFeatures-
reflectionProbeModes.html)| Flags for supported reflection probes.  
[reflectionProbes](Rendering.SupportedRenderingFeatures-
reflectionProbes.html)| Are reflection probes supported?  
[reflectionProbesBlendDistance](Rendering.SupportedRenderingFeatures-
reflectionProbesBlendDistance.html)| If this property is true, the blend
distance field in the Reflection Probe Inspector window is editable.  
[rendererPriority](Rendering.SupportedRenderingFeatures-
rendererPriority.html)| Determines if the renderer supports renderer priority
sorting.  
[rendererProbes](Rendering.SupportedRenderingFeatures-rendererProbes.html)|
Determines whether the Renderer supports probe lighting.  
[rendersUIOverlay](Rendering.SupportedRenderingFeatures-
rendersUIOverlay.html)| Determines whether the function to render UI overlays
is called by SRP and not by the engine.  
[skyOcclusion](Rendering.SupportedRenderingFeatures-skyOcclusion.html)| If
True, the renderer supports sky occlusion in Probe Volumes.  
[supportsClouds](Rendering.SupportedRenderingFeatures-supportsClouds.html)| If
True, the renderer supports cloud layers or volumetric clouds.  
[supportsHDR](Rendering.SupportedRenderingFeatures-supportsHDR.html)| If True,
the renderer supports HDR display output.  
  
Is something described here not working as you expect it to? It might be a
**Known Issue**. Please check with the Issue Tracker at
[issuetracker.unity3d.com](https://issuetracker.unity3d.com).

Copyright ©2005-2025 Unity Technologies. All rights reserved. Built from:
6000.0.36f1 (02b661dc617c). Built on: 2025-01-14.

[Tutorials](https://unity3d.com/learn) [Community
Answers](https://answers.unity3d.com) [Knowledge
Base](https://support.unity3d.com/hc/en-us)
[Forums](https://forum.unity3d.com) [Asset Store](https://unity3d.com/asset-
store) [Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)
[Legal](https://unity.com/legal) [Privacy
Policy](https://unity.com/legal/privacy-policy)
[Cookies](https://unity.com/legal/cookie-policy) [Do Not Sell or Share My
Personal Information](https://unity.com/legal/do-not-sell-my-personal-
information)

[Your Privacy Choices (Cookie Settings)](javascript:void\(0\);)

