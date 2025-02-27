[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/sprite/renderer/sprite-renderer-reference.html)
  * [中文](/cn/current/Manual/sprite/renderer/sprite-renderer-reference.html)
  * [日本語](/ja/current/Manual/sprite/renderer/sprite-renderer-reference.html)
  * [한국어](/kr/current/Manual/sprite/renderer/sprite-renderer-reference.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/sprite/renderer/sprite-renderer-reference.html)
  * [中文](/cn/current/Manual/sprite/renderer/sprite-renderer-reference.html)
  * [日本語](/ja/current/Manual/sprite/renderer/sprite-renderer-reference.html)
  * [한국어](/kr/current/Manual/sprite/renderer/sprite-renderer-reference.html)

  * [Working in Unity](../../working-in-unity.html)
  * [2D in Unity](../../Unity2D.html)
  * [Sprites](../../sprite/sprite-landing.html)
  * [Sprite Renderer](../../sprite/renderer/renderer-landing.html)
  * Sprite Renderer reference

[](../../sprite/renderer/set-sort-point-sprite.html)

Set the sort point of a sprite

[](../../sprite/placeholder/placeholder-landing.html)

Placeholder sprites

# Sprite Renderer reference

Property | Function  
---|---  
****Sprite** A 2D graphic objects. If you are used to working in 3D, Sprites
are essentially just standard textures but there are special techniques for
combining and managing sprite textures for efficiency and convenience during
development. [More info](../../sprite/sprite-landing.html)  
See in [Glossary](../../Glossary.html#Sprite)** | Define which sprite texture the component should render. Click the circle icon to the right to open the object picker window, and select from the list of available sprite assets.  
**Open Sprite Editor** | Click this button to open the [Sprite Editor](../sprite-editor/sprite-editor-landing.html) window to edit the currently selected sprite. **Note:** If the 2D Sprite package isn’t installed, a button to [install the 2D Sprite package](install-2d-sprite-package.html) will be available instead.  
**Color** | Define the vertex color of the sprite, which tints or recolors the Sprite’s image. Use the color picker to set the vertex color of the rendered sprite texture. See the [Change the color of a sprite](change-color-sprite.html) section for examples.  
**Flip** | Flips the sprite texture along the checked axis. This doesn’t flip the Transform position of the **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](../../class-GameObject.html)  
See in [Glossary](../../Glossary.html#GameObject).  
**Material** | Define the Material used to render the sprite texture.  
**Draw Mode** | Define how the sprite scales when its dimensions change. Select one of the following options from the drop-down box.  
| **Simple** | The entire image scales when its dimensions change. This is the default option.  
| **Sliced** | Select this mode if the sprite is [9-sliced](../9-slice/9-slice-landing.html).  
| **Size** | Enter the sprite’s new Width and Height to scale the 9-sliced sprite. You can also use the [Rect Transform Tool](../9-slice/9-slice-landing.html) to scale the sprite while applying 9-slicing properties.  
| **Tiled** | By default, this mode causes the middle of the 9-Sliced sprite to tile instead of scale when its dimensions change. Use **Tile Mode** to control the tiling behavior of the sprite.  
| **Continuous** | This is the default **Tile Mode**. In Continuous mode, the midsection tiles evenly when the sprite dimensions change.  
| **Adaptive** | In Adaptive mode, the sprite texture stretches when its dimensions change, similar to Simple mode. When the scale of the changed dimensions meets the Stretch Value, the midsection begins to tile.  
|  **Stretch Value** (available when **Adaptive** is selected) | Use the slider to set the value between 0 and 1. The max value is 1, which represents double the original Sprite’s scale.  
**Mask Interaction** | Set how the **Sprite Renderer** A component that lets you display images as Sprites for use in both 2D and 3D scenes. [More info](../../sprite/renderer/renderer-landing.html)  
See in [Glossary](../../Glossary.html#SpriteRenderer) behaves when interacting
with a [Sprite Mask](../mask/mask-landing.html)A texture which defines which
areas of an underlying image to reveal or hide. [More
info](../../sprite/mask/mask-landing.html)  
See in [Glossary](../../Glossary.html#SpriteMask). See examples of the
different options in the [Mask Interaction](../mask/hide-reveal-parts-sprite-
mask.html) section.  
| **None** | The Sprite Renderer doesn’t interact with any Sprite Masks in the **Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](../../CreatingScenes.html)  
See in [Glossary](../../Glossary.html#Scene). This is the default option.  
| **Visible Inside Mask** | The sprite is visible where the Sprite Mask overlays it, but not outside of it.  
| **Visible Outside Mask** | The sprite is visible outside of the Sprite Mask, but not inside it. The Sprite Mask hides the sections of the sprite it overlays.  
**Sprite Sort Point** | Choose between the Sprite’s Center or its Pivot Point when calculating the distance between the sprite and the **camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](../../CamerasOverview.html)  
See in [Glossary](../../Glossary.html#Camera). See the section on [Sprite Sort
Point](set-sort-point-sprite.html) for further details.  
| **Center** | Select this to have Unity measure the distance between the camera’s Transform position and the Center of the sprite to determine its render order.  
| **Pivot** | Select the **Pivot** option. Edit the sprite’s Pivot position in the [Sprite Editor](../sprite-editor/sprite-editor-landing.html).  
**Material** | Select the material for newly created sprites. The default material is **sprites - Default**. Click the circle icon to open the object picker window and select other materials. **Tip:** Lighting doesn’t affect this default sprite material. To have the sprite react to lighting, use the object picker window and select the **Default - Diffuse** material instead.  
**Additional settings**  
**Sorting Layer** | Set the [Sorting Layer](../../class-TagManager.html) of the sprite, which controls its priority during rendering. Select an existing Sorting Layer from the drop-down box, or create a new Sorting Layer.  
| **Default** | The default layer the sprite is on.  
| **Add Sorting Layer ⋮** | Select this to create a new sorting layer for the selected sprite.  
**Order In Layer** | Set the render priority of the sprite within its [Sorting Layer](../../class-TagManager.html). Lower numbered sprites are rendered first, with higher numbered sprites overlapping those below.  
  
[](../../sprite/renderer/set-sort-point-sprite.html)

Set the sort point of a sprite

[](../../sprite/placeholder/placeholder-landing.html)

Placeholder sprites

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

