[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/LightingGiUvs-Reference.html)
  * [中文](/cn/current/Manual/LightingGiUvs-Reference.html)
  * [日本語](/ja/current/Manual/LightingGiUvs-Reference.html)
  * [한국어](/kr/current/Manual/LightingGiUvs-Reference.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/LightingGiUvs-Reference.html)
  * [中文](/cn/current/Manual/LightingGiUvs-Reference.html)
  * [日本語](/ja/current/Manual/LightingGiUvs-Reference.html)
  * [한국어](/kr/current/Manual/LightingGiUvs-Reference.html)

  * [Lighting](LightingOverview.html)
  * [Direct and indirect lighting](direct-and-indirect-lighting.html)
  * [Precalculating surface lighting with lightmaps](Lightmapping-landing.html)
  * [Lightmap UVs](LightingGiUvs-landing.html)
  * Lightmap UVs Settings in the Model Import Settings Inspector window reference

[](LightingGiUVs-Troubleshooting.html)

Troubleshooting automatically generated lightmap UVs

[](LightProbes-landing.html)

Precalculating indirect light with Light Probes

# Lightmap UVs Settings in the Model Import Settings Inspector window
reference

These are the settings that appear in the **Model** tab of the [Model Import
Settings](class-FBXImporter.html), when you enable **Generate** Lightmap__
UVs__.

**Property:** | **Function:**  
---|---  
**Hard Angle** | The angle between neighboring triangles (in degrees) after which Unity considers it a hard edge and creates a seam. You can set this to a value between 0 and 180. This is set to 88 degrees by default.  
  
If you set this to 180 degrees, Unity considers all edges smooth, which is
realistic for organic models. The default value (88 degrees) is realistic for
mechanical models.  
**Angle Error** | The maximum possible deviation of UV angles from the angles in the source geometry (as a percentage from 0–100). This is set to 8% by default.  
  
This controls how different the triangles in UV space can be to the triangles
in the original geometry. Usually this should be fairly low, to avoid
artifacts when applying the lightmap.  
**Area Error** | The maximum possible deviation of UV areas from the areas in the source geometry (as a percentage from 0–100). This is set to 15% by default.  
  
This controls how well Unity preserves the relative triangle areas. Increasing
the value allows you to create fewer charts. However, increasing the value can
change the resolution of the triangles, so make sure the resulting distortion
does not deteriorate the lightmap quality.  
**Margin Method** | Whether you specify the [Pack Margin](LightingGiUVs-Troubleshooting.html#PackMargin) manually, or whether Unity automatically calculates it.  
| **Manual** | You specify the [Pack Margin](LightingGiUVs-Troubleshooting.html#PackMargin) manually.  
| **Calculate** | Based on expected lightmap resolution and object scale, Unity calculates a [Pack Margin](LightingGiUVs-Troubleshooting.html#PackMargin) just large enough to avoid UV overlaps.  
**Pack Margin** | The margin between neighboring charts (in pixels), assuming the Mesh takes up the entire 1024x1024 lightmap. You can set this to a value between 1 and 64. A larger value increases the margin, but also increases the amount of space the chart needs. This is set to 4 pixels by default.  
  
For more information, see [Pack Margin](LightingGiUVs-
Troubleshooting.html#PackMargin).  
  
This property is only visible when **Margin Method** is set to **Manual**.  
**Min Lightmap Resolution** | The minimum lightmap resolution (in texels per unit) of the MeshRenderers that use this Mesh, across all Scenes. The lightmap resolution of a MeshRenderer is a combination of the MeshRenderer’s `Scale in Lightmap` property, and the `Lightmap Resolution` property of the [Lighting Settings Asset](class-LightingSettings.html) of the Scene it appears in.  
  
For more information, see [Min Lightmap Resolution and Min Object
Scale](LightingGiUVs-Troubleshooting.html#MinResolutionAndScale).  
  
Unity uses this information to calculate pack margin. This property is only
visible when **Margin Method** is set to **Calculate**.  
**Min Object Scale** | The minimum transform scale that of the GameObjects that use this Mesh, across all Scenes.  
  
For more information, see [Min Lightmap Resolution and Min Object
Scale](LightingGiUVs-Troubleshooting.html#MinResolutionAndScale).  
  
Unity uses this information to calculate pack margin. This property is only
visible when **Margin Method** is set to **Calculate**.  
  
[](LightingGiUVs-Troubleshooting.html)

Troubleshooting automatically generated lightmap UVs

[](LightProbes-landing.html)

Precalculating indirect light with Light Probes

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

