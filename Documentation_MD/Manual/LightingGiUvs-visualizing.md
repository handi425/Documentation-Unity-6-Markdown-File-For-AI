[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/LightingGiUvs-visualizing.html)
  * [中文](/cn/current/Manual/LightingGiUvs-visualizing.html)
  * [日本語](/ja/current/Manual/LightingGiUvs-visualizing.html)
  * [한국어](/kr/current/Manual/LightingGiUvs-visualizing.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/LightingGiUvs-visualizing.html)
  * [中文](/cn/current/Manual/LightingGiUvs-visualizing.html)
  * [日本語](/ja/current/Manual/LightingGiUvs-visualizing.html)
  * [한국어](/kr/current/Manual/LightingGiUvs-visualizing.html)

  * [Lighting](LightingOverview.html)
  * [Direct and indirect lighting](direct-and-indirect-lighting.html)
  * [Precalculating surface lighting with lightmaps](Lightmapping-landing.html)
  * [Lightmap UVs](LightingGiUvs-landing.html)
  * Check lightmap UVs

[](LightingGiUvs-GeneratingLightmappingUVs.html)

Generate lightmap UVs

[](LightingGiUVs-Troubleshooting.html)

Troubleshooting automatically generated lightmap UVs

# Check lightmap UVs

It is important to be able to view the lightmap UVs that are being used, and
Unity has a visualization tool to help you with this. First, open the Lighting
window (menu: **Window** > **Rendering** > **Lighting**) and tick the **Auto**
checkbox at the bottom. This ensures that your bake and precompute are up-to-
date, and outputs the data that is needed to view the UVs. Wait for the
process to finish (this can take some time for large or complex Scenes).

## Check real-time lightmap UVs

To see the UVs for the Realtime **Global Illumination** A group of techniques
that model both direct and indirect lighting to provide realistic lighting
results.  
See in [Glossary](Glossary.html#globalillumination) system:

  * Select a **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) with a ****Mesh** The main
graphics primitive of Unity. Meshes make up a large part of your 3D worlds.
Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms,
Subdiv surfaces must be converted to polygons. [More info](mesh.html)  
See in [Glossary](Glossary.html#Mesh) Renderer** component.

  * In the ****Mesh Renderer** A mesh component that takes the geometry from the Mesh Filter and renders it at the position defined by the object’s Transform component. [More info](class-MeshRenderer.html)  
See in [Glossary](Glossary.html#MeshRenderer)** component, under
**Lightmapping** , open the **Realtime**Lightmap** A pre-rendered texture that
contains the effects of light sources on static objects in the scene.
Lightmaps are overlaid on top of scene geometry to create the effect of
lighting. [More info](Lightmapping.html)  
See in [Glossary](Glossary.html#Lightmap)** dropdown.

  * Double-click a lightmap texture to open the **Viewer** window.
  * In the **Viewer** window, open the dropdown and select **UV Charts**.

![](../uploads/Main/LightingGiUvs-0.jpg)

This displays the UV layout for the real-time lightmap of the selected
instance of this Mesh.

  * The charts are indicated by the different colored areas in the Preview (show in the image above on the right-hand side).
  * The UVs of the selected instance are laid over the charts, as a wireframe representation of the GameObject’s Mesh.
  * Dark gray texels show unused areas of the lightmap.

Multiple instances can be packed into a real-time lightmap, so some of the
charts you see might actually belong to other GameObjects.

## Check baked lightmap UVs

To see the UVs for the Baked Global Illumination system:

  * Select a GameObject with a **Mesh Renderer** component.
  * In the **Mesh Renderer** component, under **Lightmapping** , open the **Baked Lightmap** dropdown.
  * Double-click a lightmap texture to open the **Viewer** window.
  * In the **Viewer** window, open the dropdown and select **Baked UV Charts**.

![](../uploads/Main/LightingGiUvs-1.jpg)

As you can see, the baked UVs are very different to the precomputed real-time
UVs. This is because the requirements for baked and precomputed real-time UVs
are different.

[](LightingGiUvs-GeneratingLightmappingUVs.html)

Generate lightmap UVs

[](LightingGiUVs-Troubleshooting.html)

Troubleshooting automatically generated lightmap UVs

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

