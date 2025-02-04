[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/LightingGiUvs-GeneratingLightmappingUVs.html)
  * [中文](/cn/current/Manual/LightingGiUvs-GeneratingLightmappingUVs.html)
  * [日本語](/ja/current/Manual/LightingGiUvs-GeneratingLightmappingUVs.html)
  * [한국어](/kr/current/Manual/LightingGiUvs-GeneratingLightmappingUVs.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/LightingGiUvs-GeneratingLightmappingUVs.html)
  * [中文](/cn/current/Manual/LightingGiUvs-GeneratingLightmappingUVs.html)
  * [日本語](/ja/current/Manual/LightingGiUvs-GeneratingLightmappingUVs.html)
  * [한국어](/kr/current/Manual/LightingGiUvs-GeneratingLightmappingUVs.html)

  * [Lighting](LightingOverview.html)
  * [Direct and indirect lighting](direct-and-indirect-lighting.html)
  * [Precalculating surface lighting with lightmaps](Lightmapping-landing.html)
  * [Lightmap UVs](LightingGiUvs-landing.html)
  * Generate lightmap UVs

[](LightingGiUvs.html)

Introduction to Lightmap UVs

[](LightingGiUvs-visualizing.html)

Check lightmap UVs

# Generate lightmap UVs

Unity can calculate the UVs for baked **lightmaps** A pre-rendered texture
that contains the effects of light sources on static objects in the scene.
Lightmaps are overlaid on top of scene geometry to create the effect of
lighting. [More info](Lightmapping.html)  
See in [Glossary](Glossary.html#Lightmap) when you import a model, or you can
provide your own data.

This page contains the following information:

  * How to provide your own lightmap UVs
  * How to automatically generate lightmap UVs
    * [Automatic lightmap UV generation settings](LightingGiUvs-Reference.html)
    * [Troubleshooting automatically generated lightmap UVs](LightingGiUVs-Troubleshooting.html)

## How to provide your own lightmap UVs

You can author your own lightmap UVs in the content creation software of your
choice. Unity uses these UVs as input for its calculations.

Where you put this data depends on whether you are providing UVs for baked
lightmaps, real-time lightmaps, or both:

  * For baked lightmaps, you must place lightmap UVs in the [Mesh.uv2](../ScriptReference/Mesh-uv2.html). This channel is also called “UV1”.
  * For real-time lightmaps: 
    * If you already have baked lightmap UVs in the `Mesh.uv2` of your **mesh** The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](mesh.html)  
See in [Glossary](Glossary.html#Mesh), and you want to use the same UVs as
input for the real-time lightmaps, you do not need to do anything. Unity falls
back to sharing the baked lightmap UVs.

    * If you already have baked lightmap UVs in `Mesh.uv2`, and you want to provide different UVs as input for your real-time lightmaps, place the real-time lightmap UVs in [Mesh.uv3](../ScriptReference/Mesh-uv3.html), also called “UV2”.
    * If you do not already have baked lightmap UVs in the second channel of your mesh, it’s your choice whether you use `Mesh.uv2` or `Mesh.uv3` for real-time lightmap UVs.

A good UV set for lightmaps should adhere to the following rules:

  * It should be within the [0,1] x [0,1] UV space.
  * It should have a wide enough margin between individual charts. For more information, see [UV overlap feedback](ProgressiveLightmapper-UVOverlap.html).
  * It should not have any overlapping faces.
  * There should be a low difference between the angles in the UV and the angles in the original geometry.
  * There should be a low difference between the relative scale of triangles in the UV and the relative scale of the triangles in the original geometry), unless you want some areas to have a higher lightmap resolution.

## How to automatically generate lightmap UVs

You can tell Unity to automatically generate lightmap UVs for a Model, using
the [Model Import Settings](class-FBXImporter.html).

  1. Select the Model in your Project view. Unity opens the Model Import Settings in the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector).

  2. In the Model Import Settings, navigate to the **Model** tab, and then the **Geometry** section.
  3. Tick the **Generate Lightmap UVs** checkbox. The **Lightmap UVs settings** section appears below the Generate Lightmap UVs checkbox.
  4. Optional: Configure the settings in the **Lightmap UVs settings** section. See [Settings](LightingGiUvs-Reference.html) for more information.
  5. Click the **Apply** button. Unity generates lightmap UVs into the [Mesh.uv2](../ScriptReference/Mesh-uv2.html) channel.

[](LightingGiUvs.html)

Introduction to Lightmap UVs

[](LightingGiUvs-visualizing.html)

Check lightmap UVs

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

