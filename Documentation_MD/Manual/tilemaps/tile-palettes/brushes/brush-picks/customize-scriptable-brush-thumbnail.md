[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/tilemaps/tile-palettes/brushes/brush-picks/customize-scriptable-brush-thumbnail.html)
  * [中文](/cn/current/Manual/tilemaps/tile-palettes/brushes/brush-picks/customize-scriptable-brush-thumbnail.html)
  * [日本語](/ja/current/Manual/tilemaps/tile-palettes/brushes/brush-picks/customize-scriptable-brush-thumbnail.html)
  * [한국어](/kr/current/Manual/tilemaps/tile-palettes/brushes/brush-picks/customize-scriptable-brush-thumbnail.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/tilemaps/tile-palettes/brushes/brush-picks/customize-scriptable-brush-thumbnail.html)
  * [中文](/cn/current/Manual/tilemaps/tile-palettes/brushes/brush-picks/customize-scriptable-brush-thumbnail.html)
  * [日本語](/ja/current/Manual/tilemaps/tile-palettes/brushes/brush-picks/customize-scriptable-brush-thumbnail.html)
  * [한국어](/kr/current/Manual/tilemaps/tile-palettes/brushes/brush-picks/customize-scriptable-brush-thumbnail.html)

  * [Working in Unity](../../../../working-in-unity.html)
  * [2D in Unity](../../../../Unity2D.html)
  * [Tilemaps in Unity](../../../../tilemaps/tilemaps-landing.html)
  * [Tile palettes](../../../../tilemaps/tile-palettes/tile-palette-landing.html)
  * [Tile palette brushes](../../../../tilemaps/tile-palettes/brushes/tile-palette-brushes-landing.html)
  * [Tile palette Brush Picks](../../../../tilemaps/tile-palettes/brushes/brush-picks/tile-palette-brush-picks.html)
  * Customize a scriptable Brush's thumbnail

[](../../../../tilemaps/tile-palettes/brushes/brush-picks/work-with-brush-
picks.html)

Work with Brush Picks

[](../../../../tilemaps/tile-palettes/brushes/brush-picks/brush-picks-overlay-
reference.html)

Brush Picks overlay reference

# Customize a scriptable Brush’s thumbnail

Unity determines the preview image displayed in a Brush Pick’s thumbnail by
the [Asset Preview](../../../../../ScriptReference/AssetPreview.html) utility.
To customize the thumbnail image of your [scriptable brush](../create-
scriptable-brush.html), you will need to implement the
[RenderStaticPreview](../../../../../ScriptReference/Editor.RenderStaticPreview.html)
method for the [editor](../../../../../ScriptReference/Editor.html) of your
scriptable brush.

![](../../../../../uploads/Main/brush-pick-thumbnail.png)

The icon in the lower right of the thumbnail preview displays the [Brush
type](../brush-inspector-reference.html) of the Brush Pick. The icon is
determined by the `icon` property of the editor for the Brush. Override this
property to provide your own icon for your Brush type.

![This message appears when a compatible Brush isnt
present.](../../../../../uploads/Main/tile-palette-brush-pick-invalid.png)
This message appears when a compatible Brush isn’t present.

Unity stores Brush Picks as serialized values based on the active Brush. If
you change the script or remove your custom scriptable brush, Unity might not
be able to load saved Brush Picks as the Brush has changed. A message appears
if Unity isn’t able to find a compatible Brush for the Brush Pick.

## Additional resources

  * [Scriptable Brushes](../create-scriptable-brush.html)
  * [Scriptable Tiles](../../../tiles-for-tilemaps/scriptable-tiles/scriptable-tiles.html)

[](../../../../tilemaps/tile-palettes/brushes/brush-picks/work-with-brush-
picks.html)

Work with Brush Picks

[](../../../../tilemaps/tile-palettes/brushes/brush-picks/brush-picks-overlay-
reference.html)

Brush Picks overlay reference

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

