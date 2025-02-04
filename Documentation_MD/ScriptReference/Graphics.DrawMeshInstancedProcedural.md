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

#  [Graphics](Graphics.html).DrawMeshInstancedProcedural

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

## Declaration

public static void DrawMeshInstancedProcedural([Mesh](Mesh.html) mesh, int
submeshIndex, [Material](Material.html) material, [Bounds](Bounds.html)
bounds, int count, [MaterialPropertyBlock](MaterialPropertyBlock.html)
properties, [Rendering.ShadowCastingMode](Rendering.ShadowCastingMode.html)
castShadows, bool receiveShadows, int layer, [Camera](Camera.html) camera,
[Rendering.LightProbeUsage](Rendering.LightProbeUsage.html) lightProbeUsage,
[LightProbeProxyVolume](LightProbeProxyVolume.html) lightProbeProxyVolume);

### Parameters

mesh | The [Mesh](Mesh.html) to draw.  
---|---  
submeshIndex | Which subset of the mesh to draw. This applies only to meshes that are composed of several materials.  
material |  [Material](Material.html) to use.  
bounds | The bounding volume surrounding the instances you intend to draw.  
count | The number of instances to be drawn.  
properties | Additional material properties to apply. See [MaterialPropertyBlock](MaterialPropertyBlock.html).  
castShadows | Determines whether the Meshes should cast shadows.  
receiveShadows | Determines whether the Meshes should receive shadows.  
layer |  [Layer](../Manual/Layers.html) to use.  
camera | If `null` (default), the mesh will be drawn in all cameras. Otherwise it will be drawn in the given Camera only.  
lightProbeUsage |  [LightProbeUsage](Rendering.LightProbeUsage.html) for the instances.  
  
### Description

This function is now obsolete. Use
[Graphics.RenderMeshPrimitives](Graphics.RenderMeshPrimitives.html) instead.
Draws the same mesh multiple times using GPU instancing. This is similar to
[Graphics.DrawMeshInstancedIndirect](Graphics.DrawMeshInstancedIndirect.html),
except that when the instance count is known from script, it can be supplied
directly using this method, rather than via a ComputeBuffer.

To render the instances with light probes, provide the light probe data via
the MaterialPropertyBlock and specify `lightProbeUsage` with
[LightProbeUsage.CustomProvided](Rendering.LightProbeUsage.CustomProvided.html).
Check
[LightProbes.CalculateInterpolatedLightAndOcclusionProbes](LightProbes.CalculateInterpolatedLightAndOcclusionProbes.html)
for the details. Additional resources:
[Graphics.RenderMeshPrimitives](Graphics.RenderMeshPrimitives.html).

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

