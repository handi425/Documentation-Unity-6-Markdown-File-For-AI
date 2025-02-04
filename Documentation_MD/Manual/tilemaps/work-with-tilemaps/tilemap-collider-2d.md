[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/tilemaps/work-with-tilemaps/tilemap-collider-2d.html)
  * [中文](/cn/current/Manual/tilemaps/work-with-tilemaps/tilemap-collider-2d.html)
  * [日本語](/ja/current/Manual/tilemaps/work-with-tilemaps/tilemap-collider-2d.html)
  * [한국어](/kr/current/Manual/tilemaps/work-with-tilemaps/tilemap-collider-2d.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/tilemaps/work-with-tilemaps/tilemap-collider-2d.html)
  * [中文](/cn/current/Manual/tilemaps/work-with-tilemaps/tilemap-collider-2d.html)
  * [日本語](/ja/current/Manual/tilemaps/work-with-tilemaps/tilemap-collider-2d.html)
  * [한국어](/kr/current/Manual/tilemaps/work-with-tilemaps/tilemap-collider-2d.html)

  * [Working in Unity](../../working-in-unity.html)
  * [2D in Unity](../../Unity2D.html)
  * [Tilemaps in Unity](../../tilemaps/tilemaps-landing.html)
  * [Work with tilemaps](../../tilemaps/work-with-tilemaps/work-with-tilemaps-landing.html)
  * Tilemap Collider 2D

[](../../tilemaps/work-with-tilemaps/isometric-tilemaps/isometric-brush-
shortcut-reference.html)

Isometric brush shortcut Reference

[](../../tilemaps/work-with-tilemaps/tilemap-reference.html)

Tilemap component reference

# Tilemap Collider 2D

The **Tilemap**Collider** An invisible shape that is used to handle physical
collisions for an object. A collider doesn’t need to be exactly the same shape
as the object’s mesh - a rough approximation is often more efficient and
indistinguishable in gameplay. [More info](../../CollidersOverview.html)  
See in [Glossary](../../Glossary.html#Collider) 2D** component generates
collider shapes for [tiles](../tiles-for-tilemaps/tile-asset-reference.html)A
simple class that allows a sprite to be rendered on a Tilemap. [More
info](../../tilemaps/tiles-for-tilemaps/scriptable-tiles/scriptable-tiles-
landing.html)  
See in [Glossary](../../Glossary.html#Tile) on a [Tilemap](./tilemap-
reference.html)A GameObject that allows you to quickly create 2D levels using
tiles and a grid overlay. [More info](../../tilemaps/work-with-
tilemaps/tilemap-reference.html)  
See in [Glossary](../../Glossary.html#Tilemap) component on the same
**GameObject** The fundamental object in Unity scenes, which can represent
characters, props, scenery, cameras, waypoints, and more. A GameObject’s
functionality is defined by the Components attached to it. [More
info](../../class-GameObject.html)  
See in [Glossary](../../Glossary.html#GameObject). When you add or remove
tiles on the Tilemap component, the Tilemap Collider 2D updates the collider
shapes during `LateUpdate`. It batches multiple tile changes together to
minimize the impact on performance.

## Collider Type’s effect on collider generation

The collider shapes generated for each tile in the tilemap depend on the
**Collider Type** set in the tile’s properties. For more information on how
this component’s shape generation behavior corresponds to the **Collider
Types** , refer to [Tile asset reference](../tiles-for-tilemaps/tile-asset-
reference.html).

## Tilemap and Composite Colliders

You can use the Tilemap Collider 2D component together with the [Composite
Collider 2D](../../2d-physics/collider/composite-collider/composite-
collider-2d-reference.html) component. When you add both components to the
same tilemap, Unity composites the collider shapes of neighboring tiles
together. This smoothens the corners and edges between collider shapes in
neighboring tiles.

Using both components together reduces the number of individual collider
shapes involved in a physics update, which reduces the amount of calculations
required, and minimizes the impact on performance.

## Tilemap collider 2D API

If you require immediate changes to happen to the collider, use
[Tilemaps.TilemapCollider2D.ProcessTilemapChanges](../../../ScriptReference/Tilemaps.TilemapCollider2D.ProcessTilemapChanges.html)
to process them immediately. You can use
[Tilemaps.TilemapCollider2D-hasTilemapChanges](../../../ScriptReference/Tilemaps.TilemapCollider2D-hasTilemapChanges.html)
to check if any processing is required.

[](../../tilemaps/work-with-tilemaps/isometric-tilemaps/isometric-brush-
shortcut-reference.html)

Isometric brush shortcut Reference

[](../../tilemaps/work-with-tilemaps/tilemap-reference.html)

Tilemap component reference

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

