[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/sprite/atlas/distribution/methods-distribution.html)
  * [中文](/cn/current/Manual/sprite/atlas/distribution/methods-distribution.html)
  * [日本語](/ja/current/Manual/sprite/atlas/distribution/methods-distribution.html)
  * [한국어](/kr/current/Manual/sprite/atlas/distribution/methods-distribution.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/sprite/atlas/distribution/methods-distribution.html)
  * [中文](/cn/current/Manual/sprite/atlas/distribution/methods-distribution.html)
  * [日本語](/ja/current/Manual/sprite/atlas/distribution/methods-distribution.html)
  * [한국어](/kr/current/Manual/sprite/atlas/distribution/methods-distribution.html)

  * [Working in Unity](../../../working-in-unity.html)
  * [2D in Unity](../../../Unity2D.html)
  * [Sprites](../../../sprite/sprite-landing.html)
  * [Sprite atlas](../../../sprite/atlas/atlas-landing.html)
  * [Distribution](../../../sprite/atlas/distribution/distribution-landing.html)
  * Methods of distribution

[](../../../sprite/atlas/distribution/prepare-sprite-atlases-
distribution.html)

Prepare Sprite Atlases for distribution

[](../../../sprite/atlas/distribution/late-binding.html)

Late binding

# Methods of distribution

After you [prepare the Sprite Atlases for distribution](prepare-sprite-
atlases-distribution.html), there are several methods to distribute the
Atlases. Each method is more suitable for different Project needs or
characteristics, such as the size of the Atlas Assets or the target platform
of the Project.

The following are the two main methods to consider when you distribute
**Sprite** A 2D graphic objects. If you are used to working in 3D, Sprites are
essentially just standard textures but there are special techniques for
combining and managing sprite textures for efficiency and convenience during
development. [More info](../../../sprite/sprite-landing.html)  
See in [Glossary](../../../Glossary.html#Sprite) Atlases:

  1. Place the Sprite Atlases into the build’s _[Resources](../../../SpecialFolders.html)_ folder.
  2. Distribute them as downloadable [AssetBundles](../../../AssetBundles-Workflow.html).

## Method A: Resources folder

Unity can distribute Sprite Atlases in the final build, as long as it is
within the size limits of their chosen target platform. To distribute Sprite
Atlases together with the final build, place them in the Project’s `Resource`
folder, which includes Sprite Atlases in the exported build when users
download the application. Unity then loads these Atlases from the `Resource`
folder via [script](../../../../ScriptReference/Resources.html)). Refer to
documentation on the [Resources
API](../../../../ScriptReference/Resources.html) for more information.

## Method B: Downloadable AssetBundles

Sprite Atlases that are large in size can cause inconvenience for the
application user if Unity includes them with the exported build’s download,
because they require a lot of bandwidth and device storage. To avoid problems,
distribute large Sprite Atlases in **AssetBundles** , so that the player can
download each AssetBundle individually at their discretion. Unity then loads
the Sprite Atlases during run time via [script](late-binding.html). Refer to
the [AssetBundle Workflow](../../../AssetBundles-Workflow.html) for more
information.

[](../../../sprite/atlas/distribution/prepare-sprite-atlases-
distribution.html)

Prepare Sprite Atlases for distribution

[](../../../sprite/atlas/distribution/late-binding.html)

Late binding

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

