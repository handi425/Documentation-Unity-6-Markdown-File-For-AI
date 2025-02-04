[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/materialvariant-concept.html)
  * [中文](/cn/current/Manual/materialvariant-concept.html)
  * [日本語](/ja/current/Manual/materialvariant-concept.html)
  * [한국어](/kr/current/Manual/materialvariant-concept.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/materialvariant-concept.html)
  * [中文](/cn/current/Manual/materialvariant-concept.html)
  * [日本語](/ja/current/Manual/materialvariant-concept.html)
  * [한국어](/kr/current/Manual/materialvariant-concept.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Materials](Materials.html)
  * [Material Variants](materialvariant-landingpage.html)
  * Introduction to Material Variants

[](materialvariant-landingpage.html)

Material Variants

[](materialvariant-hierarchyconcept.html)

Material Variant inheritance

# Introduction to Material Variants

## How Material Variants help artists

Many of the materials in a game may be variations on a source—outfits with a
variety of color schemes, damaged and undamaged versions of scenery, shiny and
weathered instances of props. To help you manage and maintain these materials,
Material Variants address specific shortcomings of copied materials, as
illustrated in this table.

**Copied material** | **Material Variant**  
---|---  
Does not automatically change if its source material changes. | Automatically changes if its parent changes.  
To replicate a change to a copy in its source material, you must manually adjust the source material. | You can copy changes from a child material to its parent with two mouse clicks.  
You can’t limit changes to the Properties of copies. | You can lock one or more Properties on a Material or Material Variant to prevent modifications to those Properties in its children.  
You can’t associate a copy with a different source. | You can reparent Material Variants.  
  
### Create, convert, or reparent Material Variants

You can create Material Variants from both Materials and other Material
Variants. It is also possible to convert Material Variants into Materials. To
use the Override(s) in a variant with a variety of different Materials, you
can change the parent of that variant.  
  
See [Create, modify, and apply Material Variants](materialvariant-tasks.html)
for information about how to create and convert Material Variants.  
  
See [Material Variant inheritance](materialvariant-hierarchyconcept.html) for
an explanation of the Material Variant hierarchy.

### Variant sources

It is possible to create a Material Variant from any Material, including one
you make with [Shader
Graph](https://docs.unity3d.com/Packages/com.unity.shadergraph@13.1/manual/index.html)
or download from the [Asset Store](https://assetstore.unity.com)A growing
library of free and commercial assets created by Unity and members of the
community. Offers a wide variety of assets, from textures, models and
animations to whole project examples, tutorials and Editor extensions. [More
info](AssetStore.html)  
See in [Glossary](Glossary.html#AssetStore). See [Create, modify, and apply
Material Variants](materialvariant-tasks.html) for detailed information about
how to create Material Variants from **shaders** A program that runs on the
GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader).

### Identify and revert changes

An Override is a change you make to a Material Variant’s Properties. You can
revert one Override at a time or all Overrides at once. Unity does not handle
reverts through the Undo stack, which means that you can revert an Override
without undoing any other changes.  
  
See [Create, modify, and apply Material Variants](materialvariant-tasks.html)
for detailed information about how to identify and revert Overrides.

### Unity prevents inheritance issues

Unity protects against ancestor deletion and circular dependencies. If you
attempt to delete the parent of a Material Variant, Unity warns you to select
a new parent for the child or reparent it.  
  
See [Material Variant inheritance](materialvariant-hierarchyconcept.html) for
detailed information about Material Variant hierarchies and inheritance error
messages.

### Scripts

You can use the Material Variant API to access Material Variant functionality
for complex or large operations.  
  
See the
[Material](https://docs.unity3d.com/2022.1/Documentation/ScriptReference/Material.html)An
asset that defines how a surface should be rendered. [More info](class-
Material.html)  
See in [Glossary](Glossary.html#Material) and
[MaterialEditor](https://docs.unity3d.com/ScriptReference/MaterialEditor.html)
API documentation for information about how to work with Material Variants in
**scripts** A piece of code that allows you to create your own Components,
trigger game events, modify Component properties over time and respond to user
input in any way you like. [More info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts).

## Similarities to Prefab Variants

[Prefab Variants](https://docs.unity3d.com/Manual/PrefabVariants.html) and
Material Variants have much the same functionality, foundational concepts, and
workflow. There are two key differences between them:

  * You can reparent a Material Variant.
  * You can lock Material Variant Properties.

## Prerequisites and limitations

Material Variants are not designed to address optimization and scalability
concerns. In addition, it is not possible to use Material Variants to alter
Materials at runtime in the Player.

## Additional resources

  * [Materials introduction](materials-introduction.html)
  * [Material Inspector Reference](class-Material.html)
  * [Prefabs](Prefabs.html)An asset type that allows you to store a GameObject complete with components and properties. The prefab acts as a template from which you can create new object instances in the scene. [More info](Prefabs.html)  
See in [Glossary](Glossary.html#Prefab)

  * [Prefab Variants](PrefabVariants.html)

[](materialvariant-landingpage.html)

Material Variants

[](materialvariant-hierarchyconcept.html)

Material Variant inheritance

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

