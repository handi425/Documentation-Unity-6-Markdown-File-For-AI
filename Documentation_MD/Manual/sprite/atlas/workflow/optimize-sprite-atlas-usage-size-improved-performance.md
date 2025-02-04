[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/sprite/atlas/workflow/optimize-sprite-atlas-usage-size-improved-performance.html)
  * [中文](/cn/current/Manual/sprite/atlas/workflow/optimize-sprite-atlas-usage-size-improved-performance.html)
  * [日本語](/ja/current/Manual/sprite/atlas/workflow/optimize-sprite-atlas-usage-size-improved-performance.html)
  * [한국어](/kr/current/Manual/sprite/atlas/workflow/optimize-sprite-atlas-usage-size-improved-performance.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/sprite/atlas/workflow/optimize-sprite-atlas-usage-size-improved-performance.html)
  * [中文](/cn/current/Manual/sprite/atlas/workflow/optimize-sprite-atlas-usage-size-improved-performance.html)
  * [日本語](/ja/current/Manual/sprite/atlas/workflow/optimize-sprite-atlas-usage-size-improved-performance.html)
  * [한국어](/kr/current/Manual/sprite/atlas/workflow/optimize-sprite-atlas-usage-size-improved-performance.html)

  * [Working in Unity](../../../working-in-unity.html)
  * [2D in Unity](../../../Unity2D.html)
  * [Sprites](../../../sprite/sprite-landing.html)
  * [Sprite atlas](../../../sprite/atlas/atlas-landing.html)
  * [Sprite Atlas workflow](../../../sprite/atlas/workflow/workflow-landing.html)
  * Optimize Sprite Atlas usage and size for improved performance

[](../../../sprite/atlas/workflow/include-build.html)

Include in build

[](../../../sprite/atlas/distribution/distribution-landing.html)

Distribution

# Optimize Sprite Atlas usage and size for improved performance

When a **Sprite** A 2D graphic objects. If you are used to working in 3D,
Sprites are essentially just standard textures but there are special
techniques for combining and managing sprite textures for efficiency and
convenience during development. [More info](../../../sprite/sprite-
landing.html)  
See in [Glossary](../../../Glossary.html#Sprite) is active in a **Scene** A
Scene contains the environments and menus of your game. Think of each unique
Scene file as a unique level. In each Scene, you place your environments,
obstacles, and decorations, essentially designing and building your game in
pieces. [More info](../../../CreatingScenes.html)  
See in [Glossary](../../../Glossary.html#Scene), Unity loads the **Sprite
Atlas** A utility that packs several sprite textures tightly together within a
single texture known as an atlas. [More
info](../../../sprite/atlas/v2/v2-landing.html)  
See in [Glossary](../../../Glossary.html#SpriteAtlas) it belongs to and all
the Textures it contains. This can cause excessive performance overhead if
Unity loads a Sprite Atlas with very large Textures when nothing in the Scene
is using most of those Textures.

To optimize Sprite Atlas usage, ideally all or most sprites that are active in
the Scene should belong to the same Atlas. It is good practice to split Sprite
Textures into multiple smaller Atlases according to their common usage.

Another way to reduce performance overhead is to reduce the empty space
between packed Textures in the Sprite Atlas. This reduces the size of the
Sprite Atlas. To do this, select the Sprite Atlas and inspect the packed Atlas
Texture in the Pack Preview window at the bottom of its **Inspector** A Unity
window that displays information about the currently selected GameObject,
asset or project settings, allowing you to inspect and edit the values. [More
info](../../../UsingTheInspector.html)  
See in [Glossary](../../../Glossary.html#Inspector) settings. If there is no
Preview available, select the **Pack Preview** button under the **Objects for
Packing** list to generate the packed Texture.

![Sprite Atlas with excess empty
space.](../../../../uploads/Main/2D_ExcessSpace.png)  
Sprite Atlas with excess empty space.

If there is excess empty space visible, you can manually reduce the size of
the packed Texture to reduce the amount of empty space and optimize the
Atlas’s size. To do so, go to the **Platform-specific overrides** panel at the
bottom of the Inspector window. Select a lower value from the drop-down menu
of the **Max Texture Size** setting, then select **Pack Preview** to
regenerate the packed Texture.

![Set the Max Texture
Size.](../../../../uploads/Main/2DSpriteAtlas_MaxTexSize.png)  
Set the Max Texture Size.

When the **Max Texture Size** value is lower than the current dimensions of
the Sprite Atlas Texture, Unity reduces the packed Texture dimensions to match
the set **Max Texture Size** as closely as possible, and automatically trims
away any extra empty space. If there are selected Sprite Textures that exceed
the **Max Texture Size** setting of the Sprite Atlas, then the Sprite Atlas
ignores the **Max Texture Size** setting and remains at the minimum size
required to contain the Sprite Textures at their original dimensions.

![Textures in a Sprite Atlas remain in their original
dimensions.](../../../../uploads/Main/2DSpriteAtlas_MinTexSize.png)  
Textures in a Sprite Atlas remain in their original dimensions.

**Note:** When using [Variant Sprite Atlases](../master-variant/variant-
sprite-atlas.html), selecting a very low scale value (less than 0.25) may
result in visual artifacts, depending on the **compression** A method of
storing data that reduces the amount of storage space it requires. See
[Texture Compression](class-TextureImporterOverride), [Animation
Compression](class-AnimationClip.html#AssetProperties), [Audio
Compression](class-AudioClip.html), [Build
Compression](ReducingFilesize.html).  
See in [Glossary](../../../Glossary.html#compression) format used and original
resolution of the Sprite. It is recommended to use high padding values and
better compression formats when using Variant Atlases.

[](../../../sprite/atlas/workflow/include-build.html)

Include in build

[](../../../sprite/atlas/distribution/distribution-landing.html)

Distribution

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

