[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/sprite/atlas/distribution/retrieve-sprite-contents-runtime-getsprites.html)
  * [中文](/cn/current/Manual/sprite/atlas/distribution/retrieve-sprite-contents-runtime-getsprites.html)
  * [日本語](/ja/current/Manual/sprite/atlas/distribution/retrieve-sprite-contents-runtime-getsprites.html)
  * [한국어](/kr/current/Manual/sprite/atlas/distribution/retrieve-sprite-contents-runtime-getsprites.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/sprite/atlas/distribution/retrieve-sprite-contents-runtime-getsprites.html)
  * [中文](/cn/current/Manual/sprite/atlas/distribution/retrieve-sprite-contents-runtime-getsprites.html)
  * [日本語](/ja/current/Manual/sprite/atlas/distribution/retrieve-sprite-contents-runtime-getsprites.html)
  * [한국어](/kr/current/Manual/sprite/atlas/distribution/retrieve-sprite-contents-runtime-getsprites.html)

  * [Working in Unity](../../../working-in-unity.html)
  * [2D in Unity](../../../Unity2D.html)
  * [Sprites](../../../sprite/sprite-landing.html)
  * [Sprite atlas](../../../sprite/atlas/atlas-landing.html)
  * [Distribution](../../../sprite/atlas/distribution/distribution-landing.html)
  * Retrieve sprite contents at runtime with GetSprites

[](../../../sprite/atlas/distribution/load-sprite-atlas-
spriteatlasmanageratlasrequested.html)

Load a Sprite Atlas with SpriteAtlasManager.atlasRequested

[](../../../sprite/atlas/distribution/resolve-different-sprite-atlas-
scenarios.html)

Resolve different Sprite Atlas scenarios

# Retrieve sprite contents at runtime with GetSprites

If the sprites packed into a **Sprite** A 2D graphic objects. If you are used
to working in 3D, Sprites are essentially just standard textures but there are
special techniques for combining and managing sprite textures for efficiency
and convenience during development. [More info](../../../sprite/sprite-
landing.html)  
See in [Glossary](../../../Glossary.html#Sprite) Atlas don’t exist in the
current build or project, use
[GetSprites](../../../../ScriptReference/U2D.SpriteAtlas.GetSprites.html) to
create sprites bound to a Sprite Atlas at runtime with the following steps.

  1. Create a [custom component](../../../CreatingComponents.html) that takes [SpriteAtlas](../../../../ScriptReference/U2D.SpriteAtlas.html) as a public variable.
  2. Assign a [Sprite Atlas](../sprite-atlas-reference.html)A utility that packs several sprite textures tightly together within a single texture known as an atlas. [More info](../../../sprite/atlas/v2/v2-landing.html)  
See in [Glossary](../../../Glossary.html#SpriteAtlas) to that property.

  3. Enter the Editor’s [Play mode](../../../GameView.html).
  4. Access the variable and call the property [GetSprites](../../../../ScriptReference/U2D.SpriteAtlas.GetSprites.html) to retrieve the array of sprites packed in the selected atlas.

[](../../../sprite/atlas/distribution/load-sprite-atlas-
spriteatlasmanageratlasrequested.html)

Load a Sprite Atlas with SpriteAtlasManager.atlasRequested

[](../../../sprite/atlas/distribution/resolve-different-sprite-atlas-
scenarios.html)

Resolve different Sprite Atlas scenarios

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

