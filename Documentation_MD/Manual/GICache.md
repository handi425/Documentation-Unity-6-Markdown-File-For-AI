[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/GICache.html)
  * [中文](/cn/current/Manual/GICache.html)
  * [日本語](/ja/current/Manual/GICache.html)
  * [한국어](/kr/current/Manual/GICache.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/GICache.html)
  * [中文](/cn/current/Manual/GICache.html)
  * [日本語](/ja/current/Manual/GICache.html)
  * [한국어](/kr/current/Manual/GICache.html)

  * [Lighting](LightingOverview.html)
  * [Direct and indirect lighting](direct-and-indirect-lighting.html)
  * [Lighting data](Lightmap-data-landing.html)
  * Global Illumination (GI) cache

[](LightmapSnapshot.html)

Lighting Data Assets

[](Lightmaps-TechnicalInformation.html)

Lightmap data format

# Global Illumination (GI) cache

The **Global Illumination** A group of techniques that model both direct and
indirect lighting to provide realistic lighting results.  
See in [Glossary](Glossary.html#globalillumination) (GI) cache is an internal
data cache that the Unity Editor uses to store intermediate files when it
precomputes lighting data for Baked Global Illumination and **Enlighten** A
lighting system by Geomerics used in Unity for Enlighten Realtime Global
Illumination. [More info](https://www.siliconstudio.co.jp/en/products-
service/enlighten/)  
See in [Glossary](Glossary.html#Enlighten) Realtime Global Illumination. By
storing this data in a cache, Unity can speed up subsequent precomputations.

All Unity projects on your computer share the cache, so projects with similar
content and the same lightmapping backend can use the same cached files. You
can also copy the `GiCache` folder between different machines. This can make
your lighting build faster, because Unity fetches files from the `GiCache`
folder instead of recomputing them.

You can manage the size, location, and **compression** A method of storing
data that reduces the amount of storage space it requires. See [Texture
Compression](class-TextureImporterOverride), [Animation Compression](class-
AnimationClip.html#AssetProperties), [Audio Compression](class-
AudioClip.html), [Build Compression](ReducingFilesize.html).  
See in [Glossary](Glossary.html#compression) of the cache using the **GI
cache** preferences. For more information, refer to
[Preferences](Preferences.html).

You can also set a custom location for the GI cache folder. For more
information, refer to [Unity Editor special command line
arguments](EditorCommandLineArguments.html).

If you try to bake with more than one instance of the Editor running on the
same computer, the Editor displays the following warning message: “The GI
Cache is using increasing amounts of space on your hard drive to support
concurrent **lightmap** A pre-rendered texture that contains the effects of
light sources on static objects in the scene. Lightmaps are overlaid on top of
scene geometry to create the effect of lighting. [More
info](Lightmapping.html)  
See in [Glossary](Glossary.html#Lightmap) generation. To prevent failed bakes,
close all other instances of the Unity Editor.”

## Clear the GI cache

For details on how to clear the GI cache, refer to the [GI Cache
Preferences](Preferences.html) documentation. You can’t clear the GI cache by
selecting **Clear Baked Data** in the Lighting window.

You should only clear the GI cache as a last resort. If your project has an
issue that forces you to clear the GI cache, [report it as a
bug](https://unity.com/releases/editor/qa/bug-reporting).

[](LightmapSnapshot.html)

Lighting Data Assets

[](Lightmaps-TechnicalInformation.html)

Lightmap data format

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

