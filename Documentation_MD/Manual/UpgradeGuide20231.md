[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UpgradeGuide20231.html)
  * [中文](/cn/current/Manual/UpgradeGuide20231.html)
  * [日本語](/ja/current/Manual/UpgradeGuide20231.html)
  * [한국어](/kr/current/Manual/UpgradeGuide20231.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UpgradeGuide20231.html)
  * [中文](/cn/current/Manual/UpgradeGuide20231.html)
  * [日本語](/ja/current/Manual/UpgradeGuide20231.html)
  * [한국어](/kr/current/Manual/UpgradeGuide20231.html)

  * [Install and upgrade](install-and-upgrade.html)
  * [Upgrade Unity](UpgradeGuides.html)
  * Upgrade to Unity 2023.1

[](UpgradeGuide20232.html)

Upgrade to Unity 2023.2

[](UpgradeGuide2022LTS.html)

Upgrade to Unity 2022 LTS

# Upgrade to Unity 2023.1

This page lists changes in Unity 2023.1 which might affect existing projects
when you upgrade them from a 2022 LTS version to 2023.1.

### Page outline

  * Render pipelinesA series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](render-pipelines.html)  
See in [Glossary](Glossary.html#Renderpipeline)

  * Gaussian Filter Radius properties from `LightingSettings` are now floating point values
  * Improvements to light probe energy conservation
  * Enlighten Baked Global Illumination is no longer available
  * Android: Java class UnityPlayer needs to be renamed to UnityPlayerForActivityOrService
  * Android: UnityPlayer java class no longer extends FrameLayout
  * FetchFirstCompatibleTypeUsingScriptableRenderPipelineExtension replaced by GetDerivedTypesSupportedOnCurrentPipeline
  * CustomEditorForRenderPipelineAttribute and VolumeComponentMenuForRenderPipelineAttribute deprecated
  * Changes to Android Gradle templates usage

## Render pipelines

This upgrade guide describes how to upgrade to version 2023.1 of Unity’s
built-in render pipeline. To upgrade other render pipelines to version 2023.1,
see:

  * [The URP upgrade guide](https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@15.0/manual/upgrade-guide-2023-1.html)
  * [The HDRP upgrade guide](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@15.0/manual/Upgrading-from-2022.2-to-2023.1.html)

To upgrade other packages, refer to the documentation for the packages you are
using.

## Gaussian Filter Radius properties from LightingSettings are now floating
point values

The [Progressive Lightmapper](progressive-lightmapper.html) includes a
**Gaussian** option among its **Advanced** filtering options (**Lighting
Window > Lightmapping Settings > Filtering > Direct Filter > Gaussian**). The
**Radius** control for **Gaussian** filtering now supports decimal increments,
such as 0.5. Previously, this control only supported integer steps (1 to 5).

As a result of this change, these properties are now deprecated in the C# API:

  * `int LightingSettings.filteringGaussRadiusAO`
  * `int LightingSettings.filteringGaussRadiusDirect`
  * `int LightingSettings.filteringGaussRadiusIndirect`

The floating point replacements for the deprecated properties are:

  * `float LightingSettings.filteringGaussianRadiusAO`
  * `float LightingSettings.filteringGaussianRadiusDirect`
  * `float LightingSettings.filteringGaussianRadiusIndirect`

You can call one of the deprecated member functions to round the Gaussian
filter radius to the nearest integer.

## Improvements to light probe energy conservation

Light Probes are now as bright as **lightmaps** A pre-rendered texture that
contains the effects of light sources on static objects in the scene.
Lightmaps are overlaid on top of scene geometry to create the effect of
lighting. [More info](Lightmapping.html)  
See in [Glossary](Glossary.html#Lightmap). Previously, Unity’s **Light
Probes** Light probes store information about how light passes through space
in your scene. A collection of light probes arranged within a given space can
improve lighting on moving objects and static LOD scenery within that space.
[More info](LightProbes.html)  
See in [Glossary](Glossary.html#LightProbe) were only 94% as bright as they
should be. For this reason, objects lit with light probes appeared a bit
darker than objects lit with lightmaps. Because of the subtlety of this
change, it is possible that many users won’t see a noticeable difference.

Should you prefer the old appearance, you can achieve it in the following way:

  1. Bake light probes.
  2. Use C# to get a copy of the array [LightmapSettings.lightProbes.bakedProbes](../ScriptReference/LightProbes-bakedProbes.html).
  3. For each SphericalHarmonicsL2 instance, multiply coefficient 0 with 16/17.
  4. Write your copy of the array back into [LightmapSettings.lightProbes.bakedProbes](../ScriptReference/LightProbes-bakedProbes.html).

## Enlighten Baked Global Illumination is no longer available

The **Enlighten** A lighting system by Geomerics used in Unity for Enlighten
Realtime Global Illumination. [More
info](https://www.siliconstudio.co.jp/en/products-service/enlighten/)  
See in [Glossary](Glossary.html#Enlighten) Baked **Global Illumination** A
group of techniques that model both direct and indirect lighting to provide
realistic lighting results.  
See in [Glossary](Glossary.html#globalillumination) lightmapping backend is no
longer available.

When you upgrade a project to this version, Unity removes the Enlighten baking
backend from the **lightmapper** A tool in Unity that bakes lightmaps
according to the arrangement of lights and geometry in your scene. [More
info](Lightmapping.html)  
See in [Glossary](Glossary.html#Lightmapper) selection dropdown and
substitutes a Progressive Lightmapper in every **Scene** A Scene contains the
environments and menus of your game. Think of each unique Scene file as a
unique level. In each Scene, you place your environments, obstacles, and
decorations, essentially designing and building your game in pieces. [More
info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) where you’ve selected the Enlighten
baking backend.

On Apple silicon devices, Unity substitutes the Progressive GPU Lightmapper
for the Enlighten baking backend. On all other devices, Unity selects the CPU
Progressive Lightmapper.

Enlighten precomputed Realtime Global Illumination is still available and is
supported up until Unity 2024 LTS.

## Android: Java class UnityPlayer needs to be renamed to
UnityPlayerForActivityOrService

The `UnityPlayer` Java class has been replaced by two new bridge classes,
`UnityPlayerForActivityOrService` and `UnityPlayerForGameActivity`. These new
classes both derive from `UnityPlayer`, but public methods such as
`displayChanged` and `windowFocusChanged` have moved from `UnityPlayer`
specifically to `UnityPlayerForActivityOrService`.

If you [extend the default Unity activity](AndroidUnityPlayerActivity.html)
and use the `UnityPlayer` class, you might encounter compile errors. In this
case, rename `UnityPlayer` to `UnityPlayerForActivityOrService`.

## Android: UnityPlayer java class no longer extends FrameLayout

The `UnityPlayer` Java class no longer extends `FrameLayout`. If you need to
access `FrameLayout`, call the `getFrameLayout` function on the `UnityPlayer`
instance.

## FetchFirstCompatibleTypeUsingScriptableRenderPipelineExtension replaced by
GetDerivedTypesSupportedOnCurrentPipeline

`RenderPipelineEditorUtility.FetchFirstCompatibleTypeUsingScriptableRenderPipelineExtension`
is now deprecated. Use
[GetDerivedTypesSupportedOnCurrentPipeline](../ScriptReference/Rendering.RenderPipelineEditorUtility.GetDerivedTypesSupportedOnCurrentPipeline.html)
instead. This method’s signature is also different; now it returns all derived
types, not just the first one it encounters. This prevents inconsistencies,
because Unity does not guarantee type order.

## CustomEditorForRenderPipelineAttribute and
VolumeComponentMenuForRenderPipelineAttribute deprecated

CustomEditorForRenderPipelineAttribute and
VolumeComponentMenuForRenderPipelineAttribute are now deprecated. Use
[CustomEditor](../ScriptReference/CustomEditor.html) and
[VolumeComponentMenu](https://docs.unity3d.com/Packages/com.unity.render-
pipelines.core@15.0/api/UnityEngine.Rendering.VolumeComponentMenu.html)
instead. To restrict the choice of pipeline when these attributes are active,
combine them with
[SupportedOnRenderPipelineAttribute](../ScriptReference/Rendering.SupportedOnRenderPipelineAttribute.html)
and specify a
[RenderPipelineAsset](../ScriptReference/Rendering.RenderPipelineAsset.html)
type. If you want to activate an SRP attribute that does work with the Built-
In Render Pipeline, use
[SupportedOnRenderPipelineAttribute](../ScriptReference/Rendering.SupportedOnRenderPipelineAttribute.html)
without parameters. This provides a unified workflow for both attributes when
there’s a need to activate them on a specific pipeline.

## Changes to Android Gradle templates usage

A new [API](android-modify-gradle-project-files-agp.html) to modify the
Android **Gradle** An Android build system that automates several build
processes. This automation means that many common build errors are less likely
to occur. [More info](android-gradle-overview.html)  
See in [Glossary](Glossary.html#Gradle) project was introduced. The API can be
used to replace the old Android Gradle templates workflow. Templates will
still work as before if the new API is not used.

To use the new API a [Templates Upgrader](android-templates-upgrader-
window.html) can be used:

  1. Open **Android**Player Settings** Settings that let you set various player-specific options for the final game built by Unity. [More info](class-PlayerSettings.html)  
See in [Glossary](Glossary.html#PlayerSettings)**.

  2. Go to **Publishing Settings** > **Build**.
  3. Select **Upgrade templates to C#**.

[](UpgradeGuide20232.html)

Upgrade to Unity 2023.2

[](UpgradeGuide2022LTS.html)

Upgrade to Unity 2022 LTS

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

