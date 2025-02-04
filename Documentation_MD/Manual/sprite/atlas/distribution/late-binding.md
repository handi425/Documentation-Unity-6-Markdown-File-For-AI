[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/sprite/atlas/distribution/late-binding.html)
  * [中文](/cn/current/Manual/sprite/atlas/distribution/late-binding.html)
  * [日本語](/ja/current/Manual/sprite/atlas/distribution/late-binding.html)
  * [한국어](/kr/current/Manual/sprite/atlas/distribution/late-binding.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/sprite/atlas/distribution/late-binding.html)
  * [中文](/cn/current/Manual/sprite/atlas/distribution/late-binding.html)
  * [日本語](/ja/current/Manual/sprite/atlas/distribution/late-binding.html)
  * [한국어](/kr/current/Manual/sprite/atlas/distribution/late-binding.html)

  * [Working in Unity](../../../working-in-unity.html)
  * [2D in Unity](../../../Unity2D.html)
  * [Sprites](../../../sprite/sprite-landing.html)
  * [Sprite atlas](../../../sprite/atlas/atlas-landing.html)
  * [Distribution](../../../sprite/atlas/distribution/distribution-landing.html)
  * Late binding

[](../../../sprite/atlas/distribution/methods-distribution.html)

Methods of distribution

[](../../../sprite/atlas/distribution/load-sprite-atlas-
spriteatlasmanageratlasrequested.html)

Load a Sprite Atlas with SpriteAtlasManager.atlasRequested

# Late binding

Late binding is the process of loading or swapping in a [Sprite
Atlas](../atlas-landing.html)A utility that packs several sprite textures
tightly together within a single texture known as an atlas. [More
info](../../../sprite/atlas/v2/v2-landing.html)  
See in [Glossary](../../../Glossary.html#SpriteAtlas) at runtime via the
[Sprite Atlas API](../../../../ScriptReference/U2D.SpriteAtlas.html). It’s
necessary when the atlas isn’t available during start-up, such as when loading
assets from [AssetBundles](../../../AssetBundlesIntro.html). You can choose to
bind [different Sprite Atlases](../distribution/prepare-sprite-atlases-
distribution.html) based on specific criteria, such as loading a high or low-
resolution **Sprite** A 2D graphic objects. If you are used to working in 3D,
Sprites are essentially just standard textures but there are special
techniques for combining and managing sprite textures for efficiency and
convenience during development. [More info](../../../sprite/sprite-
landing.html)  
See in [Glossary](../../../Glossary.html#Sprite) Atlas ford different
platforms to improve performance and efficiency.

After you [pack your sprites into a Sprite Atlas](../workflow/sprite-atlas-
workflow.html) in your project, you can decide whether to [include the Sprite
Atlas with the published build](../distribution/distribution-landing.html). To
exclude the Sprite Atlas from the build, clear **Include in Build** in the
Sprite Atlas’ properties. When not included in a build, the Sprite Atlas isn’t
loaded at runtime and sprites that reference textures packed into the atlas
will appear blank until you use late binding to load the atlas. Note that this
also means that Unity Editor won’t automatically load the Sprite Atlas and
that your sprites will appear blank when you enter Play mode.

Additional samples of the different ways and scenarios to use Sprite Atlases
and late binding are available for download from the [2D
Common](https://docs.unity3d.com/Packages/com.unity.2d.common@latest)
package’s **Samples** tab.

## Additional resources

  * [Sprite Atlas workflow](../workflow/sprite-atlas-workflow.html)
  * [Methods of distribution](../distribution/methods-distribution.html)
  * [Unity Support: Sprite Atlas with late binding and Asset Bundles](https://support.unity.com/hc/en-us/articles/360000665546-Sprite-Atlas-with-late-binding-and-Asset-Bundles)

[](../../../sprite/atlas/distribution/methods-distribution.html)

Methods of distribution

[](../../../sprite/atlas/distribution/load-sprite-atlas-
spriteatlasmanageratlasrequested.html)

Load a Sprite Atlas with SpriteAtlasManager.atlasRequested

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

