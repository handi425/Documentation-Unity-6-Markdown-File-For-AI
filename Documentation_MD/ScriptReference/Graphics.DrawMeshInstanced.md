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

#  [Graphics](Graphics.html).DrawMeshInstanced

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

public static void DrawMeshInstanced([Mesh](Mesh.html) mesh, int submeshIndex,
[Material](Material.html) material, Matrix4x4[] matrices, int count =
matrices.Length, [MaterialPropertyBlock](MaterialPropertyBlock.html)
properties = null,
[Rendering.ShadowCastingMode](Rendering.ShadowCastingMode.html) castShadows =
ShadowCastingMode.On, bool receiveShadows = true, int layer = 0,
[Camera](Camera.html) camera = null,
[Rendering.LightProbeUsage](Rendering.LightProbeUsage.html) lightProbeUsage =
LightProbeUsage.BlendProbes,
[LightProbeProxyVolume](LightProbeProxyVolume.html) lightProbeProxyVolume =
null);

## Declaration

public static void DrawMeshInstanced([Mesh](Mesh.html) mesh, int submeshIndex,
[Material](Material.html) material, List<Matrix4x4> matrices,
[MaterialPropertyBlock](MaterialPropertyBlock.html) properties = null,
[Rendering.ShadowCastingMode](Rendering.ShadowCastingMode.html) castShadows =
ShadowCastingMode.On, bool receiveShadows = true, int layer = 0,
[Camera](Camera.html) camera = null,
[Rendering.LightProbeUsage](Rendering.LightProbeUsage.html) lightProbeUsage =
LightProbeUsage.BlendProbes,
[LightProbeProxyVolume](LightProbeProxyVolume.html) lightProbeProxyVolume =
null);

### Parameters

mesh | The [Mesh](Mesh.html) to draw.  
---|---  
submeshIndex | Which subset of the mesh to draw. This applies only to meshes that are composed of several materials.  
material |  [Material](Material.html) to use.  
matrices | The array of object transformation matrices.  
count | The number of instances to be drawn.  
properties | Additional material properties to apply. See [MaterialPropertyBlock](MaterialPropertyBlock.html).  
castShadows | Determines whether the Meshes should cast shadows.  
receiveShadows | Determines whether the Meshes should receive shadows.  
layer |  [Layer](../Manual/Layers.html) to use.  
camera | If `null` (default), the mesh will be drawn in all cameras. Otherwise it will be drawn in the given Camera only.  
lightProbeUsage |  [LightProbeUsage](Rendering.LightProbeUsage.html) for the instances.  
  
### Description

Draws the same mesh multiple times using GPU instancing.

Similar to [Graphics.DrawMesh](Graphics.DrawMesh.html), this function draws
meshes for one frame without the overhead of creating unnecessary game
objects. This function is now obsolete. Use
[Graphics.RenderMeshInstanced](Graphics.RenderMeshInstanced.html) instead. Use
this function in situations where you want to draw the same mesh for a
particular amount of times using an instanced shader. Unity culls and sorts
instanced Meshes as a group. It creates an axis-aligned bounding box that
contains all the Meshes, calculates the center point, then uses this
information to cull and sort the Mesh instances. Note that after culling and
sorting the combined instances, Unity does not further cull individual
instances by the view frustum or baked occluders. It also does not sort
individual instances for transparency or depth efficiency.  
  
The transformation matrix of each instance of the mesh should be packed into
the `matrices` array. You can specify the number of instances to draw, or by
default it is the length of the `matrices` array. Other per-instance data, if
required by the shader, should be provided by creating arrays on the
MaterialPropertyBlock argument using
[SetFloatArray](MaterialPropertyBlock.SetFloatArray.html),
[SetVectorArray](MaterialPropertyBlock.SetVectorArray.html) and
[SetMatrixArray](MaterialPropertyBlock.SetMatrixArray.html).  
  
To render the instances with light probes, provide the light probe data via
the MaterialPropertyBlock and specify `lightProbeUsage` with
[LightProbeUsage.CustomProvided](Rendering.LightProbeUsage.CustomProvided.html).
Check
[LightProbes.CalculateInterpolatedLightAndOcclusionProbes](LightProbes.CalculateInterpolatedLightAndOcclusionProbes.html)
for the details.  
  
Note: You can only draw a maximum of 1023 instances at once.  
  
InvalidOperationException will be thrown if the material doesn't have
[Material.enableInstancing](Material-enableInstancing.html) set to true, or
the current platform doesn't support this API (i.e. if GPU instancing is not
available). See [SystemInfo.supportsInstancing](SystemInfo-
supportsInstancing.html).  
  
Additional resources: [Graphics.DrawMesh](Graphics.DrawMesh.html),
[Graphics.RenderMeshInstanced](Graphics.RenderMeshInstanced.html).

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

